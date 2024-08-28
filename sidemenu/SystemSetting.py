from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QDate, QTime
from PySide6.QtGui import QGuiApplication
import sys, os
import shutil

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

        screen = self.screen().availableGeometry()
        screen_n = f"{screen.width()} x {screen.height()}"
        print(screen_n)
        self.w.screen_comboBox.addItems([screen_n])


    def datetime(self):
        from datetime import datetime
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/system_setting/ServerConnection_datesetting_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("Date/Time Settings")
        
        datenow = datetime.today().strftime('%Y-%m-%d')
        q_date = QDate.fromString(datenow, "yyyy-MM-dd")
        self.popup.dateEdit.setDate(q_date)

        timenow = datetime.today().strftime('%H:%M:%S')
        q_time = QTime.fromString(timenow)
        self.popup.timeEdit.setTime(q_time)


        self.popup.exec()

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