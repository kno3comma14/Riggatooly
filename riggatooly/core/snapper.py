from psd_tools import PSDImage
import numpy as np
from riggatooly import utils
import json

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.floating, np.float64, np.float32)):
            return float(obj)
        if isinstance(obj, (np.integer, np.int64, np.int32)):
            return int(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


def get_image_data(layer):
    return layer.topil()

def save_image(layer, rig_data, image_name, format="png"):
    image_data = get_image_data(layer)
    path = rig_data["metadata"]["image_folder_path"] + "/" + utils.clean_string(image_name) + "." + format    
    if image_data:
        image_data.save(path)

def save_image_list(targets_to_save, rig_data, format="png"):
    for target in targets_to_save:
        save_image(target, rig_data, target.name, format)

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

def calculate_offsets(psd_path, image_folder_path, target_rgb, enable_peg_per_drawing):
    psd = PSDImage.open(psd_path)
    canvas_w, canvas_h = psd.width, psd.height
    
    rig_data = {
        "metadata": {
            "width": canvas_w, 
            "height": canvas_h,
            "psd_path": psd_path,
            "image_folder_path": image_folder_path
        },
        "parent_pegs": [], 
        "parts": {}
    }

    def walk_layers(item):
        clean_name = utils.clean_string(item.name)
        
        if clean_name == "ParentPegs" and item.is_group():
            rig_data["parent_pegs"] = [utils.clean_string(child.name) for child in item]
            return
        elif clean_name == "Puppet" and item.is_group():
            targets_to_save = [child for child in item]
            save_image_list(targets_to_save, rig_data)
            

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
        
    if not enable_peg_per_drawing:
        for p in rig_data["parts"].keys():
            if p in rig_data["parent_pegs"]:    
                rig_data["parts"][p]["parent"] = p + "-P"
            else:
                rig_data["parts"][p]["parent"] = None
    else:
        for p in rig_data["parts"].keys():
            rig_data["parts"][p]["parent"] = p + "-P"

    del rig_data["parent_pegs"]

    with open(image_folder_path + "/manifest.json", "w") as f:
        json.dump(rig_data, f, indent=4, cls=NpEncoder)
    
    return rig_data