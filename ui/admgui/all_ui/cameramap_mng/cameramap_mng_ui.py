# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameramap_mng.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolButton, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(833, 373)
        Form.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(Form)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setContentsMargins(9, 0, 9, 6)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 21))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(434, 16, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16, 16))
        icon = QIcon()
        icon.addFile(u":/icon/icons/reject.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_10 = QPushButton(self.frame_6)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_12 = QPushButton(self.frame_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_6)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_13)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.gridLayout_2.addWidget(self.frame_6, 1, 1, 1, 1)

        self.tb_show = QTableWidget(self.frame_2)
        if (self.tb_show.columnCount() < 6):
            self.tb_show.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
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
        self.tb_show.setObjectName(u"tb_show")
        self.tb_show.setFocusPolicy(Qt.NoFocus)
        self.tb_show.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_show.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tb_show, 0, 0, 1, 3)


        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(9, 9, 9, 6)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.fileName_edit = QLineEdit(self.frame_4)
        self.fileName_edit.setObjectName(u"fileName_edit")

        self.gridLayout_3.addWidget(self.fileName_edit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)

        self.mapDescript_edit = QTextEdit(self.frame_4)
        self.mapDescript_edit.setObjectName(u"mapDescript_edit")
        self.mapDescript_edit.setEnabled(True)
        self.mapDescript_edit.setMinimumSize(QSize(111, 64))

        self.gridLayout_3.addWidget(self.mapDescript_edit, 0, 3, 2, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mapRegist_edit = QLineEdit(self.frame_4)
        self.mapRegist_edit.setObjectName(u"mapRegist_edit")

        self.horizontalLayout_2.addWidget(self.mapRegist_edit)

        self.findFile_btn = QToolButton(self.frame_4)
        self.findFile_btn.setObjectName(u"findFile_btn")
        self.findFile_btn.setPopupMode(QToolButton.InstantPopup)
        self.findFile_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_2.addWidget(self.findFile_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(54, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.new_map_btn = QPushButton(self.frame_3)
        self.new_map_btn.setObjectName(u"new_map_btn")
        self.new_map_btn.setMaximumSize(QSize(71, 23))

        self.gridLayout_4.addWidget(self.new_map_btn, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(71, 23))

        self.gridLayout_4.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.del_map_btn = QPushButton(self.frame_3)
        self.del_map_btn.setObjectName(u"del_map_btn")
        self.del_map_btn.setMaximumSize(QSize(71, 23))

        self.gridLayout_4.addWidget(self.del_map_btn, 0, 2, 1, 1)

        self.add_map_btn = QPushButton(self.frame_3)
        self.add_map_btn.setObjectName(u"add_map_btn")
        self.add_map_btn.setMaximumSize(QSize(71, 23))

        self.gridLayout_4.addWidget(self.add_map_btn, 0, 3, 1, 1)

        self.change_map_btn = QPushButton(self.frame_3)
        self.change_map_btn.setObjectName(u"change_map_btn")
        self.change_map_btn.setMaximumSize(QSize(999, 23))

        self.gridLayout_4.addWidget(self.change_map_btn, 0, 4, 1, 1)

        self.close_btn = QPushButton(self.frame_3)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(71, 23))

        self.gridLayout_4.addWidget(self.close_btn, 0, 5, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(54, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.frame_4.raise_()

        self.gridLayout_6.addWidget(self.frame_3, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Camera Map Management", None))
        self.pushButton.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"<<", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u">>", None))
        ___qtablewidgetitem = self.tb_show.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"No.", None));
        ___qtablewidgetitem1 = self.tb_show.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Map Name", None));
        ___qtablewidgetitem2 = self.tb_show.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"File Map Name", None));
        ___qtablewidgetitem3 = self.tb_show.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"View Map", None));
        ___qtablewidgetitem4 = self.tb_show.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Registration Date", None));
        ___qtablewidgetitem5 = self.tb_show.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Map Description", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"Map File Name", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Map Description", None))
        self.mapDescript_edit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Map Registration", None))
        self.findFile_btn.setText(QCoreApplication.translate("Form", u"Find File", None))
        self.new_map_btn.setText(QCoreApplication.translate("Form", u"New", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.del_map_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.add_map_btn.setText(QCoreApplication.translate("Form", u"Add Map", None))
        self.change_map_btn.setText(QCoreApplication.translate("Form", u"Change Map", None))
        self.close_btn.setText(QCoreApplication.translate("Form", u"Close", None))
    # retranslateUi

