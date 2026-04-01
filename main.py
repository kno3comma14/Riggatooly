import sys
from PySide6.QtWidgets import QApplication
from riggatooly.gui.main_window import MainWindow
import riggatooly.utils as utils
from qt_material import apply_stylesheet
import rc_resources
from PySide6.QtCore import QFile, QTextStream

def load_stylesheet(app):
    style_file = QFile(":/data/style.qss")
    if style_file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(style_file)
        app.setStyleSheet(stream.readAll())

def run():
    app = QApplication(sys.argv)
    
    load_stylesheet(app)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()
