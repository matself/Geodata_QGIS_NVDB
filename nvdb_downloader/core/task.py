"""Background task: fetch one or more NVDB object types and save them as one
GeoPackage layer."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from qgis.core import Qgis, QgsFeedback, QgsMessageLog, QgsTask
from qgis.PyQt.QtCore import pyqtSignal

from ..config import PLUGIN_NAME
from .client import NvdbClient
from .export import write_gpkg
from .query import NvdbApiError


@dataclass(frozen=True)
class SourceSpec:
    """One object type to fetch, with an optional per-record transform (None drops)."""

    objecttype: str
    namespace: str
    transform: Callable[[dict], dict | None] | None = None


class DownloadTask(QgsTask):
    completed = pyqtSignal(str, str, int, str)  # gpkg path, layer name, count, style
    failed = pyqtSignal(str)
    status = pyqtSignal(str)

    def __init__(
        self,
        title: str,
        api_key: str,
        schemaversion: str,
        sources: list[SourceSpec],
        layer_name: str,
        geometry: str | None,
        bbox,
        output_dir: Path,
        stamp: str,
        style: str = "",
    ):
        super().__init__(f"NVDB: hämtar {title}", QgsTask.Flag.CanCancel)
        self.api_key = api_key
        self.schemaversion = schemaversion
        self.sources = sources
        self.layer_name = layer_name
        self.geometry = geometry
        self.bbox = bbox
        self.style = style
        self.gpkg_path = output_dir / f"{layer_name}_{stamp}.gpkg"
        self.feature_count = 0
        self.error: str | None = None
        self._feedback = QgsFeedback()

    def cancel(self) -> None:
        self._feedback.cancel()  # aborts an in-flight request, not just the next page
        super().cancel()

    def run(self) -> bool:
        records: list[dict] = []
        self.status.emit("söker…")
        try:
            for source in self.sources:
                client = NvdbClient(
                    self.api_key, source.namespace, self.schemaversion, self._feedback
                )
                for page_no, page in enumerate(
                    client.pages(source.objecttype, self.bbox), start=1
                ):
                    if source.transform:
                        page = [r for r in map(source.transform, page) if r is not None]
                    records.extend(page)
                    self.status.emit(
                        f"{source.objecttype}: {len(records)} objekt hämtade (anrop {page_no})"
                    )
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
                records, self.gpkg_path, self.layer_name, self.geometry
            )
        except Exception as e:  # noqa: BLE001 — report any write failure to the UI
            self.error = str(e)
            return False
        return True

    def finished(self, result: bool) -> None:
        if result:
            self.completed.emit(
                str(self.gpkg_path), self.layer_name, self.feature_count, self.style
            )
        elif not self.isCanceled():
            message = self.error or "Okänt fel"
            QgsMessageLog.logMessage(message, PLUGIN_NAME, Qgis.MessageLevel.Critical)
            self.failed.emit(message)
