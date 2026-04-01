import xml.etree.ElementTree as ET
import json

def prepare_peg_name(peg_name):
    return peg_name[:-2] + "_P"

def create_parent_peg(next_id, child_peg, pegbars):
    child_peg_name = child_peg.find(".//name").text.strip()
    parent_peg_name = prepare_peg_name(child_peg_name)
    parent_peg = ET.SubElement(pegbars, "pegbar", {"id": "Peg" + str(next_id)})
    
    center = "0 0 0 0"
    
    ET.SubElement(parent_peg, "parent", {
        "handle": "B", 
        "id": "Table", 
        "parentHandle": "B"
    })

    name = ET.SubElement(parent_peg, "name")
    name.text = parent_peg_name
    
    ET.SubElement(parent_peg, "isOpened").text = " 0 "
    ET.SubElement(parent_peg, "status").text = " 0 "

    ET.SubElement(parent_peg, "center").text = f" {center} "

    ET.SubElement(parent_peg, "isOpened").text = " 0 "
    ET.SubElement(parent_peg, "status").text = " 0 "

    for tag in ["sx", "sy", "sc"]:
        parent_tag = ET.SubElement(parent_peg, tag)
        default = ET.SubElement(parent_tag, "default")
        default.text = " 1 "

    # 7. Add node position
    ET.SubElement(parent_peg, "nodePos").text = " 24350.6 24990.9 "
    
    return parent_peg


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


def inject_offsets(tnz_path, json_path, output_path, dpi=120):
    with open(json_path, 'r') as f:
        raw_offsets = json.load(f)
    
    offsets = {k.replace('\x00', ''): v for k, v in raw_offsets.items()}
    print(offsets)
    tree = ET.parse(tnz_path)
    root = tree.getroot()
    pegbars = root.find(".//pegbars")
    pegs_counter = 0
    for p in pegbars.findall("pegbar"):
        peg_name = ""
        peg_name_element = p.find(".//name")
        if peg_name_element is not None:
            peg_name = peg_name_element.text.strip()
        if peg_name in offsets:
            tpx = offsets[peg_name]['x']
            tpy = offsets[peg_name]['y']

            sx = tpx / dpi
            sy = tpy / dpi
            
            new_center_value = f"{str(sx)} {str(sy)} 0 0"
            
            p.find(".//center").text = new_center_value

            inject_compensation(p, sx, sy)

            pegs_counter += 1
            parent_peg = create_parent_peg(pegs_counter, p, pegbars)
            parent_peg.find(".//center").text = new_center_value
            inject_compensation(parent_peg, sx, sy)
            p.find(".//parent").attrib["id"] = parent_peg.attrib["id"]

    tree.write(output_path, encoding="utf-8")
    print(f"Successfully injected {len(offsets)} pivots into {output_path}")
