"""Extract one layer's style from a Lantmäteriet Topografi 10 .qlr into a QML.

Usage: python tools/make_topo10_vaglinje_style.py <Topografi10_vektor.qlr> <Layer name> <out.qml>
e.g.   ... thematic.qlr Väglinje nvdb_downloader/styles/topo10_vaglinje.qml

The styles filter on Topo10 attributes (objekttypnr, ...); see core/topo10.py.
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

KEEP = ("renderer-v2", "labeling", "blendMode", "featureBlendMode", "layerOpacity")


def main(qlr: Path, layer_name: str, out: Path) -> None:
    root = ET.parse(qlr).getroot()
    layer = next(m for m in root.iter("maplayer") if m.findtext("layername") == layer_name)
    qgis = ET.Element("qgis", version="3.34.0", styleCategories="Symbology|Labeling|Rendering")
    for tag in KEEP:
        node = layer.find(tag)
        if node is not None:
            qgis.append(node)
    ET.indent(qgis)
    out.write_text("<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>\n"
                   + ET.tostring(qgis, encoding="unicode"), encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]))
