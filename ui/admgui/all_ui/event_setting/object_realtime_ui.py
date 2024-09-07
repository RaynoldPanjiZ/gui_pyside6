# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'object_realtime.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSplitter, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(678, 347)
        Form.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 6)
        self.horizontalSpacer_3 = QSpacerItem(150, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(150, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 3, 3, 1, 1)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 0, 9, -1)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QSize(16777215, 150))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 9, -1, 9)
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_9.addWidget(self.label_8)

        self.splitter_4 = QSplitter(self.frame_7)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.noVehicle = QLineEdit(self.splitter_4)
        self.noVehicle.setObjectName(u"noVehicle")
        self.noVehicle.setMaximumSize(QSize(16777215, 18))
        self.splitter_4.addWidget(self.noVehicle)
        self.splitter_2 = QSplitter(self.splitter_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.vehicle_select_btn = QPushButton(self.splitter_2)
        self.vehicle_select_btn.setObjectName(u"vehicle_select_btn")
        self.vehicle_select_btn.setMaximumSize(QSize(50, 23))
        self.splitter_2.addWidget(self.vehicle_select_btn)
        self.vehicle_newReg_btn = QPushButton(self.splitter_2)
        self.vehicle_newReg_btn.setObjectName(u"vehicle_newReg_btn")
        self.vehicle_newReg_btn.setMaximumSize(QSize(16777215, 23))
        self.splitter_2.addWidget(self.vehicle_newReg_btn)
        self.splitter_4.addWidget(self.splitter_2)

        self.horizontalLayout_9.addWidget(self.splitter_4)


        self.gridLayout.addWidget(self.frame_7, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_12.addWidget(self.label_11)

        self.model_comboBox = QComboBox(self.frame_10)
        self.model_comboBox.addItem("")
        self.model_comboBox.setObjectName(u"model_comboBox")

        self.horizontalLayout_12.addWidget(self.model_comboBox)


        self.gridLayout.addWidget(self.frame_10, 4, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_13.addWidget(self.label_12)

        self.color_comboBox = QComboBox(self.frame_11)
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.setObjectName(u"color_comboBox")

        self.horizontalLayout_13.addWidget(self.color_comboBox)


        self.gridLayout.addWidget(self.frame_11, 5, 0, 1, 1)

        self.vehicle_radiobtn = QRadioButton(self.frame_3)
        self.groupbtnForm = QButtonGroup(Form)
        self.groupbtnForm.setObjectName(u"groupbtnForm")
        self.groupbtnForm.addButton(self.vehicle_radiobtn)
        self.vehicle_radiobtn.setObjectName(u"vehicle_radiobtn")
        self.vehicle_radiobtn.setAutoExclusive(False)

        self.gridLayout.addWidget(self.vehicle_radiobtn, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_11.addWidget(self.label_10)

        self.brand_comboBox = QComboBox(self.frame_9)
        self.brand_comboBox.addItem("")
        self.brand_comboBox.addItem("")
        self.brand_comboBox.addItem("")
        self.brand_comboBox.setObjectName(u"brand_comboBox")

        self.horizontalLayout_11.addWidget(self.brand_comboBox)


        self.gridLayout.addWidget(self.frame_9, 3, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_10.addWidget(self.label_9)

        self.car_comboBox = QComboBox(self.frame_8)
        self.car_comboBox.addItem("")
        self.car_comboBox.setObjectName(u"car_comboBox")

        self.horizontalLayout_10.addWidget(self.car_comboBox)


        self.gridLayout.addWidget(self.frame_8, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 1, 2, 1, 2)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 6, 0)
        self.person_radiobtn = QRadioButton(self.frame_2)
        self.groupbtnForm.addButton(self.person_radiobtn)
        self.person_radiobtn.setObjectName(u"person_radiobtn")
        self.person_radiobtn.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.person_radiobtn)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(16777215, 150))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.splitter_3 = QSplitter(self.frame_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.personName = QLineEdit(self.splitter_3)
        self.personName.setObjectName(u"personName")
        self.personName.setMaximumSize(QSize(16777215, 18))
        self.splitter_3.addWidget(self.personName)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.person_select_btn = QPushButton(self.splitter)
        self.person_select_btn.setObjectName(u"person_select_btn")
        self.person_select_btn.setMaximumSize(QSize(50, 23))
        self.splitter.addWidget(self.person_select_btn)
        self.person_newReg_btn = QPushButton(self.splitter)
        self.person_newReg_btn.setObjectName(u"person_newReg_btn")
        self.person_newReg_btn.setMaximumSize(QSize(16777215, 23))
        self.splitter.addWidget(self.person_newReg_btn)
        self.splitter_3.addWidget(self.splitter)

        self.horizontalLayout_3.addWidget(self.splitter_3)

        self.label_foto = QLabel(self.frame_4)
        self.label_foto.setObjectName(u"label_foto")
        self.label_foto.setMinimumSize(QSize(61, 71))
        self.label_foto.setFrameShape(QFrame.Box)
        self.label_foto.setLineWidth(1)
        self.label_foto.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_foto)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 3)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.gender_radioGroup = QHBoxLayout()
        self.gender_radioGroup.setObjectName(u"gender_radioGroup")
        self.Gmale_radiobtn = QRadioButton(self.frame_5)
        self.genderbtngroup = QButtonGroup(Form)
        self.genderbtngroup.setObjectName(u"genderbtngroup")
        self.genderbtngroup.addButton(self.Gmale_radiobtn)
        self.Gmale_radiobtn.setObjectName(u"Gmale_radiobtn")
        self.Gmale_radiobtn.setCheckable(True)
        self.Gmale_radiobtn.setChecked(False)
        self.Gmale_radiobtn.setAutoRepeat(False)
        self.Gmale_radiobtn.setAutoExclusive(False)

        self.gender_radioGroup.addWidget(self.Gmale_radiobtn)

        self.Gfemale_radiobtn = QRadioButton(self.frame_5)
        self.genderbtngroup.addButton(self.Gfemale_radiobtn)
        self.Gfemale_radiobtn.setObjectName(u"Gfemale_radiobtn")
        self.Gfemale_radiobtn.setAutoExclusive(False)

        self.gender_radioGroup.addWidget(self.Gfemale_radiobtn)


        self.horizontalLayout_7.addLayout(self.gender_radioGroup)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 3, -1, 9)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_8.addWidget(self.label_6)

        self.hairstyle_radioGroup = QHBoxLayout()
        self.hairstyle_radioGroup.setObjectName(u"hairstyle_radioGroup")
        self.Hlong_radiobtn = QRadioButton(self.frame_6)
        self.hairbtngroup = QButtonGroup(Form)
        self.hairbtngroup.setObjectName(u"hairbtngroup")
        self.hairbtngroup.addButton(self.Hlong_radiobtn)
        self.Hlong_radiobtn.setObjectName(u"Hlong_radiobtn")
        self.Hlong_radiobtn.setCheckable(True)
        self.Hlong_radiobtn.setChecked(False)
        self.Hlong_radiobtn.setAutoExclusive(False)

        self.hairstyle_radioGroup.addWidget(self.Hlong_radiobtn)

        self.Hshort_radiobtn = QRadioButton(self.frame_6)
        self.hairbtngroup.addButton(self.Hshort_radiobtn)
        self.Hshort_radiobtn.setObjectName(u"Hshort_radiobtn")
        self.Hshort_radiobtn.setAutoExclusive(False)

        self.hairstyle_radioGroup.addWidget(self.Hshort_radiobtn)


        self.horizontalLayout_8.addLayout(self.hairstyle_radioGroup)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.frame_6)

        self.attr_checkboxGroup = QHBoxLayout()
        self.attr_checkboxGroup.setObjectName(u"attr_checkboxGroup")
        self.attrHat_chbx = QCheckBox(self.frame_2)
        self.attrHat_chbx.setObjectName(u"attrHat_chbx")

        self.attr_checkboxGroup.addWidget(self.attrHat_chbx)

        self.attrBag_chbx = QCheckBox(self.frame_2)
        self.attrBag_chbx.setObjectName(u"attrBag_chbx")

        self.attr_checkboxGroup.addWidget(self.attrBag_chbx)

        self.attrMask_chbx = QCheckBox(self.frame_2)
        self.attrMask_chbx.setObjectName(u"attrMask_chbx")

        self.attr_checkboxGroup.addWidget(self.attrMask_chbx)

        self.attrGlasses_chbx = QCheckBox(self.frame_2)
        self.attrGlasses_chbx.setObjectName(u"attrGlasses_chbx")

        self.attr_checkboxGroup.addWidget(self.attrGlasses_chbx)


        self.verticalLayout.addLayout(self.attr_checkboxGroup)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.close_btn = QPushButton(Form)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_2.addWidget(self.close_btn)

        self.startSearch_btn = QPushButton(Form)
        self.startSearch_btn.setObjectName(u"startSearch_btn")
        self.startSearch_btn.setMinimumSize(QSize(95, 0))
        self.startSearch_btn.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_2.addWidget(self.startSearch_btn)

        self.searchResult_btn = QPushButton(Form)
        self.searchResult_btn.setObjectName(u"searchResult_btn")
        self.searchResult_btn.setMinimumSize(QSize(95, 0))
        self.searchResult_btn.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_2.addWidget(self.searchResult_btn)

        self.reset_btn = QPushButton(Form)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout_2.addWidget(self.reset_btn)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 3, 1, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout.addWidget(self.label)

        self.camera_edit = QLineEdit(Form)
        self.camera_edit.setObjectName(u"camera_edit")
        self.camera_edit.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout.addWidget(self.camera_edit)

        self.selectCam_btn = QPushButton(Form)
        self.selectCam_btn.setObjectName(u"selectCam_btn")
        self.selectCam_btn.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout.addWidget(self.selectCam_btn)


        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 0, 1, 4)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 21))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16, 16))
        icon = QIcon()
        icon.addFile(u":/icon/icons/reject.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(201, 16))

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(50, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 4)


        self.retranslateUi(Form)

        self.model_comboBox.setCurrentIndex(-1)
        self.color_comboBox.setCurrentIndex(-1)
        self.brand_comboBox.setCurrentIndex(-1)
        self.car_comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Vehicle No.", None))
        self.vehicle_select_btn.setText(QCoreApplication.translate("Form", u"Select", None))
        self.vehicle_newReg_btn.setText(QCoreApplication.translate("Form", u"New Registration", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Model", None))
        self.model_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Grandeur", None))

        self.label_12.setText(QCoreApplication.translate("Form", u"Color", None))
        self.color_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Black", None))
        self.color_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Red", None))
        self.color_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Blue", None))
        self.color_comboBox.setItemText(3, QCoreApplication.translate("Form", u"White", None))

        self.vehicle_radiobtn.setText(QCoreApplication.translate("Form", u"Vehicle", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Brand", None))
        self.brand_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Hyundai", None))
        self.brand_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Mazda", None))
        self.brand_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Honda", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"Car Type", None))
        self.car_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Car", None))

        self.car_comboBox.setCurrentText("")
        self.car_comboBox.setPlaceholderText("")
        self.person_radiobtn.setText(QCoreApplication.translate("Form", u"Person", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Name", None))
        self.person_select_btn.setText(QCoreApplication.translate("Form", u"Select", None))
        self.person_newReg_btn.setText(QCoreApplication.translate("Form", u"New Registration", None))
        self.label_foto.setText(QCoreApplication.translate("Form", u"Foto", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Gender", None))
        self.Gmale_radiobtn.setText(QCoreApplication.translate("Form", u"Male", None))
        self.Gfemale_radiobtn.setText(QCoreApplication.translate("Form", u"Female", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Hairstyle", None))
        self.Hlong_radiobtn.setText(QCoreApplication.translate("Form", u"Long", None))
        self.Hshort_radiobtn.setText(QCoreApplication.translate("Form", u"Short", None))
        self.attrHat_chbx.setText(QCoreApplication.translate("Form", u"Hat", None))
        self.attrBag_chbx.setText(QCoreApplication.translate("Form", u"Bag", None))
        self.attrMask_chbx.setText(QCoreApplication.translate("Form", u"Mask", None))
        self.attrGlasses_chbx.setText(QCoreApplication.translate("Form", u"Glasses", None))
        self.close_btn.setText(QCoreApplication.translate("Form", u"Close", None))
        self.startSearch_btn.setText(QCoreApplication.translate("Form", u"Start Search", None))
        self.searchResult_btn.setText(QCoreApplication.translate("Form", u"Search Result", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"reset input", None))
        self.label.setText(QCoreApplication.translate("Form", u"  Camera", None))
        self.selectCam_btn.setText(QCoreApplication.translate("Form", u"Select Camera", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"  Object Realtime Tracking", None))
    # retranslateUi

