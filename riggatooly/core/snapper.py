from psd_tools import PSDImage
import numpy as np
import json

def get_color_pivot(layer, target_rgb):
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

def calculate_offsets(psd_path, target_rgb):
    psd = PSDImage.open(psd_path)
    canvas_w, canvas_h = psd.width, psd.height
    
    rig_data = {}

    def walk_layers(item):
        if item.is_group():
            for child in item: walk_layers(child)
        else:
            pivot = get_color_pivot(item, target_rgb)
            if pivot:
                gx, gy = pivot
                tx = gx - (canvas_w / 2)
                ty = (canvas_h / 2) - gy
                
                rig_data[item.name] = {"x": round(tx, 2), "y": round(ty, 2)}

    for layer in psd:
        walk_layers(layer)
        
    return rig_data

# if __name__ == "__main__":
#     # Example: Look for bright RED (255, 0, 0) marks in 'char.psd'
#     results = calculate_offsets("first_break_down.psd", [255, 0, 0])
    
#     with open("rig_offsets.json", "w") as f:
#         json.dump(results, f, indent=4)
        
#     print("Snapping data generated in rig_offsets.json")
