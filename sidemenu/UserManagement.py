# from PySide6 import QtWidgets
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import QFile, QIODevice, Qt, QTimer

import PySide6
import sys, os
import json
from utils.ScreenKeyboard import InputHandler
from utils import UtilsVariables

# print(os.getcwd())
style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class UserManagement(PySide6.QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("User Management")
        self.setStyleSheet(style)
        self.w.new_btn.clicked.connect(self.new_data)
        self.w.edit_btn.clicked.connect(self.edit_data)
        self.w.chpasswd_btn.clicked.connect(self.ch_passwd)
        self.w.close_btn.clicked.connect(self.close)

        print("user:", UtilsVariables.keyboard_active)
        print("user:", UtilsVariables.key_widget)

        if UtilsVariables.keyboard_active and UtilsVariables.key_widget is not None:
            self.input_handler1 = InputHandler(UtilsVariables.key_widget)
            UtilsVariables.key_widget.key_pressed.connect(self.input_handler1.on_key_pressed)
            input_widgets = self.findChildren(PySide6.QtWidgets.QLineEdit) + self.findChildren(PySide6.QtWidgets.QTextEdit)
            for widget in input_widgets:
                widget.installEventFilter(self.input_handler1)

        self.grouplist = [
            "system administrator", "manager", "regular user"
        ]
        self.w.usrGroup_comboBox.addItems(self.grouplist)

        self.datas = []
        if os.path.exists('./datas/userManagement.json'):
            f = open('./datas/userManagement.json')
            self.datas = json.load(f)

        self.timer_fetch = PySide6.QtCore.QTimer()
        self.timer_fetch.timeout.connect(self.update_table)
        self.timer_fetch.start(700)
    
    def update_table(self):
        tb_show = self.w.tb_show
        tb_show.setRowCount(len(self.datas))
        
        header = tb_show.horizontalHeader()
        for i in range(tb_show.columnCount()):  # Stretch the tables by column horizontally
            header.setSectionResizeMode(i, PySide6.QtWidgets.QHeaderView.Stretch)
        
        if self.datas:
            for idx, data_num in enumerate(range(len(self.datas))):
                it = PySide6.QtWidgets.QTableWidgetItem(str(data_num+1))
                it.setTextAlignment(PySide6.QtCore.Qt.AlignCenter)
                tb_show.setItem(int(idx), 0, it)
                i=0
                for (key, value) in (self.datas[data_num].items()):
                    if key == "password": continue
                    elif key == "msg" or key == "img":
                        chbox_frame = PySide6.QtWidgets.QFrame()
                        chbox_layout = PySide6.QtWidgets.QHBoxLayout(chbox_frame)
                        # chbox_frame.setMaximumWidth(19)
                        # chbox_frame.setStyleSheet("QFrame{border: None; background-color: rgba(0,0,0,0;}")
                        checkbox = PySide6.QtWidgets.QCheckBox('', self)
                        checkbox.setChecked(value == 1)
                        checkbox.setEnabled(False)
                        chbox_layout.addWidget(checkbox)
                        chbox_layout.setAlignment(checkbox, PySide6.QtCore.Qt.AlignCenter)
                        chbox_layout.setContentsMargins(0,0,0,0)
                        chbox_frame.setLayout(chbox_layout)
                        tb_show.setCellWidget(idx, i+1, chbox_frame)
                    else:
                        it = PySide6.QtWidgets.QTableWidgetItem(str(value))
                        it.setTextAlignment(PySide6.QtCore.Qt.AlignCenter)
                        tb_show.setItem(int(idx), i+1, it)
                    i+=1
                btn_delete = PySide6.QtWidgets.QPushButton()
                btn_delete.setText("Delete")
                # btn_delete.setStyleSheet(btn_style)
                tb_show.setCellWidget(idx, i+1, btn_delete)
                btn_delete.clicked.connect(lambda _, x=idx:self.del_row(x))
                tb_show.cellClicked.connect(self.selected_row)

    def selected_row(self, row_id, col_id):
        self.w.id_edit.setText(str(self.datas[row_id]["id"]))
        for group_id, value in enumerate(self.grouplist):
            if str(self.datas[row_id]["usr_group"]) == value:
                self.w.usrGroup_comboBox.setCurrentIndex(group_id)
                break
        self.w.name_edit.setText(str(self.datas[row_id]["name"]))
        self.w.contact_edit.setText(str(self.datas[row_id]["contact"]))
        self.w.email_edit.setText(str(self.datas[row_id]["email"]))
        self.w.pass_edit.setText(str(self.datas[row_id]["password"]))
        self.w.verifyPass_edit.setText(str(self.datas[row_id]["password"]))
        self.w.msg_checkbox.setChecked(self.datas[row_id]["msg"] == 1)
        self.w.img_checkBox.setChecked(self.datas[row_id]["img"] == 1)
    
    def new_data(self):
        id = self.w.id_edit.text()
        name = self.w.name_edit.text()
        usrgroup = self.w.usrGroup_comboBox.currentText()
        contact = self.w.contact_edit.text()
        email = self.w.email_edit.text()
        passwd = self.w.pass_edit.text()
        msg = self.w.msg_checkbox.isChecked()
        img = self.w.img_checkBox.isChecked()

        if id in [i["id"] for i in self.datas]:
            PySide6.QtWidgets.QMessageBox.critical(self, "Error", f"ID '{id}' already exists")
            return
        
        update_data = {
            'id': id,
            'name': name,
            'usr_group': usrgroup,
            'password': passwd,
            'contact': contact,
            'email': email,
            'msg': 1 if msg==True else 0,
            'img': 1 if img==True else 0
        }
        self.datas.append(update_data)
        with open("datas/userManagement.json", "w") as outfile: 
            json.dump(self.datas, outfile, indent=4)
    
    def edit_data(self):
        id = self.w.id_edit.text()
        name = self.w.name_edit.text()
        usrgroup = self.w.usrGroup_comboBox.currentText()
        contact = self.w.contact_edit.text()
        email = self.w.email_edit.text()
        passwd = self.w.pass_edit.text()
        msg = self.w.msg_checkbox.isChecked()
        img = self.w.img_checkBox.isChecked()

        idx = None
        for i, idd in enumerate([i["id"] for i in self.datas]):
            if id in idd:
                idx = i
                break
        else:
            PySide6.QtWidgets.QMessageBox.critical(self, "Error", f"ID '{id}' not found")
            return
        print(idx,":", id)
        update_data = {
            'id': id,
            'name': name,
            'usr_group': usrgroup,
            'password': passwd,
            'contact': contact,
            'email': email,
            'msg': 1 if msg==True else 0,
            'img': 1 if img==True else 0
        }
        self.datas[idx] = update_data
        with open("datas/userManagement.json", "w") as outfile: 
            json.dump(self.datas, outfile, indent=4)

    def ch_passwd(self):
        print("Success!")
        loader = PySide6.QtUiTools.QUiLoader()
        ui_file = PySide6.QtCore.QFile("ui/admgui/all_ui/user_management/change_pw_dialog.ui")
        if not ui_file.open(PySide6.QtCore.QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("Change Password")
        if UtilsVariables.keyboard_active and UtilsVariables.key_widget is not None:
            UtilsVariables.key_widget.setWindowFlags(self.windowFlags() | PySide6.QtCore.Qt.WindowType.WindowStaysOnTopHint)
            self.input_handler2 = InputHandler(UtilsVariables.key_widget)
            UtilsVariables.key_widget.key_pressed.connect(self.input_handler2.on_key_pressed)
            input_widgets = self.popup.findChildren(PySide6.QtWidgets.QLineEdit) + self.popup.findChildren(PySide6.QtWidgets.QTextEdit)
            for widget in input_widgets:
                widget.installEventFilter(self.input_handler2)

        def confirm():
            print("confirm")
        
        self.popup.btn_confirm.clicked.connect(confirm)
        self.popup.btn_cancel.clicked.connect(self.popup.close)
        self.popup.show()

    def del_row(self, row_id):
        self.selected_row(row_id, None)
        loader = PySide6.QtUiTools.QUiLoader()
        ui_file = PySide6.QtCore.QFile("ui/admgui/all_ui/user_management/delete_user_dialog.ui")
        if not ui_file.open(PySide6.QtCore.QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("Delete User")

        self.popup.text_msg.setText(f"Do you want to delete user ID '{self.datas[row_id]['id']}'?")
        def confirm():
            id = self.datas[row_id]['id']
            self.datas = [item for item in self.datas if item["id"] != id]
            with open("datas/userManagement.json", "w") as outfile: 
                json.dump(self.datas, outfile, indent=4)
            self.popup.close()
        
        self.popup.btn_confirm.clicked.connect(confirm)
        self.popup.btn_cancel.clicked.connect(self.popup.close)
        self.popup.exec()

