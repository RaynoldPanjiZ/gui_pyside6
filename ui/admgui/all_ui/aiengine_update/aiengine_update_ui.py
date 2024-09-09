# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aiengine_update.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(659, 372)
        Form.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_title = QFrame(Form)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMaximumSize(QSize(16777215, 21))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_title)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 0, 2, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(125, 16))

        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(530, 13, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.btn_exit = QPushButton(self.frame_title)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 0))
        self.btn_exit.setMaximumSize(QSize(16, 16))
        icon = QIcon()
        icon.addFile(u":/icon/icons/reject.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_exit.setIcon(icon)

        self.gridLayout.addWidget(self.btn_exit, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frame_title, 0, 0, 1, 3)

        self.label_network1 = QLabel(Form)
        self.label_network1.setObjectName(u"label_network1")
        self.label_network1.setMaximumSize(QSize(130, 16))

        self.gridLayout_5.addWidget(self.label_network1, 1, 0, 1, 1)

        self.widget_1 = QWidget(Form)
        self.widget_1.setObjectName(u"widget_1")
        self.gridLayout_2 = QGridLayout(self.widget_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_13 = QLabel(self.widget_1)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.local_id = QLineEdit(self.widget_1)
        self.local_id.setObjectName(u"local_id")

        self.gridLayout_2.addWidget(self.local_id, 0, 1, 1, 1)

        self.label_11 = QLabel(self.widget_1)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 2, 1, 1)

        self.local_ip = QLineEdit(self.widget_1)
        self.local_ip.setObjectName(u"local_ip")

        self.gridLayout_2.addWidget(self.local_ip, 0, 3, 1, 1)

        self.label_10 = QLabel(self.widget_1)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 4, 1, 1)

        self.local_port = QLineEdit(self.widget_1)
        self.local_port.setObjectName(u"local_port")

        self.gridLayout_2.addWidget(self.local_port, 0, 5, 1, 1)

        self.label_15 = QLabel(self.widget_1)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)

        self.local_loginId = QLineEdit(self.widget_1)
        self.local_loginId.setObjectName(u"local_loginId")

        self.gridLayout_2.addWidget(self.local_loginId, 1, 1, 1, 1)

        self.label_14 = QLabel(self.widget_1)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 1, 2, 1, 1)

        self.local_swVer = QLineEdit(self.widget_1)
        self.local_swVer.setObjectName(u"local_swVer")

        self.gridLayout_2.addWidget(self.local_swVer, 1, 3, 1, 1)

        self.label_12 = QLabel(self.widget_1)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 1, 4, 1, 1)

        self.local_verDate = QLineEdit(self.widget_1)
        self.local_verDate.setObjectName(u"local_verDate")

        self.gridLayout_2.addWidget(self.local_verDate, 1, 5, 1, 1)


        self.gridLayout_5.addWidget(self.widget_1, 2, 0, 1, 3)

        self.label_network2 = QLabel(Form)
        self.label_network2.setObjectName(u"label_network2")
        self.label_network2.setMaximumSize(QSize(130, 16))

        self.gridLayout_5.addWidget(self.label_network2, 3, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.server_id = QLineEdit(self.widget_2)
        self.server_id.setObjectName(u"server_id")

        self.gridLayout_3.addWidget(self.server_id, 0, 1, 1, 1)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)

        self.server_ip = QLineEdit(self.widget_2)
        self.server_ip.setObjectName(u"server_ip")

        self.gridLayout_3.addWidget(self.server_ip, 0, 3, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 4, 1, 1)

        self.server_port = QLineEdit(self.widget_2)
        self.server_port.setObjectName(u"server_port")

        self.gridLayout_3.addWidget(self.server_port, 0, 5, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.server_loginId = QLineEdit(self.widget_2)
        self.server_loginId.setObjectName(u"server_loginId")

        self.gridLayout_3.addWidget(self.server_loginId, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 2, 1, 1)

        self.server_swVer = QLineEdit(self.widget_2)
        self.server_swVer.setObjectName(u"server_swVer")

        self.gridLayout_3.addWidget(self.server_swVer, 1, 3, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 4, 1, 1)

        self.server_verDate = QLineEdit(self.widget_2)
        self.server_verDate.setObjectName(u"server_verDate")

        self.gridLayout_3.addWidget(self.server_verDate, 1, 5, 1, 1)


        self.gridLayout_5.addWidget(self.widget_2, 4, 0, 1, 3)

        self.label_networkServer = QLabel(Form)
        self.label_networkServer.setObjectName(u"label_networkServer")
        self.label_networkServer.setMaximumSize(QSize(130, 16))

        self.gridLayout_5.addWidget(self.label_networkServer, 5, 0, 1, 1)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.localVer_edit = QLineEdit(self.widget_3)
        self.localVer_edit.setObjectName(u"localVer_edit")

        self.gridLayout_4.addWidget(self.localVer_edit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1)

        self.latestVer_edit = QLineEdit(self.widget_3)
        self.latestVer_edit.setObjectName(u"latestVer_edit")

        self.gridLayout_4.addWidget(self.latestVer_edit, 0, 3, 1, 1)

        self.upgradable_btn = QPushButton(self.widget_3)
        self.upgradable_btn.setObjectName(u"upgradable_btn")

        self.gridLayout_4.addWidget(self.upgradable_btn, 0, 4, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.pass_edit = QLineEdit(self.widget_3)
        self.pass_edit.setObjectName(u"pass_edit")

        self.gridLayout_4.addWidget(self.pass_edit, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_maxCon = QLabel(self.widget_3)
        self.label_maxCon.setObjectName(u"label_maxCon")

        self.horizontalLayout.addWidget(self.label_maxCon)

        self.usedAuto_radiobtn = QRadioButton(self.widget_3)
        self.usedAuto_radiobtn.setObjectName(u"usedAuto_radiobtn")

        self.horizontalLayout.addWidget(self.usedAuto_radiobtn)

        self.unusedAuto_radiobtn = QRadioButton(self.widget_3)
        self.unusedAuto_radiobtn.setObjectName(u"unusedAuto_radiobtn")

        self.horizontalLayout.addWidget(self.unusedAuto_radiobtn)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 2, 1, 2)

        self.run_upgrade_btn = QPushButton(self.widget_3)
        self.run_upgrade_btn.setObjectName(u"run_upgrade_btn")

        self.gridLayout_4.addWidget(self.run_upgrade_btn, 1, 4, 1, 1)


        self.gridLayout_5.addWidget(self.widget_3, 6, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(287, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 7, 0, 1, 1)

        self.btn_cancel = QPushButton(Form)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMaximumSize(QSize(50, 23))

        self.gridLayout_5.addWidget(self.btn_cancel, 7, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(286, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 7, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("Form", u"Network Settings", None))
        self.btn_exit.setText("")
        self.label_network1.setText(QCoreApplication.translate("Form", u"Local Information", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Local ID", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Local IP", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Local Port", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Login ID", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"S/W Ver.", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Ver. Date", None))
        self.label_network2.setText(QCoreApplication.translate("Form", u"Server Information", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Server ID", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Server IP", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Server Port", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Login ID", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"S/W Ver.", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Ver. Date", None))
        self.label_networkServer.setText(QCoreApplication.translate("Form", u"Remote Upgrade", None))
        self.label.setText(QCoreApplication.translate("Form", u"Local Version", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Latest Ver.", None))
        self.upgradable_btn.setText(QCoreApplication.translate("Form", u"Upgradable", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_maxCon.setText(QCoreApplication.translate("Form", u"Automatic Upgrade", None))
        self.usedAuto_radiobtn.setText(QCoreApplication.translate("Form", u"Used", None))
        self.unusedAuto_radiobtn.setText(QCoreApplication.translate("Form", u"Unused", None))
        self.run_upgrade_btn.setText(QCoreApplication.translate("Form", u"Run Upgrade", None))
        self.btn_cancel.setText(QCoreApplication.translate("Form", u"Close", None))
    # retranslateUi

