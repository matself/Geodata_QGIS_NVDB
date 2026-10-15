"""Write NVDB records to a GeoPackage layer (SWEREF 99 TM)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from osgeo import ogr, osr

from .query import flatten

_GEOMETRY_TYPES = {
    "point": ogr.wkbPoint,
    "linestring": ogr.wkbLineString,
}


def _field_type(value: Any) -> int:
    if isinstance(value, bool):
        return ogr.OFTInteger
    if isinstance(value, int):
        return ogr.OFTInteger64
    if isinstance(value, float):
        return ogr.OFTReal
    return ogr.OFTString


def _unique_case_insensitive(attrs: dict[str, Any], wkt: str | None):
    """GeoPackage field names are case-insensitive; keep the first of any clashing pair."""
    seen: set[str] = set()
    unique = {}
    for key, value in attrs.items():
        if key.lower() not in seen:
            seen.add(key.lower())
            unique[key] = value
    return unique, wkt


def write_gpkg(
    records: list[dict[str, Any]], path: Path, layer_name: str, geometry: str | None
) -> int:
    """Write records to `path`, replacing the file. Returns the number written."""
    rows = [_unique_case_insensitive(*flatten(r)) for r in records]
    types: dict[str, int] = {}
    for attrs, _ in rows:
        for key, value in attrs.items():
            if value is not None and key not in types:
                types[key] = _field_type(value)
        # Fields whose first records are null still need a column.
        for key in attrs:
            types.setdefault(key, ogr.OFTString)

    if path.exists():
        path.unlink()
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(3006)
    srs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)

    ds = ogr.GetDriverByName("GPKG").CreateDataSource(str(path))
    layer = ds.CreateLayer(
        layer_name, srs, _GEOMETRY_TYPES.get(geometry or "", ogr.wkbUnknown)
    )
    for key, ftype in types.items():
        layer.CreateField(ogr.FieldDefn(key, ftype))

    layer.StartTransaction()
    count = 0
    for attrs, wkt in rows:
        feature = ogr.Feature(layer.GetLayerDefn())
        for key, value in attrs.items():
            if value is not None:
                feature.SetField(key, int(value) if isinstance(value, bool) else value)
        if wkt:
            geom = ogr.CreateGeometryFromWkt(wkt)
            if geom is not None:
                geom.FlattenTo2D()  # Z is often the -99999 "missing" marker
                feature.SetGeometry(geom)
        layer.CreateFeature(feature)
        count += 1
    layer.CommitTransaction()
    ds = None  # flush and close
    return count
