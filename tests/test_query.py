"""Tests for the pure query helpers. Run: python -m unittest discover -s tests"""

import importlib.util
import sys
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


_T = importlib.util.spec_from_file_location(
    "topo10", Path(__file__).resolve().parent.parent / "nvdb_downloader" / "core" / "topo10.py"
)
topo10 = importlib.util.module_from_spec(_T)
sys.modules["topo10"] = topo10  # dataclasses needs the module registered
_T.loader.exec_module(topo10)


class Topo10Test(unittest.TestCase):
    def test_vaglinje_fields(self):
        rec = topo10.vaglinje({"Typ": "Landsväg liten", "Avfartsväg_Påfartsväg": "Ja",
                               "Bro_och_tunnel": None, "Gatunamn": "Storgatan"})
        self.assertEqual(rec["objekttypnr"], 1805)
        self.assertEqual(rec["bro_och_tunnel"], "Ingen information")
        self.assertEqual(rec["avfartsvag_pafartsvag"], "Ja")
        self.assertEqual(rec["gatunamn"], "Storgatan")
        self.assertNotIn("Gatunamn", rec)  # renamed: GeoPackage fields are case-insensitive

    def test_unknown_typ_is_unclassified(self):
        self.assertEqual(topo10.vaglinje({"Typ": "Något nytt"})["objekttypnr"], 1816)

    def test_vaghinder(self):
        rec = topo10.vaghinder({"Hindertyp": "övrigt", "Feature_Oid": "1:2", "Geometry": {"g": 1}})
        self.assertEqual((rec["objekttypnr"], rec["vaghindertyp"]), (2203, "övrigt hinder"))

    def test_korsning_only_cirkulationsplats(self):
        self.assertIsNone(topo10.cirkulationsplats({"Generaliseringstyp": "enkel korsning"}))
        rec = topo10.cirkulationsplats({"Generaliseringstyp": "cirkulationsplats", "Namn": "X"})
        self.assertEqual(rec["objekttypnr"], 2210)

    def test_every_recipe_source_is_in_the_register(self):
        import json
        path = Path(__file__).resolve().parent.parent / "nvdb_downloader" / "datasets.json"
        ids = {d["id"] for d in json.loads(path.read_text(encoding="utf-8"))["datasets"] if d["verified"]}
        for r in topo10.RECIPES:
            for source in r.sources:
                self.assertIn(source.dataset_id, ids)


if __name__ == "__main__":
    unittest.main()
