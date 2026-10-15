"""Background task: fetch one NVDB object type and save it as GeoPackage."""

from __future__ import annotations

from pathlib import Path

from qgis.core import Qgis, QgsFeedback, QgsMessageLog, QgsTask
from qgis.PyQt.QtCore import pyqtSignal

from ..config import PLUGIN_NAME
from .client import NvdbClient
from .export import write_gpkg
from .query import NvdbApiError


class DownloadTask(QgsTask):
    completed = pyqtSignal(str, str, int)  # gpkg path, layer name, feature count
    failed = pyqtSignal(str)
    status = pyqtSignal(str)

    def __init__(self, api_key, namespace, schemaversion, dataset, bbox, output_dir: Path, stamp: str):
        super().__init__(f"NVDB: hämtar {dataset.title}", QgsTask.Flag.CanCancel)
        self.api_key = api_key
        self.namespace = namespace
        self.schemaversion = schemaversion
        self.dataset = dataset
        self.bbox = bbox
        self.layer_name = dataset.id
        self.gpkg_path = output_dir / f"{dataset.id}_{stamp}.gpkg"
        self.feature_count = 0
        self.error: str | None = None
        self._feedback = QgsFeedback()

    def cancel(self) -> None:
        self._feedback.cancel()  # aborts an in-flight request, not just the next page
        super().cancel()

    def run(self) -> bool:
        client = NvdbClient(self.api_key, self.namespace, self.schemaversion, self._feedback)
        records: list[dict] = []
        self.status.emit("söker…")
        try:
            for page_no, page in enumerate(client.pages(self.dataset.id, self.bbox), start=1):
                records.extend(page)
                self.status.emit(f"{len(records)} objekt hämtade (anrop {page_no})")
        except NvdbApiError as e:
            self.error = str(e)
            return False
        if self.isCanceled():
            return False
        if not records:
            self.error = "Sökningen gav inga träffar."
            return False
        self.status.emit(f"{len(records)} objekt – skriver GeoPackage…")
        try:
            self.gpkg_path.parent.mkdir(parents=True, exist_ok=True)
            self.feature_count = write_gpkg(
                records, self.gpkg_path, self.layer_name, self.dataset.geometry
            )
        except Exception as e:  # noqa: BLE001 — report any write failure to the UI
            self.error = str(e)
            return False
        return True

    def finished(self, result: bool) -> None:
        if result:
            self.completed.emit(str(self.gpkg_path), self.layer_name, self.feature_count)
        elif not self.isCanceled():
            message = self.error or "Okänt fel"
            QgsMessageLog.logMessage(message, PLUGIN_NAME, Qgis.MessageLevel.Critical)
            self.failed.emit(message)
