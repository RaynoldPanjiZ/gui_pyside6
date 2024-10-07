import PySide6

import sys, os
from utils.ScreenKeyboard import InputHandler
from utils import UtilsVariables

style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class SystemLogin(PySide6.QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("Log in")
        self.setStyleSheet(style)

        if UtilsVariables.keyboard_active and UtilsVariables.key_widget is not None:
            self.input_handler1 = InputHandler(UtilsVariables.key_widget)
            UtilsVariables.key_widget.key_pressed.connect(self.input_handler1.on_key_pressed)
            input_widgets = self.findChildren(PySide6.QtWidgets.QLineEdit)
            for widget in input_widgets:
                widget.installEventFilter(self.input_handler1)
