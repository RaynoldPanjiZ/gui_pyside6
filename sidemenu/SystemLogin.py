from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os
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
