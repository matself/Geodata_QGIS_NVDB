"""Loads the dataset register (datasets.json)."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

REGISTRY_PATH = Path(__file__).resolve().parent.parent / "datasets.json"


@dataclass(frozen=True)
class Dataset:
    id: str
    title: str
    geometry: str | None  # "linestring" or "point"
    verified: bool = False
    namespace: str | None = None  # overrides the register default


@dataclass(frozen=True)
class Registry:
    namespace: str
    schemaversion: str
    datasets: tuple[Dataset, ...]

    def get(self, dataset_id: str) -> Dataset:
        return next(d for d in self.datasets if d.id == dataset_id)

    def namespace_of(self, dataset: Dataset) -> str:
        return dataset.namespace or self.namespace


def load_registry(path: Path = REGISTRY_PATH) -> Registry:
    raw = json.loads(path.read_text(encoding="utf-8"))
    datasets = tuple(
        Dataset(
            d["id"], d.get("title", d["id"]), d.get("geometry"),
            d.get("verified", False), d.get("namespace"),
        )
        for d in raw["datasets"]
    )
    return Registry(raw["namespace"], raw["schemaversion"], datasets)
