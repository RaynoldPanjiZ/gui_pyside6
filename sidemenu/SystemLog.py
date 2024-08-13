from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os

# print(os.getcwd())
style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class SystemLog(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("System Settings")
        self.setStyleSheet(style)
        self.w.auto_del_btn.clicked.connect(self.auto_delete)
        self.w.manually_del_btn.clicked.connect(self.manual_delete)

    def auto_delete(self):
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/system_log/auto_delete_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("Auto-Delete System Logs")
        self.popup.exec()

    def manual_delete(self):
        print("Success!")
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/system_log/manually_delete.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = ManualDeleteLogs(dialog)
        self.popup.show()
        self.close()
        
class ManualDeleteLogs(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.setCentralWidget(w)
        self.setWindowTitle("Manually Delete System Logs")
        self.setStyleSheet(style)