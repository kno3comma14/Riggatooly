import sys
from PySide6.QtWidgets import QApplication
from riggatooly.gui.main_window import MainWindow
from qt_material import apply_stylesheet

def load_stylesheet(app, path):
    with open(path, "r") as f:
        app.setStyleSheet(f.read())

def run():
    app = QApplication(sys.argv)
    
    load_stylesheet(app, "riggatooly/resources/style.qss")
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()
