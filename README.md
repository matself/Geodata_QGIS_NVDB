# Geodata_QGIS_NVDB
QGIS plugin to search and download NVDB road data from Trafikverket's open API
(Datautbytesportalen, "API Öppna Data") and save it as GeoPackage in SWEREF 99 TM.

The plugin is independent and not developed by Trafikverket.

## Status
Early prototype (0.1.0). Works end to end: API key → select object types → area
(map extent or all of Sweden) → GeoPackage → layer in the project.

37 of the 45 NVDB object types listed on the portal answer with data in namespace
`vägdata.nvdb_dk_o`, schema version 1.2. The other eight (Betalstation,
Katastroföverfart, PlankorsningVägJärnväg, Rastplatser, Sidoanläggningsväg, Trafik,
Vägklasser_För_Trafik_Och_Skyddsanordningar, Vägslag) return "does not exist" and are
marked `verified: false` in `nvdb_downloader/datasets.json`.

## API
| | |
|---|---|
| Endpoint | `POST https://api.trafikinfo.trafikverket.se/v2/data.json` (XML request body) |
| Auth | API key from data.trafikverket.se, sent in the request (`LOGIN authenticationkey`) |
| Geofilter | `WITHIN` box on `Geometry.WKT-SWEREF99TM-3D` |
| Paging | `limit` + `skip`, 10 000 per page |

The key is stored in QGIS' encrypted authentication database, never in plain text.

## Layout
- `nvdb_downloader/` – the plugin (`core/` has no UI; `core/query.py` has no QGIS imports)
- `tests/` – `python -m unittest discover -s tests`

## Known issues
- `limit=200000` in a single request hung; keep pages ≤ 50 000.
- Fields are all kept as returned (values such as `Högsta_tillåtna_hastighet` are strings).
- No styling, icon or English/Swedish split of the UI yet.
