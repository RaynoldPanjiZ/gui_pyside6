from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os

# print(os.getcwd())
style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()



class EventSetting(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("Event Settings")
        self.setStyleSheet(style)
        self.w.close_btn.clicked.connect(self.close)
        
        self.w.obj_track_btn.clicked.connect(lambda:self.show_popup(ObjTracking))

    def show_popup(self, PopupClass):
        print("Success!")
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/event_setting/object_realtime.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = PopupClass(dialog)
        self.popup.show()
        self.close()
        
class ObjTracking(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("Object Real-Time Tracking")
        self.setStyleSheet(style)
        self.w.close_btn.clicked.connect(self.close)