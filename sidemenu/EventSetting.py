from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QTimer
from PySide6.QtGui import QPixmap, QImage
import sys, os
import cv2
import json
import re

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
        
        self.cameralist = {
            "vid1": "vid/test1.mp4", 
            "vid2": "vid/test2.mp4", 
            "vid3": "vid/test3.mp4",
            "Channel 1 (IP: 192.168.45.166)": "rtsp://admin:aery2021!@192.168.45.166:554/cam/realmonitor?channel=1&subtype=0&unaicast=true&proto=Onvif",
            "Channel 2 (IP: 192.168.45.167)": "rtsp://admin:aery2021!@192.168.45.167:554/cam/realmonitor?channel=1&subtype=0&unaicast=true&proto=Onvif" 
        }
        self.cam_usage = None

        if not os.path.exists("./imgs/profile"):
            os.mkdir("./imgs/profile")
        self.imlen = len(os.listdir("./imgs/profile"))

        self.datas = dict()
        self.datas1 = []
        self.datas2 = []
        
        if os.path.exists('./datas/objTracking.json'):
            f = open('./datas/objTracking.json')
            self.datas = json.load(f)
        self.datas1 = self.datas["person"]
        self.datas2 = self.datas["vehicle"]

        self.filtered_datas = []
        
        completer_cam = QtWidgets.QCompleter(list(self.cameralist.keys()))
        completer_cam.setCaseSensitivity(Qt.CaseInsensitive)
        self.w.camera_edit.setCompleter(completer_cam)
        completer_cam.popup().setStyleSheet("color:#37383E;")

        names = [item["name"] for item in self.datas1]
        completer_name = QtWidgets.QCompleter(names)
        completer_name.setCaseSensitivity(Qt.CaseInsensitive)
        self.w.personName.setCompleter(completer_name)
        completer_name.popup().setStyleSheet("color:#37383E;")
        
        vahicles = [item["vehicle_no"] for item in self.datas2]
        completer_vahicle = QtWidgets.QCompleter(vahicles)
        completer_vahicle.setCaseSensitivity(Qt.CaseInsensitive)
        self.w.noVehicle.setCompleter(completer_vahicle)
        completer_vahicle.popup().setStyleSheet("color:#37383E;")

        self.w.selectCam_btn.clicked.connect(self.selct_camera)
        self.w.startSearch_btn.clicked.connect(self.handle_filter)
        self.w.searchResult_btn.clicked.connect(self.show_filter)

        self.last_radiobutton_checked = None
        # self.w.groupbtnForm.buttonClicked.connect(self.check_button)
        
        # def check_button(self):
        #     self.last_radiobutton_checked = "Person" if self.w.person_radiobtn.isChecked() else "Vehicle" if self.w.vehicle_radiobtn.isChecked() else None


    def selct_camera(self):
        cam_id = self.w.camera_edit.text()
        if cam_id == "" or cam_id == " ":
            QtWidgets.QMessageBox.critical(self, "Empty Fields", "All fields must be filled out.")
        elif cam_id not in list(self.cameralist.keys()):
            QtWidgets.QMessageBox.critical(self, "Invalid Input", f"{cam_id} not exist")
        else:
            self.cam_usage = self.cameralist[cam_id]
            QtWidgets.QMessageBox.information(self, "Success", f"Camera selected {cam_id}")


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
        tb_show = self.popup.tb_show1

        # print(self.popup.frame_tb.layout())
        
        data_to_show = {}
        self.form = ""
        if button == self.w.person_select_btn:
            self.popup.label_head1.setText("Data Person")
            tb_show.setRowCount(len(self.datas1))
            tb_show.setColumnCount(len(self.datas1[0]))
            
            header = tb_show.horizontalHeader()
            header.setMinimumHeight(34)
            header.setDefaultAlignment(Qt.AlignCenter | Qt.Alignment(Qt.TextWordWrap))

            header_items = ["No.", "Name", "Img", "Gender", "Hairstyle", "attribute", "vehicle"]
            for i in range(tb_show.columnCount()):
                hItem = QtWidgets.QTableWidgetItem(header_items[i])
                tb_show.setHorizontalHeaderItem(i, hItem)
                if i==0:
                    tb_show.setColumnWidth(0, 20)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            data_to_show = self.datas1
            self.form = "Person"

            if data_to_show:
                for idx, data_num in enumerate(range(len(data_to_show))):
                    for i, (key, value) in enumerate(data_to_show[data_num].items()):
                        if key == "id":
                            it = QtWidgets.QTableWidgetItem(str(idx+1))
                            it.setTextAlignment(Qt.AlignCenter)
                            tb_show.setItem(int(idx), 0, it)
                        elif key == "vehicles":
                            if value is not False:
                                it = QtWidgets.QTableWidgetItem(str(value))
                                it.setTextAlignment(Qt.AlignCenter)
                                tb_show.setItem(int(idx), i, it)
                                tb_show.cellClicked.connect(self.selected_row)
                        else:
                            it = QtWidgets.QTableWidgetItem(str(value))
                            it.setTextAlignment(Qt.AlignCenter)
                            tb_show.setItem(int(idx), i, it)
                            tb_show.cellClicked.connect(self.selected_row)
                            

        elif button == self.w.vehicle_select_btn:
            self.popup.label_head1.setText("Data Vehicle")
            tb_show.setRowCount(len(self.datas2))
            tb_show.setColumnCount(len(self.datas2[0])+1)
            
            header = tb_show.horizontalHeader()
            header.setMinimumHeight(34)
            header.setDefaultAlignment(Qt.AlignCenter | Qt.Alignment(Qt.TextWordWrap))

            header_items = ["No.", "Vehicle No", "Car Type", "Brand", "Model", "Color", "Person"]
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
                        if key == "person_id":
                            if value is not False:
                                it = QtWidgets.QTableWidgetItem(str(self.datas1[value]["name"]))
                                it.setTextAlignment(Qt.AlignCenter)
                                tb_show.setItem(int(idx), i+1, it)
                                tb_show.cellClicked.connect(self.selected_row)
                        else:
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
                "color": color,
                "person_id": False
            })
            self.datas["vehicle"] = self.datas2
            with open("./datas/objTracking.json", "w") as outfile: 
                json.dump(self.datas, outfile, indent=4) 
            print("success")

    def new_registPerson(self):
        if self.sender() != self.w.person_newReg_btn:
            return
        
        if self.w.personName.text() == "":
            QtWidgets.QMessageBox.critical(self, "Alert", f"Please enter the name field")
            return
        if self.cam_usage is None and self.cam_usage not in list(self.cameralist.keys()):
            QtWidgets.QMessageBox.critical(self, "Alert", "Please select the camera channel")
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

        self.popup.camname.setText(f"Camera ch : {self.cam_usage}")

        self.popup.activateWindow()     ## https://www.geeksforgeeks.org/pyqt5-qcalendarwidget-checking-if-it-is-active-window-or-not/

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
        
        self.camera = cv2.VideoCapture(self.cam_usage)
        self.frame = None
        self.timer = QTimer()
        self.timer.timeout.connect(lambda n=name, g=gender, h=hair, a=attrs:self.display_vid(n,g,h,a))
        self.timer.start(40)

        self.popup.exec()
        

    def display_vid(self, name, gender, hair, attrs):
        if self.popup.isActiveWindow() == False:
            self.close_form()
        # print("FORM :", self.popup.isActiveWindow())
        button = self.sender()
        if button is not self.w.person_newReg_btn:
            self.close_form()
        elif self.popup is None:
            self.close_form()    
        elif self.popup.capture_btn.isChecked():
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
                        "id": 12,
                        "name": name,
                        "img": self.filename,
                        "gender": gender,
                        "hairstyle": hair,
                        "attribute": attrs,
                        "vehicles": False
                    }

    def confirm_newPerson(self):
        self.datas1.append(self.update_data)
        self.datas["person"] = self.datas1
        with open("./datas/objTracking.json", "w") as outfile: 
            json.dump(self.datas, outfile, indent=4) 
        pixmap = QPixmap(self.update_data["img"])  
        scaled_pixmap = pixmap.scaled(self.w.label_foto.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.w.label_foto.setPixmap(scaled_pixmap)

        self.imlen = len(os.listdir("./imgs/profile"))
        self.close_form()

    def close_form(self):
        if self.timer:
            self.timer.stop()
        if self.camera:
            self.camera.release()
            self.camera = None
            # cv2.destroyAllWindows()
        if self.popup:
            self.popup.close()
            self.popup = None



    def handle_filter(self):
        name_filter = self.w.personName.text()
        gender_fliter = "Male" if self.w.Gmale_radiobtn.isChecked() else "Female" if self.w.Gfemale_radiobtn.isChecked() else None
        hairstyle_fliter = "Long" if self.w.Hlong_radiobtn.isChecked() else "Short" if self.w.Hshort_radiobtn.isChecked() else None

        vehicle_filter = self.w.noVehicle.text()
        type_fliter = self.w.car_comboBox.currentText()
        brnad_fliter = self.w.brand_comboBox.currentText()
        model_fliter = self.w.model_comboBox.currentText()
        color_fliter = self.w.color_comboBox.currentText()

        print(f"Filter person: {name_filter}, {gender_fliter}, {hairstyle_fliter}")
        print(f"Filter vehicle: {vehicle_filter}, {type_fliter}, {brnad_fliter}, {model_fliter}, {color_fliter}")
        
        self.filtered_datas = []
        if bool(re.search(r'[^\s]', name_filter)) and bool(re.search(r'[^\s]', vehicle_filter)):
            for d1 in self.datas1:
                name_match = d1["name"] == name_filter
                # gender_match = d1["gender"] == gender_fliter
                # hair_match = d1["hairstyle"] == hairstyle_fliter
                vehicle_match = False
                if d1["vehicles"]:
                    for d2 in self.datas2:
                        vehicle_match = vehicle_filter in d1["vehicles"] and vehicle_filter in d2["vehicle_no"]
                        if vehicle_match:
                            # type_match = d2["type"] == type_fliter
                            # brand_match = d2["brand"] == brnad_fliter
                            # model_match = d2["model"] == model_fliter
                            # color_match = d2["color"] == color_fliter
                        
                            # if type_match and brand_match and model_match and color_match:
                            #     vehicle_match = True
                            break
                        vehicle_match = False
                
                if name_match and vehicle_match:
                    filter_d1 = d1.copy()
                    filter_d1["vehicles"] = vehicle_filter
                    filter_d1["car_type"] = type_fliter
                    filter_d1["car_brand"] = brnad_fliter
                    filter_d1["car_model"] = model_fliter
                    filter_d1["color"] = color_fliter
                    self.filtered_datas.append(filter_d1)            
            print(f"Filter Data: {self.filtered_datas}")
        elif bool(re.search(r'[^\s]', name_filter)) and not bool(re.search(r'[^\s]', vehicle_filter)):
            for d1 in self.datas1:
                name_match = d1["name"] == name_filter
                if name_match:
                    filter_d1 = d1.copy()
                    # filter_d1["car_type"] = ""
                    # filter_d1["car_brand"] = ""
                    # filter_d1["car_model"] = ""
                    # filter_d1["color"] = ""
                    filter_d1["vehicles"] = filter_d1["vehicles"] if filter_d1["vehicles"] is not False else "None"
                    self.filtered_datas.append(filter_d1)
            print(f"Filter Data: {self.filtered_datas}")
        elif not bool(re.search(r'[^\s]', name_filter)) and bool(re.search(r'[^\s]', vehicle_filter)):
            for d2 in self.datas2:
                vehicle_match = d2["vehicle_no"] == vehicle_filter
                if vehicle_match:
                    filter_d1 = dict()
                    filter_d2 = d2.copy()
                    if d2["person_id"] is not False:
                        for d1 in self.datas1:
                            if d1["id"] == d2["person_id"]:
                                filter_d1 = d1.copy()
                                del filter_d1["vehicles"]
                                break
                    else:
                        filter_d1 = {
                            "id":"",
                            "name": "None",
                            "img": "None",
                            "gender": "None",
                            "hairstyle": "None",
                            "attribute": "None",
                        }

                    filter_d1.update(filter_d2)
                    del filter_d1["person_id"]
                    self.filtered_datas.append(filter_d1)
            print(f"Filter Data: {self.filtered_datas}")

        if self.filtered_datas:
            QtWidgets.QMessageBox.information(self, "Searching info", f"filtered data : {len(self.filtered_datas)}")
        else:
            QtWidgets.QMessageBox.critical(self, "Searching info", f"filtered data : {len(self.filtered_datas)}")


    def show_filter(self):
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
        tb_show = self.popup.tb_show1
        
        self.popup.label_head1.setText("All Data Filter Results")
        data_to_show = self.filtered_datas
        if data_to_show:
            ## define table header
            header_items = []
            if len(data_to_show[0]) == 7:
                header_items = ["No.", "Name", "Img", "Gender", "Hairstyle", "Attribute", "Vehicle No"]
            else:
                header_items = ["No.", "Name", "Img", "Gender", "Hairstyle", "Attribute", "Vehicle No", "Car Type", "Brand", "Model", "Color"]
            tb_show.setRowCount(len(data_to_show))
            tb_show.setColumnCount(len(header_items))
            
            header = tb_show.horizontalHeader()
            header.setMinimumHeight(34)
            header.setDefaultAlignment(Qt.AlignCenter | Qt.Alignment(Qt.TextWordWrap))

            for i in range(tb_show.columnCount()):
                hItem = QtWidgets.QTableWidgetItem(header_items[i])
                tb_show.setHorizontalHeaderItem(i, hItem)
                if i==0:
                    tb_show.setColumnWidth(i, 20)
                elif i==1:
                    tb_show.setColumnWidth(i, 100)
                elif i==5:
                    tb_show.setColumnWidth(i, 120)
                elif i==6:
                    tb_show.setColumnWidth(i, 120)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

            ## show data
            for idx, data_num in enumerate(range(len(data_to_show))):
                for i, (key, value) in enumerate(data_to_show[data_num].items()):
                    if key == "id":
                        it = QtWidgets.QTableWidgetItem(str(idx+1))
                        it.setTextAlignment(Qt.AlignCenter)
                        tb_show.setItem(int(idx), 0, it)
                    elif key == "vehicles":
                        if value is not False:
                            it = QtWidgets.QTableWidgetItem(str(value))
                            it.setTextAlignment(Qt.AlignCenter)
                            tb_show.setItem(int(idx), i, it)
                    else:
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setTextAlignment(Qt.AlignCenter)
                        tb_show.setItem(int(idx), i, it)
        
        self.popup.exec()