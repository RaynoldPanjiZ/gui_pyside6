# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_management.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(768, 461)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.frame_title = QFrame(Form)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setMinimumSize(QSize(0, 30))
        self.frame_title.setMaximumSize(QSize(16777215, 40))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 0, 2, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(125, 16))
        self.label_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_title)

        self.horizontalSpacer_2 = QSpacerItem(534, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_exit = QPushButton(self.frame_title)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 0))
        self.btn_exit.setMaximumSize(QSize(16, 16))
        icon = QIcon()
        icon.addFile(u":/icon/icons/reject.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_exit.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_exit)


        self.verticalLayout.addWidget(self.frame_title)

        self.widget_1 = QFrame(Form)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setFrameShape(QFrame.NoFrame)
        self.widget_1.setFrameShadow(QFrame.Raised)
        self.widget_1.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.widget_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tb_show = QTableWidget(self.widget_1)
        if (self.tb_show.columnCount() < 9):
            self.tb_show.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tb_show.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_show.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_show.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_show.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_show.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_show.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_show.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_show.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_show.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tb_show.setObjectName(u"tb_show")
        self.tb_show.setFocusPolicy(Qt.NoFocus)
        self.tb_show.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tb_show.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.tb_show.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_show.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_show.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tb_show)

        self.frame_6 = QFrame(self.widget_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_12 = QPushButton(self.frame_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_6)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_13)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.widget_1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer_5 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.id_edit = QLineEdit(self.frame_4)
        self.id_edit.setObjectName(u"id_edit")

        self.gridLayout_4.addWidget(self.id_edit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 2, 1, 1)

        self.name_edit = QLineEdit(self.frame_4)
        self.name_edit.setObjectName(u"name_edit")

        self.gridLayout_4.addWidget(self.name_edit, 0, 3, 1, 1)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 4, 1, 1)

        self.usrGroup_comboBox = QComboBox(self.frame_4)
        self.usrGroup_comboBox.setObjectName(u"usrGroup_comboBox")

        self.gridLayout_4.addWidget(self.usrGroup_comboBox, 0, 5, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.pass_edit = QLineEdit(self.frame_4)
        self.pass_edit.setObjectName(u"pass_edit")

        self.gridLayout_4.addWidget(self.pass_edit, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 2, 1, 1)

        self.contact_edit = QLineEdit(self.frame_4)
        self.contact_edit.setObjectName(u"contact_edit")

        self.gridLayout_4.addWidget(self.contact_edit, 1, 3, 1, 1)

        self.msg_checkbox = QCheckBox(self.frame_4)
        self.msg_checkbox.setObjectName(u"msg_checkbox")
        self.msg_checkbox.setLayoutDirection(Qt.RightToLeft)
        self.msg_checkbox.setAutoExclusive(False)
        self.msg_checkbox.setAutoRepeatDelay(0)

        self.gridLayout_4.addWidget(self.msg_checkbox, 1, 4, 1, 2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.verifyPass_edit = QLineEdit(self.frame_4)
        self.verifyPass_edit.setObjectName(u"verifyPass_edit")

        self.gridLayout_4.addWidget(self.verifyPass_edit, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 2, 2, 1, 1)

        self.email_edit = QLineEdit(self.frame_4)
        self.email_edit.setObjectName(u"email_edit")

        self.gridLayout_4.addWidget(self.email_edit, 2, 3, 1, 1)

        self.img_checkBox = QCheckBox(self.frame_4)
        self.img_checkBox.setObjectName(u"img_checkBox")
        self.img_checkBox.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_4.addWidget(self.img_checkBox, 2, 4, 1, 2)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 3)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 26))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.new_btn = QPushButton(self.frame_3)
        self.new_btn.setObjectName(u"new_btn")
        self.new_btn.setMaximumSize(QSize(70, 35))

        self.gridLayout_3.addWidget(self.new_btn, 0, 0, 1, 1)

        self.chpasswd_btn = QPushButton(self.frame_3)
        self.chpasswd_btn.setObjectName(u"chpasswd_btn")
        self.chpasswd_btn.setMinimumSize(QSize(96, 0))
        self.chpasswd_btn.setMaximumSize(QSize(116, 35))

        self.gridLayout_3.addWidget(self.chpasswd_btn, 0, 2, 1, 1)

        self.edit_btn = QPushButton(self.frame_3)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMaximumSize(QSize(70, 35))

        self.gridLayout_3.addWidget(self.edit_btn, 0, 1, 1, 1)

        self.close_btn = QPushButton(self.frame_3)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(70, 35))

        self.gridLayout_3.addWidget(self.close_btn, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(121, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 55, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("Form", u" User Management", None))
        self.btn_exit.setText(QCoreApplication.translate("Form", u"X", None))
        ___qtablewidgetitem = self.tb_show.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"No.", None));
        ___qtablewidgetitem1 = self.tb_show.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem2 = self.tb_show.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem3 = self.tb_show.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"User Group", None));
        ___qtablewidgetitem4 = self.tb_show.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Contact", None));
        ___qtablewidgetitem5 = self.tb_show.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Email", None));
        ___qtablewidgetitem6 = self.tb_show.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Message", None));
        ___qtablewidgetitem7 = self.tb_show.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Image", None));
        ___qtablewidgetitem8 = self.tb_show.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Delete", None));
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"<<", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u">>", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"User Group", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Contact", None))
        self.msg_checkbox.setText(QCoreApplication.translate("Form", u"Send Event Text Message", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Verify Password", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Email", None))
        self.img_checkBox.setText(QCoreApplication.translate("Form", u"Event Image Transmission", None))
        self.new_btn.setText(QCoreApplication.translate("Form", u"New", None))
        self.chpasswd_btn.setText(QCoreApplication.translate("Form", u"Change Password", None))
        self.edit_btn.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.close_btn.setText(QCoreApplication.translate("Form", u"Close", None))
    # retranslateUi

