"""Recipes that emulate Lantmäteriet's Topografi 10 road layers from NVDB data.

Each Topo10 layer is built from one or more named Trafikverket products (see the
Topo10 product description, Tema Kommunikation). A recipe lists those sources, how
each record is mapped onto Topo10's attributes, and the QML style to apply.
A transform returns the mapped record, or None to drop it.

No QGIS imports: testable with plain Python.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

Record = dict[str, Any]
Transform = Callable[[Record], "Record | None"]

NO_INFO = "Ingen information"

# Vägslag.Typ -> Topo10 objekttypnr (1816 Oklassificerad does not occur in the API).
VAGSLAG_TYP_NR = {
    "Motorväg": 1801,
    "Motortrafikled": 1802,
    "Mötesfri väg": 1803,
    "Landsväg": 1804,
    "Landsväg liten": 1805,
    "Småväg": 1806,
    "Småväg enkel standard": 1807,
    "Övergripande länk": 1808,
    "Huvudgata": 1809,
    "Lokalgata stor": 1810,
    "Lokalgata liten": 1811,
    "Kvartersväg": 1812,
    "Parkeringsområdesväg": 1813,
    "Infartsväg/Utfartsväg": 1814,
    "Leveransväg": 1815,
}


def vaglinje(record: Record) -> Record:
    """Vägslag -> Väglinje. Keeps all Vägslag fields and adds the Topo10 ones."""
    typ = record.get("Typ")
    record["objekttypnr"] = VAGSLAG_TYP_NR.get(typ, 1816)
    record["objekttyp"] = typ or "Oklassificerad"
    # GeoPackage field names are case-insensitive: rename, do not duplicate.
    record["bro_och_tunnel"] = record.pop("Bro_och_tunnel", None) or NO_INFO
    record["avfartsvag_pafartsvag"] = record.get("Avfartsväg_Påfartsväg") or "Nej"
    record["gatunamn"] = record.pop("Gatunamn", None)
    return record


def _point(record: Record, **fields: Any) -> Record:
    """A minimal Topo10-shaped record: identity, geometry and the given fields."""
    out = {"objektidentitet": record.get("Feature_Oid"), "Geometry": record.get("Geometry")}
    out.update(fields)
    return out


def vaghinder(record: Record) -> Record:
    typ = record.get("Hindertyp")
    return _point(
        record,
        objekttypnr=2203,
        objekttyp="Väghinder",
        vaghindertyp="övrigt hinder" if typ == "övrigt" else typ,
        # Lantmäteriet computes the symbol rotation from the road; 0 is an approximation.
        rotation=0.0,
    )


def rastplats(record: Record) -> Record:
    return _point(
        record, objekttypnr=2207, objekttyp="Rastplats", trv_namn=record.get("Rastplatsnamn")
    )


def cirkulationsplats(record: Record) -> Record | None:
    """Korsning -> Cirkulationsplats (2210). Trafikplats (2209) is not emulated yet."""
    if record.get("Generaliseringstyp") != "cirkulationsplats":
        return None
    return _point(
        record, objekttypnr=2210, objekttyp="Cirkulationsplats", trv_namn=record.get("Namn")
    )


def farjeled(record: Record) -> Record:
    return _point(
        record, objekttypnr=1891, objekttyp="Färjeled", destination=record.get("Färjeledsnamn")
    )


@dataclass(frozen=True)
class Source:
    dataset_id: str
    transform: Transform


@dataclass(frozen=True)
class Recipe:
    id: str
    title: str  # shown in the UI
    layer_name: str  # Topo10 layer name, also the GeoPackage layer
    geometry: str  # "linestring" or "point"
    style: str  # styles/<style>.qml
    sources: tuple[Source, ...]
    note: str = ""


RECIPES: tuple[Recipe, ...] = (
    Recipe(
        "vaglinje", "Väglinje", "vaglinje", "linestring", "topo10_vaglinje",
        (Source("Vägslag", vaglinje),),
    ),
    Recipe(
        "vagpunkt", "Vägpunkt", "vagpunkt", "point", "topo10_vagpunkt",
        (
            Source("Väghinder", vaghinder),
            Source("Rastplatser", rastplats),
            Source("Korsning", cirkulationsplats),
        ),
        note="Saknar Vändmöjlighet och Trafikplats; Väghinder utan vägriktning.",
    ),
    Recipe(
        "farjeled", "Färjeled", "farjeled", "linestring", "topo10_farjeled",
        (Source("Färjeled", farjeled),),
    ),
)


def recipe(recipe_id: str) -> Recipe:
    return next(r for r in RECIPES if r.id == recipe_id)
