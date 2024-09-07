# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_pw_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 257)
        self.gridLayout_4 = QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setMaximumSize(QSize(16777215, 61))
        self.textEdit.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 3)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16, 16))
        self.label.setPixmap(QPixmap(u":/icon/icons/padlock.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(19999, 50))

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(197, 11, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/icon/icons/reject.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 3)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.existPass_edit = QLineEdit(self.frame_2)
        self.existPass_edit.setObjectName(u"existPass_edit")
        self.existPass_edit.setMinimumSize(QSize(150, 0))
        self.existPass_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.existPass_edit, 0, 1, 1, 2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.verifyPass_edit = QLineEdit(self.frame_2)
        self.verifyPass_edit.setObjectName(u"verifyPass_edit")
        self.verifyPass_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.verifyPass_edit, 2, 1, 1, 2)

        self.btn_checkPass = QPushButton(self.frame_2)
        self.btn_checkPass.setObjectName(u"btn_checkPass")
        self.btn_checkPass.setEnabled(True)
        self.btn_checkPass.setAutoDefault(False)
        self.btn_checkPass.setFlat(False)

        self.gridLayout_2.addWidget(self.btn_checkPass, 0, 5, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, 0, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_cancel = QPushButton(self.frame_4)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setEnabled(True)
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_confirm = QPushButton(self.frame_4)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setEnabled(True)
        self.btn_confirm.setAutoDefault(False)
        self.btn_confirm.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_confirm)


        self.gridLayout_2.addWidget(self.frame_4, 3, 0, 1, 3)

        self.newPass_edit = QLineEdit(self.frame_2)
        self.newPass_edit.setObjectName(u"newPass_edit")
        self.newPass_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.newPass_edit, 1, 1, 1, 2)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)


        self.retranslateUi(Dialog)

        self.btn_checkPass.setDefault(False)
        self.btn_cancel.setDefault(False)
        self.btn_confirm.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-style:italic;\">The minimum password length is 8 characters and must contain</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-style:italic;\">a combination of at least two of English letters, numbers, and</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-style:italic;\">special characters</span></p></body></html>", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Change Password", None))
        self.pushButton_4.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Verify Password", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"New Password", None))
        self.btn_checkPass.setText(QCoreApplication.translate("Dialog", u"Check", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_confirm.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Existing Password", None))
    # retranslateUi

