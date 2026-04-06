from psd_tools import PSDImage
import numpy as np
from riggatooly import utils

def get_color_pivot(psd_item, pil_img, target_rgb):
    data = np.array(pil_img.convert('RGBA'))
    mask = np.all(data == target_rgb, axis=-1)
    coords = np.argwhere(mask)
    
    if coords.size == 0:
        return None
        
    local_y, local_x = coords.mean(axis=0)
    
    global_x = psd_item.left + local_x
    global_y = psd_item.top + local_y
    
    return (global_x, global_y)

def calculate_offsets(psd_path, target_rgb):
    psd = PSDImage.open(psd_path)
    canvas_w, canvas_h = psd.width, psd.height
    
    rig_data = {"parent_pegs": [], "parts": {}}

    def walk_layers(item):
        clean_name = utils.clean_string(item.name)
        
        if clean_name == "ParentPegs" and item.is_group():
            rig_data["parent_pegs"] = [utils.clean_string(child.name) for child in item]
            return 

        if item.is_group() and item.is_visible():
            for child in item: 
                walk_layers(child)
            
        elif item.is_visible() and not item.is_group():
            if item.parent and utils.clean_string(item.parent.name) == "ParentPegs":
                return

            left, top, right, bottom = item.bbox 
            
            pixel_center_x = (left + right) / 2
            pixel_center_y = (top + bottom) / 2
            
            pos_x = pixel_center_x - (canvas_w / 2)
            pos_y = (canvas_h / 2) - pixel_center_y
            
            pil_image = item.topil()
            
            if pil_image is not None:
                pivot = get_color_pivot(item, pil_image, target_rgb)
                
                if pivot:
                    gx, gy = pivot
                    tx = gx - (canvas_w / 2)
                    ty = (canvas_h / 2) - gy
                    
                    rig_data["parts"][clean_name] = {
                        "pivote": {"x": float(tx), "y": float(ty)},
                        "position": {"x": float(pos_x), "y": float(pos_y)},
                        "bbox": [left, top, right, bottom]
                    }
            else:
                pass

    for layer in psd:
        walk_layers(layer)
        
    for p in rig_data["parts"].keys():
        if p in rig_data["parent_pegs"]:    
            rig_data["parts"][p]["parent"] = p + "-P"
        else:
            rig_data["parts"][p]["parent"] = None

    del rig_data["parent_pegs"]
    
    return rig_data