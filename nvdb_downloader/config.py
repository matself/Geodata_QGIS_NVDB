"""Endpoints and constants for Trafikverket's Öppna API (NVDB data)."""

PLUGIN_NAME = "Geodata: NVDB (Trafikverket)"
SETTINGS_PREFIX = "nvdb_downloader"

API_URL = "https://api.trafikinfo.trafikverket.se/v2/data.json"
NVDB_CRS = "EPSG:3006"  # SWEREF 99 TM
PAGE_LIMIT = 10000
