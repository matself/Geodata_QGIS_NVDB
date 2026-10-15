<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.34.0" styleCategories="Symbology|Labeling|Rendering">
  <renderer-v2 enableorderby="0" symbollevels="0" forceraster="0" type="RuleRenderer" referencescale="-1">
    <rules key="{c1272a98-38fc-4be9-89e0-11f44198a817}">
      <rule key="{fc8d37f4-36f4-4f28-a21c-56aeb500ca1c}" label="Pollare" symbol="0" filter="&quot;objekttypnr&quot; = 2203  AND  &quot;vaghindertyp&quot; IS  'pollare'" />
      <rule key="{8b18faee-6e28-4c95-a402-f8c85a4648ad}" label="Eftergivlig grind" symbol="1" filter="&quot;objekttypnr&quot; = 2203  AND  &quot;vaghindertyp&quot; IS  'eftergivlig grind'" />
      <rule key="{e27169ff-3504-4f4e-8697-df7c30535b01}" label="Ej öppningsbar grind eller cykelfålla" symbol="2" filter="&quot;objekttypnr&quot; = 2203  AND  &quot;vaghindertyp&quot; IS  'ej öppningsbar grind eller cykelfålla' " />
      <rule key="{70195947-8519-44a8-992a-550f7f8b9833}" label="Låst grind eller bom" symbol="3" filter="&quot;objekttypnr&quot; = 2203  AND  &quot;vaghindertyp&quot; IS 'låst grind eller bom' AND  &quot;rotation&quot;  IS  NOT  NULL " />
      <rule key="{1252ebbf-1670-4421-adc3-2ed4a05493a1}" label="Betonghinder" symbol="4" filter="&quot;objekttypnr&quot; = 2203  AND  &quot;vaghindertyp&quot; IS  'betonghinder'" />
      <rule key="{a10fe816-75e6-4f8d-954e-196ee25ca27b}" label="Spårviddshinder" symbol="5" filter="&quot;objekttypnr&quot; = 2203  AND  &quot;vaghindertyp&quot; IS  'spårviddshinder'" />
      <rule key="{4d554ac8-19f5-4958-aff3-c801ed57ab6e}" label="Övrigt hinder" symbol="6" filter="&quot;objekttypnr&quot; = 2203  AND  &quot;vaghindertyp&quot; IS  'övrigt hinder'" />
      <rule key="{da9a833a-f120-4d27-91ba-75fde5e86991}" label="Stenhinder" symbol="7" filter="&quot;objekttypnr&quot; = 2203  AND  &quot;vaghindertyp&quot; IS  'stenhinder'" />
      <rule key="{14a68324-1bc1-4e9d-b764-5cfae411e1f1}" label="Vändplan" symbol="8" filter="&quot;objekttypnr&quot; = 2205  AND  &quot;vandmojlighetstyp&quot;  IN  (  'vändplan'  ) " />
      <rule key="{e5b42f62-9350-4241-a3df-32565d0b4d7b}" label="Rastplats" symbol="9" filter="&quot;objekttypnr&quot; = 2207" />
    </rules>
    <symbols>
      <symbol name="0" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{d23f16ba-f084-472b-937d-d95483ce5732}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="" type="QString" />
            <Option name="color" value="78,78,78,255,rgb:0.3058824,0.3058824,0.3058824,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-0.29999999999999993" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="2.5" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool" />
                  <Option name="expression" value="coalesce(scale_linear(&quot;rotation&quot; , 0, 360, 0, 360), 0)-90" type="QString" />
                  <Option name="type" value="3" type="int" />
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="1" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{d23f16ba-f084-472b-937d-d95483ce5732}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="" type="QString" />
            <Option name="color" value="78,78,78,255,rgb:0.3058824,0.3058824,0.3058824,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-0.29999999999999993" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="2.5" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool" />
                  <Option name="expression" value="coalesce(scale_linear(&quot;rotation&quot; , 0, 360, 0, 360), 0)-90" type="QString" />
                  <Option name="type" value="3" type="int" />
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="2" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{d23f16ba-f084-472b-937d-d95483ce5732}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="" type="QString" />
            <Option name="color" value="78,78,78,255,rgb:0.3058824,0.3058824,0.3058824,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-0.29999999999999993" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="2.5" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool" />
                  <Option name="expression" value="coalesce(scale_linear(&quot;rotation&quot; , 0, 360, 0, 360), 0)-90" type="QString" />
                  <Option name="type" value="3" type="int" />
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="3" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{d23f16ba-f084-472b-937d-d95483ce5732}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="\" type="QString" />
            <Option name="color" value="78,78,78,255,rgb:0.3058824,0.3058824,0.3058824,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-1" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="3.175" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool" />
                  <Option name="field" value="rotation" type="QString" />
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option name="curve" type="Map">
                        <Option name="x" value="0,1" type="QString" />
                        <Option name="y" value="0,1" type="QString" />
                      </Option>
                      <Option name="exponent" value="1" type="double" />
                      <Option name="maxOutput" value="360" type="double" />
                      <Option name="maxValue" value="360" type="double" />
                      <Option name="minOutput" value="0" type="double" />
                      <Option name="minValue" value="0" type="double" />
                      <Option name="nullOutput" value="0" type="double" />
                    </Option>
                    <Option name="t" value="0" type="int" />
                  </Option>
                  <Option name="type" value="2" type="int" />
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="4" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{d23f16ba-f084-472b-937d-d95483ce5732}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="" type="QString" />
            <Option name="color" value="78,78,78,255,rgb:0.3058824,0.3058824,0.3058824,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-0.29999999999999993" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="2.5" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool" />
                  <Option name="expression" value="coalesce(scale_linear(&quot;rotation&quot; , 0, 360, 0, 360), 0)-90" type="QString" />
                  <Option name="type" value="3" type="int" />
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="5" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{d23f16ba-f084-472b-937d-d95483ce5732}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="" type="QString" />
            <Option name="color" value="78,78,78,255,rgb:0.3058824,0.3058824,0.3058824,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-0.29999999999999993" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="2.5" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool" />
                  <Option name="expression" value="coalesce(scale_linear(&quot;rotation&quot; , 0, 360, 0, 360), 0)-90" type="QString" />
                  <Option name="type" value="3" type="int" />
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="6" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{d23f16ba-f084-472b-937d-d95483ce5732}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="" type="QString" />
            <Option name="color" value="78,78,78,255,rgb:0.3058824,0.3058824,0.3058824,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-0.29999999999999993" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="2.5" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool" />
                  <Option name="expression" value="coalesce(scale_linear(&quot;rotation&quot; , 0, 360, 0, 360), 0)-90" type="QString" />
                  <Option name="type" value="3" type="int" />
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="7" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{d23f16ba-f084-472b-937d-d95483ce5732}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="" type="QString" />
            <Option name="color" value="78,78,78,255,rgb:0.3058824,0.3058824,0.3058824,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-0.29999999999999993" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="2.5" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool" />
                  <Option name="expression" value="coalesce(scale_linear(&quot;rotation&quot; , 0, 360, 0, 360), 0)-90" type="QString" />
                  <Option name="type" value="3" type="int" />
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="8" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{e71946ac-b216-4254-baa5-fde4a4ecffb2}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="," type="QString" />
            <Option name="color" value="255,255,255,255,rgb:1,1,1,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-0.20000000000000001" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="2.117" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" />
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" pass="0" locked="0" id="{955577ca-5701-4ad1-8e7b-cb2251f482f4}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="]" type="QString" />
            <Option name="color" value="78,78,78,255,rgb:0.3058824,0.3058824,0.3058824,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-0.20000000000000001" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="2.469" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" />
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="9" is_animated="0" alpha="1" clip_to_extent="1" frame_rate="10" force_rhr="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString" />
            <Option name="properties" />
            <Option name="type" value="collection" type="QString" />
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" id="{a3926fda-fef5-428d-a8bd-3210b6aa367a}" class="FontMarker">
          <Option type="Map">
            <Option name="angle" value="0" type="QString" />
            <Option name="chr" value="" type="QString" />
            <Option name="color" value="196,73,130,255,rgb:0.7686275,0.2862745,0.5098039,1" type="QString" />
            <Option name="font" value="LMTopografisymboler" type="QString" />
            <Option name="font_style" value="" type="QString" />
            <Option name="horizontal_anchor_point" value="1" type="QString" />
            <Option name="joinstyle" value="bevel" type="QString" />
            <Option name="offset" value="0,-1.19999999999999996" type="QString" />
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="offset_unit" value="MM" type="QString" />
            <Option name="outline_color" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" type="QString" />
            <Option name="outline_width" value="0" type="QString" />
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="outline_width_unit" value="MM" type="QString" />
            <Option name="size" value="6.703" type="QString" />
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString" />
            <Option name="size_unit" value="MM" type="QString" />
            <Option name="vertical_anchor_point" value="1" type="QString" />
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString" />
              <Option name="properties" />
              <Option name="type" value="collection" type="QString" />
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <data-defined-properties>
      <Option type="Map">
        <Option name="name" value="" type="QString" />
        <Option name="properties" />
        <Option name="type" value="collection" type="QString" />
      </Option>
    </data-defined-properties>
  </renderer-v2>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
</qgis>