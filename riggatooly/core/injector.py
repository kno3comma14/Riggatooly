import xml.etree.ElementTree as ET
import json

def inject_compensation(peg_element, stage_x, stage_y):
    x_tag = peg_element.find("x")
    if x_tag is None:
        x_tag = ET.SubElement(peg_element, "x")
    
    x_default = x_tag.find("default")
    if x_default is None:
        x_default = ET.SubElement(x_tag, "default")
    
    x_default.text = f" {round(stage_x, 5)} "

    y_tag = peg_element.find("y")
    if y_tag is None:
        y_tag = ET.SubElement(peg_element, "y")
    
    y_default = y_tag.find("default")
    if y_default is None:
        y_default = ET.SubElement(y_tag, "default")
    
    y_default.text = f" {round(stage_y, 5)} "


def inject_offsets(tnz_path, json_path, output_path):
    with open(json_path, 'r') as f:
        raw_offsets = json.load(f)
    
    offsets = {k.replace('\x00', ''): v for k, v in raw_offsets.items()}
    print(offsets)
    tree = ET.parse(tnz_path)
    root = tree.getroot()
    pegbars = root.find(".//pegbars")
    for p in pegbars.findall("pegbar"):
        peg_name = ""
        peg_name_element = p.find(".//name")
        if peg_name_element is not None:
            peg_name = peg_name_element.text.strip()
            print(peg_name)
        if peg_name in offsets:
            print("In offset")
            dpi = 120
            
            tpx = offsets[peg_name]['x']
            tpy = offsets[peg_name]['y']

            sx = tpx / dpi
            sy = tpy / dpi
            
            new_center_value = f"{str(sx)} {str(sy)} 0 0"
            
            p.find(".//center").text = new_center_value

            inject_compensation(p, sx, sy)
                


    tree.write(output_path, encoding="utf-8")
    # print(f"Successfully injected {len(offsets)} pivots into {output_path}")

# if __name__ == "__main__":
#     inject_offsets("/Users/enyertvinas/Projects/learning/drawing/basics/tahoma2d/serious_step/serious_steps/scenes/testing_auto_snapping.tnz", 
#                    "rig_offsets.json", 
#                    "/Users/enyertvinas/Projects/learning/drawing/basics/tahoma2d/serious_step/serious_steps/scenes/testing_auto_snapping.tnz")
