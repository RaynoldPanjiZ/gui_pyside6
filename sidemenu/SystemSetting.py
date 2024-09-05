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
from utils.ScreenKeyboard import ScreenKeyboard, ScreenKeyboard2
# from sidemenu import virtual_key

style = None
virtual_key = ""
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class SystemSetting(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        
        self.virtual_key = ''
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

        self.keypopup = None
        self.w.groupbtnKeyboard.buttonClicked.connect(self.screen_keyboard)

        self.current_line_edit = None
        self.w.id_edit.installEventFilter(self)
        self.w.version_edit.installEventFilter(self)
        self.w.elapsed_time.installEventFilter(self)
    
    def eventFilter(self, source, event):       ## https://stackoverflow.com/questions/66235661/qevent-mousebuttonpress-enum-type-missing-in-pyqt6
        global virtual_key
        # print(event.type())
        if event.type() == event.Type.MouseButtonPress:
            self.current_line_edit = source  # Update focused line edit
            self.keypopup.activateWindow()  
            self.keypopup.raise_()  
            if isinstance(source, QtWidgets.QLineEdit):
                virtual_key = self.current_line_edit.text()
            elif isinstance(source, QtWidgets.QSpinBox):
                virtual_key = str(self.current_line_edit.value())
            elif isinstance(source, QtWidgets.QTextEdit):
                virtual_key = self.current_line_edit.textCursor()
        return super().eventFilter(source, event)
    
    def screen_keyboard(self):
        if self.w.keyboard_used.isChecked():
            if self.keypopup is None:
                loader = QUiLoader()
                ui_file = QFile("ui/admgui/all_ui/keyboard.ui")
                if not ui_file.open(QIODevice.ReadOnly):
                    print(f"Cannot open UI file: {ui_file.errorString()}")
                    return
                ui = loader.load(ui_file, self)
                ui_file.close()
                self.keypopup = ScreenKeyboard(ui)
                self.keypopup.key_pressed.connect(self.recv_key)
                self.keypopup.show()
        else:
            if self.keypopup is not None:
                # if self.keypopup.isActiveWindow() == True
                self.keypopup.close()
                self.keypopup = None

        
    
    def recv_key(self, key):
        global virtual_key

        if self.current_line_edit is not None:
            if isinstance(self.current_line_edit, QtWidgets.QLineEdit):
                if key == '': 
                    virtual_key += ' '
                elif key == '←': 
                    virtual_key = virtual_key[:-1]
                elif key == 'ENTER':
                    pass
                else:
                    virtual_key += key
                # print(virtual_key)
                self.keypopup.w.edit_text.setText(virtual_key)
                self.current_line_edit.setText(virtual_key)
            elif isinstance(self.current_line_edit, QtWidgets.QSpinBox):
                if key.isdigit():
                    # new_value = virtual_key + key if virtual_key != "0" else key
                    virtual_key = str(virtual_key) + str(key)
                    virtual_key = virtual_key if str(self.current_line_edit.maximum()) == virtual_key else ''
                elif key == "←":
                    virtual_key = virtual_key[:-1]
                elif key == 'ENTER': 
                    pass
                elif key == '': 
                    pass
                print(virtual_key)
                self.keypopup.w.edit_text.setText(virtual_key)
                self.current_line_edit.setValue(int(virtual_key))



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
        dateedit = self.popup.dateEdit.date()
        self.date_field = dateedit.toString('yyyy-MM-dd')

        timeedit = self.popup.timeEdit.time()
        self.time_field = timeedit.toString('HH:mm:ss')

        if platform.system() == "Linux":
            os.system("sudo timedatectl set-ntp no")
            # os.system(f"sudo timedatectl set-timezone {self.timezone_name}")
            os.system(f"sudo timedatectl set-time {self.date_field}")
            os.system(f"sudo timedatectl set-time {self.time_field}")
            print(self.date_field, self.time_field)
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