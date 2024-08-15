from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os
import json

style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class ZoneSetting(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("User Defined Area Management")
        self.setStyleSheet(style)

        self.w.btn_close.clicked.connect(self.close)

        self.datas = []
        if os.path.exists('./datas/userDefined_data.json'):
            f = open('./datas/userDefined_data.json')
            self.datas = json.load(f)
        
        tbZone_show = self.w.tbZone_show
        tbZone_show.setRowCount(len(self.datas))
        
        header = tbZone_show.horizontalHeader()
        for i in range(tbZone_show.columnCount()):
            if i == 0:
                tbZone_show.setColumnWidth(i, 20)
            else:
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        if self.datas:
            for idx, data_num in enumerate(range(len(self.datas))):
                it = QtWidgets.QTableWidgetItem(str(idx))
                it.setTextAlignment(Qt.AlignCenter)
                tbZone_show.setItem(int(idx), 0, it)
                data_if = self.datas[data_num]
                value = data_if["zone_name"]
                it = QtWidgets.QTableWidgetItem(str(value))
                it.setTextAlignment(Qt.AlignCenter)
                tbZone_show.setItem(int(idx), 1, it)
                tbZone_show.cellClicked.connect(self.selected_row)

    def selected_row(self, row_id, col_id):
        self.w.label_CamInfo.setText(self.datas[row_id]["zone_name"])
        self.w.zoneName_edit.setText(self.datas[row_id]["zone_name"])
        cam_infos = self.datas[row_id]["cam_infos"]
        
        tbCam_show = self.w.tbCam_show
        tbCam_show.setRowCount(len(cam_infos))

        header = tbCam_show.horizontalHeader()
        for i in range(tbCam_show.columnCount()):
            if i == 0:
                tbCam_show.setColumnWidth(i, 20)
            elif i == 3:
                tbCam_show.setColumnWidth(i, 45)
            else:
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        

        if cam_infos:
            for idx in range(len(cam_infos)):
                it = QtWidgets.QTableWidgetItem(str(idx))
                it.setTextAlignment(Qt.AlignCenter)
                tbCam_show.setItem(int(idx), 0, it)
                for i, (key, value) in enumerate(cam_infos[idx].items()):
                    if i == 2:
                        chbox_frame = QtWidgets.QFrame()
                        chbox_layout = QtWidgets.QHBoxLayout(chbox_frame)
                        checkbox = QtWidgets.QCheckBox('', self)
                        checkbox.setChecked(value == 1)
                        checkbox.setEnabled(False)
                        chbox_layout.addWidget(checkbox)
                        chbox_layout.setAlignment(checkbox, Qt.AlignCenter)
                        chbox_frame.setLayout(chbox_layout)
                        tbCam_show.setCellWidget(idx, i+1, chbox_frame)
                    else:
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setTextAlignment(Qt.AlignCenter)
                        tbCam_show.setItem(int(idx), i+1, it)
        