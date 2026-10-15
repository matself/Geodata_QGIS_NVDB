"""HTTP client for the Öppna API. Uses QgsBlockingNetworkRequest so QGIS proxy and
SSL settings apply. Safe to use from a QgsTask worker thread."""

from __future__ import annotations

import json
from collections.abc import Iterator
from typing import Any

from qgis.core import QgsBlockingNetworkRequest, QgsFeedback
from qgis.PyQt.QtCore import QByteArray, QUrl
from qgis.PyQt.QtNetwork import QNetworkRequest

from ..config import API_URL, PAGE_LIMIT
from .query import NvdbApiError, build_request, parse_response


class NvdbClient:
    def __init__(self, api_key: str, namespace: str, schemaversion: str,
                 feedback: QgsFeedback | None = None):
        self.api_key = api_key
        self.namespace = namespace
        self.schemaversion = schemaversion
        self.feedback = feedback

    def _post(self, xml: str) -> dict[str, Any]:
        request = QNetworkRequest(QUrl(API_URL))
        request.setHeader(
            QNetworkRequest.KnownHeaders.ContentTypeHeader, "text/xml; charset=utf-8"
        )
        blocking = QgsBlockingNetworkRequest()
        error = blocking.post(request, QByteArray(xml.encode("utf-8")), True, self.feedback)
        reply = blocking.reply()
        content = bytes(reply.content()).decode("utf-8", "replace")
        if error != QgsBlockingNetworkRequest.ErrorCode.NoError:
            # The API puts a readable message in the 400 body.
            try:
                message = json.loads(content)["RESPONSE"]["RESULT"][0]["ERROR"]["MESSAGE"]
            except (ValueError, KeyError, IndexError, TypeError):
                message = f"{blocking.errorMessage()} {content[:300]}".strip()
            raise NvdbApiError(message)
        try:
            return json.loads(content)
        except ValueError as e:
            raise NvdbApiError(f"Ogiltigt JSON-svar: {e}") from e

    def pages(self, objecttype: str, bbox=None, limit: int = PAGE_LIMIT) -> Iterator[list[dict]]:
        """Yield one list of records per page until the data is exhausted."""
        skip = 0
        while True:
            if self.feedback and self.feedback.isCanceled():
                return
            xml = build_request(
                self.api_key, objecttype, self.namespace, self.schemaversion, limit, skip, bbox
            )
            records = parse_response(self._post(xml), objecttype)
            if records:
                yield records
            if len(records) < limit:
                return
            skip += limit
