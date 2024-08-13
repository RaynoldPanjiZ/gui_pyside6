from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
import sys, os

# print(os.getcwd())
style = None
with open("ui/style/style_form.qss", "r") as file:
    style = file.read()


class UserManagement(QtWidgets.QMainWindow):
    def __init__(self, w):
        super().__init__()
        self.w = w
        self.setCentralWidget(w)
        self.setWindowTitle("User Management")
        self.setStyleSheet(style)
        self.w.chpasswd_btn.clicked.connect(self.ch_passwd)
        self.w.close_btn.clicked.connect(self.close)
        self.grouplist = [
            "system administrator", "manager", "regular user"
        ]
        self.w.usrGroup_comboBox.addItems(self.grouplist)

        self.datas1 = [
            ["admin", "manager", "system administrator", "010-1234-5678", "abc@gmail.com", 0, 0],
            ["test123", "user1", "manager", "010-1234-5678", "abc@gmail.com", 1, 0]
        ]

        tb_show = self.w.tb_show
        tb_show.setRowCount(len(self.datas1))
        
        header = tb_show.horizontalHeader()
        for i in range(tb_show.columnCount()):  # Stretch the tables by column horizontally
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        if self.datas1:
            for idx, data_num in enumerate(range(len(self.datas1))):
                data_if = self.datas1[data_num]
                print("dataif:", data_if)
                it = QtWidgets.QTableWidgetItem(str(data_num + 1))  # numbering
                it.setTextAlignment(Qt.AlignCenter)
                tb_show.setItem(int(idx), 0, it)
                for i, value in enumerate(data_if):
                    if i == 5 or i == 6:
                        chbox_frame = QtWidgets.QFrame()
                        chbox_layout = QtWidgets.QHBoxLayout(chbox_frame)
                        checkbox = QtWidgets.QCheckBox('', self)
                        checkbox.setChecked(value == 1)
                        checkbox.setEnabled(False)
                        chbox_layout.addWidget(checkbox)
                        chbox_layout.setAlignment(checkbox, Qt.AlignCenter)
                        chbox_frame.setLayout(chbox_layout)
                        tb_show.setCellWidget(idx, i+1, chbox_frame)
                    else:
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setTextAlignment(Qt.AlignCenter)
                        tb_show.setItem(int(idx), i+1, it)
                btn_delete = QtWidgets.QPushButton()
                btn_delete.setText("Delete")
                # btn_delete.setStyleSheet(btn_style)
                tb_show.setCellWidget(idx, i+2, btn_delete)
                btn_delete.clicked.connect(lambda _, x=idx:self.del_row(x))
                tb_show.cellClicked.connect(self.selected_row)

    def selected_row(self, row_id, col_id):
        self.w.id_edit.setText(str(self.datas1[row_id][0]))
        for group_id, value in enumerate(self.grouplist):
            if str(self.datas1[row_id][2]) == value:
                self.w.usrGroup_comboBox.setCurrentIndex(group_id)
                break
        self.w.name_edit.setText(str(self.datas1[row_id][1]))
        self.w.contact_edit.setText(str(self.datas1[row_id][3]))
        self.w.email_edit.setText(str(self.datas1[row_id][4]))
        self.w.msg_checkbox.setChecked(self.datas1[row_id][5] == 1)
        self.w.img_checkBox.setChecked(self.datas1[row_id][6] == 1)
    
    def ch_passwd(self):
        print("Success!")
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/user_management/change_pw_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("Change Password")
        def confirm():
            print("confirm")
        
        self.popup.btn_confirm.clicked.connect(confirm)
        self.popup.btn_cancel.clicked.connect(self.popup.close)
        self.popup.exec()

    def del_row(self, row_id):
        self.selected_row(row_id, None)
        loader = QUiLoader()
        ui_file = QFile("ui/admgui/all_ui/user_management/delete_user_dialog.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            return
        dialog = loader.load(ui_file, self)
        ui_file.close()
        self.popup = dialog
        self.popup.setWindowTitle("Delete User")

        self.popup.text_msg.setText(f"Do you want to delete user ID '{self.datas1[row_id][0]}'?")
        def confirm():
            print("confirm")
        
        self.popup.btn_confirm.clicked.connect(confirm)
        self.popup.btn_cancel.clicked.connect(self.popup.close)
        self.popup.exec()

