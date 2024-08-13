import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QTimer
from PySide6.QtGui import QPixmap, QIcon

import time
import os
import socket
from datetime import datetime

from sidemenu.UserManagement import UserManagement
from sidemenu.NetworkSetting import NetSetting
from sidemenu.CameraMapManag import CameraMapMng
from sidemenu.ZoneSetting import ZoneSetting
from sidemenu.SurveillanceArea import SurveillanceArea
from sidemenu.EventSetting import EventSetting
from sidemenu.AIEngineUpdate import AIEngineUpdate
from sidemenu.SystemSetting import SystemSetting
from sidemenu.SystemLog import SystemLog

from sidemenu.SystemLogin import SystemLogin


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.w.setWindowTitle("MainWindow Title")
        self.w.label_3.setPixmap(QPixmap(u"ui/icon/aery_rm.png"))
        self.w.screen_lock_btn.setIcon(QIcon(u"ui/icon/lock (1).png"))
        self.w.btn_screen1x.setIcon(QIcon(u"ui/icon/grid1_.png"))
        self.w.btn_screen4x.setIcon(QIcon(u"ui/icon/grid4_.png"))
        self.w.btn_screen9x.setIcon(QIcon(u"ui/icon/grid9_.png"))
        self.w.fullscreen_ch_btn.setIcon(QIcon(u"ui/icon/fullscreen1.png"))

        self.w.map_mng_frame.setVisible(False)
        self.w.delete_cam_btn.clicked.connect(self.delete_camera_dialog)
        
        self.popup = None  # Keep a reference to the popup
        self.sidebar_forms = [
            "ui/admgui/all_ui/network_setting/network_setting.ui",
            "ui/admgui/all_ui/user_management/user_management.ui",
            "ui/admgui/all_ui/cameramap_mng/cameramap_mng.ui",
            "ui/admgui/all_ui/userda_mng/userda_mng.ui",
            "ui/admgui/all_ui/surveillance_areaSett/camera_selection.ui",
            "ui/admgui/all_ui/event_setting/event_setting.ui",
            "ui/admgui/all_ui/aiengine_update/aiengine_update.ui",
            "ui/admgui/all_ui/system_setting/system_setting_SuperAdmin.ui",
            "ui/admgui/all_ui/system_log/system_log.ui",
            "ui/admgui/all_ui/system_setting/ServerConnection_login.ui"
        ]
        self.w.net_setting.clicked.connect(lambda:self.show_popup(0, NetSetting))
        self.w.user_management.clicked.connect(lambda:self.show_popup(1, UserManagement))
        self.w.camera_map_manag.clicked.connect(lambda:self.show_popup(2, CameraMapMng))
        self.w.custom_zone_setting.clicked.connect(lambda:self.show_popup(3, ZoneSetting))
        self.w.surv_area_setting.clicked.connect(lambda:self.show_popup(4, SurveillanceArea))
        self.w.event_setting.clicked.connect(lambda:self.show_popup(5, EventSetting))
        self.w.ai_engine_up.clicked.connect(lambda:self.show_popup(6, AIEngineUpdate))
        self.w.system_setting.clicked.connect(lambda:self.show_popup(7, SystemSetting))
        self.w.system_log.clicked.connect(lambda:self.show_popup(8, SystemLog))
        
        self.w.login_btn.clicked.connect(lambda:self.show_popup(9, SystemLogin))
        
        self.w.minimize_btn.clicked.connect(self.minimize_window)
        self.w.exit_btn.clicked.connect(self.exit_button)
        self.show_popup(0, NetSetting)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_gui)
        self.timer.start(1000)
        print(self.timer.isActive())

    def update_gui(self):
        # hostname = socket.gethostname()
        # IPAddr = socket.gethostbyname(hostname)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IPAddr_s = s.getsockname()[0]
        self.w.ipaddr_foot.setText(f"IP: {IPAddr_s}")
        
        datetime_s = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.w.datetime_foot.setText(datetime_s)



    def show_popup(self, event, PopupClass):
        print("Success!")
        loader = QUiLoader()
        ui_file = QFile(self.sidebar_forms[event])
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        
        dialog = loader.load(ui_file, self)
        ui_file.close()
        
        # Store the popup instance to prevent it from being garbage collected
        self.popup = PopupClass(dialog)

        if event == 2:
            self.w.map_mng_frame.setVisible(True)
        else:
            self.w.map_mng_frame.setVisible(False)
        
        self.popup.show()
    
    def delete_camera_dialog(self):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("Delete Camera")
        dlg.setText("Do you want to delete this camera?")
        dlg.addButton('Confirm', QtWidgets.QMessageBox.YesRole)
        dlg.addButton(QtWidgets.QMessageBox.Cancel)
        with open("ui/style/style_form.qss", "r") as file:
            dlg.setStyleSheet(file.read())
        button = dlg.exec()

        if button == QtWidgets.QMessageBox.Cancel:
            print("No!")
        else:
            print("Yes!")
    
    def minimize_window(self):
        app = QtWidgets.QApplication.instance()
        app.activeWindow().showMinimized()

    def exit_button(self):
        QtWidgets.QApplication.instance().quit()

if __name__ == "__main__":
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)

    # Load the main window UI
    ui_file = QFile("ui/admgui/all_ui/mainwindow.ui")
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open UI file: {ui_file.errorString()}")
        sys.exit(-1)
    
    window = loader.load(ui_file, None)
    ui_file.close()

    # Create and show the main window
    main_window = MainWindow(window)
    main_window.w.showFullScreen()

    # Apply the stylesheet
    with open("ui/style/style.qss", "r") as file:
        app.setStyleSheet(file.read())

    app.exec()
