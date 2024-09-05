# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1210, 644)
        MainWindow.setStyleSheet(u"/*background-color: #1E1E1E;\n"
"color: #FFFFFF;*/")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.centralwidget)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setStyleSheet(u"")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.title_bar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 20))
        self.label_3.setPixmap(QPixmap(u"../../icon/aery_logo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_2 = QLabel(self.title_bar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.title_bar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minimize_btn = QPushButton(self.frame_4)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy)
        self.minimize_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.minimize_btn)

        self.exit_btn = QPushButton(self.frame_4)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.exit_btn)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.title_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.content)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setEnabled(True)
        self.side_menu.setMaximumSize(QSize(250, 16777215))
        self.side_menu.setStyleSheet(u"background-color: #1E1E1E;\n"
"color: #FFFFFF;\n"
"font: 10px;\n"
"\n"
"\n"
"border-style: solid;\n"
"border-color: #37383E;\n"
"border-width: 1px;\n"
"\n"
"text-align: left;")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.side_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.panel = QFrame(self.side_menu)
        self.panel.setObjectName(u"panel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.panel.sizePolicy().hasHeightForWidth())
        self.panel.setSizePolicy(sizePolicy1)
        self.panel.setStyleSheet(u"")
        self.panel.setFrameShape(QFrame.StyledPanel)
        self.panel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.panel)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.panel)
        self.frame_5.setObjectName(u"frame_5")
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)

        self.horizontalLayout_6.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame = QFrame(self.panel)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nvr_reg_btn = QPushButton(self.frame)
        self.nvr_reg_btn.setObjectName(u"nvr_reg_btn")
        self.nvr_reg_btn.setIconSize(QSize(16, 16))

        self.verticalLayout_4.addWidget(self.nvr_reg_btn)

        self.camera_reg_btn = QPushButton(self.frame)
        self.camera_reg_btn.setObjectName(u"camera_reg_btn")

        self.verticalLayout_4.addWidget(self.camera_reg_btn)

        self.camera_list_btn = QPushButton(self.frame)
        self.camera_list_btn.setObjectName(u"camera_list_btn")

        self.verticalLayout_4.addWidget(self.camera_list_btn)

        self.camera_map_f = QFrame(self.frame)
        self.camera_map_f.setObjectName(u"camera_map_f")
        self.camera_map_f.setMinimumSize(QSize(0, 10))
        self.camera_map_f.setFrameShape(QFrame.StyledPanel)
        self.camera_map_f.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.camera_map_f)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.camera_map_btn = QPushButton(self.camera_map_f)
        self.camera_map_btn.setObjectName(u"camera_map_btn")
        self.camera_map_btn.setEnabled(True)
        self.camera_map_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.camera_map_btn.setAcceptDrops(False)

        self.verticalLayout_8.addWidget(self.camera_map_btn)

        self.cammap_cs = QFrame(self.camera_map_f)
        self.cammap_cs.setObjectName(u"cammap_cs")
        self.cammap_cs.setMinimumSize(QSize(0, 0))
        self.cammap_cs.setMaximumSize(QSize(300, 0))
        self.cammap_cs.setFrameShape(QFrame.StyledPanel)
        self.cammap_cs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.cammap_cs)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_9 = QPushButton(self.cammap_cs)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_9.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.cammap_cs)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_9.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.cammap_cs)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_9.addWidget(self.pushButton_11)


        self.verticalLayout_8.addWidget(self.cammap_cs)


        self.verticalLayout_4.addWidget(self.camera_map_f)

        self.user_def_btn = QPushButton(self.frame)
        self.user_def_btn.setObjectName(u"user_def_btn")
        self.user_def_btn.setFlat(False)

        self.verticalLayout_4.addWidget(self.user_def_btn)

        self.vehicle_reg_btn = QPushButton(self.frame)
        self.vehicle_reg_btn.setObjectName(u"vehicle_reg_btn")

        self.verticalLayout_4.addWidget(self.vehicle_reg_btn)

        self.people_reg_btn = QPushButton(self.frame)
        self.people_reg_btn.setObjectName(u"people_reg_btn")

        self.verticalLayout_4.addWidget(self.people_reg_btn)

        self.event_setting_btn = QPushButton(self.frame)
        self.event_setting_btn.setObjectName(u"event_setting_btn")

        self.verticalLayout_4.addWidget(self.event_setting_btn)

        self.search_func_f = QFrame(self.frame)
        self.search_func_f.setObjectName(u"search_func_f")
        self.search_func_f.setFrameShape(QFrame.StyledPanel)
        self.search_func_f.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.search_func_f)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.search_func_btn = QPushButton(self.search_func_f)
        self.search_func_btn.setObjectName(u"search_func_btn")

        self.verticalLayout_10.addWidget(self.search_func_btn)

        self.sfunc_cs = QFrame(self.search_func_f)
        self.sfunc_cs.setObjectName(u"sfunc_cs")
        self.sfunc_cs.setMaximumSize(QSize(16777215, 0))
        self.sfunc_cs.setFrameShape(QFrame.StyledPanel)
        self.sfunc_cs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.sfunc_cs)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.people_search_btn = QPushButton(self.sfunc_cs)
        self.people_search_btn.setObjectName(u"people_search_btn")

        self.verticalLayout_11.addWidget(self.people_search_btn)

        self.vehicle_search_btn = QPushButton(self.sfunc_cs)
        self.vehicle_search_btn.setObjectName(u"vehicle_search_btn")

        self.verticalLayout_11.addWidget(self.vehicle_search_btn)

        self.vehicle_accident_search_btn = QPushButton(self.sfunc_cs)
        self.vehicle_accident_search_btn.setObjectName(u"vehicle_accident_search_btn")

        self.verticalLayout_11.addWidget(self.vehicle_accident_search_btn)

        self.fire_detection_search_btn = QPushButton(self.sfunc_cs)
        self.fire_detection_search_btn.setObjectName(u"fire_detection_search_btn")

        self.verticalLayout_11.addWidget(self.fire_detection_search_btn)

        self.behavior_search_btn = QPushButton(self.sfunc_cs)
        self.behavior_search_btn.setObjectName(u"behavior_search_btn")

        self.verticalLayout_11.addWidget(self.behavior_search_btn)

        self.obj_tracking_search_btn = QPushButton(self.sfunc_cs)
        self.obj_tracking_search_btn.setObjectName(u"obj_tracking_search_btn")

        self.verticalLayout_11.addWidget(self.obj_tracking_search_btn)


        self.verticalLayout_10.addWidget(self.sfunc_cs)


        self.verticalLayout_4.addWidget(self.search_func_f)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame_6 = QFrame(self.panel)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.panel)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.net_setting = QPushButton(self.frame_3)
        self.net_setting.setObjectName(u"net_setting")

        self.verticalLayout_7.addWidget(self.net_setting)

        self.user_management = QPushButton(self.frame_3)
        self.user_management.setObjectName(u"user_management")

        self.verticalLayout_7.addWidget(self.user_management)

        self.camera_map_manag = QPushButton(self.frame_3)
        self.camera_map_manag.setObjectName(u"camera_map_manag")

        self.verticalLayout_7.addWidget(self.camera_map_manag)

        self.camera_map_f_2 = QFrame(self.frame_3)
        self.camera_map_f_2.setObjectName(u"camera_map_f_2")
        self.camera_map_f_2.setMinimumSize(QSize(0, 10))
        self.camera_map_f_2.setFrameShape(QFrame.StyledPanel)
        self.camera_map_f_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.camera_map_f_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.custom_zone_setting = QPushButton(self.camera_map_f_2)
        self.custom_zone_setting.setObjectName(u"custom_zone_setting")
        self.custom_zone_setting.setEnabled(True)
        self.custom_zone_setting.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.custom_zone_setting.setAcceptDrops(False)

        self.verticalLayout_12.addWidget(self.custom_zone_setting)

        self.cammap_cs_2 = QFrame(self.camera_map_f_2)
        self.cammap_cs_2.setObjectName(u"cammap_cs_2")
        self.cammap_cs_2.setMinimumSize(QSize(0, 0))
        self.cammap_cs_2.setMaximumSize(QSize(300, 0))
        self.cammap_cs_2.setFrameShape(QFrame.StyledPanel)
        self.cammap_cs_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.cammap_cs_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_12 = QPushButton(self.cammap_cs_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_13.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.cammap_cs_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_13.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.cammap_cs_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_13.addWidget(self.pushButton_14)


        self.verticalLayout_12.addWidget(self.cammap_cs_2)


        self.verticalLayout_7.addWidget(self.camera_map_f_2)

        self.surv_area_setting = QPushButton(self.frame_3)
        self.surv_area_setting.setObjectName(u"surv_area_setting")
        self.surv_area_setting.setFlat(False)

        self.verticalLayout_7.addWidget(self.surv_area_setting)

        self.event_setting = QPushButton(self.frame_3)
        self.event_setting.setObjectName(u"event_setting")

        self.verticalLayout_7.addWidget(self.event_setting)

        self.ai_engine_up = QPushButton(self.frame_3)
        self.ai_engine_up.setObjectName(u"ai_engine_up")

        self.verticalLayout_7.addWidget(self.ai_engine_up)

        self.system_setting = QPushButton(self.frame_3)
        self.system_setting.setObjectName(u"system_setting")

        self.verticalLayout_7.addWidget(self.system_setting)

        self.search_func_f_2 = QFrame(self.frame_3)
        self.search_func_f_2.setObjectName(u"search_func_f_2")
        self.search_func_f_2.setFrameShape(QFrame.StyledPanel)
        self.search_func_f_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.search_func_f_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.system_log = QPushButton(self.search_func_f_2)
        self.system_log.setObjectName(u"system_log")

        self.verticalLayout_14.addWidget(self.system_log)

        self.sfunc_cs_2 = QFrame(self.search_func_f_2)
        self.sfunc_cs_2.setObjectName(u"sfunc_cs_2")
        self.sfunc_cs_2.setMaximumSize(QSize(16777215, 0))
        self.sfunc_cs_2.setFrameShape(QFrame.StyledPanel)
        self.sfunc_cs_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.sfunc_cs_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.people_search_btn_2 = QPushButton(self.sfunc_cs_2)
        self.people_search_btn_2.setObjectName(u"people_search_btn_2")

        self.verticalLayout_15.addWidget(self.people_search_btn_2)

        self.vehicle_search_btn_2 = QPushButton(self.sfunc_cs_2)
        self.vehicle_search_btn_2.setObjectName(u"vehicle_search_btn_2")

        self.verticalLayout_15.addWidget(self.vehicle_search_btn_2)

        self.vehicle_accident_search_btn_2 = QPushButton(self.sfunc_cs_2)
        self.vehicle_accident_search_btn_2.setObjectName(u"vehicle_accident_search_btn_2")

        self.verticalLayout_15.addWidget(self.vehicle_accident_search_btn_2)

        self.fire_detection_search_btn_2 = QPushButton(self.sfunc_cs_2)
        self.fire_detection_search_btn_2.setObjectName(u"fire_detection_search_btn_2")

        self.verticalLayout_15.addWidget(self.fire_detection_search_btn_2)

        self.behavior_search_btn_2 = QPushButton(self.sfunc_cs_2)
        self.behavior_search_btn_2.setObjectName(u"behavior_search_btn_2")

        self.verticalLayout_15.addWidget(self.behavior_search_btn_2)

        self.obj_tracking_search_btn_2 = QPushButton(self.sfunc_cs_2)
        self.obj_tracking_search_btn_2.setObjectName(u"obj_tracking_search_btn_2")

        self.verticalLayout_15.addWidget(self.obj_tracking_search_btn_2)


        self.verticalLayout_14.addWidget(self.sfunc_cs_2)


        self.verticalLayout_7.addWidget(self.search_func_f_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.panel)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.setting_btn = QPushButton(self.frame_2)
        self.setting_btn.setObjectName(u"setting_btn")

        self.verticalLayout_5.addWidget(self.setting_btn)

        self.login_btn = QPushButton(self.frame_2)
        self.login_btn.setObjectName(u"login_btn")

        self.verticalLayout_5.addWidget(self.login_btn)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.panel)


        self.horizontalLayout_2.addWidget(self.side_menu)

        self.split_screen = QFrame(self.content)
        self.split_screen.setObjectName(u"split_screen")
        self.split_screen.setFrameShape(QFrame.NoFrame)
        self.split_screen.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.split_screen)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.foot_panel = QFrame(self.split_screen)
        self.foot_panel.setObjectName(u"foot_panel")
        self.foot_panel.setMaximumSize(QSize(16777215, 40))
        self.foot_panel.setStyleSheet(u"background-color: #1E1E1E;\n"
"color: #FFFFFF;\n"
"/**font-family: 'inter';*/\n"
"font: 12px;")
        self.foot_panel.setFrameShape(QFrame.StyledPanel)
        self.foot_panel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.foot_panel)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.screen_lock_btn = QPushButton(self.foot_panel)
        self.screen_lock_btn.setObjectName(u"screen_lock_btn")
        icon = QIcon()
        icon.addFile(u"../../icon/lock (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.screen_lock_btn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.screen_lock_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.map_mng_frame = QFrame(self.foot_panel)
        self.map_mng_frame.setObjectName(u"map_mng_frame")
        self.map_mng_frame.setMinimumSize(QSize(0, 0))
        self.map_mng_frame.setFrameShape(QFrame.NoFrame)
        self.map_mng_frame.setFrameShadow(QFrame.Raised)
        self.map_mng_frame.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.map_mng_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.map_mng_btn = QPushButton(self.map_mng_frame)
        self.map_mng_btn.setObjectName(u"map_mng_btn")
        sizePolicy.setHeightForWidth(self.map_mng_btn.sizePolicy().hasHeightForWidth())
        self.map_mng_btn.setSizePolicy(sizePolicy)
        self.map_mng_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.map_mng_btn)

        self.cam_regis_btn = QPushButton(self.map_mng_frame)
        self.cam_regis_btn.setObjectName(u"cam_regis_btn")
        self.cam_regis_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.cam_regis_btn)

        self.delete_cam_btn = QPushButton(self.map_mng_frame)
        self.delete_cam_btn.setObjectName(u"delete_cam_btn")
        self.delete_cam_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.delete_cam_btn)

        self.eventsett_map_btn = QPushButton(self.map_mng_frame)
        self.eventsett_map_btn.setObjectName(u"eventsett_map_btn")
        self.eventsett_map_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.eventsett_map_btn)


        self.horizontalLayout_3.addWidget(self.map_mng_frame)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.btn_screen1x = QPushButton(self.foot_panel)
        self.btn_screen1x.setObjectName(u"btn_screen1x")
        self.btn_screen1x.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"../../icon/grid1_.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_screen1x.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btn_screen1x)

        self.btn_screen4x = QPushButton(self.foot_panel)
        self.btn_screen4x.setObjectName(u"btn_screen4x")
        self.btn_screen4x.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"../../icon/grid4_.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_screen4x.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btn_screen4x)

        self.btn_screen9x = QPushButton(self.foot_panel)
        self.btn_screen9x.setObjectName(u"btn_screen9x")
        self.btn_screen9x.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u"../../icon/grid6_.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_screen9x.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.btn_screen9x)

        self.btn_screen16x = QPushButton(self.foot_panel)
        self.btn_screen16x.setObjectName(u"btn_screen16x")
        self.btn_screen16x.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_screen16x)

        self.btn_screen25x = QPushButton(self.foot_panel)
        self.btn_screen25x.setObjectName(u"btn_screen25x")
        self.btn_screen25x.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_screen25x)

        self.btn_screen36x = QPushButton(self.foot_panel)
        self.btn_screen36x.setObjectName(u"btn_screen36x")
        self.btn_screen36x.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_screen36x)

        self.btn_screen49x = QPushButton(self.foot_panel)
        self.btn_screen49x.setObjectName(u"btn_screen49x")
        self.btn_screen49x.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_screen49x)

        self.btn_screen64x = QPushButton(self.foot_panel)
        self.btn_screen64x.setObjectName(u"btn_screen64x")
        self.btn_screen64x.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_screen64x)

        self.fullscreen_ch_btn = QPushButton(self.foot_panel)
        self.fullscreen_ch_btn.setObjectName(u"fullscreen_ch_btn")
        self.fullscreen_ch_btn.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u"../../icon/fullscreen1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fullscreen_ch_btn.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.fullscreen_ch_btn)


        self.verticalLayout_2.addWidget(self.foot_panel)

        self.MultiScreenWg = QStackedWidget(self.split_screen)
        self.MultiScreenWg.setObjectName(u"MultiScreenWg")
        self.MultiScreenWg.setStyleSheet(u"background-color: #000000;\n"
"border-style: solid;\n"
"border-color: #37383E;\n"
"border-width: 1px;")
        self.screen1x = QWidget()
        self.screen1x.setObjectName(u"screen1x")
        self.gridLayout_4 = QGridLayout(self.screen1x)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.chscreen_0_00 = QLabel(self.screen1x)
        self.chscreen_0_00.setObjectName(u"chscreen_0_00")

        self.gridLayout_4.addWidget(self.chscreen_0_00, 0, 0, 1, 1)

        self.MultiScreenWg.addWidget(self.screen1x)
        self.screen4x = QWidget()
        self.screen4x.setObjectName(u"screen4x")
        self.gridLayout_2 = QGridLayout(self.screen4x)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.chscreen_1_01 = QLabel(self.screen4x)
        self.chscreen_1_01.setObjectName(u"chscreen_1_01")

        self.gridLayout_2.addWidget(self.chscreen_1_01, 0, 1, 1, 1)

        self.chscreen_1_11 = QLabel(self.screen4x)
        self.chscreen_1_11.setObjectName(u"chscreen_1_11")

        self.gridLayout_2.addWidget(self.chscreen_1_11, 1, 1, 1, 1)

        self.chscreen_1_00 = QLabel(self.screen4x)
        self.chscreen_1_00.setObjectName(u"chscreen_1_00")

        self.gridLayout_2.addWidget(self.chscreen_1_00, 0, 0, 1, 1)

        self.chscreen_1_10 = QLabel(self.screen4x)
        self.chscreen_1_10.setObjectName(u"chscreen_1_10")

        self.gridLayout_2.addWidget(self.chscreen_1_10, 1, 0, 1, 1)

        self.MultiScreenWg.addWidget(self.screen4x)
        self.screen9x = QWidget()
        self.screen9x.setObjectName(u"screen9x")
        self.gridLayout_3 = QGridLayout(self.screen9x)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.chscreen_2_01 = QLabel(self.screen9x)
        self.chscreen_2_01.setObjectName(u"chscreen_2_01")

        self.gridLayout_3.addWidget(self.chscreen_2_01, 0, 1, 1, 1)

        self.chscreen_2_00 = QLabel(self.screen9x)
        self.chscreen_2_00.setObjectName(u"chscreen_2_00")

        self.gridLayout_3.addWidget(self.chscreen_2_00, 0, 0, 1, 1)

        self.chscreen_2_11 = QLabel(self.screen9x)
        self.chscreen_2_11.setObjectName(u"chscreen_2_11")

        self.gridLayout_3.addWidget(self.chscreen_2_11, 1, 1, 1, 1)

        self.chscreen_2_10 = QLabel(self.screen9x)
        self.chscreen_2_10.setObjectName(u"chscreen_2_10")

        self.gridLayout_3.addWidget(self.chscreen_2_10, 1, 0, 1, 1)

        self.chscreen_2_12 = QLabel(self.screen9x)
        self.chscreen_2_12.setObjectName(u"chscreen_2_12")

        self.gridLayout_3.addWidget(self.chscreen_2_12, 1, 2, 1, 1)

        self.chscreen_2_21 = QLabel(self.screen9x)
        self.chscreen_2_21.setObjectName(u"chscreen_2_21")

        self.gridLayout_3.addWidget(self.chscreen_2_21, 2, 1, 1, 1)

        self.chscreen_2_20 = QLabel(self.screen9x)
        self.chscreen_2_20.setObjectName(u"chscreen_2_20")

        self.gridLayout_3.addWidget(self.chscreen_2_20, 2, 0, 1, 1)

        self.chscreen_2_22 = QLabel(self.screen9x)
        self.chscreen_2_22.setObjectName(u"chscreen_2_22")
        self.chscreen_2_22.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.chscreen_2_22, 2, 2, 1, 1)

        self.chscreen_2_02 = QLabel(self.screen9x)
        self.chscreen_2_02.setObjectName(u"chscreen_2_02")

        self.gridLayout_3.addWidget(self.chscreen_2_02, 0, 2, 1, 1)

        self.MultiScreenWg.addWidget(self.screen9x)
        self.screen16x = QWidget()
        self.screen16x.setObjectName(u"screen16x")
        self.gridLayout_5 = QGridLayout(self.screen16x)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.chscreen_3_31 = QLabel(self.screen16x)
        self.chscreen_3_31.setObjectName(u"chscreen_3_31")

        self.gridLayout_5.addWidget(self.chscreen_3_31, 3, 1, 1, 1)

        self.chscreen_3_03 = QLabel(self.screen16x)
        self.chscreen_3_03.setObjectName(u"chscreen_3_03")

        self.gridLayout_5.addWidget(self.chscreen_3_03, 0, 3, 1, 1)

        self.chscreen_3_21 = QLabel(self.screen16x)
        self.chscreen_3_21.setObjectName(u"chscreen_3_21")

        self.gridLayout_5.addWidget(self.chscreen_3_21, 2, 1, 1, 1)

        self.chscreen_3_00 = QLabel(self.screen16x)
        self.chscreen_3_00.setObjectName(u"chscreen_3_00")

        self.gridLayout_5.addWidget(self.chscreen_3_00, 0, 0, 1, 1)

        self.chscreen_3_13 = QLabel(self.screen16x)
        self.chscreen_3_13.setObjectName(u"chscreen_3_13")

        self.gridLayout_5.addWidget(self.chscreen_3_13, 1, 3, 1, 1)

        self.chscreen_3_12 = QLabel(self.screen16x)
        self.chscreen_3_12.setObjectName(u"chscreen_3_12")

        self.gridLayout_5.addWidget(self.chscreen_3_12, 1, 2, 1, 1)

        self.chscreen_3_10 = QLabel(self.screen16x)
        self.chscreen_3_10.setObjectName(u"chscreen_3_10")

        self.gridLayout_5.addWidget(self.chscreen_3_10, 1, 0, 1, 1)

        self.chscreen_3_01 = QLabel(self.screen16x)
        self.chscreen_3_01.setObjectName(u"chscreen_3_01")

        self.gridLayout_5.addWidget(self.chscreen_3_01, 0, 1, 1, 1)

        self.chscreen_3_11 = QLabel(self.screen16x)
        self.chscreen_3_11.setObjectName(u"chscreen_3_11")

        self.gridLayout_5.addWidget(self.chscreen_3_11, 1, 1, 1, 1)

        self.chscreen_3_02 = QLabel(self.screen16x)
        self.chscreen_3_02.setObjectName(u"chscreen_3_02")

        self.gridLayout_5.addWidget(self.chscreen_3_02, 0, 2, 1, 1)

        self.chscreen_3_20 = QLabel(self.screen16x)
        self.chscreen_3_20.setObjectName(u"chscreen_3_20")

        self.gridLayout_5.addWidget(self.chscreen_3_20, 2, 0, 1, 1)

        self.chscreen_3_30 = QLabel(self.screen16x)
        self.chscreen_3_30.setObjectName(u"chscreen_3_30")

        self.gridLayout_5.addWidget(self.chscreen_3_30, 3, 0, 1, 1)

        self.chscreen_3_22 = QLabel(self.screen16x)
        self.chscreen_3_22.setObjectName(u"chscreen_3_22")

        self.gridLayout_5.addWidget(self.chscreen_3_22, 2, 2, 1, 1)

        self.chscreen_3_23 = QLabel(self.screen16x)
        self.chscreen_3_23.setObjectName(u"chscreen_3_23")

        self.gridLayout_5.addWidget(self.chscreen_3_23, 2, 3, 1, 1)

        self.chscreen_3_32 = QLabel(self.screen16x)
        self.chscreen_3_32.setObjectName(u"chscreen_3_32")

        self.gridLayout_5.addWidget(self.chscreen_3_32, 3, 2, 1, 1)

        self.chscreen_3_33 = QLabel(self.screen16x)
        self.chscreen_3_33.setObjectName(u"chscreen_3_33")

        self.gridLayout_5.addWidget(self.chscreen_3_33, 3, 3, 1, 1)

        self.MultiScreenWg.addWidget(self.screen16x)
        self.screen25x = QWidget()
        self.screen25x.setObjectName(u"screen25x")
        self.gridLayout_6 = QGridLayout(self.screen25x)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.chscreen_4_44 = QLabel(self.screen25x)
        self.chscreen_4_44.setObjectName(u"chscreen_4_44")

        self.gridLayout_6.addWidget(self.chscreen_4_44, 7, 4, 1, 1)

        self.chscreen_4_24 = QLabel(self.screen25x)
        self.chscreen_4_24.setObjectName(u"chscreen_4_24")

        self.gridLayout_6.addWidget(self.chscreen_4_24, 5, 4, 1, 1)

        self.chscreen_4_43 = QLabel(self.screen25x)
        self.chscreen_4_43.setObjectName(u"chscreen_4_43")

        self.gridLayout_6.addWidget(self.chscreen_4_43, 7, 3, 1, 1)

        self.chscreen_4_41 = QLabel(self.screen25x)
        self.chscreen_4_41.setObjectName(u"chscreen_4_41")

        self.gridLayout_6.addWidget(self.chscreen_4_41, 7, 1, 1, 1)

        self.chscreen_4_14 = QLabel(self.screen25x)
        self.chscreen_4_14.setObjectName(u"chscreen_4_14")

        self.gridLayout_6.addWidget(self.chscreen_4_14, 4, 4, 1, 1)

        self.chscreen_4_04 = QLabel(self.screen25x)
        self.chscreen_4_04.setObjectName(u"chscreen_4_04")

        self.gridLayout_6.addWidget(self.chscreen_4_04, 2, 4, 1, 1)

        self.chscreen_4_34 = QLabel(self.screen25x)
        self.chscreen_4_34.setObjectName(u"chscreen_4_34")

        self.gridLayout_6.addWidget(self.chscreen_4_34, 6, 4, 1, 1)

        self.chscreen_4_42 = QLabel(self.screen25x)
        self.chscreen_4_42.setObjectName(u"chscreen_4_42")

        self.gridLayout_6.addWidget(self.chscreen_4_42, 7, 2, 1, 1)

        self.chscreen_4_40 = QLabel(self.screen25x)
        self.chscreen_4_40.setObjectName(u"chscreen_4_40")

        self.gridLayout_6.addWidget(self.chscreen_4_40, 7, 0, 1, 1)

        self.chscreen_4_30 = QLabel(self.screen25x)
        self.chscreen_4_30.setObjectName(u"chscreen_4_30")

        self.gridLayout_6.addWidget(self.chscreen_4_30, 6, 0, 1, 1)

        self.chscreen_4_33 = QLabel(self.screen25x)
        self.chscreen_4_33.setObjectName(u"chscreen_4_33")

        self.gridLayout_6.addWidget(self.chscreen_4_33, 6, 3, 1, 1)

        self.chscreen_4_23 = QLabel(self.screen25x)
        self.chscreen_4_23.setObjectName(u"chscreen_4_23")

        self.gridLayout_6.addWidget(self.chscreen_4_23, 5, 3, 1, 1)

        self.chscreen_4_13 = QLabel(self.screen25x)
        self.chscreen_4_13.setObjectName(u"chscreen_4_13")

        self.gridLayout_6.addWidget(self.chscreen_4_13, 4, 3, 1, 1)

        self.chscreen_4_32 = QLabel(self.screen25x)
        self.chscreen_4_32.setObjectName(u"chscreen_4_32")

        self.gridLayout_6.addWidget(self.chscreen_4_32, 6, 2, 1, 1)

        self.chscreen_4_03 = QLabel(self.screen25x)
        self.chscreen_4_03.setObjectName(u"chscreen_4_03")

        self.gridLayout_6.addWidget(self.chscreen_4_03, 2, 3, 1, 1)

        self.chscreen_4_22 = QLabel(self.screen25x)
        self.chscreen_4_22.setObjectName(u"chscreen_4_22")

        self.gridLayout_6.addWidget(self.chscreen_4_22, 5, 2, 1, 1)

        self.chscreen_4_21 = QLabel(self.screen25x)
        self.chscreen_4_21.setObjectName(u"chscreen_4_21")

        self.gridLayout_6.addWidget(self.chscreen_4_21, 5, 1, 1, 1)

        self.chscreen_4_31 = QLabel(self.screen25x)
        self.chscreen_4_31.setObjectName(u"chscreen_4_31")

        self.gridLayout_6.addWidget(self.chscreen_4_31, 6, 1, 1, 1)

        self.chscreen_4_20 = QLabel(self.screen25x)
        self.chscreen_4_20.setObjectName(u"chscreen_4_20")

        self.gridLayout_6.addWidget(self.chscreen_4_20, 5, 0, 1, 1)

        self.chscreen_4_11 = QLabel(self.screen25x)
        self.chscreen_4_11.setObjectName(u"chscreen_4_11")

        self.gridLayout_6.addWidget(self.chscreen_4_11, 4, 1, 1, 1)

        self.chscreen_4_10 = QLabel(self.screen25x)
        self.chscreen_4_10.setObjectName(u"chscreen_4_10")

        self.gridLayout_6.addWidget(self.chscreen_4_10, 4, 0, 1, 1)

        self.chscreen_4_12 = QLabel(self.screen25x)
        self.chscreen_4_12.setObjectName(u"chscreen_4_12")

        self.gridLayout_6.addWidget(self.chscreen_4_12, 4, 2, 1, 1)

        self.chscreen_4_02 = QLabel(self.screen25x)
        self.chscreen_4_02.setObjectName(u"chscreen_4_02")

        self.gridLayout_6.addWidget(self.chscreen_4_02, 2, 2, 1, 1)

        self.chscreen_4_01 = QLabel(self.screen25x)
        self.chscreen_4_01.setObjectName(u"chscreen_4_01")

        self.gridLayout_6.addWidget(self.chscreen_4_01, 2, 1, 1, 1)

        self.chscreen_4_00 = QLabel(self.screen25x)
        self.chscreen_4_00.setObjectName(u"chscreen_4_00")

        self.gridLayout_6.addWidget(self.chscreen_4_00, 2, 0, 1, 1)

        self.MultiScreenWg.addWidget(self.screen25x)
        self.screen36x = QWidget()
        self.screen36x.setObjectName(u"screen36x")
        self.gridLayout_7 = QGridLayout(self.screen36x)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.chscreen_5_12 = QLabel(self.screen36x)
        self.chscreen_5_12.setObjectName(u"chscreen_5_12")

        self.gridLayout_7.addWidget(self.chscreen_5_12, 3, 2, 1, 1)

        self.chscreen_5_31 = QLabel(self.screen36x)
        self.chscreen_5_31.setObjectName(u"chscreen_5_31")

        self.gridLayout_7.addWidget(self.chscreen_5_31, 6, 1, 1, 1)

        self.chscreen_5_21 = QLabel(self.screen36x)
        self.chscreen_5_21.setObjectName(u"chscreen_5_21")

        self.gridLayout_7.addWidget(self.chscreen_5_21, 4, 1, 1, 1)

        self.chscreen_5_50 = QLabel(self.screen36x)
        self.chscreen_5_50.setObjectName(u"chscreen_5_50")

        self.gridLayout_7.addWidget(self.chscreen_5_50, 8, 0, 1, 1)

        self.chscreen_5_42 = QLabel(self.screen36x)
        self.chscreen_5_42.setObjectName(u"chscreen_5_42")

        self.gridLayout_7.addWidget(self.chscreen_5_42, 7, 2, 1, 1)

        self.chscreen_5_41 = QLabel(self.screen36x)
        self.chscreen_5_41.setObjectName(u"chscreen_5_41")

        self.gridLayout_7.addWidget(self.chscreen_5_41, 7, 1, 1, 1)

        self.chscreen_5_10 = QLabel(self.screen36x)
        self.chscreen_5_10.setObjectName(u"chscreen_5_10")

        self.gridLayout_7.addWidget(self.chscreen_5_10, 3, 0, 1, 1)

        self.chscreen_5_20 = QLabel(self.screen36x)
        self.chscreen_5_20.setObjectName(u"chscreen_5_20")

        self.gridLayout_7.addWidget(self.chscreen_5_20, 4, 0, 1, 1)

        self.chscreen_5_00 = QLabel(self.screen36x)
        self.chscreen_5_00.setObjectName(u"chscreen_5_00")

        self.gridLayout_7.addWidget(self.chscreen_5_00, 2, 0, 1, 1)

        self.chscreen_5_03 = QLabel(self.screen36x)
        self.chscreen_5_03.setObjectName(u"chscreen_5_03")

        self.gridLayout_7.addWidget(self.chscreen_5_03, 2, 3, 1, 1)

        self.chscreen_5_30 = QLabel(self.screen36x)
        self.chscreen_5_30.setObjectName(u"chscreen_5_30")

        self.gridLayout_7.addWidget(self.chscreen_5_30, 6, 0, 1, 1)

        self.chscreen_5_02 = QLabel(self.screen36x)
        self.chscreen_5_02.setObjectName(u"chscreen_5_02")

        self.gridLayout_7.addWidget(self.chscreen_5_02, 2, 2, 1, 1)

        self.chscreen_5_32 = QLabel(self.screen36x)
        self.chscreen_5_32.setObjectName(u"chscreen_5_32")

        self.gridLayout_7.addWidget(self.chscreen_5_32, 6, 2, 1, 1)

        self.chscreen_5_52 = QLabel(self.screen36x)
        self.chscreen_5_52.setObjectName(u"chscreen_5_52")

        self.gridLayout_7.addWidget(self.chscreen_5_52, 8, 2, 1, 1)

        self.chscreen_5_40 = QLabel(self.screen36x)
        self.chscreen_5_40.setObjectName(u"chscreen_5_40")

        self.gridLayout_7.addWidget(self.chscreen_5_40, 7, 0, 1, 1)

        self.chscreen_5_01 = QLabel(self.screen36x)
        self.chscreen_5_01.setObjectName(u"chscreen_5_01")

        self.gridLayout_7.addWidget(self.chscreen_5_01, 2, 1, 1, 1)

        self.chscreen_5_04 = QLabel(self.screen36x)
        self.chscreen_5_04.setObjectName(u"chscreen_5_04")

        self.gridLayout_7.addWidget(self.chscreen_5_04, 2, 4, 1, 1)

        self.chscreen_5_51 = QLabel(self.screen36x)
        self.chscreen_5_51.setObjectName(u"chscreen_5_51")

        self.gridLayout_7.addWidget(self.chscreen_5_51, 8, 1, 1, 1)

        self.chscreen_5_11 = QLabel(self.screen36x)
        self.chscreen_5_11.setObjectName(u"chscreen_5_11")

        self.gridLayout_7.addWidget(self.chscreen_5_11, 3, 1, 1, 1)

        self.chscreen_5_22 = QLabel(self.screen36x)
        self.chscreen_5_22.setObjectName(u"chscreen_5_22")

        self.gridLayout_7.addWidget(self.chscreen_5_22, 4, 2, 1, 1)

        self.chscreen_5_05 = QLabel(self.screen36x)
        self.chscreen_5_05.setObjectName(u"chscreen_5_05")

        self.gridLayout_7.addWidget(self.chscreen_5_05, 2, 5, 1, 1)

        self.chscreen_5_13 = QLabel(self.screen36x)
        self.chscreen_5_13.setObjectName(u"chscreen_5_13")

        self.gridLayout_7.addWidget(self.chscreen_5_13, 3, 3, 1, 1)

        self.chscreen_5_14 = QLabel(self.screen36x)
        self.chscreen_5_14.setObjectName(u"chscreen_5_14")

        self.gridLayout_7.addWidget(self.chscreen_5_14, 3, 4, 1, 1)

        self.chscreen_5_23 = QLabel(self.screen36x)
        self.chscreen_5_23.setObjectName(u"chscreen_5_23")

        self.gridLayout_7.addWidget(self.chscreen_5_23, 4, 3, 1, 1)

        self.chscreen_5_33 = QLabel(self.screen36x)
        self.chscreen_5_33.setObjectName(u"chscreen_5_33")

        self.gridLayout_7.addWidget(self.chscreen_5_33, 6, 3, 1, 1)

        self.chscreen_5_24 = QLabel(self.screen36x)
        self.chscreen_5_24.setObjectName(u"chscreen_5_24")

        self.gridLayout_7.addWidget(self.chscreen_5_24, 4, 4, 1, 1)

        self.chscreen_5_43 = QLabel(self.screen36x)
        self.chscreen_5_43.setObjectName(u"chscreen_5_43")

        self.gridLayout_7.addWidget(self.chscreen_5_43, 7, 3, 1, 1)

        self.chscreen_5_44 = QLabel(self.screen36x)
        self.chscreen_5_44.setObjectName(u"chscreen_5_44")

        self.gridLayout_7.addWidget(self.chscreen_5_44, 7, 4, 1, 1)

        self.chscreen_5_53 = QLabel(self.screen36x)
        self.chscreen_5_53.setObjectName(u"chscreen_5_53")

        self.gridLayout_7.addWidget(self.chscreen_5_53, 8, 3, 1, 1)

        self.chscreen_5_34 = QLabel(self.screen36x)
        self.chscreen_5_34.setObjectName(u"chscreen_5_34")

        self.gridLayout_7.addWidget(self.chscreen_5_34, 6, 4, 1, 1)

        self.chscreen_5_15 = QLabel(self.screen36x)
        self.chscreen_5_15.setObjectName(u"chscreen_5_15")

        self.gridLayout_7.addWidget(self.chscreen_5_15, 3, 5, 1, 1)

        self.chscreen_5_25 = QLabel(self.screen36x)
        self.chscreen_5_25.setObjectName(u"chscreen_5_25")

        self.gridLayout_7.addWidget(self.chscreen_5_25, 4, 5, 1, 1)

        self.chscreen_5_35 = QLabel(self.screen36x)
        self.chscreen_5_35.setObjectName(u"chscreen_5_35")

        self.gridLayout_7.addWidget(self.chscreen_5_35, 6, 5, 1, 1)

        self.chscreen_5_45 = QLabel(self.screen36x)
        self.chscreen_5_45.setObjectName(u"chscreen_5_45")

        self.gridLayout_7.addWidget(self.chscreen_5_45, 7, 5, 1, 1)

        self.chscreen_5_55 = QLabel(self.screen36x)
        self.chscreen_5_55.setObjectName(u"chscreen_5_55")

        self.gridLayout_7.addWidget(self.chscreen_5_55, 8, 5, 1, 1)

        self.chscreen_5_54 = QLabel(self.screen36x)
        self.chscreen_5_54.setObjectName(u"chscreen_5_54")

        self.gridLayout_7.addWidget(self.chscreen_5_54, 8, 4, 1, 1)

        self.MultiScreenWg.addWidget(self.screen36x)
        self.screen49x = QWidget()
        self.screen49x.setObjectName(u"screen49x")
        self.gridLayout_8 = QGridLayout(self.screen49x)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.chscreen_6_14 = QLabel(self.screen49x)
        self.chscreen_6_14.setObjectName(u"chscreen_6_14")

        self.gridLayout_8.addWidget(self.chscreen_6_14, 1, 4, 1, 1)

        self.chscreen_6_21 = QLabel(self.screen49x)
        self.chscreen_6_21.setObjectName(u"chscreen_6_21")

        self.gridLayout_8.addWidget(self.chscreen_6_21, 2, 1, 1, 1)

        self.chscreen_6_20 = QLabel(self.screen49x)
        self.chscreen_6_20.setObjectName(u"chscreen_6_20")

        self.gridLayout_8.addWidget(self.chscreen_6_20, 2, 0, 1, 1)

        self.chscreen_6_23 = QLabel(self.screen49x)
        self.chscreen_6_23.setObjectName(u"chscreen_6_23")

        self.gridLayout_8.addWidget(self.chscreen_6_23, 2, 3, 1, 1)

        self.chscreen_6_40 = QLabel(self.screen49x)
        self.chscreen_6_40.setObjectName(u"chscreen_6_40")

        self.gridLayout_8.addWidget(self.chscreen_6_40, 4, 0, 1, 1)

        self.chscreen_6_16 = QLabel(self.screen49x)
        self.chscreen_6_16.setObjectName(u"chscreen_6_16")

        self.gridLayout_8.addWidget(self.chscreen_6_16, 1, 6, 1, 1)

        self.chscreen_6_33 = QLabel(self.screen49x)
        self.chscreen_6_33.setObjectName(u"chscreen_6_33")

        self.gridLayout_8.addWidget(self.chscreen_6_33, 3, 3, 1, 1)

        self.chscreen_6_24 = QLabel(self.screen49x)
        self.chscreen_6_24.setObjectName(u"chscreen_6_24")

        self.gridLayout_8.addWidget(self.chscreen_6_24, 2, 4, 1, 1)

        self.chscreen_6_41 = QLabel(self.screen49x)
        self.chscreen_6_41.setObjectName(u"chscreen_6_41")

        self.gridLayout_8.addWidget(self.chscreen_6_41, 4, 1, 1, 1)

        self.chscreen_6_02 = QLabel(self.screen49x)
        self.chscreen_6_02.setObjectName(u"chscreen_6_02")

        self.gridLayout_8.addWidget(self.chscreen_6_02, 0, 2, 1, 1)

        self.chscreen_6_04 = QLabel(self.screen49x)
        self.chscreen_6_04.setObjectName(u"chscreen_6_04")

        self.gridLayout_8.addWidget(self.chscreen_6_04, 0, 4, 1, 1)

        self.chscreen_6_11 = QLabel(self.screen49x)
        self.chscreen_6_11.setObjectName(u"chscreen_6_11")

        self.gridLayout_8.addWidget(self.chscreen_6_11, 1, 1, 1, 1)

        self.chscreen_6_03 = QLabel(self.screen49x)
        self.chscreen_6_03.setObjectName(u"chscreen_6_03")

        self.gridLayout_8.addWidget(self.chscreen_6_03, 0, 3, 1, 1)

        self.chscreen_6_50 = QLabel(self.screen49x)
        self.chscreen_6_50.setObjectName(u"chscreen_6_50")

        self.gridLayout_8.addWidget(self.chscreen_6_50, 5, 0, 1, 1)

        self.chscreen_6_55 = QLabel(self.screen49x)
        self.chscreen_6_55.setObjectName(u"chscreen_6_55")

        self.gridLayout_8.addWidget(self.chscreen_6_55, 5, 5, 1, 1)

        self.chscreen_6_31 = QLabel(self.screen49x)
        self.chscreen_6_31.setObjectName(u"chscreen_6_31")

        self.gridLayout_8.addWidget(self.chscreen_6_31, 3, 1, 1, 1)

        self.chscreen_6_32 = QLabel(self.screen49x)
        self.chscreen_6_32.setObjectName(u"chscreen_6_32")

        self.gridLayout_8.addWidget(self.chscreen_6_32, 3, 2, 1, 1)

        self.chscreen_6_44 = QLabel(self.screen49x)
        self.chscreen_6_44.setObjectName(u"chscreen_6_44")

        self.gridLayout_8.addWidget(self.chscreen_6_44, 4, 4, 1, 1)

        self.chscreen_6_52 = QLabel(self.screen49x)
        self.chscreen_6_52.setObjectName(u"chscreen_6_52")

        self.gridLayout_8.addWidget(self.chscreen_6_52, 5, 2, 1, 1)

        self.chscreen_6_22 = QLabel(self.screen49x)
        self.chscreen_6_22.setObjectName(u"chscreen_6_22")

        self.gridLayout_8.addWidget(self.chscreen_6_22, 2, 2, 1, 1)

        self.chscreen_6_26 = QLabel(self.screen49x)
        self.chscreen_6_26.setObjectName(u"chscreen_6_26")

        self.gridLayout_8.addWidget(self.chscreen_6_26, 2, 6, 1, 1)

        self.chscreen_6_51 = QLabel(self.screen49x)
        self.chscreen_6_51.setObjectName(u"chscreen_6_51")

        self.gridLayout_8.addWidget(self.chscreen_6_51, 5, 1, 1, 1)

        self.chscreen_6_54 = QLabel(self.screen49x)
        self.chscreen_6_54.setObjectName(u"chscreen_6_54")

        self.gridLayout_8.addWidget(self.chscreen_6_54, 5, 4, 1, 1)

        self.chscreen_6_12 = QLabel(self.screen49x)
        self.chscreen_6_12.setObjectName(u"chscreen_6_12")

        self.gridLayout_8.addWidget(self.chscreen_6_12, 1, 2, 1, 1)

        self.chscreen_6_06 = QLabel(self.screen49x)
        self.chscreen_6_06.setObjectName(u"chscreen_6_06")

        self.gridLayout_8.addWidget(self.chscreen_6_06, 0, 6, 1, 1)

        self.chscreen_6_53 = QLabel(self.screen49x)
        self.chscreen_6_53.setObjectName(u"chscreen_6_53")

        self.gridLayout_8.addWidget(self.chscreen_6_53, 5, 3, 1, 1)

        self.chscreen_6_01 = QLabel(self.screen49x)
        self.chscreen_6_01.setObjectName(u"chscreen_6_01")

        self.gridLayout_8.addWidget(self.chscreen_6_01, 0, 1, 1, 1)

        self.chscreen_6_25 = QLabel(self.screen49x)
        self.chscreen_6_25.setObjectName(u"chscreen_6_25")

        self.gridLayout_8.addWidget(self.chscreen_6_25, 2, 5, 1, 1)

        self.chscreen_6_10 = QLabel(self.screen49x)
        self.chscreen_6_10.setObjectName(u"chscreen_6_10")

        self.gridLayout_8.addWidget(self.chscreen_6_10, 1, 0, 1, 1)

        self.chscreen_6_05 = QLabel(self.screen49x)
        self.chscreen_6_05.setObjectName(u"chscreen_6_05")

        self.gridLayout_8.addWidget(self.chscreen_6_05, 0, 5, 1, 1)

        self.chscreen_6_46 = QLabel(self.screen49x)
        self.chscreen_6_46.setObjectName(u"chscreen_6_46")

        self.gridLayout_8.addWidget(self.chscreen_6_46, 4, 6, 1, 1)

        self.chscreen_6_43 = QLabel(self.screen49x)
        self.chscreen_6_43.setObjectName(u"chscreen_6_43")

        self.gridLayout_8.addWidget(self.chscreen_6_43, 4, 3, 1, 1)

        self.chscreen_6_35 = QLabel(self.screen49x)
        self.chscreen_6_35.setObjectName(u"chscreen_6_35")

        self.gridLayout_8.addWidget(self.chscreen_6_35, 3, 5, 1, 1)

        self.chscreen_6_00 = QLabel(self.screen49x)
        self.chscreen_6_00.setObjectName(u"chscreen_6_00")

        self.gridLayout_8.addWidget(self.chscreen_6_00, 0, 0, 1, 1)

        self.chscreen_6_42 = QLabel(self.screen49x)
        self.chscreen_6_42.setObjectName(u"chscreen_6_42")

        self.gridLayout_8.addWidget(self.chscreen_6_42, 4, 2, 1, 1)

        self.chscreen_6_36 = QLabel(self.screen49x)
        self.chscreen_6_36.setObjectName(u"chscreen_6_36")

        self.gridLayout_8.addWidget(self.chscreen_6_36, 3, 6, 1, 1)

        self.chscreen_6_13 = QLabel(self.screen49x)
        self.chscreen_6_13.setObjectName(u"chscreen_6_13")

        self.gridLayout_8.addWidget(self.chscreen_6_13, 1, 3, 1, 1)

        self.chscreen_6_30 = QLabel(self.screen49x)
        self.chscreen_6_30.setObjectName(u"chscreen_6_30")

        self.gridLayout_8.addWidget(self.chscreen_6_30, 3, 0, 1, 1)

        self.chscreen_6_34 = QLabel(self.screen49x)
        self.chscreen_6_34.setObjectName(u"chscreen_6_34")

        self.gridLayout_8.addWidget(self.chscreen_6_34, 3, 4, 1, 1)

        self.chscreen_6_45 = QLabel(self.screen49x)
        self.chscreen_6_45.setObjectName(u"chscreen_6_45")

        self.gridLayout_8.addWidget(self.chscreen_6_45, 4, 5, 1, 1)

        self.chscreen_6_15 = QLabel(self.screen49x)
        self.chscreen_6_15.setObjectName(u"chscreen_6_15")

        self.gridLayout_8.addWidget(self.chscreen_6_15, 1, 5, 1, 1)

        self.chscreen_6_56 = QLabel(self.screen49x)
        self.chscreen_6_56.setObjectName(u"chscreen_6_56")

        self.gridLayout_8.addWidget(self.chscreen_6_56, 5, 6, 1, 1)

        self.chscreen_6_60 = QLabel(self.screen49x)
        self.chscreen_6_60.setObjectName(u"chscreen_6_60")

        self.gridLayout_8.addWidget(self.chscreen_6_60, 6, 0, 1, 1)

        self.chscreen_6_61 = QLabel(self.screen49x)
        self.chscreen_6_61.setObjectName(u"chscreen_6_61")

        self.gridLayout_8.addWidget(self.chscreen_6_61, 6, 1, 1, 1)

        self.chscreen_6_62 = QLabel(self.screen49x)
        self.chscreen_6_62.setObjectName(u"chscreen_6_62")

        self.gridLayout_8.addWidget(self.chscreen_6_62, 6, 2, 1, 1)

        self.chscreen_6_63 = QLabel(self.screen49x)
        self.chscreen_6_63.setObjectName(u"chscreen_6_63")

        self.gridLayout_8.addWidget(self.chscreen_6_63, 6, 3, 1, 1)

        self.chscreen_6_64 = QLabel(self.screen49x)
        self.chscreen_6_64.setObjectName(u"chscreen_6_64")

        self.gridLayout_8.addWidget(self.chscreen_6_64, 6, 4, 1, 1)

        self.chscreen_6_65 = QLabel(self.screen49x)
        self.chscreen_6_65.setObjectName(u"chscreen_6_65")

        self.gridLayout_8.addWidget(self.chscreen_6_65, 6, 5, 1, 1)

        self.chscreen_6_66 = QLabel(self.screen49x)
        self.chscreen_6_66.setObjectName(u"chscreen_6_66")

        self.gridLayout_8.addWidget(self.chscreen_6_66, 6, 6, 1, 1)

        self.MultiScreenWg.addWidget(self.screen49x)
        self.screen64x = QWidget()
        self.screen64x.setObjectName(u"screen64x")
        self.gridLayout = QGridLayout(self.screen64x)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chscreen_7_70 = QLabel(self.screen64x)
        self.chscreen_7_70.setObjectName(u"chscreen_7_70")

        self.gridLayout.addWidget(self.chscreen_7_70, 8, 0, 1, 1)

        self.chscreen_7_10 = QLabel(self.screen64x)
        self.chscreen_7_10.setObjectName(u"chscreen_7_10")

        self.gridLayout.addWidget(self.chscreen_7_10, 1, 0, 1, 1)

        self.chscreen_7_51 = QLabel(self.screen64x)
        self.chscreen_7_51.setObjectName(u"chscreen_7_51")

        self.gridLayout.addWidget(self.chscreen_7_51, 5, 1, 1, 1)

        self.chscreen_7_03 = QLabel(self.screen64x)
        self.chscreen_7_03.setObjectName(u"chscreen_7_03")

        self.gridLayout.addWidget(self.chscreen_7_03, 0, 3, 1, 1)

        self.chscreen_7_00 = QLabel(self.screen64x)
        self.chscreen_7_00.setObjectName(u"chscreen_7_00")

        self.gridLayout.addWidget(self.chscreen_7_00, 0, 0, 1, 1)

        self.chscreen_7_71 = QLabel(self.screen64x)
        self.chscreen_7_71.setObjectName(u"chscreen_7_71")

        self.gridLayout.addWidget(self.chscreen_7_71, 8, 1, 1, 1)

        self.chscreen_7_30 = QLabel(self.screen64x)
        self.chscreen_7_30.setObjectName(u"chscreen_7_30")

        self.gridLayout.addWidget(self.chscreen_7_30, 3, 0, 1, 1)

        self.chscreen_7_02 = QLabel(self.screen64x)
        self.chscreen_7_02.setObjectName(u"chscreen_7_02")

        self.gridLayout.addWidget(self.chscreen_7_02, 0, 2, 1, 1)

        self.chscreen_7_05 = QLabel(self.screen64x)
        self.chscreen_7_05.setObjectName(u"chscreen_7_05")

        self.gridLayout.addWidget(self.chscreen_7_05, 0, 5, 1, 1)

        self.chscreen_7_50 = QLabel(self.screen64x)
        self.chscreen_7_50.setObjectName(u"chscreen_7_50")

        self.gridLayout.addWidget(self.chscreen_7_50, 5, 0, 1, 1)

        self.chscreen_7_07 = QLabel(self.screen64x)
        self.chscreen_7_07.setObjectName(u"chscreen_7_07")

        self.gridLayout.addWidget(self.chscreen_7_07, 0, 7, 1, 1)

        self.chscreen_7_20 = QLabel(self.screen64x)
        self.chscreen_7_20.setObjectName(u"chscreen_7_20")

        self.gridLayout.addWidget(self.chscreen_7_20, 2, 0, 1, 1)

        self.chscreen_7_04 = QLabel(self.screen64x)
        self.chscreen_7_04.setObjectName(u"chscreen_7_04")

        self.gridLayout.addWidget(self.chscreen_7_04, 0, 4, 1, 1)

        self.chscreen_7_06 = QLabel(self.screen64x)
        self.chscreen_7_06.setObjectName(u"chscreen_7_06")

        self.gridLayout.addWidget(self.chscreen_7_06, 0, 6, 1, 1)

        self.chscreen_7_01 = QLabel(self.screen64x)
        self.chscreen_7_01.setObjectName(u"chscreen_7_01")

        self.gridLayout.addWidget(self.chscreen_7_01, 0, 1, 1, 1)

        self.chscreen_7_40 = QLabel(self.screen64x)
        self.chscreen_7_40.setObjectName(u"chscreen_7_40")

        self.gridLayout.addWidget(self.chscreen_7_40, 4, 0, 1, 1)

        self.chscreen_7_60 = QLabel(self.screen64x)
        self.chscreen_7_60.setObjectName(u"chscreen_7_60")

        self.gridLayout.addWidget(self.chscreen_7_60, 6, 0, 1, 1)

        self.chscreen_7_61 = QLabel(self.screen64x)
        self.chscreen_7_61.setObjectName(u"chscreen_7_61")

        self.gridLayout.addWidget(self.chscreen_7_61, 6, 1, 1, 1)

        self.chscreen_7_42 = QLabel(self.screen64x)
        self.chscreen_7_42.setObjectName(u"chscreen_7_42")

        self.gridLayout.addWidget(self.chscreen_7_42, 4, 2, 1, 1)

        self.chscreen_7_32 = QLabel(self.screen64x)
        self.chscreen_7_32.setObjectName(u"chscreen_7_32")

        self.gridLayout.addWidget(self.chscreen_7_32, 3, 2, 1, 1)

        self.chscreen_7_22 = QLabel(self.screen64x)
        self.chscreen_7_22.setObjectName(u"chscreen_7_22")

        self.gridLayout.addWidget(self.chscreen_7_22, 2, 2, 1, 1)

        self.chscreen_7_12 = QLabel(self.screen64x)
        self.chscreen_7_12.setObjectName(u"chscreen_7_12")

        self.gridLayout.addWidget(self.chscreen_7_12, 1, 2, 1, 1)

        self.chscreen_7_52 = QLabel(self.screen64x)
        self.chscreen_7_52.setObjectName(u"chscreen_7_52")

        self.gridLayout.addWidget(self.chscreen_7_52, 5, 2, 1, 1)

        self.chscreen_7_53 = QLabel(self.screen64x)
        self.chscreen_7_53.setObjectName(u"chscreen_7_53")

        self.gridLayout.addWidget(self.chscreen_7_53, 5, 3, 1, 1)

        self.chscreen_7_44 = QLabel(self.screen64x)
        self.chscreen_7_44.setObjectName(u"chscreen_7_44")

        self.gridLayout.addWidget(self.chscreen_7_44, 4, 4, 1, 1)

        self.chscreen_7_35 = QLabel(self.screen64x)
        self.chscreen_7_35.setObjectName(u"chscreen_7_35")

        self.gridLayout.addWidget(self.chscreen_7_35, 3, 5, 1, 1)

        self.chscreen_7_46 = QLabel(self.screen64x)
        self.chscreen_7_46.setObjectName(u"chscreen_7_46")

        self.gridLayout.addWidget(self.chscreen_7_46, 4, 6, 1, 1)

        self.chscreen_7_57 = QLabel(self.screen64x)
        self.chscreen_7_57.setObjectName(u"chscreen_7_57")

        self.gridLayout.addWidget(self.chscreen_7_57, 5, 7, 1, 1)

        self.chscreen_7_11 = QLabel(self.screen64x)
        self.chscreen_7_11.setObjectName(u"chscreen_7_11")

        self.gridLayout.addWidget(self.chscreen_7_11, 1, 1, 1, 1)

        self.chscreen_7_21 = QLabel(self.screen64x)
        self.chscreen_7_21.setObjectName(u"chscreen_7_21")

        self.gridLayout.addWidget(self.chscreen_7_21, 2, 1, 1, 1)

        self.chscreen_7_31 = QLabel(self.screen64x)
        self.chscreen_7_31.setObjectName(u"chscreen_7_31")

        self.gridLayout.addWidget(self.chscreen_7_31, 3, 1, 1, 1)

        self.chscreen_7_41 = QLabel(self.screen64x)
        self.chscreen_7_41.setObjectName(u"chscreen_7_41")

        self.gridLayout.addWidget(self.chscreen_7_41, 4, 1, 1, 1)

        self.chscreen_7_43 = QLabel(self.screen64x)
        self.chscreen_7_43.setObjectName(u"chscreen_7_43")

        self.gridLayout.addWidget(self.chscreen_7_43, 4, 3, 1, 1)

        self.chscreen_7_62 = QLabel(self.screen64x)
        self.chscreen_7_62.setObjectName(u"chscreen_7_62")

        self.gridLayout.addWidget(self.chscreen_7_62, 6, 2, 1, 1)

        self.chscreen_7_72 = QLabel(self.screen64x)
        self.chscreen_7_72.setObjectName(u"chscreen_7_72")

        self.gridLayout.addWidget(self.chscreen_7_72, 8, 2, 1, 1)

        self.chscreen_7_23 = QLabel(self.screen64x)
        self.chscreen_7_23.setObjectName(u"chscreen_7_23")

        self.gridLayout.addWidget(self.chscreen_7_23, 2, 3, 1, 1)

        self.chscreen_7_34 = QLabel(self.screen64x)
        self.chscreen_7_34.setObjectName(u"chscreen_7_34")

        self.gridLayout.addWidget(self.chscreen_7_34, 3, 4, 1, 1)

        self.chscreen_7_45 = QLabel(self.screen64x)
        self.chscreen_7_45.setObjectName(u"chscreen_7_45")

        self.gridLayout.addWidget(self.chscreen_7_45, 4, 5, 1, 1)

        self.chscreen_7_36 = QLabel(self.screen64x)
        self.chscreen_7_36.setObjectName(u"chscreen_7_36")

        self.gridLayout.addWidget(self.chscreen_7_36, 3, 6, 1, 1)

        self.chscreen_7_47 = QLabel(self.screen64x)
        self.chscreen_7_47.setObjectName(u"chscreen_7_47")

        self.gridLayout.addWidget(self.chscreen_7_47, 4, 7, 1, 1)

        self.chscreen_7_14 = QLabel(self.screen64x)
        self.chscreen_7_14.setObjectName(u"chscreen_7_14")

        self.gridLayout.addWidget(self.chscreen_7_14, 1, 4, 1, 1)

        self.chscreen_7_24 = QLabel(self.screen64x)
        self.chscreen_7_24.setObjectName(u"chscreen_7_24")

        self.gridLayout.addWidget(self.chscreen_7_24, 2, 4, 1, 1)

        self.chscreen_7_33 = QLabel(self.screen64x)
        self.chscreen_7_33.setObjectName(u"chscreen_7_33")

        self.gridLayout.addWidget(self.chscreen_7_33, 3, 3, 1, 1)

        self.chscreen_7_54 = QLabel(self.screen64x)
        self.chscreen_7_54.setObjectName(u"chscreen_7_54")

        self.gridLayout.addWidget(self.chscreen_7_54, 5, 4, 1, 1)

        self.chscreen_7_63 = QLabel(self.screen64x)
        self.chscreen_7_63.setObjectName(u"chscreen_7_63")

        self.gridLayout.addWidget(self.chscreen_7_63, 6, 3, 1, 1)

        self.chscreen_7_73 = QLabel(self.screen64x)
        self.chscreen_7_73.setObjectName(u"chscreen_7_73")

        self.gridLayout.addWidget(self.chscreen_7_73, 8, 3, 1, 1)

        self.chscreen_7_74 = QLabel(self.screen64x)
        self.chscreen_7_74.setObjectName(u"chscreen_7_74")

        self.gridLayout.addWidget(self.chscreen_7_74, 8, 4, 1, 1)

        self.chscreen_7_64 = QLabel(self.screen64x)
        self.chscreen_7_64.setObjectName(u"chscreen_7_64")

        self.gridLayout.addWidget(self.chscreen_7_64, 6, 4, 1, 1)

        self.chscreen_7_55 = QLabel(self.screen64x)
        self.chscreen_7_55.setObjectName(u"chscreen_7_55")

        self.gridLayout.addWidget(self.chscreen_7_55, 5, 5, 1, 1)

        self.chscreen_7_37 = QLabel(self.screen64x)
        self.chscreen_7_37.setObjectName(u"chscreen_7_37")

        self.gridLayout.addWidget(self.chscreen_7_37, 3, 7, 1, 1)

        self.chscreen_7_25 = QLabel(self.screen64x)
        self.chscreen_7_25.setObjectName(u"chscreen_7_25")

        self.gridLayout.addWidget(self.chscreen_7_25, 2, 5, 1, 1)

        self.chscreen_7_13 = QLabel(self.screen64x)
        self.chscreen_7_13.setObjectName(u"chscreen_7_13")

        self.gridLayout.addWidget(self.chscreen_7_13, 1, 3, 1, 1)

        self.chscreen_7_15 = QLabel(self.screen64x)
        self.chscreen_7_15.setObjectName(u"chscreen_7_15")

        self.gridLayout.addWidget(self.chscreen_7_15, 1, 5, 1, 1)

        self.chscreen_7_65 = QLabel(self.screen64x)
        self.chscreen_7_65.setObjectName(u"chscreen_7_65")

        self.gridLayout.addWidget(self.chscreen_7_65, 6, 5, 1, 1)

        self.chscreen_7_75 = QLabel(self.screen64x)
        self.chscreen_7_75.setObjectName(u"chscreen_7_75")

        self.gridLayout.addWidget(self.chscreen_7_75, 8, 5, 1, 1)

        self.chscreen_7_26 = QLabel(self.screen64x)
        self.chscreen_7_26.setObjectName(u"chscreen_7_26")

        self.gridLayout.addWidget(self.chscreen_7_26, 2, 6, 1, 1)

        self.chscreen_7_16 = QLabel(self.screen64x)
        self.chscreen_7_16.setObjectName(u"chscreen_7_16")

        self.gridLayout.addWidget(self.chscreen_7_16, 1, 6, 1, 1)

        self.chscreen_7_76 = QLabel(self.screen64x)
        self.chscreen_7_76.setObjectName(u"chscreen_7_76")

        self.gridLayout.addWidget(self.chscreen_7_76, 8, 6, 1, 1)

        self.chscreen_7_56 = QLabel(self.screen64x)
        self.chscreen_7_56.setObjectName(u"chscreen_7_56")

        self.gridLayout.addWidget(self.chscreen_7_56, 5, 6, 1, 1)

        self.chscreen_7_66 = QLabel(self.screen64x)
        self.chscreen_7_66.setObjectName(u"chscreen_7_66")

        self.gridLayout.addWidget(self.chscreen_7_66, 6, 6, 1, 1)

        self.chscreen_7_17 = QLabel(self.screen64x)
        self.chscreen_7_17.setObjectName(u"chscreen_7_17")

        self.gridLayout.addWidget(self.chscreen_7_17, 1, 7, 1, 1)

        self.chscreen_7_27 = QLabel(self.screen64x)
        self.chscreen_7_27.setObjectName(u"chscreen_7_27")

        self.gridLayout.addWidget(self.chscreen_7_27, 2, 7, 1, 1)

        self.chscreen_7_67 = QLabel(self.screen64x)
        self.chscreen_7_67.setObjectName(u"chscreen_7_67")

        self.gridLayout.addWidget(self.chscreen_7_67, 6, 7, 1, 1)

        self.chscreen_7_77 = QLabel(self.screen64x)
        self.chscreen_7_77.setObjectName(u"chscreen_7_77")

        self.gridLayout.addWidget(self.chscreen_7_77, 8, 7, 1, 1)

        self.MultiScreenWg.addWidget(self.screen64x)

        self.verticalLayout_2.addWidget(self.MultiScreenWg)


        self.horizontalLayout_2.addWidget(self.split_screen)


        self.verticalLayout_6.addWidget(self.content)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background-color: #1E1E1E;\n"
