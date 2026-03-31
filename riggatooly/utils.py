import json
import os

def load_strings():
    path = os.path.join(os.path.dirname(__file__), "resources", "strings.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Global access
STRINGS = load_strings()
