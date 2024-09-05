# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_setting_SuperAdmin.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(905, 375)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_bar = QFrame(Form)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.label_5 = QLabel(self.title_bar)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.pushButton_9 = QPushButton(self.title_bar)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton_9)


        self.verticalLayout.addWidget(self.title_bar)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.keyboard_used = QRadioButton(self.frame_7)
        self.groupbtnKeyboard = QButtonGroup(Form)
        self.groupbtnKeyboard.setObjectName(u"groupbtnKeyboard")
        self.groupbtnKeyboard.addButton(self.keyboard_used)
        self.keyboard_used.setObjectName(u"keyboard_used")

        self.horizontalLayout_6.addWidget(self.keyboard_used)

        self.keyboard_unused = QRadioButton(self.frame_7)
        self.groupbtnKeyboard.addButton(self.keyboard_unused)
        self.keyboard_unused.setObjectName(u"keyboard_unused")

        self.horizontalLayout_6.addWidget(self.keyboard_unused)


        self.gridLayout.addWidget(self.frame_7, 1, 9, 1, 2)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_5.addWidget(self.label_18)

        self.comboBox_4 = QComboBox(self.frame_8)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_5.addWidget(self.comboBox_4)

        self.comboBox_6 = QComboBox(self.frame_8)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_5.addWidget(self.comboBox_6)

        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_19)

        self.comboBox_5 = QComboBox(self.frame_8)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_5.addWidget(self.comboBox_5)

        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_20)


        self.gridLayout.addWidget(self.frame_8, 5, 5, 1, 7)

        self.storageSpace_edit = QLineEdit(self.frame)
        self.storageSpace_edit.setObjectName(u"storageSpace_edit")
        self.storageSpace_edit.setEnabled(False)

        self.gridLayout.addWidget(self.storageSpace_edit, 3, 9, 1, 1)

        self.storageSpace_percent = QLabel(self.frame)
        self.storageSpace_percent.setObjectName(u"storageSpace_percent")

        self.gridLayout.addWidget(self.storageSpace_percent, 3, 10, 1, 1)

        self.id_edit = QLineEdit(self.frame)
        self.id_edit.setObjectName(u"id_edit")
        self.id_edit.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.id_edit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.rebootCycle_comboBox = QComboBox(self.frame)
        self.rebootCycle_comboBox.addItem("")
        self.rebootCycle_comboBox.addItem("")
        self.rebootCycle_comboBox.addItem("")
        self.rebootCycle_comboBox.setObjectName(u"rebootCycle_comboBox")

        self.gridLayout.addWidget(self.rebootCycle_comboBox, 5, 4, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 3, 1, 1)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 1, 7, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton = QRadioButton(self.frame_4)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_4)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)


        self.gridLayout.addWidget(self.frame_4, 5, 1, 1, 1)

        self.version_edit = QLineEdit(self.frame)
        self.version_edit.setObjectName(u"version_edit")
        self.version_edit.setMouseTracking(True)
        self.version_edit.setFocusPolicy(Qt.StrongFocus)
        self.version_edit.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout.addWidget(self.version_edit, 0, 4, 1, 2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 7, 3, 1, 1)

        self.storageUsage_edit = QLineEdit(self.frame)
        self.storageUsage_edit.setObjectName(u"storageUsage_edit")
        self.storageUsage_edit.setEnabled(False)

        self.gridLayout.addWidget(self.storageUsage_edit, 3, 4, 1, 1)

        self.server_connect_btn = QPushButton(self.frame)
        self.server_connect_btn.setObjectName(u"server_connect_btn")

        self.gridLayout.addWidget(self.server_connect_btn, 0, 6, 1, 2)

        self.screen_comboBox = QComboBox(self.frame)
        self.screen_comboBox.setObjectName(u"screen_comboBox")

        self.gridLayout.addWidget(self.screen_comboBox, 1, 4, 1, 2)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 3, 7, 1, 1)

        self.elapsed_time = QSpinBox(self.frame)
        self.elapsed_time.setObjectName(u"elapsed_time")

        self.gridLayout.addWidget(self.elapsed_time, 7, 4, 1, 1)

        self.storageUsage_percent = QLabel(self.frame)
        self.storageUsage_percent.setObjectName(u"storageUsage_percent")

        self.gridLayout.addWidget(self.storageUsage_percent, 3, 5, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_3 = QRadioButton(self.frame_5)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.frame_5)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_3.addWidget(self.radioButton_4)


        self.gridLayout.addWidget(self.frame_5, 7, 1, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 3, 1, 1)

        self.lang_comboBox = QComboBox(self.frame)
        self.lang_comboBox.addItem("")
        self.lang_comboBox.addItem("")
        self.lang_comboBox.setObjectName(u"lang_comboBox")

        self.gridLayout.addWidget(self.lang_comboBox, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(170, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout.addWidget(self.label_13)

        self.storageCapacity_edit = QLineEdit(self.frame_2)
        self.storageCapacity_edit.setObjectName(u"storageCapacity_edit")
        self.storageCapacity_edit.setEnabled(False)

        self.horizontalLayout.addWidget(self.storageCapacity_edit)


        self.gridLayout.addWidget(self.frame_2, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 11, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_2.addWidget(self.pushButton_10, 1, 4, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 1, 3, 1, 1)

        self.factory_reset_btn = QPushButton(self.frame_3)
        self.factory_reset_btn.setObjectName(u"factory_reset_btn")

        self.gridLayout_2.addWidget(self.factory_reset_btn, 0, 4, 1, 1)

        self.datetime_setting_btn = QPushButton(self.frame_3)
        self.datetime_setting_btn.setObjectName(u"datetime_setting_btn")

        self.gridLayout_2.addWidget(self.datetime_setting_btn, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(170, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"System Settings", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Usage", None))
        self.keyboard_used.setText(QCoreApplication.translate("Form", u"Used", None))
        self.keyboard_unused.setText(QCoreApplication.translate("Form", u"Unused", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Time", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Form", u"AM", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Form", u"PM", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("Form", u"12", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Form", u"11", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("Form", u"10", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("Form", u"9", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("Form", u"8", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("Form", u"7", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("Form", u"6", None))
        self.comboBox_6.setItemText(7, QCoreApplication.translate("Form", u"5", None))
        self.comboBox_6.setItemText(8, QCoreApplication.translate("Form", u"4", None))
        self.comboBox_6.setItemText(9, QCoreApplication.translate("Form", u"3", None))
        self.comboBox_6.setItemText(10, QCoreApplication.translate("Form", u"2", None))
        self.comboBox_6.setItemText(11, QCoreApplication.translate("Form", u"1", None))
        self.comboBox_6.setItemText(12, QCoreApplication.translate("Form", u"0", None))

        self.label_19.setText(QCoreApplication.translate("Form", u"h", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Form", u"60", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Form", u"45", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("Form", u"30", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("Form", u"25", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("Form", u"10", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("Form", u"9", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("Form", u"8", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("Form", u"7", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("Form", u"6", None))
        self.comboBox_5.setItemText(9, QCoreApplication.translate("Form", u"5", None))
        self.comboBox_5.setItemText(10, QCoreApplication.translate("Form", u"4", None))
        self.comboBox_5.setItemText(11, QCoreApplication.translate("Form", u"3", None))
        self.comboBox_5.setItemText(12, QCoreApplication.translate("Form", u"2", None))
        self.comboBox_5.setItemText(13, QCoreApplication.translate("Form", u"1", None))
        self.comboBox_5.setItemText(14, QCoreApplication.translate("Form", u"0", None))

        self.label_20.setText(QCoreApplication.translate("Form", u"m", None))
        self.storageSpace_percent.setText(QCoreApplication.translate("Form", u"-%", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Equipment ID", None))
        self.rebootCycle_comboBox.setItemText(0, QCoreApplication.translate("Form", u"1 week", None))
        self.rebootCycle_comboBox.setItemText(1, QCoreApplication.translate("Form", u"1 month", None))
        self.rebootCycle_comboBox.setItemText(2, QCoreApplication.translate("Form", u"3 months", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"Automatic Restart", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Automatic Logout", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Reboot Cycle", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Screen Keyboard", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Language", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Used", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Unused", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"HDD Information", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"S/W Ver.", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Elapsed Time", None))
        self.server_connect_btn.setText(QCoreApplication.translate("Form", u"Server Connection", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Remaining Space", None))
        self.storageUsage_percent.setText(QCoreApplication.translate("Form", u"-%", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"Used", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"Unused", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Screen Resolution", None))
        self.lang_comboBox.setItemText(0, QCoreApplication.translate("Form", u"English", None))
        self.lang_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Korea", None))

        self.label_13.setText(QCoreApplication.translate("Form", u"Capacity", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Data Deletion", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Export", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"Terminate", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"System Restart", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Load", None))
        self.label.setText(QCoreApplication.translate("Form", u"System Information", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"System Shutdown", None))
        self.factory_reset_btn.setText(QCoreApplication.translate("Form", u"Factory Reset", None))
        self.datetime_setting_btn.setText(QCoreApplication.translate("Form", u"Date/Time Setting", None))
    # retranslateUi

