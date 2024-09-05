# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyboard.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 240)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.field_layout = QHBoxLayout()
        self.field_layout.setSpacing(10)
        self.field_layout.setObjectName(u"field_layout")
        self.horizontalSpacer_5 = QSpacerItem(142, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.field_layout.addItem(self.horizontalSpacer_5)

        self.edit_text = QLineEdit(Form)
        self.edit_text.setObjectName(u"edit_text")
        self.edit_text.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_text.sizePolicy().hasHeightForWidth())
        self.edit_text.setSizePolicy(sizePolicy)
        self.edit_text.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        self.edit_text.setFont(font)
        self.edit_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.edit_text.setAlignment(Qt.AlignCenter)

        self.field_layout.addWidget(self.edit_text)

        self.horizontalSpacer_6 = QSpacerItem(142, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.field_layout.addItem(self.horizontalSpacer_6)

        self.field_layout.setStretch(1, 60)

        self.verticalLayout.addLayout(self.field_layout)

        self.num_layout = QHBoxLayout()
        self.num_layout.setSpacing(10)
        self.num_layout.setObjectName(u"num_layout")
        self.horizontalSpacer_9 = QSpacerItem(5, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.num_layout.addItem(self.horizontalSpacer_9)

        self.btn_1 = QPushButton(Form)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setMinimumSize(QSize(70, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_1.setFont(font1)
        self.btn_1.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_1)

        self.btn_2 = QPushButton(Form)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setFont(font1)
        self.btn_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_2)

        self.btn_3 = QPushButton(Form)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setFont(font1)
        self.btn_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_3)

        self.btn_4 = QPushButton(Form)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setFont(font1)
        self.btn_4.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_4)

        self.btn_5 = QPushButton(Form)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setFont(font1)
        self.btn_5.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_5)

        self.btn_6 = QPushButton(Form)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setFont(font1)
        self.btn_6.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_6)

        self.btn_7 = QPushButton(Form)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setFont(font1)
        self.btn_7.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_7)

        self.btn_8 = QPushButton(Form)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setFont(font1)
        self.btn_8.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_8)

        self.btn_9 = QPushButton(Form)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setFont(font1)
        self.btn_9.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_9)

        self.btn_0 = QPushButton(Form)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setFont(font1)
        self.btn_0.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.num_layout.addWidget(self.btn_0)

        self.horizontalSpacer_10 = QSpacerItem(5, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.num_layout.addItem(self.horizontalSpacer_10)

        self.num_layout.setStretch(1, 10)
        self.num_layout.setStretch(2, 10)
        self.num_layout.setStretch(3, 10)
        self.num_layout.setStretch(4, 10)
        self.num_layout.setStretch(5, 10)
        self.num_layout.setStretch(6, 10)
        self.num_layout.setStretch(7, 10)
        self.num_layout.setStretch(8, 10)
        self.num_layout.setStretch(9, 10)
        self.num_layout.setStretch(10, 10)

        self.verticalLayout.addLayout(self.num_layout)

        self.alpha_layout_1 = QHBoxLayout()
        self.alpha_layout_1.setSpacing(10)
        self.alpha_layout_1.setObjectName(u"alpha_layout_1")
        self.btn_q = QPushButton(Form)
        self.btn_q.setObjectName(u"btn_q")
        sizePolicy1.setHeightForWidth(self.btn_q.sizePolicy().hasHeightForWidth())
        self.btn_q.setSizePolicy(sizePolicy1)
        self.btn_q.setMinimumSize(QSize(70, 30))
        self.btn_q.setFont(font1)
        self.btn_q.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_q)

        self.btn_w = QPushButton(Form)
        self.btn_w.setObjectName(u"btn_w")
        sizePolicy2.setHeightForWidth(self.btn_w.sizePolicy().hasHeightForWidth())
        self.btn_w.setSizePolicy(sizePolicy2)
        self.btn_w.setFont(font1)
        self.btn_w.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_w)

        self.btn_e = QPushButton(Form)
        self.btn_e.setObjectName(u"btn_e")
        sizePolicy2.setHeightForWidth(self.btn_e.sizePolicy().hasHeightForWidth())
        self.btn_e.setSizePolicy(sizePolicy2)
        self.btn_e.setFont(font1)
        self.btn_e.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_e)

        self.btn_r = QPushButton(Form)
        self.btn_r.setObjectName(u"btn_r")
        sizePolicy2.setHeightForWidth(self.btn_r.sizePolicy().hasHeightForWidth())
        self.btn_r.setSizePolicy(sizePolicy2)
        self.btn_r.setFont(font1)
        self.btn_r.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_r)

        self.btn_t = QPushButton(Form)
        self.btn_t.setObjectName(u"btn_t")
        sizePolicy2.setHeightForWidth(self.btn_t.sizePolicy().hasHeightForWidth())
        self.btn_t.setSizePolicy(sizePolicy2)
        self.btn_t.setFont(font1)
        self.btn_t.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_t)

        self.btn_y = QPushButton(Form)
        self.btn_y.setObjectName(u"btn_y")
        sizePolicy2.setHeightForWidth(self.btn_y.sizePolicy().hasHeightForWidth())
        self.btn_y.setSizePolicy(sizePolicy2)
        self.btn_y.setFont(font1)
        self.btn_y.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_y)

        self.btn_u = QPushButton(Form)
        self.btn_u.setObjectName(u"btn_u")
        sizePolicy2.setHeightForWidth(self.btn_u.sizePolicy().hasHeightForWidth())
        self.btn_u.setSizePolicy(sizePolicy2)
        self.btn_u.setFont(font1)
        self.btn_u.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_u)

        self.btn_i = QPushButton(Form)
        self.btn_i.setObjectName(u"btn_i")
        sizePolicy2.setHeightForWidth(self.btn_i.sizePolicy().hasHeightForWidth())
        self.btn_i.setSizePolicy(sizePolicy2)
        self.btn_i.setFont(font1)
        self.btn_i.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_i)

        self.btn_o = QPushButton(Form)
        self.btn_o.setObjectName(u"btn_o")
        sizePolicy2.setHeightForWidth(self.btn_o.sizePolicy().hasHeightForWidth())
        self.btn_o.setSizePolicy(sizePolicy2)
        self.btn_o.setFont(font1)
        self.btn_o.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_o)

        self.btn_p = QPushButton(Form)
        self.btn_p.setObjectName(u"btn_p")
        sizePolicy2.setHeightForWidth(self.btn_p.sizePolicy().hasHeightForWidth())
        self.btn_p.setSizePolicy(sizePolicy2)
        self.btn_p.setFont(font1)
        self.btn_p.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_1.addWidget(self.btn_p)

        self.alpha_layout_1.setStretch(0, 10)
        self.alpha_layout_1.setStretch(1, 10)
        self.alpha_layout_1.setStretch(2, 10)
        self.alpha_layout_1.setStretch(3, 10)
        self.alpha_layout_1.setStretch(4, 10)
        self.alpha_layout_1.setStretch(5, 10)
        self.alpha_layout_1.setStretch(6, 10)
        self.alpha_layout_1.setStretch(7, 10)
        self.alpha_layout_1.setStretch(8, 10)
        self.alpha_layout_1.setStretch(9, 10)

        self.verticalLayout.addLayout(self.alpha_layout_1)

        self.alpha_layout_2 = QHBoxLayout()
        self.alpha_layout_2.setSpacing(10)
        self.alpha_layout_2.setObjectName(u"alpha_layout_2")
        self.horizontalSpacer = QSpacerItem(30, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.alpha_layout_2.addItem(self.horizontalSpacer)

        self.btn_a = QPushButton(Form)
        self.btn_a.setObjectName(u"btn_a")
        sizePolicy1.setHeightForWidth(self.btn_a.sizePolicy().hasHeightForWidth())
        self.btn_a.setSizePolicy(sizePolicy1)
        self.btn_a.setMinimumSize(QSize(70, 30))
        self.btn_a.setFont(font1)
        self.btn_a.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_2.addWidget(self.btn_a)

        self.btn_s = QPushButton(Form)
        self.btn_s.setObjectName(u"btn_s")
        sizePolicy2.setHeightForWidth(self.btn_s.sizePolicy().hasHeightForWidth())
        self.btn_s.setSizePolicy(sizePolicy2)
        self.btn_s.setFont(font1)
        self.btn_s.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_2.addWidget(self.btn_s)

        self.btn_d = QPushButton(Form)
        self.btn_d.setObjectName(u"btn_d")
        sizePolicy2.setHeightForWidth(self.btn_d.sizePolicy().hasHeightForWidth())
        self.btn_d.setSizePolicy(sizePolicy2)
        self.btn_d.setFont(font1)
        self.btn_d.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_2.addWidget(self.btn_d)

        self.btn_f = QPushButton(Form)
        self.btn_f.setObjectName(u"btn_f")
        sizePolicy2.setHeightForWidth(self.btn_f.sizePolicy().hasHeightForWidth())
        self.btn_f.setSizePolicy(sizePolicy2)
        self.btn_f.setFont(font1)
        self.btn_f.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_2.addWidget(self.btn_f)

        self.btn_g = QPushButton(Form)
        self.btn_g.setObjectName(u"btn_g")
        sizePolicy2.setHeightForWidth(self.btn_g.sizePolicy().hasHeightForWidth())
        self.btn_g.setSizePolicy(sizePolicy2)
        self.btn_g.setFont(font1)
        self.btn_g.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_2.addWidget(self.btn_g)

        self.btn_h = QPushButton(Form)
        self.btn_h.setObjectName(u"btn_h")
        sizePolicy2.setHeightForWidth(self.btn_h.sizePolicy().hasHeightForWidth())
        self.btn_h.setSizePolicy(sizePolicy2)
        self.btn_h.setFont(font1)
        self.btn_h.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_2.addWidget(self.btn_h)

        self.btn_j = QPushButton(Form)
        self.btn_j.setObjectName(u"btn_j")
        sizePolicy2.setHeightForWidth(self.btn_j.sizePolicy().hasHeightForWidth())
        self.btn_j.setSizePolicy(sizePolicy2)
        self.btn_j.setFont(font1)
        self.btn_j.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_2.addWidget(self.btn_j)

        self.btn_k = QPushButton(Form)
        self.btn_k.setObjectName(u"btn_k")
        sizePolicy2.setHeightForWidth(self.btn_k.sizePolicy().hasHeightForWidth())
        self.btn_k.setSizePolicy(sizePolicy2)
        self.btn_k.setFont(font1)
        self.btn_k.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_2.addWidget(self.btn_k)

        self.btn_l = QPushButton(Form)
        self.btn_l.setObjectName(u"btn_l")
        sizePolicy2.setHeightForWidth(self.btn_l.sizePolicy().hasHeightForWidth())
        self.btn_l.setSizePolicy(sizePolicy2)
        self.btn_l.setFont(font1)
        self.btn_l.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_2.addWidget(self.btn_l)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.alpha_layout_2.addItem(self.horizontalSpacer_2)

        self.alpha_layout_2.setStretch(1, 10)
        self.alpha_layout_2.setStretch(2, 10)
        self.alpha_layout_2.setStretch(3, 10)
        self.alpha_layout_2.setStretch(4, 10)
        self.alpha_layout_2.setStretch(5, 10)
        self.alpha_layout_2.setStretch(6, 10)
        self.alpha_layout_2.setStretch(7, 10)
        self.alpha_layout_2.setStretch(8, 10)
        self.alpha_layout_2.setStretch(9, 10)

        self.verticalLayout.addLayout(self.alpha_layout_2)

        self.alpha_layout_3 = QHBoxLayout()
        self.alpha_layout_3.setSpacing(10)
        self.alpha_layout_3.setObjectName(u"alpha_layout_3")
        self.horizontalSpacer_3 = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.alpha_layout_3.addItem(self.horizontalSpacer_3)

        self.btn_z = QPushButton(Form)
        self.btn_z.setObjectName(u"btn_z")
        sizePolicy1.setHeightForWidth(self.btn_z.sizePolicy().hasHeightForWidth())
        self.btn_z.setSizePolicy(sizePolicy1)
        self.btn_z.setMinimumSize(QSize(70, 30))
        self.btn_z.setFont(font1)
        self.btn_z.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_3.addWidget(self.btn_z)

        self.btn_x = QPushButton(Form)
        self.btn_x.setObjectName(u"btn_x")
        sizePolicy2.setHeightForWidth(self.btn_x.sizePolicy().hasHeightForWidth())
        self.btn_x.setSizePolicy(sizePolicy2)
        self.btn_x.setFont(font1)
        self.btn_x.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_3.addWidget(self.btn_x)

        self.btn_c = QPushButton(Form)
        self.btn_c.setObjectName(u"btn_c")
        sizePolicy2.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy2)
        self.btn_c.setFont(font1)
        self.btn_c.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_3.addWidget(self.btn_c)

        self.btn_v = QPushButton(Form)
        self.btn_v.setObjectName(u"btn_v")
        sizePolicy2.setHeightForWidth(self.btn_v.sizePolicy().hasHeightForWidth())
        self.btn_v.setSizePolicy(sizePolicy2)
        self.btn_v.setFont(font1)
        self.btn_v.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_3.addWidget(self.btn_v)

        self.btn_b = QPushButton(Form)
        self.btn_b.setObjectName(u"btn_b")
        sizePolicy2.setHeightForWidth(self.btn_b.sizePolicy().hasHeightForWidth())
        self.btn_b.setSizePolicy(sizePolicy2)
        self.btn_b.setFont(font1)
        self.btn_b.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_3.addWidget(self.btn_b)

        self.btn_n = QPushButton(Form)
        self.btn_n.setObjectName(u"btn_n")
        sizePolicy2.setHeightForWidth(self.btn_n.sizePolicy().hasHeightForWidth())
        self.btn_n.setSizePolicy(sizePolicy2)
        self.btn_n.setFont(font1)
        self.btn_n.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_3.addWidget(self.btn_n)

        self.btn_m = QPushButton(Form)
        self.btn_m.setObjectName(u"btn_m")
        sizePolicy2.setHeightForWidth(self.btn_m.sizePolicy().hasHeightForWidth())
        self.btn_m.setSizePolicy(sizePolicy2)
        self.btn_m.setFont(font1)
        self.btn_m.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.alpha_layout_3.addWidget(self.btn_m)

        self.horizontalSpacer_4 = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.alpha_layout_3.addItem(self.horizontalSpacer_4)

        self.alpha_layout_3.setStretch(1, 10)
        self.alpha_layout_3.setStretch(2, 10)
        self.alpha_layout_3.setStretch(3, 10)
        self.alpha_layout_3.setStretch(4, 10)
        self.alpha_layout_3.setStretch(5, 10)
        self.alpha_layout_3.setStretch(6, 10)
        self.alpha_layout_3.setStretch(7, 10)

        self.verticalLayout.addLayout(self.alpha_layout_3)

        self.char_layout = QHBoxLayout()
        self.char_layout.setSpacing(10)
        self.char_layout.setObjectName(u"char_layout")
        self.btn_upper = QPushButton(Form)
        self.btn_upper.setObjectName(u"btn_upper")
        sizePolicy1.setHeightForWidth(self.btn_upper.sizePolicy().hasHeightForWidth())
        self.btn_upper.setSizePolicy(sizePolicy1)
        self.btn_upper.setMinimumSize(QSize(70, 30))
        self.btn_upper.setFont(font1)
        self.btn_upper.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.char_layout.addWidget(self.btn_upper)

        self.btn_underscore = QPushButton(Form)
        self.btn_underscore.setObjectName(u"btn_underscore")
        sizePolicy1.setHeightForWidth(self.btn_underscore.sizePolicy().hasHeightForWidth())
        self.btn_underscore.setSizePolicy(sizePolicy1)
        self.btn_underscore.setMinimumSize(QSize(70, 30))
        self.btn_underscore.setFont(font1)
        self.btn_underscore.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.char_layout.addWidget(self.btn_underscore)

        self.btn_at = QPushButton(Form)
        self.btn_at.setObjectName(u"btn_at")
        sizePolicy1.setHeightForWidth(self.btn_at.sizePolicy().hasHeightForWidth())
        self.btn_at.setSizePolicy(sizePolicy1)
        self.btn_at.setMinimumSize(QSize(70, 30))
        self.btn_at.setFont(font1)
        self.btn_at.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.char_layout.addWidget(self.btn_at)

        self.btn_space = QPushButton(Form)
        self.btn_space.setObjectName(u"btn_space")
        sizePolicy1.setHeightForWidth(self.btn_space.sizePolicy().hasHeightForWidth())
        self.btn_space.setSizePolicy(sizePolicy1)
        self.btn_space.setMinimumSize(QSize(250, 30))
        self.btn_space.setFont(font1)
        self.btn_space.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.char_layout.addWidget(self.btn_space)

        self.btn_period = QPushButton(Form)
        self.btn_period.setObjectName(u"btn_period")
        sizePolicy1.setHeightForWidth(self.btn_period.sizePolicy().hasHeightForWidth())
        self.btn_period.setSizePolicy(sizePolicy1)
        self.btn_period.setMinimumSize(QSize(70, 30))
        self.btn_period.setFont(font1)
        self.btn_period.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.char_layout.addWidget(self.btn_period)

        self.btn_backspace = QPushButton(Form)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy2)
        self.btn_backspace.setMinimumSize(QSize(70, 30))
        self.btn_backspace.setFont(font1)
        self.btn_backspace.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.char_layout.addWidget(self.btn_backspace)

        self.btn_ok = QPushButton(Form)
        self.btn_ok.setObjectName(u"btn_ok")
        sizePolicy2.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy2)
        self.btn_ok.setMinimumSize(QSize(70, 30))
        self.btn_ok.setFont(font1)
        self.btn_ok.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{	\n"
"	background-color: rgb(140, 223, 255);\n"
" }")

        self.char_layout.addWidget(self.btn_ok)

        self.char_layout.setStretch(0, 10)
        self.char_layout.setStretch(1, 10)
        self.char_layout.setStretch(2, 10)
        self.char_layout.setStretch(3, 40)
        self.char_layout.setStretch(4, 10)
        self.char_layout.setStretch(5, 10)
        self.char_layout.setStretch(6, 10)

        self.verticalLayout.addLayout(self.char_layout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_q.setText(QCoreApplication.translate("Form", u"q", None))
        self.btn_w.setText(QCoreApplication.translate("Form", u"w", None))
        self.btn_e.setText(QCoreApplication.translate("Form", u"e", None))
        self.btn_r.setText(QCoreApplication.translate("Form", u"r", None))
        self.btn_t.setText(QCoreApplication.translate("Form", u"t", None))
        self.btn_y.setText(QCoreApplication.translate("Form", u"y", None))
        self.btn_u.setText(QCoreApplication.translate("Form", u"u", None))
        self.btn_i.setText(QCoreApplication.translate("Form", u"i", None))
        self.btn_o.setText(QCoreApplication.translate("Form", u"o", None))
        self.btn_p.setText(QCoreApplication.translate("Form", u"p", None))
        self.btn_a.setText(QCoreApplication.translate("Form", u"a", None))
        self.btn_s.setText(QCoreApplication.translate("Form", u"s", None))
        self.btn_d.setText(QCoreApplication.translate("Form", u"d", None))
        self.btn_f.setText(QCoreApplication.translate("Form", u"f", None))
        self.btn_g.setText(QCoreApplication.translate("Form", u"g", None))
        self.btn_h.setText(QCoreApplication.translate("Form", u"h", None))
        self.btn_j.setText(QCoreApplication.translate("Form", u"j", None))
        self.btn_k.setText(QCoreApplication.translate("Form", u"k", None))
        self.btn_l.setText(QCoreApplication.translate("Form", u"l", None))
        self.btn_z.setText(QCoreApplication.translate("Form", u"z", None))
        self.btn_x.setText(QCoreApplication.translate("Form", u"x", None))
        self.btn_c.setText(QCoreApplication.translate("Form", u"c", None))
        self.btn_v.setText(QCoreApplication.translate("Form", u"v", None))
        self.btn_b.setText(QCoreApplication.translate("Form", u"b", None))
        self.btn_n.setText(QCoreApplication.translate("Form", u"n", None))
        self.btn_m.setText(QCoreApplication.translate("Form", u"m", None))
        self.btn_upper.setText(QCoreApplication.translate("Form", u"\u2191", None))
        self.btn_underscore.setText(QCoreApplication.translate("Form", u"_", None))
        self.btn_at.setText(QCoreApplication.translate("Form", u"@", None))
        self.btn_space.setText("")
        self.btn_period.setText(QCoreApplication.translate("Form", u".", None))
        self.btn_backspace.setText(QCoreApplication.translate("Form", u"\u2190", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

