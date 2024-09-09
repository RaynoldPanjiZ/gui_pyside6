from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os
from utils.ScreenKeyboard import InputHandler
from utils import UtilsVariables

style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class SystemLogin(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("Log in")
        self.setStyleSheet(style)

        if UtilsVariables.keyboard_active and UtilsVariables.key_widget is not None:
            self.input_handler1 = InputHandler(UtilsVariables.key_widget)
            UtilsVariables.key_widget.key_pressed.connect(self.input_handler1.on_key_pressed)
            input_widgets = self.findChildren(QtWidgets.QLineEdit)
            for widget in input_widgets:
                widget.installEventFilter(self.input_handler1)
