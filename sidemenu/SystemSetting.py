from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os

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