"color: #FFFFFF;\n"
"font: inter 16px;\n"
"font-style: normal;")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 5, 9, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.ipaddr_foot = QLabel(self.footer)
        self.ipaddr_foot.setObjectName(u"ipaddr_foot")
        sizePolicy1.setHeightForWidth(self.ipaddr_foot.sizePolicy().hasHeightForWidth())
        self.ipaddr_foot.setSizePolicy(sizePolicy1)
        self.ipaddr_foot.setMinimumSize(QSize(0, 0))
        self.ipaddr_foot.setStyleSheet(u"color: #FFFFFF;")

        self.horizontalLayout_5.addWidget(self.ipaddr_foot)

        self.horizontalSpacer_5 = QSpacerItem(7, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.usrid_foot = QLabel(self.footer)
        self.usrid_foot.setObjectName(u"usrid_foot")

        self.horizontalLayout_5.addWidget(self.usrid_foot)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.datetime_foot = QLabel(self.footer)
        self.datetime_foot.setObjectName(u"datetime_foot")

        self.horizontalLayout_5.addWidget(self.datetime_foot)


        self.verticalLayout_6.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MultiScreenWg.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Intelligence CCTV AI Analysis System (v1.0)", None))
        self.minimize_btn.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AI BOX Menu", None))
        self.nvr_reg_btn.setText(QCoreApplication.translate("MainWindow", u"NVR Registration", None))
        self.camera_reg_btn.setText(QCoreApplication.translate("MainWindow", u"Camera Registration", None))
        self.camera_list_btn.setText(QCoreApplication.translate("MainWindow", u"Camera List", None))
        self.camera_map_btn.setText(QCoreApplication.translate("MainWindow", u"Camera Map", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Map 1", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Map 2", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Map 3", None))
        self.user_def_btn.setText(QCoreApplication.translate("MainWindow", u"User Defined Area", None))
        self.vehicle_reg_btn.setText(QCoreApplication.translate("MainWindow", u"Vehicle Registration", None))
        self.people_reg_btn.setText(QCoreApplication.translate("MainWindow", u"Find People Regitration", None))
        self.event_setting_btn.setText(QCoreApplication.translate("MainWindow", u"Event Setting", None))
        self.search_func_btn.setText(QCoreApplication.translate("MainWindow", u"Search Function", None))
        self.people_search_btn.setText(QCoreApplication.translate("MainWindow", u"People Search", None))
        self.vehicle_search_btn.setText(QCoreApplication.translate("MainWindow", u"Vehicle Search", None))
        self.vehicle_accident_search_btn.setText(QCoreApplication.translate("MainWindow", u"Vehicle Accident Search", None))
        self.fire_detection_search_btn.setText(QCoreApplication.translate("MainWindow", u"Fire Detection", None))
        self.behavior_search_btn.setText(QCoreApplication.translate("MainWindow", u"Behavior Search", None))
        self.obj_tracking_search_btn.setText(QCoreApplication.translate("MainWindow", u"Object Tracking Search", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Administrator Menu", None))
        self.net_setting.setText(QCoreApplication.translate("MainWindow", u"Network Setting", None))
        self.user_management.setText(QCoreApplication.translate("MainWindow", u"User Management", None))
        self.camera_map_manag.setText(QCoreApplication.translate("MainWindow", u"Camera Map Management", None))
        self.custom_zone_setting.setText(QCoreApplication.translate("MainWindow", u"Custom Zone Setting", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Map 1", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Map 2", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Map 3", None))
        self.surv_area_setting.setText(QCoreApplication.translate("MainWindow", u"Surveillance Area Setting", None))
        self.event_setting.setText(QCoreApplication.translate("MainWindow", u"Event Settings", None))
        self.ai_engine_up.setText(QCoreApplication.translate("MainWindow", u"AI Engine Upgrade", None))
        self.system_setting.setText(QCoreApplication.translate("MainWindow", u"System Settings", None))
        self.system_log.setText(QCoreApplication.translate("MainWindow", u"System Log", None))
        self.people_search_btn_2.setText(QCoreApplication.translate("MainWindow", u"People Search", None))
        self.vehicle_search_btn_2.setText(QCoreApplication.translate("MainWindow", u"Vehicle Search", None))
        self.vehicle_accident_search_btn_2.setText(QCoreApplication.translate("MainWindow", u"Vehicle Accident Search", None))
        self.fire_detection_search_btn_2.setText(QCoreApplication.translate("MainWindow", u"Fire Detection", None))
        self.behavior_search_btn_2.setText(QCoreApplication.translate("MainWindow", u"Behavior Search", None))
        self.obj_tracking_search_btn_2.setText(QCoreApplication.translate("MainWindow", u"Object Tracking Search", None))
        self.setting_btn.setText(QCoreApplication.translate("MainWindow", u"System Setting", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.screen_lock_btn.setText(QCoreApplication.translate("MainWindow", u"Screen Lock", None))
        self.map_mng_btn.setText(QCoreApplication.translate("MainWindow", u"Map Management", None))
        self.cam_regis_btn.setText(QCoreApplication.translate("MainWindow", u"Camera Registration", None))
        self.delete_cam_btn.setText(QCoreApplication.translate("MainWindow", u"Delete Camera", None))
        self.eventsett_map_btn.setText(QCoreApplication.translate("MainWindow", u"Event Setting", None))
        self.btn_screen1x.setText("")
        self.btn_screen4x.setText("")
        self.btn_screen9x.setText("")
        self.btn_screen16x.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.btn_screen25x.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.btn_screen36x.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.btn_screen49x.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.btn_screen64x.setText(QCoreApplication.translate("MainWindow", u"64", None))
        self.fullscreen_ch_btn.setText("")
        self.chscreen_0_00.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_1_01.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_1_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_1_00.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_1_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_2_01.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_2_00.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_2_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_2_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_2_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_2_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_2_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_2_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_2_02.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_03.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_00.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_01.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_02.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_3_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_44.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_04.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_03.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_02.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_01.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_4_00.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_00.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_03.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_02.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_52.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_01.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_04.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_51.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_05.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_44.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_53.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_55.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_5_54.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_02.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_04.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_03.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_55.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_44.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_52.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_51.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_54.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_06.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_53.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_01.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_05.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_46.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_00.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_56.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_61.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_62.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_63.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_64.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_65.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_6_66.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_70.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_51.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_03.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_00.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_71.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_02.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_05.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_07.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_04.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_06.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_01.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_61.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_52.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_53.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_44.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_46.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_57.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_62.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_72.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_47.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_54.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_63.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_73.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_74.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_64.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_55.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_65.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_75.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_76.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_56.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_66.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_67.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.chscreen_7_77.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ipaddr_foot.setText(QCoreApplication.translate("MainWindow", u"IP: ---.---.-.-", None))
        self.usrid_foot.setText(QCoreApplication.translate("MainWindow", u"ID: 123KOR456", None))
        self.datetime_foot.setText(QCoreApplication.translate("MainWindow", u"2024-01-11 15:29:30", None))
    # retranslateUi

