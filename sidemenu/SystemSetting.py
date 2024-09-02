from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QDate, QTime, QTimeZone
from PySide6.QtGui import QGuiApplication
import sys, os
import subprocess
import shutil
# import ntplib
import time
import platform
from datetime import datetime
from pytz import timezone

style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class SystemSetting(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("System Settings")
        self.setStyleSheet(style)
        self.w.datetime_setting_btn.clicked.connect(self.datetime)
        self.w.server_connect_btn.clicked.connect(self.server_connection)
        self.w.factory_reset_btn.clicked.connect(self.factory_reset)

        total, used, free = shutil.disk_usage("/")
        total_gb = f"{total // (2**30)} GB"
        used_gb = f"{used // (2**30)} GB"
        used_percent = f"{round((used/total)*100, 2)} %"
        free_gb = f"{free // (2**30)} GB"
        free_percent = f"{round((free/total)*100, 2)} %"

        self.w.storageCapacity_edit.setText(total_gb)
        self.w.storageUsage_edit.setText(used_gb)
        self.w.storageUsage_percent.setText(used_percent)
        self.w.storageSpace_edit.setText(free_gb)
        self.w.storageSpace_percent.setText(free_percent)

        screen_list = [
            "800x600", 
            "1024x768", 
            "1280x720", 
            "1280x1024", 
            "1366x768", 
            "1920x1080", 
            "1920x1200"
        ]

        screen = self.screen().availableGeometry()
        screen_n = f"{screen.width()}x{screen.height()}"
        print(screen_n)
        self.w.screen_comboBox.addItems(screen_list)
        for i, scr in enumerate(screen_list):
            if scr == screen_n:
                self.w.screen_comboBox.setCurrentIndex(i)
                break
        self.w.screen_comboBox.currentIndexChanged.connect(self.change_resolution)
    
    def change_resolution(self):
        selected_resolution = self.w.screen_comboBox.currentText()
        xres, yres = selected_resolution.split('x')     # Split resolution to xres dan yres
        
        # fbset command https://www.linuxquestions.org/questions/linux-from-scratch-13/so-i-got-fbset-working-can-change-resolution-at-run-time-4175502019/
        try:
            subprocess.run(['fbset', '-xres', xres, '-yres', yres, '-match'], check=True)
            QtWidgets.QMessageBox.information(self, "Display resolution", f"Resolution successfully changed to : {selected_resolution}")
        except subprocess.CalledProcessError as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to changed resolution: {e}")


    def datetime(self):
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/system_setting/ServerConnection_datesetting_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("Date/Time Settings")

        self.popup.sync_ntpserver.clicked.connect(self.sync_time)
        self.popup.cancel_button.clicked.connect(self.popup.close)
        self.popup.apply_button.clicked.connect(self.apply_btn)
        self.ntp_sync_active = False
        
        datetimenow = datetime.today()
        self.date_field = datetimenow.strftime('%Y-%m-%d')
        q_date = QDate.fromString(self.date_field, "yyyy-MM-dd")
        self.popup.dateEdit.setDate(q_date)

        self.time_field = datetimenow.strftime('%H:%M:%S')
        q_time = QTime.fromString(self.time_field)
        self.popup.timeEdit.setTime(q_time)

        self.timezone_name = '/'.join(os.path.realpath('/etc/localtime').split('/')[-2:])      ## https://stackoverflow.com/a/25634136

        timezones = QTimeZone.availableTimeZoneIds()
        for i, timezone in enumerate(timezones):
            self.popup.timezone_combobox.addItem(timezone.data().decode("utf-8"))   ## https://forum.qt.io/post/426497
            if timezone == self.timezone_name:
                self.popup.timezone_combobox.setCurrentIndex(i)

        self.popup.exec()

    def sync_time(self):
        """Synchronize time with NTP server."""
        self.timezone_name = self.popup.timezone_combobox.currentText()

        try:
            ## https://www.tutorialspoint.com/how-to-convert-date-and-time-with-different-timezones-in-python#:~:text=Enter%20the%20date%20format%20as,to%20it%20say%20'UTC'.
            ## https://phoenixnap.com/kb/how-to-set-or-change-timezone-date-time-ubuntu
            datetime_by_timezone = datetime.now(timezone(self.timezone_name))

            datenow_format = datetime_by_timezone.strftime("%Y-%m-%d")
            q_date = QDate.fromString(datenow_format, "yyyy-MM-dd")
            self.popup.dateEdit.setDate(q_date)

            timenow_format = datetime_by_timezone.strftime("%H:%M:%S")
            q_time = QTime.fromString(timenow_format)
            self.popup.timeEdit.setTime(q_time)

            # self.popup.apply_button.clicked.connect(self.apply_sync)
            self.ntp_sync_active = True

            QtWidgets.QMessageBox.information(self, "NTP Sync", f"Time synchronized with NTP server.\nNTP Time: {timenow_format}\nTimezone: {self.timezone_name}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "NTP Sync Error", f"Failed to synchronize with NTP server.\nError: {str(e)}")
    
    def apply_btn(self):
        if self.ntp_sync_active:
            self.apply_sync()
        else:
            self.apply_datetime_change()
    
    
    def apply_datetime_change(self):
        if platform.system() == "Linux":
            os.system("sudo timedatectl set-ntp no")
            # os.system(f"sudo timedatectl set-timezone {self.timezone_name}")
            os.system(f"sudo timedatectl set-time {self.date_field}")
            os.system(f"sudo timedatectl set-time {self.time_field}")
        self.ntp_sync_active = False
        self.popup.close()

    def apply_sync(self):
        if platform.system() == "Linux":
            os.system("sudo timedatectl set-ntp yes")
            os.system(f"sudo timedatectl set-timezone {self.timezone_name}")
        self.ntp_sync_active = False
        self.popup.close()



    def server_connection(self, s):     # https://doc.qt.io/qt-6/qmessagebox.html
        print("click", s)
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("Server Connection")
        dlg.setText("The server connection was successfull")
        dlg.addButton(QtWidgets.QMessageBox.Close)
        with open("ui/style/style_form.qss", "r") as file:
            dlg.setStyleSheet(file.read())
        button = dlg.exec()

        if button == QtWidgets.QMessageBox.Close:
            print("Success!")   

    def factory_reset(self, s):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("Factory Initiation")
        dlg.setText("Would you like to proceed with factory reset?")
        dlg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes)
        with open("ui/style/style_form.qss", "r") as file:
            dlg.setStyleSheet(file.read())
        button = dlg.exec()

        if button == QtWidgets.QMessageBox.Yes:
            print("Success!")
            loader = QUiLoader()
            ui_file = QFile("ui/admgui/all_ui/system_setting/ServerConnection_factory_initial_progress_bar_dialog.ui")
            if not ui_file.open(QIODevice.ReadOnly):
                print(f"Cannot open UI file: {ui_file.errorString()}")
                return
            dialog = loader.load(ui_file, self)
            ui_file.close()
            self.popup = dialog
            self.popup.setWindowTitle("Factory Initiation")
            self.popup.exec()
        else:
            print("Failed!")