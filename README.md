# Geodata_QGIS_NVDB
QGIS plugin to search and download NVDB road data from Trafikverket's open API
(Datautbytesportalen, "API Öppna Data") and save it as GeoPackage in SWEREF 99 TM.

The plugin is independent and not developed by Trafikverket.

## Status
Early prototype (0.1.0). Works end to end: API key → select object types → area
(map extent or all of Sweden) → GeoPackage → layer in the project.

All 45 NVDB object types on the portal answer with data. Namespace and schema version
are set per type in `nvdb_downloader/datasets.json` (`vägdata.nvdb_dk_o`,
`Vägdata.AGGREGAT_O`, `Vägdata.VIS_DK_O`, `Vägdata.TRAFIK_DK_O`).

## Two tabs
1. **Rådata** – pick any NVDB table and an area, get the records as they are.
2. **Topo10-uttag** – emulates Lantmäteriet's Topografi 10 road layers from NVDB and
   applies the Topo10 style (extracted from a Topo10 `.qlr`). Each layer is a *recipe*
   in `core/topo10.py`: source tables + attribute mapping + QML.

| Topo10 layer | Built from | Known gaps |
|---|---|---|
| Väglinje | Vägslag | Oklassificerad (1816) does not occur in the API |
| Vägpunkt | Väghinder, Rastplatser, Korsning (cirkulationsplats) | No Vändmöjlighet or Trafikplats; Väghinder rotation fixed at 0 |
| Färjeled | Färjeled | Only the ferry name is mapped |

Övrig väg and Rälstrafik are not NVDB products and are not emulated. If you only need
Topo10 itself, Lantmäteriet's ready-made Topografi 10 download is simpler; this tab is
for NVDB's fresher data and for cutting out an area through the API.

## API
| | |
|---|---|
| Endpoint | `POST https://api.trafikinfo.trafikverket.se/v2/data.json` (XML request body) |
| Auth | API key from data.trafikverket.se, sent in the request (`LOGIN authenticationkey`) |
| Geofilter | `INTERSECTS` box on `Geometry.WKT-SWEREF99TM-3D` |
| Paging | `limit` + `skip`, 10 000 per page |

The key is stored in QGIS' encrypted authentication database, never in plain text.

## Layout
- `nvdb_downloader/` – the plugin (`core/` has no UI; `core/query.py` has no QGIS imports)
- `tools/make_topo10_style.py` – extract a layer style from a Topo10 `.qlr`
- `tests/` – `python -m unittest discover -s tests`

## Known issues
- `limit=200000` in a single request hung; keep pages ≤ 50 000.
- Fields are all kept as returned (values such as `Högsta_tillåtna_hastighet` are strings).
- No styling, icon or English/Swedish split of the UI yet.
