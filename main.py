import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QTimer, QUrl, QSize, QThread, QObject, Signal
from PySide6.QtGui import QPixmap, QIcon, QScreen
# from PySide6.QtWebEngineWidgets import QWebEngineView

import io
import time
import os
import socket
from datetime import datetime
# import folium
import cv2
import numpy as np

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

from utils.ScreenKeyboard import InputHandler, ScreenKeyboard 
from utils import UtilsVariables


# class KeyboardThread(QThread):
#     def __init__(self, input_handler):
#         super().__init__()
#         self.input_handler = input_handler

#     def run(self):
#         # Connect the key pressed signal to the input handler's function
#         self.input_handler.keyboard.key_pressed.connect(self.input_handler.on_key_pressed)
#         self.exec_()


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
        
        self.key_widget = None
        self.input_handler = None
        
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

        self.w.MultiScreenWg.setCurrentIndex(0)
        self.w.btn_screen1x.clicked.connect(lambda : self.spliScreen(0))
        self.w.btn_screen4x.clicked.connect(lambda : self.spliScreen(1))
        self.w.btn_screen9x.clicked.connect(lambda : self.spliScreen(2))
        self.w.btn_screen16x.clicked.connect(lambda : self.spliScreen(3))
        self.w.btn_screen25x.clicked.connect(lambda : self.spliScreen(4))
        self.w.btn_screen36x.clicked.connect(lambda : self.spliScreen(5))
        self.w.btn_screen49x.clicked.connect(lambda : self.spliScreen(6))
        self.w.btn_screen64x.clicked.connect(lambda : self.spliScreen(7))

        self.screen = None
        self.screen0 = self.w.chscreen_0_00
        self.screen0.setMinimumSize(QSize(self.screen0.width(), self.screen0.height()))
        self.screen0_available = True
        self.screen1_available = False
        self.screen2_available = False
        self.screen3_available = False
        self.screen4_available = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_gui)
        self.timer.start(1000)
        print(self.timer.isActive())

    def update_gui(self):
        sw_id = "123KOR456"
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IPAddr_s = s.getsockname()[0]
        self.w.ipaddr_foot.setText(f"IP: {IPAddr_s}")
        
        datetime_s = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.w.datetime_foot.setText(datetime_s)

    
    def screen_keyboard(self):
        print("Key Active:", UtilsVariables.keyboard_active)
        if UtilsVariables.keyboard_active:
            if self.key_widget is None:
                loader = QUiLoader()
                ui_file = QFile("ui/admgui/all_ui/keyboard.ui")
                if not ui_file.open(QIODevice.ReadOnly):
                    print(f"Cannot open UI file: {ui_file.errorString()}")
                    return
                ui = loader.load(ui_file, self)
                ui_file.close()
                self.key_widget = ScreenKeyboard(ui, self)
                
                self.input_handler = InputHandler(self.key_widget)
                self.popup.regist_widgets(self.input_handler)
                self.key_widget.key_pressed.connect(self.input_handler.on_key_pressed) # Connect the keyboard signal to the handler
                UtilsVariables.key_widget_func(self.key_widget)

        else:
            if self.key_widget is not None:
                # if self.key_widget.isActiveWindow() == True
                self.key_widget.close()
                self.key_widget = None
                self.input_handler = None
                

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
        # self.popup.setWindowFlags(Qt.WindowType.Tool)

        if event == 2:
            self.w.map_mng_frame.setVisible(True)
        else:
            self.w.map_mng_frame.setVisible(False)
        self.popup.activateWindow()
        # self.popup.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowTitleHint \
        #                     | Qt.WindowType.WindowMaximizeButtonHint | \
        #                         Qt.WindowType.WindowMinimizeButtonHint | \
        #                             Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.Window )
        self.popup.show()
        

        if event == 7:
            print("1",self.popup.w.groupbtnKeyboard)
            print("2",dialog.groupbtnKeyboard)
            self.popup.w.groupbtnKeyboard.buttonClicked.connect(self.screen_keyboard)
            if self.popup.isActiveWindow() == False:
                print("window exited")
                self.input_handler = None
            if self.key_widget is not None and self.input_handler is None:
                self.input_handler = InputHandler(self.key_widget)
                self.popup.regist_widgets(self.input_handler)
                self.key_widget.key_pressed.connect(self.input_handler.on_key_pressed)
                # print("input hanlder: inactive")
            # print(self.key_widget)
        else:
            if UtilsVariables.keyboard_active:
                self.screen_keyboard()
            self.input_handler = None
            # print(self.input_handler)
    
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
    

    def spliScreen(self, event):
        self.w.MultiScreenWg.setCurrentIndex(event)
        if event == 0:
            self.screen0_available = True
            self.screen0 = self.w.chscreen_0_00
            self.screen1_available = False
            self.screen2_available = False
            self.screen3_available = False
            self.screen4_available = False
            self.screen5_available = False
        elif event == 1:
            self.screen0 = self.w.chscreen_1_00
            self.screen0.setMinimumSize(QSize(self.screen0.width(), self.screen0.height()))
            self.screen0.setMaximumSize(QSize(self.screen0.width(), self.screen0.height()))
            
            self.screen1_available = True
            self.screen1 = self.w.chscreen_1_01
            self.screen1.setMinimumSize(QSize(self.screen1.width(), self.screen1.height()))
            self.screen1.setMaximumSize(QSize(self.screen1.width(), self.screen1.height()))
            
            self.screen2_available = True
            self.screen2 = self.w.chscreen_1_10
            self.screen2.setMinimumSize(QSize(self.screen2.width(), self.screen2.height()))
            self.screen2.setMaximumSize(QSize(self.screen2.width(), self.screen2.height()))
            
            self.screen3_available = True
            self.screen3 = self.w.chscreen_1_11
            self.screen3.setMinimumSize(QSize(self.screen3.width(), self.screen3.height()))
            self.screen3.setMaximumSize(QSize(self.screen3.width(), self.screen3.height()))

            self.screen4_available = False

            self.screen5_available = False
        elif event == 2:
            self.screen0 = self.w.chscreen_2_00
            self.screen0.setMinimumSize(QSize(self.screen0.width(), self.screen0.height()))
            self.screen0.setMaximumSize(QSize(self.screen0.width(), self.screen0.height()))
            
            self.screen1_available = True
            self.screen1 = self.w.chscreen_2_01
            self.screen1.setMinimumSize(QSize(self.screen1.width(), self.screen1.height()))
            self.screen1.setMaximumSize(QSize(self.screen1.width(), self.screen1.height()))
            
            self.screen2_available = True
            self.screen2 = self.w.chscreen_2_02
            self.screen2.setMinimumSize(QSize(self.screen2.width(), self.screen2.height()))
            self.screen2.setMaximumSize(QSize(self.screen2.width(), self.screen2.height()))
            
            self.screen3_available = True
            self.screen3 = self.w.chscreen_2_10
            self.screen3.setMinimumSize(QSize(self.screen3.width(), self.screen3.height()))
            self.screen3.setMaximumSize(QSize(self.screen3.width(), self.screen3.height()))
            
            self.screen4_available = True
            self.screen4 = self.w.chscreen_2_11
            self.screen4.setMinimumSize(QSize(self.screen4.width(), self.screen4.height()))
            self.screen4.setMaximumSize(QSize(self.screen4.width(), self.screen4.height()))
        elif event == 3:
            self.screen0 = self.w.chscreen_3_00
            self.screen0.setMinimumSize(QSize(self.screen0.width(), self.screen0.height()))
            self.screen0.setMaximumSize(QSize(self.screen0.width(), self.screen0.height()))
            
            self.screen1_available = True
            self.screen1 = self.w.chscreen_3_01
            self.screen1.setMinimumSize(QSize(self.screen1.width(), self.screen1.height()))
            self.screen1.setMaximumSize(QSize(self.screen1.width(), self.screen1.height()))
            
            self.screen2_available = True
            self.screen2 = self.w.chscreen_3_02
            self.screen2.setMinimumSize(QSize(self.screen2.width(), self.screen2.height()))
            self.screen2.setMaximumSize(QSize(self.screen2.width(), self.screen2.height()))
            
            self.screen3_available = True
            self.screen3 = self.w.chscreen_3_03
            self.screen3.setMinimumSize(QSize(self.screen3.width(), self.screen3.height()))
            self.screen3.setMaximumSize(QSize(self.screen3.width(), self.screen3.height()))
            
            self.screen4_available = True
            self.screen4 = self.w.chscreen_3_10
            self.screen4.setMinimumSize(QSize(self.screen4.width(), self.screen4.height()))
            self.screen4.setMaximumSize(QSize(self.screen4.width(), self.screen4.height()))
        elif event == 4:
            self.screen0 = self.w.chscreen_4_00
            self.screen0.setMinimumSize(QSize(self.screen0.width(), self.screen0.height()))
            self.screen0.setMaximumSize(QSize(self.screen0.width(), self.screen0.height()))
            
            self.screen1_available = True
            self.screen1 = self.w.chscreen_4_01
            self.screen1.setMinimumSize(QSize(self.screen1.width(), self.screen1.height()))
            self.screen1.setMaximumSize(QSize(self.screen1.width(), self.screen1.height()))
            
            self.screen2_available = True
            self.screen2 = self.w.chscreen_4_02
            self.screen2.setMinimumSize(QSize(self.screen2.width(), self.screen2.height()))
            self.screen2.setMaximumSize(QSize(self.screen2.width(), self.screen2.height()))
            
            self.screen3_available = True
            self.screen3 = self.w.chscreen_4_03
            self.screen3.setMinimumSize(QSize(self.screen3.width(), self.screen3.height()))
            self.screen3.setMaximumSize(QSize(self.screen3.width(), self.screen3.height()))
            
            self.screen4_available = True
            self.screen4 = self.w.chscreen_4_04
            self.screen4.setMinimumSize(QSize(self.screen4.width(), self.screen4.height()))
            self.screen4.setMaximumSize(QSize(self.screen4.width(), self.screen4.height()))
        elif event == 5:
            self.screen0 = self.w.chscreen_5_00
            self.screen0.setMinimumSize(QSize(self.screen0.width(), self.screen0.height()))
            self.screen0.setMaximumSize(QSize(self.screen0.width(), self.screen0.height()))
            
            self.screen1_available = True
            self.screen1 = self.w.chscreen_5_01
            self.screen1.setMinimumSize(QSize(self.screen1.width(), self.screen1.height()))
            self.screen1.setMaximumSize(QSize(self.screen1.width(), self.screen1.height()))
            
            self.screen2_available = True
            self.screen2 = self.w.chscreen_5_02
            self.screen2.setMinimumSize(QSize(self.screen2.width(), self.screen2.height()))
            self.screen2.setMaximumSize(QSize(self.screen2.width(), self.screen2.height()))
            
            self.screen3_available = True
            self.screen3 = self.w.chscreen_5_03
            self.screen3.setMinimumSize(QSize(self.screen3.width(), self.screen3.height()))
            self.screen3.setMaximumSize(QSize(self.screen3.width(), self.screen3.height()))
            
            self.screen4_available = True
            self.screen4 = self.w.chscreen_5_04
            self.screen4.setMinimumSize(QSize(self.screen4.width(), self.screen4.height()))
            self.screen4.setMaximumSize(QSize(self.screen4.width(), self.screen4.height()))
        elif event == 6:
            self.screen0 = self.w.chscreen_6_00
            self.screen0.setMinimumSize(QSize(self.screen0.width(), self.screen0.height()))
            self.screen0.setMaximumSize(QSize(self.screen0.width(), self.screen0.height()))
            
            self.screen1_available = True
            self.screen1 = self.w.chscreen_6_01
            self.screen1.setMinimumSize(QSize(self.screen1.width(), self.screen1.height()))
            self.screen1.setMaximumSize(QSize(self.screen1.width(), self.screen1.height()))
            
            self.screen2_available = True
            self.screen2 = self.w.chscreen_6_02
            self.screen2.setMinimumSize(QSize(self.screen2.width(), self.screen2.height()))
            self.screen2.setMaximumSize(QSize(self.screen2.width(), self.screen2.height()))
            
            self.screen3_available = True
            self.screen3 = self.w.chscreen_6_03
            self.screen3.setMinimumSize(QSize(self.screen3.width(), self.screen3.height()))
            self.screen3.setMaximumSize(QSize(self.screen3.width(), self.screen3.height()))
            
            self.screen4_available = True
            self.screen4 = self.w.chscreen_6_04
            self.screen4.setMinimumSize(QSize(self.screen4.width(), self.screen4.height()))
            self.screen4.setMaximumSize(QSize(self.screen4.width(), self.screen4.height()))
        elif event == 7:
            self.screen0 = self.w.chscreen_7_00
            self.screen0.setMinimumSize(QSize(self.screen0.width(), self.screen0.height()))
            self.screen0.setMaximumSize(QSize(self.screen0.width(), self.screen0.height()))
            
            self.screen1_available = True
            self.screen1 = self.w.chscreen_7_01
            self.screen1.setMinimumSize(QSize(self.screen1.width(), self.screen1.height()))
            self.screen1.setMaximumSize(QSize(self.screen1.width(), self.screen1.height()))
            
            self.screen2_available = True
            self.screen2 = self.w.chscreen_7_02
            self.screen2.setMinimumSize(QSize(self.screen2.width(), self.screen2.height()))
            self.screen2.setMaximumSize(QSize(self.screen2.width(), self.screen2.height()))
            
            self.screen3_available = True
            self.screen3 = self.w.chscreen_7_03
            self.screen3.setMinimumSize(QSize(self.screen3.width(), self.screen3.height()))
            self.screen3.setMaximumSize(QSize(self.screen3.width(), self.screen3.height()))
            
            self.screen4_available = True
            self.screen4 = self.w.chscreen_7_04
            self.screen4.setMinimumSize(QSize(self.screen4.width(), self.screen4.height()))
            self.screen4.setMaximumSize(QSize(self.screen4.width(), self.screen4.height()))


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
    # main_window.w.show()

    # Apply the stylesheet
    with open("ui/style/style.qss", "r") as file:
        app.setStyleSheet(file.read())

    app.exec()
