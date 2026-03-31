import json
import os
import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QFileDialog, QTextEdit, QFrame)
from PySide6.QtCore import Qt, Signal

from riggatooly.utils import STRINGS

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = self.load_config()

        win_cfg = self.config.get("window", {})

        self.setWindowTitle(STRINGS["ui"]["window_title"])
        self.resize(800, 500)

        # Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 1. Header
        self.header = QLabel(STRINGS["ui"]["header"])
        # self.header.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        self.layout.addWidget(self.header)

        # 2. Drop Area (Visual placeholder)
        self.drop_frame = QFrame()
        self.drop_frame.setObjectName("DropFrame")
        self.drop_frame.setMinimumHeight(150)
        
        self.drop_layout = QVBoxLayout(self.drop_frame)
        self.drop_label = QLabel(STRINGS["ui"]["drop_label"])
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.drop_layout.addWidget(self.drop_label)

        self.btn_browse = QPushButton(STRINGS["ui"]["browse_btn"])
        self.btn_browse.setFixedWidth(150)
        self.btn_browse.clicked.connect(self.open_file_dialog)
        self.drop_layout.addWidget(self.btn_browse, alignment=Qt.AlignCenter)
        
        self.layout.addWidget(self.drop_frame)

        # 3. Log Console (Crucial for Technical Art tools)
        self.layout.addWidget(QLabel(STRINGS["ui"]["log_header"]))
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        # self.console.setStyleSheet("background-color: #111; color: #00ff00; font-family: Courier;")
        self.console.setPlaceholderText(STRINGS["ui"]["waiting_input"])
        self.layout.addWidget(self.console)

        # 4. Action Buttons
        self.btn_run = QPushButton(STRINGS["ui"]["run_btn"])
        self.btn_run.setObjectName("RunButton")
        self.btn_run.setFixedHeight(40)
        # self.btn_run.setStyleSheet("background-color: #00adb5; font-weight: bold;")
        self.btn_run.clicked.connect(self.process_files)
        self.layout.addWidget(self.btn_run)

    def load_config(self):
        config_path = "config.json"
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                return json.load(f)
        return {} # Return defaults if file is missing
    
    def closeEvent(self, event):
        """Save current window size when closing the app."""
        self.config["window"]["width"] = self.width()
        self.config["window"]["height"] = self.height()
        with open("config.json", "w") as f:
            json.dump(self.config, f, indent=4)
        event.accept()
    
    def log(self, message):
        """Append messages to the UI console."""
        self.console.append(f"> {message}")

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Supported Files (*.tnz *.json)")
        if file_path:
            self.log(f"Loaded: {file_path}")

    def process_files(self):
        self.log("Starting transformation...")
        self.log("Converting PS coordinates to Tahoma Stage Inches...")
        # Here you will call your core/xml_injector.py functions
        self.log("Success: XML structure modified.")

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
