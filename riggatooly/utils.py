import json
import os
import sys
import rc_resources

from PySide6.QtCore import QFile, QTextStream

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_strings():
    json_file = QFile(":/data/strings.json")
    
    if json_file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(json_file)
        return json.loads(stream.readAll())
    return {}

# Global access
STRINGS = load_strings()
