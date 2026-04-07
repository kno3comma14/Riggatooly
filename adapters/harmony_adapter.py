import os
import json
from ToonBoom import harmony

class HarmonyRigBuilder:
    def __init__(self, manifest_path):
        self.session = harmony.session()
        self.project = self.session.project
        self.scene = self.project.scene
        
        # Load and Parse Manifest
        with open(manifest_path, 'r') as f:
            self.manifest = json.load(f)
            
        self.metadata = self.manifest.get("metadata", {})
        self.parts = self.manifest.get("parts", {})
        self.assets_root = self.metadata.get("image_folder_path")
        
        # Calculation: Harmony Fields vs PSD Pixels
        # Default 1080p is 24 fields high (-12 to +12)
        self.field_factor = self.metadata.get("height", 1080) / 24.0

    def pixels_to_fields(self, pixel_val):
        """Converts PSD pixel units to Harmony field units."""
        return str(pixel_val / self.field_factor)

    def create_drawing_element(self, name):
        """Creates the internal Harmony element and imports the asset."""
        element_id = self.project.elements.add(name=name, type=1)
        element = self.project.elements.find_by_id(element_id)
        
        img_path = os.path.join(self.assets_root, f"{name}.png")
        if os.path.exists(img_path):
            element.import_file(img_path, 0)
        return element_id

    def setup_peg(self, name, data):
        """Creates and transforms the Peg node based on JSON data."""
        peg = self.scene.root.add_node("Peg")
        peg.name = f"{name}-P"
        
        # Set Pivot
        piv = peg.attributes.find("PIVOT")
        piv.x.text_value = self.pixels_to_fields(data["pivote"]["x"])
        piv.y.text_value = self.pixels_to_fields(data["pivote"]["y"])
        
        # Set Position (Offset)
        pos = peg.attributes.find("POSITION")
        pos.x.text_value = self.pixels_to_fields(data["position"]["x"])
        pos.y.text_value = self.pixels_to_fields(data["position"]["y"])
        
        return peg

    def build_rig(self):
        """Pass 1: Creation and local transformation."""
        nodes_map = {}

        for part_name, data in self.parts.items():
            # 1. Element & Image
            el_id = self.create_drawing_element(part_name)
            
            # 2. Drawing Node
            draw_node = self.scene.root.add_node("Drawing")
            draw_node.name = part_name
            draw_node.attributes.find("ELEMENT_ID").text_value = str(el_id)
            
            # 3. Peg Node
            peg_node = self.setup_peg(part_name, data)
            peg_node.link(draw_node)
            
            nodes_map[part_name] = peg_node

        # Pass 2: Global Hierarchy (Parenting)
        self.apply_hierarchy(nodes_map)
        
        print(f"U2DM: Successfully rigged {len(self.parts)} components.")

    def apply_hierarchy(self, nodes_map):
        """Pass 2: Linking children to parent pegs."""
        for part_name, data in self.parts.items():
            parent_name = data.get("parent")
            if parent_name:
                child_peg = nodes_map[part_name]
                # Look for parent peg in current build or existing scene
                parent_peg = self.scene.find_node(f"Top/{parent_name}")
                
                if parent_peg:
                    parent_peg.link(child_peg)

# To execute in Harmony:
# builder = HarmonyRigBuilder("/path/to/manifest.json")
# builder.build_rig()
