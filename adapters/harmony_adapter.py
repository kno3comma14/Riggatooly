import os
import json
from ToonBoom import harmony

class HarmonyRigBuilder:
    def __init__(self, manifest_path):
        self.session = harmony.session()
        self.project = self.session.project
        self.scene = self.project.scene
        self.import_handler = self.project.import_handler
        
        with open(manifest_path, 'r') as f:
            self.manifest = json.load(f)
            
        self.metadata = self.manifest.get("metadata", {})
        self.parts = self.manifest.get("parts", {})
        self.assets_root = self.metadata.get("assets_root") or self.metadata.get("image_folder_path")
        
        self.scene_height = self.metadata.get("height", 1080)
        self.scene_width = self.metadata.get("width", 1920)
        self.field_factor_Y = float(self.scene_height) / 24.0
        self.field_factor_X = float(self.scene_width) / 32.0


    def calculate_mid_bbox(self, bbox):
        mid_y = (self.scene_height / 2.0 -  (bbox[1] + bbox[3]) / 2.0) / self.field_factor_Y
        mid_x = ((bbox[0] + bbox[2]) / 2.0 - self.scene_width / 2.0) / self.field_factor_X
        
        return {"x": mid_x / 16.0, "y": mid_y / 12.0}  
    
    
    def pixels_to_fields_X(self, pixel_val):
        return float(pixel_val) / self.field_factor_X
    
    
    def pixels_to_fields_Y(self, pixel_val):
        return float(pixel_val) / self.field_factor_Y
    

    def create_drawing(self, name, image_path, raster_settings=harmony.ImportRasterSettings()):
        if os.path.exists(image_path):
            raster_settings.vectorization_type = "TOON_BOOM_BITMAP"
            res = self.import_handler.import_image(image_path, self.scene, raster_settings,name)
            return res
        else:
            print(f"Image not found: {image_path}. Probably it doesn't have color data associated.")

        return None
    
    
    def create_peg(self, name):
        ns = self.scene.nodes
        peg = ns.create("PEG", name)

        return peg

    
    def connect_peg_to_drawing(self, peg, drawing):
        d = drawing["nodes"][0]
        peg.ports_out[0].link(d.ports_in[0])


    def prepare_peg(self, peg, pivote, position):
        attr = peg.attributes["POSITION"]
        x = self.pixels_to_fields_X(position["x"])
        y = self.pixels_to_fields_Y(position["y"])
        attr.set_value(1, harmony.Point3d(x, y, 0))
        piv_attr = peg.attributes["PIVOT"]
        # px = self.pixels_to_fields_X(pivote["x"])
        # py = -self.pixels_to_fields_Y(pivote["y"])
        piv_attr.set_value(1, harmony.Point3d(0, 0, 0))
        
    
    def prepare_drawing(self, drawing, peg_pivot):
        drawing_piv_attr = drawing["nodes"][0].attributes["PIVOT"]
        drawing_piv_attr.set_value(1, harmony.Point3d(self.pixels_to_fields_X(peg_pivot["x"]), -self.pixels_to_fields_Y(peg_pivot["y"]), 0))
    
    
    def import_nodes(self):
        keys = list(self.parts.keys())
        keys.reverse()
        for p in keys:
            img_path = os.path.join(self.assets_root, f"{p}.png")
            drawing = self.create_drawing(p, img_path)
            if self.parts[p]["parent"] and drawing:
                peg = self.create_peg(self.parts[p]["parent"])
                self.prepare_peg(peg, self.parts[p]["pivote"], self.parts[p]["position"])
                self.prepare_drawing(drawing, self.parts[p]["pivote"])
                self.connect_peg_to_drawing(peg, drawing)
                

    
    def build_rig(self):
        self.import_nodes()

# --- EXECUTION ---
# path = "/path/to/manifest.json"
# builder = HarmonyRigBuilder(path)
# builder.build_rig()
# [left, top, right, bottom] bbox