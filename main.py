import sys
from riggatooly.gui.main_window import MainWindow

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
