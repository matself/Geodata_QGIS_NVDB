"""Pure helpers (no QGIS imports) to build requests to and parse responses from
Trafikverket's Öppna API (datacache)."""

from __future__ import annotations

from typing import Any
from xml.sax.saxutils import quoteattr

GEOMETRY_FIELD = "Geometry.WKT-SWEREF99TM-3D"
WKT_KEY = "WKT-SWEREF99TM-3D"


class NvdbApiError(Exception):
    pass


def build_request(
    api_key: str,
    objecttype: str,
    namespace: str,
    schemaversion: str,
    limit: int,
    skip: int = 0,
    bbox: tuple[float, float, float, float] | None = None,
) -> str:
    """XML request for one page. `bbox` is (xmin, ymin, xmax, ymax) in SWEREF 99 TM.

    Uses INTERSECTS so objects crossing the box edge are included (WITHIN drops them)."""
    if bbox:
        xmin, ymin, xmax, ymax = bbox
        value = f"{xmin:.1f} {ymin:.1f}, {xmax:.1f} {ymax:.1f}"
        within = (
            f'<INTERSECTS name="{GEOMETRY_FIELD}" shape="box" value={quoteattr(value)}/>'
        )
    else:
        within = ""
    skip_attr = f' skip="{int(skip)}"' if skip else ""
    return (
        "<REQUEST>"
        f"<LOGIN authenticationkey={quoteattr(api_key)}/>"
        f"<QUERY objecttype={quoteattr(objecttype)} namespace={quoteattr(namespace)}"
        f' schemaversion={quoteattr(schemaversion)} limit="{int(limit)}"{skip_attr}>'
        f"<FILTER>{within}</FILTER>"
        "</QUERY></REQUEST>"
    )


def parse_response(data: dict[str, Any], objecttype: str) -> list[dict[str, Any]]:
    """Return the records of one page; raise NvdbApiError on an API error."""
    try:
        result = data["RESPONSE"]["RESULT"][0]
    except (KeyError, IndexError, TypeError) as e:
        raise NvdbApiError(f"Oväntat svar från API:t: {str(data)[:200]}") from e
    if "ERROR" in result:
        raise NvdbApiError(result["ERROR"].get("MESSAGE", "Okänt API-fel"))
    return result.get(objecttype) or []


def flatten(record: dict[str, Any]) -> tuple[dict[str, Any], str | None]:
    """Split a record into (attributes, SWEREF 99 TM WKT)."""
    attrs = {k: v for k, v in record.items() if k != "Geometry"}
    wkt = (record.get("Geometry") or {}).get(WKT_KEY)
    return attrs, wkt
