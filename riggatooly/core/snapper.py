from psd_tools import PSDImage
import numpy as np


def get_color_pivot(layer, target_rgb):
    if  layer.topil() is not None:
        img = layer.topil().convert('RGB')
        data = np.array(img)
        
        mask = np.all(data == target_rgb, axis=-1)
        coords = np.argwhere(mask)
        
        if coords.size == 0:
            return None
            
        local_y, local_x = coords.mean(axis=0)
        global_x = layer.left + local_x
        global_y = layer.top + local_y
        
        return (global_x, global_y)
    
    return None

def calculate_offsets(psd_path, target_rgb):
    psd = PSDImage.open(psd_path)
    canvas_w, canvas_h = psd.width, psd.height
    
    rig_data = {
        "ParentPegs": []
    }

    def walk_layers(item):
        if item.is_group() and item.is_visible():
            for child in item: walk_layers(child)
        elif item.is_visible() and item.parent.name != "ParentPegs":
            pivot = get_color_pivot(item, target_rgb)
            if pivot:
                gx, gy = pivot
                tx = gx - (canvas_w / 2)
                ty = (canvas_h / 2) - gy
                
                rig_data[item.name] = {"x": round(tx, 2), "y": round(ty, 2)}
        elif item.is_visible() and item.parent.name == "ParentPegs":
            rig_data["ParentPegs"].append(item.name)

    for layer in psd:
        walk_layers(layer)
        
    return rig_data
