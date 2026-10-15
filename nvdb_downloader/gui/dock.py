"""Dock widget with two tabs: raw NVDB tables, and emulated Topografi 10 layers."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from qgis.core import (
    QgsApplication,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsProject,
    QgsSettings,
    QgsVectorLayer,
)
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QDockWidget,
    QFileDialog,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QRadioButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from ..config import NVDB_CRS, PLUGIN_NAME, SETTINGS_PREFIX
from ..core.auth import load_api_key, store_api_key
from ..core.registry import load_registry
from ..core.task import DownloadTask, SourceSpec
from ..core.topo10 import RECIPES, recipe

S_AUTHCFG = f"{SETTINGS_PREFIX}/authcfg"
S_OUTDIR = f"{SETTINGS_PREFIX}/output_dir"


class NvdbDock(QDockWidget):
    def __init__(self, iface, parent=None):
        super().__init__(PLUGIN_NAME, parent)
        self.iface = iface
        self.registry = load_registry()
        self.settings = QgsSettings()
        self._tasks: list[DownloadTask] = []
        self._pending = 0

        root = QWidget()
        layout = QVBoxLayout(root)

        self.key_label = QLabel()
        key_button = QPushButton("Ange API-nyckel…")
        key_button.clicked.connect(self._set_key)
        row = QHBoxLayout()
        row.addWidget(self.key_label, 1)
        row.addWidget(key_button)
        layout.addLayout(row)

        self.tabs = QTabWidget()
        layout.addWidget(self.tabs, 1)

        # Tab 1: raw data, any NVDB table
        raw = QWidget()
        raw_layout = QVBoxLayout(raw)
        self.search = QLineEdit()
        self.search.setPlaceholderText("Sök objekttyp…")
        self.search.textChanged.connect(self._filter)
        raw_layout.addWidget(self.search)
        self.list = QListWidget()
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        for d in self.registry.datasets:
            if not d.verified:
                continue
            item = QListWidgetItem(d.title)
            item.setData(Qt.ItemDataRole.UserRole, d.id)
            self.list.addItem(item)
        raw_layout.addWidget(self.list, 1)
        self.tabs.addTab(raw, "Rådata")

        # Tab 2: emulate Lantmäteriet's Topografi 10 layers from NVDB
        topo = QWidget()
        topo_layout = QVBoxLayout(topo)
        topo_layout.addWidget(
            QLabel("Bygger Topografi 10-skikt av NVDB-data och stilsätter dem som Topo10.")
        )
        self.topo_list = QListWidget()
        self.topo_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        for r in RECIPES:
            item = QListWidgetItem(r.title + (f" – {r.note}" if r.note else ""))
            item.setData(Qt.ItemDataRole.UserRole, r.id)
            self.topo_list.addItem(item)
        topo_layout.addWidget(self.topo_list, 1)
        self.tabs.addTab(topo, "Topo10-uttag")

        self.area_canvas = QRadioButton("Kartans nuvarande utsnitt")
        self.area_all = QRadioButton("Hela Sverige (kan vara stort)")
        self.area_canvas.setChecked(True)
        layout.addWidget(self.area_canvas)
        layout.addWidget(self.area_all)

        self.add_to_map = QCheckBox("Lägg till i kartan")
        self.add_to_map.setChecked(True)
        layout.addWidget(self.add_to_map)

        out_row = QHBoxLayout()
        self.outdir = QLineEdit(self.settings.value(S_OUTDIR, str(Path.home() / "NVDB")))
        browse = QPushButton("…")
        browse.clicked.connect(self._browse)
        out_row.addWidget(self.outdir, 1)
        out_row.addWidget(browse)
        layout.addLayout(out_row)

        self.button = QPushButton("Hämta")
        self.button.clicked.connect(self._download)
        layout.addWidget(self.button)
        self.status = QLabel()
        self.status.setWordWrap(True)
        layout.addWidget(self.status)

        self.setWidget(root)
        self._refresh_key_label()

    # --- helpers ---------------------------------------------------------

    def _api_key(self) -> str:
        return load_api_key(self.settings.value(S_AUTHCFG, ""))

    def _refresh_key_label(self) -> None:
        self.key_label.setText("API-nyckel: sparad" if self._api_key() else "API-nyckel saknas")

    def _set_key(self) -> None:
        key, ok = QInputDialog.getText(
            self, PLUGIN_NAME, "API-nyckel från data.trafikverket.se:",
            QLineEdit.EchoMode.Password,
        )
        if not ok or not key.strip():
            return
        try:
            authcfg = store_api_key(PLUGIN_NAME, key.strip())
        except RuntimeError as e:
            QMessageBox.warning(self, PLUGIN_NAME, str(e))
            return
        self.settings.setValue(S_AUTHCFG, authcfg)
        self._refresh_key_label()

    def _filter(self, text: str) -> None:
        text = text.lower()
        for i in range(self.list.count()):
            self.list.item(i).setHidden(text not in self.list.item(i).text().lower())

    def _browse(self) -> None:
        path = QFileDialog.getExistingDirectory(self, PLUGIN_NAME, self.outdir.text())
        if path:
            self.outdir.setText(path)

    def _bbox(self):
        """Canvas extent in SWEREF 99 TM, or None for the whole country."""
        if self.area_all.isChecked():
            return None
        canvas = self.iface.mapCanvas()
        src = canvas.mapSettings().destinationCrs()
        dst = QgsCoordinateReferenceSystem(NVDB_CRS)
        rect = QgsCoordinateTransform(src, dst, QgsProject.instance()).transformBoundingBox(
            canvas.extent()
        )
        return rect.xMinimum(), rect.yMinimum(), rect.xMaximum(), rect.yMaximum()

    # --- download --------------------------------------------------------

    def _jobs(self):
        """(title, layer_name, geometry, style, sources) per selected item in the current tab."""
        reg = self.registry
        jobs = []
        if self.tabs.currentIndex() == 0:
            for item in self.list.selectedItems():
                d = reg.get(item.data(Qt.ItemDataRole.UserRole))
                jobs.append((d.title, d.id, d.geometry, "", [SourceSpec(d.id, reg.namespace_of(d))]))
        else:
            for item in self.topo_list.selectedItems():
                r = recipe(item.data(Qt.ItemDataRole.UserRole))
                sources = [
                    SourceSpec(s.dataset_id, reg.namespace_of(reg.get(s.dataset_id)), s.transform)
                    for s in r.sources
                ]
                jobs.append((r.title, r.layer_name, r.geometry, r.style, sources))
        return jobs

    def _download(self) -> None:
        key = self._api_key()
        if not key:
            QMessageBox.information(self, PLUGIN_NAME, "Ange en API-nyckel först.")
            return
        jobs = self._jobs()
        if not jobs:
            QMessageBox.information(self, PLUGIN_NAME, "Välj minst en post i listan.")
            return
        if self.area_all.isChecked():
            answer = QMessageBox.question(
                self, PLUGIN_NAME,
                "Hela Sverige kan ge hundratusentals objekt per typ. Fortsätta?",
            )
            if answer != QMessageBox.StandardButton.Yes:
                return
        bbox = self._bbox()
        out = Path(self.outdir.text())
        self.settings.setValue(S_OUTDIR, str(out))
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.button.setEnabled(False)
        self._pending = len(jobs)
        for title, layer_name, geometry, style, sources in jobs:
            task = DownloadTask(
                title, key, self.registry.schemaversion, sources, layer_name, geometry,
                bbox, out, stamp, style,
            )
            task.status.connect(lambda text, t=title: self.status.setText(f"{t}: {text}"))
            task.completed.connect(self._on_completed)
            task.failed.connect(self._on_failed)
            self._tasks.append(task)
            QgsApplication.taskManager().addTask(task)

    def _task_done(self) -> None:
        self._pending -= 1
        if self._pending <= 0:
            self.button.setEnabled(True)
            self._tasks.clear()

    def _on_completed(self, gpkg: str, layer_name: str, count: int, style: str) -> None:
        self.status.setText(f"{layer_name}: {count} objekt sparade i {gpkg}")
        if self.add_to_map.isChecked():
            layer = QgsVectorLayer(f"{gpkg}|layername={layer_name}", layer_name, "ogr")
            if layer.isValid():
                qml = Path(__file__).resolve().parent.parent / "styles" / f"{style}.qml"
                if style and qml.exists():
                    layer.loadNamedStyle(str(qml))
                QgsProject.instance().addMapLayer(layer)
        self._task_done()

    def _on_failed(self, message: str) -> None:
        self.status.setText(message)
        self.iface.messageBar().pushWarning(PLUGIN_NAME, message)
        self._task_done()
