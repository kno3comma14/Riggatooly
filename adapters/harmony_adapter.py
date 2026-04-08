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
        
        scene_height = self.metadata.get("height", 1080)
        self.field_factor = scene_height / 24.0

    def pixels_to_fields(self, pixel_val):
        return pixel_val / self.field_factor
    
    def create_drawing(self, name, image_path, pos_x, pos_y, raster_settings=harmony.RasterSettings()):
        raster_settings.vectorization_type = "TOON_BOOM_BITMAP"
        res = self.import_handler.import_image(
            image_path, 
            self.scene, 
            raster_settings,
            name
        )

        return res
    
    
    def create_peg(self, name, pivote, pos):
        ns = self.scene.nodes
        peg = ns.create("PEG", name)

    
    def connect_peg_to_drawing(self, peg, drawing):
        peg.ports_out[0].link(drawing.ports_in[0])


    def prepare_peg(self, peg, pivote, pos):
        attr = peg.attributes["POSITION"]
        attr.set_value = (1, harmony.Point3d(self.pixels_to_fields(pos["x"]), self.pixels_to_fields(pos["y"]), 0))
        peg.set_pivot(1, harmony.Vector3d(self.pixels_to_fields(pivote["x"]), self.pixels_to_fields(pivote["y"]), 0))
    

    # def create_drawing_element(self, name):
    #     element = next((e for e in self.project.elements if e.name == name), None)
    #     if not element:
    #         element = self.project.elements.create(name, "COLOR", 12.0, "SCAN", "TVG")
        
    #     if not element: return None

    #     col = next((c for c in self.scene.columns if c.name == element.name), None)
    #     img_path = os.path.join(self.assets_root, f"{name}.png")
    #     if col and os.path.exists(img_path):
    #         col.import_file(img_path, 1)

    #         col.create_drawing("1")
    #         col.set_entry(1, "1")
            
    #     return element.id

    # def setup_peg(self, name, data):
    #     peg = self.scene.top.nodes.create("PEG", f"{name}-P")
        
    #     piv_attr = next((a for a in peg.attributes if a.keyword == "PIVOT"), None)
    #     if piv_attr:
    #         piv_attr.subattributes["X"].text_value = self.pixels_to_fields(data["pivote"]["x"])
    #         piv_attr.subattributes["Y"].text_value = self.pixels_to_fields(data["pivote"]["y"])
        
    #     pos_attr = next((a for a in peg.attributes if a.keyword == "POSITION"), None)
    #     if pos_attr:
    #         pos_attr.subattributes["X"].text_value = self.pixels_to_fields(data["position"]["x"])
    #         pos_attr.subattributes["Y"].text_value = self.pixels_to_fields(data["position"]["y"])
        
    #     return peg

    # def build_rig(self):
    #     nodes_map = {}
    #     print(f"U2DM: Starting injection for {len(self.parts)} parts...")

    #     for part_name, data in self.parts.items():
    #         el_id = self.create_drawing_element(part_name)
    #         if el_id is None: continue
            
    #         draw_node = self.scene.top.nodes.create("READ", part_name)
    #         el_attr = next((a for a in draw_node.attributes if a.keyword == "ELEMENT_ID"), None)
    #         if el_attr:
    #             el_attr.text_value = str(el_id)
            
    #         peg_node = self.setup_peg(part_name, data)
            
    #         # This is the port linking that worked
    #         peg_node.ports_out[0].link(draw_node.ports_in[0])
            
    #         nodes_map[part_name] = {"peg": peg_node, "draw": draw_node}

    #     self.apply_hierarchy(nodes_map)
    #     print("U2DM: Skeletal Rigging complete.")

    # def apply_hierarchy(self, nodes_map):
    #     for part_name, nodes in nodes_map.items():
    #         data = self.parts.get(part_name)
    #         parent_name = data.get("parent")
            
    #         if parent_name:
    #             child_peg = nodes["peg"]
    #             parent_peg = next((n for n in self.scene.top.nodes if n.name == parent_name), None)
                
    #             if child_peg and parent_peg and child_peg.path != parent_peg.path:
    #                 parent_peg.ports_out[0].link(child_peg.ports_in[0])

# --- EXECUTION ---
# path = "/path/to/manifest.json"
# builder = HarmonyRigBuilder(path)
# builder.build_rig()
