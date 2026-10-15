"""The API key lives in QGIS' encrypted authentication database.

The plugin only keeps the id of the auth configuration (authcfg). The key is
sent in the request body, so it is read from the configuration when needed.
"""

from __future__ import annotations

from qgis.core import QgsApplication, QgsAuthMethodConfig


def store_api_key(name: str, api_key: str) -> str:
    """Store the key as a Basic auth configuration; returns the authcfg id."""
    auth_manager = QgsApplication.authManager()
    if not auth_manager.setMasterPassword(True):
        raise RuntimeError("QGIS huvudlösenord krävs för att spara nyckeln.")
    config = QgsAuthMethodConfig("Basic")
    config.setName(name)
    config.setConfig("username", "nvdb")
    config.setConfig("password", api_key)
    result = auth_manager.storeAuthenticationConfig(config)
    ok, config = result if isinstance(result, tuple) else (result, config)
    if not ok or not config.id():
        raise RuntimeError("Kunde inte spara nyckeln.")
    return config.id()


def load_api_key(authcfg: str) -> str:
    """Return the stored key, or "" if the configuration is missing."""
    if not authcfg or authcfg not in QgsApplication.authManager().configIds():
        return ""
    config = QgsAuthMethodConfig()
    ok = QgsApplication.authManager().loadAuthenticationConfig(authcfg, config, True)
    if isinstance(ok, tuple):
        ok = ok[0]
    return config.config("password") if ok else ""
