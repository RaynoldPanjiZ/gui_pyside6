from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os
import socket
import psutil
import subprocess
import ipaddress
from utils.ScreenKeyboard import InputHandler
from utils import UtilsVariables

# print(os.getcwd())
style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()
    


class AIEngineUpdate(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("AI Engine Update")
        self.setStyleSheet(style)
        self.w.btn_cancel.clicked.connect(self.close)
        self.w.run_upgrade_btn.clicked.connect(self.upgrade)

        if UtilsVariables.keyboard_active and UtilsVariables.key_widget is not None:
            self.input_handler1 = InputHandler(UtilsVariables.key_widget)
            UtilsVariables.key_widget.key_pressed.connect(self.input_handler1.on_key_pressed)
            input_widgets = self.findChildren(QtWidgets.QLineEdit)
            for widget in input_widgets:
                widget.installEventFilter(self.input_handler1)


    def upgrade(self):
        print("Success!")
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/aiengine_update/aiengine_upgrade_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("AERY AI BOX Engine Upgrade")
        self.popup.btn_cancel.clicked.connect(self.close)

        # self.popup.lineEdit.setText("Test")
        self.popup.exec()
