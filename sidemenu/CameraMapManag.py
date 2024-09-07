from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os
import json
from utils.ScreenKeyboard import InputHandler
from utils import UtilsVariables

style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class CameraMapMng(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("Camera Map Management")
        self.setStyleSheet(style)
        self.w.del_map_btn.clicked.connect(self.delete_map_dialog)
        self.w.add_map_btn.clicked.connect(self.add_map_dialog)
        self.w.findFile_btn.clicked.connect(self.open_file_dialog)
        self.w.close_btn.clicked.connect(self.close)

        if UtilsVariables.keyboard_active and UtilsVariables.key_widget is not None:
            self.input_handler1 = InputHandler(UtilsVariables.key_widget)
            UtilsVariables.key_widget.key_pressed.connect(self.input_handler1.on_key_pressed)
            self.w.fileName_edit.installEventFilter(self.input_handler1)
            self.w.mapRegist_edit.installEventFilter(self.input_handler1)
            self.w.mapDescript_edit.installEventFilter(self.input_handler1)

        # self.datas = [
        #     ["CU convinience store", "34567.jpg", "2023-10-10 12:23:45", "Sigil-dong CU convinience store"],
        #     ["Buss stop 1", "123456.jpg", "2023-10-10 12:23:45", "Sigil-dong CU convinience store"],
        #     ["Map station 1", "125690.jpg", "2023-10-10 12:23:45", "Sigil-dong CU convinience store"],
        # ]
        self.datas = []
        if os.path.exists('./datas/cameraMapManage.json'):
            f = open('./datas/cameraMapManage.json')
            self.datas = json.load(f)

        tb_show = self.w.tb_show
        tb_show.setRowCount(len(self.datas))
        
        header = tb_show.horizontalHeader()
        tb_show.setColumnWidth(0, 20)
        tb_show.setColumnWidth(1, 150)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        
        if self.datas:
            for idx, data_num in enumerate(range(len(self.datas))):
                it = QtWidgets.QTableWidgetItem(str(data_num+1))
                it.setTextAlignment(Qt.AlignCenter)
                tb_show.setItem(int(idx), 0, it)
                i=0
                for (key, value) in (self.datas[data_num].items()):
                    if key == "regist_date":
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setTextAlignment(Qt.AlignCenter)
                        tb_show.setItem(int(idx), i+2, it)
                    if i == 2:
                        btn_preview = QtWidgets.QPushButton()
                        btn_preview.setText("Preview")
                        tb_show.setCellWidget(idx, i+1, btn_preview)
                        btn_preview.clicked.connect(lambda _, x=idx:self.prev_window(x))
                        i+=1
                    else:
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setTextAlignment(Qt.AlignCenter)
                        tb_show.setItem(int(idx), i+1, it)
                    i+=1
                tb_show.cellClicked.connect(self.selected_row)

    def selected_row(self, row_id, col_id):
        self.w.fileName_edit.setText(str(self.datas[row_id]["map_file"]))
        self.w.mapDescript_edit.setText(str(self.datas[row_id]["description"]))

    def open_file_dialog(self):
        """Membuka file explorer dan menampilkan path file yang dipilih"""
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.w.mapRegist_edit.setText(str(file_name))

    def delete_map_dialog(self):
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/cameramap_mng/delete_map_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("Delete Map")
        def confirm():
            print("deleted")
        
        self.popup.btn_confirm.clicked.connect(confirm)
        self.popup.btn_cancel.clicked.connect(self.popup.close)
        self.popup.exec()
        
    def add_map_dialog(self):
        print("Success!")
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/cameramap_mng/popup_addnewmap_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("Add Camera Map")
        def confirm():
            print("confirm")
        
        self.popup.btn_confirm.clicked.connect(confirm)
        self.popup.btn_cancel.clicked.connect(self.popup.close)
        self.popup.exec()

    def prev_window(self, row_id):
        self.selected_row(row_id, 0)