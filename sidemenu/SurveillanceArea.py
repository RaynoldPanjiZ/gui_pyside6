# from PySide6 import QtWidgets
# from PySide6.QtCore import Qt, QTimer
# from PySide6.QtGui import QPixmap, QIcon, QImage

import PySide6
import sys, os
import cv2

style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class SurveillanceArea(PySide6.QtWidgets.QMainWindow): 
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("Camera Selection")
        self.setStyleSheet(style)
        self.w.btn_cancel.clicked.connect(self.close)

        # self.datas = [
        #     ["192.168.100.101", "Korean Restaurant-1", 0, "vid/test1.mp4"],
        #     ["192.168.100.102", "Korean Restaurant-2", 1, "vid/test2.mp4"]
        # ]
        self.datas = [
            ["192.168.100.101", "Korean Restaurant-1", 0, "rtsp://admin:aery2021!@192.168.45.166:554/cam/realmonitor?channel=1&subtype=0&unaicast=true&proto=Onvif"],
            ["192.168.100.102", "Korean Restaurant-2", 1, "rtsp://admin:aery2021!@192.168.45.167:554/cam/realmonitor?channel=1&subtype=0&unaicast=true&proto=Onvif"]
        ]

        tb_show = self.w.tb_show
        tb_show.setRowCount(len(self.datas))
        
        header = tb_show.horizontalHeader()
        header.setMinimumHeight(34)
        for i in range(tb_show.columnCount()):  # Stretch the tables by column horizontally
            if i == 0:
                tb_show.setColumnWidth(i, 20)
            elif i == 3:
                tb_show.setColumnWidth(i, 65)
                header.setDefaultAlignment(PySide6.QtCore.Qt.AlignCenter | PySide6.QtCore.Qt.Alignment(PySide6.QtCore.Qt.TextWordWrap))
            elif i == 4:
                tb_show.setColumnWidth(i, 45)
            else:
                header.setSectionResizeMode(i, PySide6.QtWidgets.QHeaderView.Stretch)
        
        if self.datas:
            for idx, data_num in enumerate(range(len(self.datas))):
                data_if = self.datas[data_num]
                it = PySide6.QtWidgets.QTableWidgetItem(str(data_num + 1))  # numbering
                it.setTextAlignment(PySide6.QtCore.Qt.AlignCenter)
                tb_show.setItem(int(idx), 0, it)
                for i, value in enumerate(data_if):
                    if i == 2:
                        checkbox = PySide6.QtWidgets.QCheckBox('', self)
                        chbox_frame = PySide6.QtWidgets.QFrame()
                        chbox_layout = PySide6.QtWidgets.QHBoxLayout(chbox_frame)
                        checkbox.setChecked(value == 1)
                        checkbox.setEnabled(False)
                        chbox_layout.addWidget(checkbox)
                        chbox_layout.setAlignment(checkbox, PySide6.QtCore.Qt.AlignCenter)
                        chbox_frame.setLayout(chbox_layout)
                        tb_show.setCellWidget(idx, i+1, chbox_frame)
                    elif i == 3:
                        radio_button = PySide6.QtWidgets.QRadioButton()
                        tb_show.setCellWidget(idx, i+1, radio_button)
                        radio_button.clicked.connect(lambda checked, row_idx=idx, widget=radio_button: self.selected_row(row_idx, widget))
                    else:
                        it = PySide6.QtWidgets.QTableWidgetItem(str(value))
                        it.setTextAlignment(PySide6.QtCore.Qt.AlignCenter)
                        tb_show.setItem(int(idx), i+1, it)

    def selected_row(self, row_idx, radioWidget):
        # radioWidget.setChecked(True)
        self.camera = cv2.VideoCapture(self.datas[row_idx][-1])

        self.timer = PySide6.QtCore.QTimer()
        self.timer.timeout.connect(self.display_vid)
        self.timer.start(30)

    
    def display_vid(self):
        ret, frame = self.camera.read()
        if ret:
            print(frame.shape)
            self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # frame_resize = cv2.resize(self.frame, (self.w.label_cam.width(), self.w.label_cam.height()))
            image = PySide6.QtGui.QImage(self.frame, self.frame.shape[1], self.frame.shape[0], PySide6.QtGui.QImage.Format_RGB888)
            pixmap = PySide6.QtGui.QPixmap.fromImage(image)
            self.w.label_cam.setPixmap(pixmap)
            self.w.label_cam.setScaledContents(True)