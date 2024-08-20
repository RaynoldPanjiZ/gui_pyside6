from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
from PySide6.QtGui import QPixmap
import sys, os
import json

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
        self.w.person_select_btn.clicked.connect(self.select_form)
        self.w.person_newReg_btn.clicked.connect(self.new_regist)

        self.datas = []
        if os.path.exists('./datas/dataPerson.json'):
            f = open('./datas/dataPerson.json')
            self.datas = json.load(f)
    
    def select_form(self):
        name = self.datas[0]["name"]
        self.w.personName.setText(name)

        profile_file = self.datas[0]["img"]
        pixmap = QPixmap(profile_file)  
        scaled_pixmap = pixmap.scaled(self.w.label_foto.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.w.label_foto.setPixmap(scaled_pixmap)

        gender = self.datas[0]["gender"]
        if self.w.Gmale_radiobtn.text() == gender:
            self.w.Gmale_radiobtn.setChecked(True)
        elif self.w.Gfemale_radiobtn.text() == gender:
            self.w.Gfemale_radiobtn.setChecked(True)

        hair = self.datas[0]["Hairstyle"]
        if self.w.Hlong_radiobtn.text() == hair:
            self.w.Hlong_radiobtn.setChecked(True)
        elif self.w.Hshort_radiobtn.text() == hair:
            self.w.Hshort_radiobtn.setChecked(True)

        attrs = self.datas[0]["attribute"]
        checkboxes = self.w.attr_checkboxGroup.parentWidget().findChildren(QtWidgets.QCheckBox)
        for chbx in checkboxes:
            if chbx.text() in attrs:
                chbx.setChecked(True)

    def new_regist(self):
        name = self.w.personName.text()
        
        gender = ""
        if self.w.Gmale_radiobtn.isChecked():
            gender = self.w.Gmale_radiobtn.text()
        elif self.w.Gfemale_radiobtn.isChecked():
            gender = self.w.Gfemale_radiobtn.text()
        
        hair = ""
        if self.w.Hlong_radiobtn.isChecked():
            hair = self.w.Hlong_radiobtn.text()
        elif self.w.Hshort_radiobtn.isChecked():
            hair = self.w.Hshort_radiobtn.text()
        
        attrs = []
        for chbx in self.w.attr_checkboxGroup.parentWidget().findChildren(QtWidgets.QCheckBox):
            if chbx.isChecked():
                attrs.append(chbx.text())

        update_data = {
            "name": name,
            "img": "imgs/test.jpg",
            "gender": gender,
            "Hairstyle": hair,
            "attribute": attrs
        }
        self.datas.append(update_data)
        with open("datas/dataPerson.json", "w") as outfile: 
            json.dump(self.datas, outfile, indent=4)        