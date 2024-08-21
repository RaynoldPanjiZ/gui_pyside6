from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QTimer
from PySide6.QtGui import QPixmap, QImage
import sys, os
import cv2
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
        self.w.person_newReg_btn.clicked.connect(self.new_registPerson)
        
        self.w.vehicle_select_btn.clicked.connect(self.select_form)
        self.w.vehicle_newReg_btn.clicked.connect(self.new_registVehicle)
        
        if not os.path.exists("./imgs/profile"):
            os.mkdir("./imgs/profile")
        self.imlen = len(os.listdir("./imgs/profile"))

        self.datas1 = []
        if os.path.exists('./datas/dataPerson.json'):
            f = open('./datas/dataPerson.json')
            self.datas1 = json.load(f)
        
        self.datas2 = []
        if os.path.exists('./datas/dataVehicle.json'):
            f = open('./datas/dataVehicle.json')
            self.datas2 = json.load(f)

        self.active_form = 0
        self.w.groupbtnForm.buttonClicked.connect(self.check_button)
    
    def check_button(self):
        pass


    def select_form(self):
        button = self.sender()

        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/event_setting/select_data_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.cancel_btn.clicked.connect(self.popup.close)
        self.popup.setWindowTitle("Select item")
        tb_show = self.popup.tb_show
        
        data_to_show = {}
        self.form = ""
        if button == self.w.person_select_btn:
            tb_show.setRowCount(len(self.datas1))
            tb_show.setColumnCount(len(self.datas1[0])+1)
            
            header = tb_show.horizontalHeader()
            header.setMinimumHeight(34)
            header.setDefaultAlignment(Qt.AlignCenter | Qt.Alignment(Qt.TextWordWrap))

            header_items = ["No.", "Name", "Img", "Gender", "Hairstyle", "attribute"]
            for i in range(tb_show.columnCount()):
                hItem = QtWidgets.QTableWidgetItem(header_items[i])
                tb_show.setHorizontalHeaderItem(i, hItem)
                if i==0:
                    tb_show.setColumnWidth(0, 20)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            data_to_show = self.datas1
            self.form = "Person"
        elif button == self.w.vehicle_select_btn:
            tb_show.setRowCount(len(self.datas2))
            tb_show.setColumnCount(len(self.datas2[0])+1)
            
            header = tb_show.horizontalHeader()
            header.setMinimumHeight(34)
            header.setDefaultAlignment(Qt.AlignCenter | Qt.Alignment(Qt.TextWordWrap))

            header_items = ["No.", "Vehicle No", "Car Type", "Brand", "Model", "Color"]
            for i in range(tb_show.columnCount()):
                hItem = QtWidgets.QTableWidgetItem(header_items[i])
                tb_show.setHorizontalHeaderItem(i, hItem)
                if i==0:
                    tb_show.setColumnWidth(0, 20)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            data_to_show = self.datas2
            self.form = "Vehicle"

        
        if data_to_show:
            for idx, data_num in enumerate(range(len(data_to_show))):
                it = QtWidgets.QTableWidgetItem(str(idx+1))
                it.setTextAlignment(Qt.AlignCenter)
                tb_show.setItem(int(idx), 0, it)
                for i, (key, value) in enumerate(data_to_show[data_num].items()):
                    it = QtWidgets.QTableWidgetItem(str(value))
                    it.setTextAlignment(Qt.AlignCenter)
                    tb_show.setItem(int(idx), i+1, it)
                    tb_show.cellClicked.connect(self.selected_row)

        self.popup.exec()

    def selected_row(self, row_id, col_id):
        if self.form == "Person":
            datatoform = self.datas1[row_id]

            name = datatoform["name"]
            self.w.personName.setText(name)

            profile_file = datatoform["img"]
            pixmap = QPixmap(profile_file)  
            scaled_pixmap = pixmap.scaled(self.w.label_foto.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.w.label_foto.setPixmap(scaled_pixmap)

            gender = datatoform["gender"]
            if self.w.Gmale_radiobtn.text() == gender:
                self.w.Gmale_radiobtn.setChecked(True)
            elif self.w.Gfemale_radiobtn.text() == gender:
                self.w.Gfemale_radiobtn.setChecked(True)

            hair = datatoform["hairstyle"]
            if self.w.Hlong_radiobtn.text() == hair:
                self.w.Hlong_radiobtn.setChecked(True)
            elif self.w.Hshort_radiobtn.text() == hair:
                self.w.Hshort_radiobtn.setChecked(True)

            attrs = datatoform["attribute"]
            checkboxes = self.w.attr_checkboxGroup.parentWidget().findChildren(QtWidgets.QCheckBox)
            for chbx in checkboxes:
                if chbx.text() in attrs:
                    chbx.setChecked(True)
                else:
                    chbx.setChecked(False)

        elif self.form == "Vehicle":
            datatoform = self.datas2[row_id]

            vehicle_no = datatoform["vehicle_no"]
            self.w.noVehicle.setText(vehicle_no)

            cartype = datatoform["type"]
            for i in range(self.w.car_comboBox.count()):
                if cartype == str(self.w.car_comboBox.itemText(i)):
                    self.w.car_comboBox.setCurrentIndex(i)
                    break

            brand = datatoform["brand"]
            for i in range(self.w.brand_comboBox.count()):
                if brand == str(self.w.brand_comboBox.itemText(i)):
                    self.w.brand_comboBox.setCurrentIndex(i)
                    break
            
            model = datatoform["model"]
            for i in range(self.w.model_comboBox.count()):
                if model == str(self.w.model_comboBox.itemText(i)):
                    self.w.model_comboBox.setCurrentIndex(i)
                    break
            
            color = datatoform["color"]
            for i in range(self.w.color_comboBox.count()):
                if color == str(self.w.color_comboBox.itemText(i)):
                    self.w.color_comboBox.setCurrentIndex(i)
                    break

        self.popup.close()


    def new_registVehicle(self):
        if self.w.noVehicle.text() == "":
            QtWidgets.QMessageBox.critical(self, "Alert", f"Please enter the Vehicle No field")
            return
        
        noVehicle = self.w.noVehicle.text()
        cartype = self.w.car_comboBox.currentText()
        brand = self.w.brand_comboBox.currentText()
        model = self.w.model_comboBox.currentText()
        color = self.w.color_comboBox.currentText()
        qm = QtWidgets.QMessageBox
        ret = qm.question(self,'Data Confirmation', "Save data registration?", qm.Yes | qm.No)
        if ret == qm.Yes:
            self.datas2.append({
                "vehicle_no": noVehicle,
                "type": cartype,
                "brand": brand,
                "model": model,
                "color": color
            })
            with open("datas/dataVehicle.json", "w") as outfile: 
                json.dump(self.datas2, outfile, indent=4) 
            print("success")

    def new_registPerson(self):
        if self.w.personName.text() == "":
            QtWidgets.QMessageBox.critical(self, "Alert", f"Please enter the name field")
            return
        
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/event_setting/camera_confirm_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.confirm_btn.clicked.connect(self.confirm_newPerson)
        self.popup.cancel_btn.clicked.connect(self.close_form)
        self.popup.setWindowTitle("Confirmation registration")

        name = self.w.personName.text()
        self.popup.name_label.setText(name)
        
        gender = "-"
        if self.w.Gmale_radiobtn.isChecked():
            gender = self.w.Gmale_radiobtn.text()
        elif self.w.Gfemale_radiobtn.isChecked():
            gender = self.w.Gfemale_radiobtn.text()
        self.popup.gender_label.setText(gender)
        
        hair = "-"
        if self.w.Hlong_radiobtn.isChecked():
            hair = self.w.Hlong_radiobtn.text()
        elif self.w.Hshort_radiobtn.isChecked():
            hair = self.w.Hshort_radiobtn.text()
        self.popup.hairstyle_label.setText(hair)
        
        attrs = []
        attr_string = "-"
        for chbx in self.w.attr_checkboxGroup.parentWidget().findChildren(QtWidgets.QCheckBox):
            if chbx.isChecked():
                attrs.append(chbx.text())
                if attr_string == "-":
                    attr_string = str(chbx.text())
                else:
                    attr_string += f", {str(chbx.text())}"
                    
        self.popup.attr_label.setText(attr_string)
        
        self.filename = "-"
        self.update_data = {}
        
        self.camera = cv2.VideoCapture("vid/test1.mp4")
        self.frame = None
        self.timer = QTimer()
        self.timer.timeout.connect(lambda n=name, g=gender, h=hair, a=attrs:self.display_vid(n,g,h,a))
        self.timer.start(40)

        self.popup.exec()
        

    def display_vid(self, name, gender, hair, attrs):
        if self.popup.capture_btn.isChecked():
            self.popup.capture_btn.setText("save image")
            ret, self.frame = self.camera.read()
            if ret:
                print(self.frame.shape)
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                image = QImage(self.frame, self.frame.shape[1], self.frame.shape[0], QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(image)
                self.popup.label_cam.setPixmap(pixmap)
                self.popup.label_cam.setScaledContents(True)
                self.popup.confirm_btn.setEnabled(False)
        else:
            self.popup.capture_btn.setText("start video capture")
            if self.frame is not None:
                self.filename = f"./imgs/profile/p_{self.imlen}.jpg"
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR)
                cv2.imwrite(self.filename, self.frame)
                print("Image captured!")
                self.frame = None
                self.popup.img_label.setText(self.filename)
            else:
                if self.filename != "-":
                    self.popup.confirm_btn.setEnabled(True)
                    self.update_data = {
                        "name": name,
                        "img": self.filename,
                        "gender": gender,
                        "hairstyle": hair,
                        "attribute": attrs
                    }

    def confirm_newPerson(self):
        self.datas1.append(self.update_data)
        with open("datas/dataPerson.json", "w") as outfile: 
            json.dump(self.datas1, outfile, indent=4) 
        self.camera.release()
        cv2.destroyAllWindows()
        self.close_form()

    def close_form(self):
        if self.timer:
            self.timer.stop()
        self.popup.close()
        self.popup = None