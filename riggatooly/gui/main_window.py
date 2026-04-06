import json
import os
import sys
from riggatooly.core import snapper
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QFileDialog, QTextEdit, QFrame, QColorDialog)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, Signal

from riggatooly.utils import STRINGS

file_map = {
    "image_file": ""
}

pivote_color = list(QColor("red").getRgb())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = self.load_config()

        win_cfg = self.config.get("window", {})

        self.setWindowTitle(STRINGS["english"]["ui"]["window_title"])
        self.resize(800, 500)

        # Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 1. Header
        self.header = QLabel(STRINGS["english"]["ui"]["header"])
        # self.header.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        self.layout.addWidget(self.header)

        # 2. Drop Area (Visual placeholder)
        self.drop_frame = QFrame()
        self.drop_frame.setObjectName("DropFrame")
        self.drop_frame.setMinimumHeight(150)
        
        self.drop_layout = QVBoxLayout(self.drop_frame)
        self.drop_label = QLabel(STRINGS["english"]["ui"]["drop_label"])
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.drop_layout.addWidget(self.drop_label)

        self.btn_browse = QPushButton(STRINGS["english"]["ui"]["browse_btn"])
        self.btn_browse.setFixedWidth(150)
        self.btn_browse.clicked.connect(self.open_file_dialog)
        self.drop_layout.addWidget(self.btn_browse, alignment=Qt.AlignCenter)
        
        self.layout.addWidget(self.drop_frame)

        # Pivote Color
        self.piv_btn_color = QPushButton(STRINGS["english"]["ui"]["change_pivote_color_btn"])
        self.piv_btn_color.clicked.connect(self.open_color_dialog)
        self.layout.addWidget(self.piv_btn_color)

        # 3. Log Console (Crucial for Technical Art tools)
        self.layout.addWidget(QLabel(STRINGS["english"]["ui"]["log_header"]))
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        # self.console.setStyleSheet("background-color: #111; color: #00ff00; font-family: Courier;")
        self.console.setPlaceholderText(STRINGS["english"]["ui"]["waiting_input"])
        self.layout.addWidget(self.console)

        # 4. Action Buttons
        self.btn_run = QPushButton(STRINGS["english"]["ui"]["run_btn"])
        self.btn_run.setObjectName("RunButton")
        self.btn_run.setFixedHeight(40)
        self.btn_run.setEnabled(False)
        # self.btn_run.setStyleSheet("background-color: #00adb5; font-weight: bold;")
        self.btn_run.clicked.connect(self.process_files)
        self.layout.addWidget(self.btn_run)

    def open_color_dialog(self):
        color = QColorDialog.getColor(
            initial=QColor("red"),
            options=QColorDialog.ShowAlphaChannel, 
        )

        if color.isValid():
            global pivote_color
            pivote_color = list(color.getRgb())
            self.piv_btn_color.setStyleSheet(f"background-color: rgba({pivote_color[0]}, {pivote_color[1]}, {pivote_color[2]}, {pivote_color[3]})")
    
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

    def store_input_files(self, file_path):
        
        if file_path.endswith(".kra") or file_path.endswith(".psd"):
            file_map["image_file"] = file_path
            self.log("Image file detected. Path: {}".format(file_path))

        if not file_map["image_file"] == "":
            self.btn_run.setEnabled(True)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Supported Files (*.psd *.kra)")
        if file_path:
            self.store_input_files(file_path)
            self.drop_label.setText(os.path.basename(file_path))
            self.log(f"Loaded: {file_path}")

    def process_files(self):
        self.btn_run.setEnabled(False)
        self.log("Converting PSD coordinates and sizes")
        pixels_data = snapper.calculate_offsets(file_map["image_file"], pivote_color)
        self.log("Success: PSD coordinates and sizes calculated.")
        self.log("Creating universal rigging structure file...")
        self.log("Done.")
        self.btn_run.setEnabled(True)

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
