"""Tests for the pure query helpers. Run: python -m unittest discover -s tests"""

import importlib.util
import unittest
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "query", Path(__file__).resolve().parent.parent / "nvdb_downloader" / "core" / "query.py"
)
query = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(query)


class BuildRequestTest(unittest.TestCase):
    def test_bbox_and_paging(self):
        xml = query.build_request(
            "KEY", "Hastighetsgräns", "vägdata.nvdb_dk_o", "1.2", 100, 200,
            (674000, 6579000, 676000, 6581000),
        )
        self.assertIn('objecttype="Hastighetsgräns"', xml)
        self.assertIn('skip="200"', xml)
        self.assertIn('shape="box" value="674000.0 6579000.0, 676000.0 6581000.0"', xml)

    def test_no_bbox_has_empty_filter(self):
        xml = query.build_request("K", "Vägnummer", "ns", "1.2", 10)
        self.assertIn("<FILTER></FILTER>", xml)
        self.assertNotIn("skip=", xml)

    def test_key_is_escaped(self):
        xml = query.build_request('a"b', "T", "ns", "1.2", 1)
        self.assertNotIn('authenticationkey="a"b"', xml)


class ParseTest(unittest.TestCase):
    def test_records(self):
        data = {"RESPONSE": {"RESULT": [{"T": [{"GID": 1}]}]}}
        self.assertEqual(query.parse_response(data, "T"), [{"GID": 1}])

    def test_error(self):
        data = {"RESPONSE": {"RESULT": [{"ERROR": {"MESSAGE": "boom"}}]}}
        with self.assertRaises(query.NvdbApiError):
            query.parse_response(data, "T")

    def test_flatten(self):
        attrs, wkt = query.flatten(
            {"GID": 1, "Geometry": {"WKT-SWEREF99TM-3D": "POINT Z (1 2 3)"}}
        )
        self.assertEqual(attrs, {"GID": 1})
        self.assertEqual(wkt, "POINT Z (1 2 3)")


if __name__ == "__main__":
    unittest.main()
