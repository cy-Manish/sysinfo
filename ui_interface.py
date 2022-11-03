# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacekBCKsZ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from PySide2extn import *
from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar
from icons_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(743, 487)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"}\n"
"QProgressBar{\n"
"background-color:rgb(20,30,43);\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align: center;\n"
"color:rgb(255,0,0);\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,136,255,255), stop:1 rgba(255,255,255,255));\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(0, 78, 115);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_central = QFrame(self.header_frame)
        self.header_left_central.setObjectName(u"header_left_central")
        self.header_left_central.setStyleSheet(u"padding:0;\n"
"margin:0;")
        self.header_left_central.setFrameShape(QFrame.StyledPanel)
        self.header_left_central.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_central)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.header_left_central)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        font = QFont()
        font.setBold(True)
        self.open_close_side_bar_btn.setFont(font)
        self.open_close_side_bar_btn.setStyleSheet(u"margin:0;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_central, 0, Qt.AlignLeft)

        self.header_central_framel = QFrame(self.header_frame)
        self.header_central_framel.setObjectName(u"header_central_framel")
        self.header_central_framel.setFrameShape(QFrame.StyledPanel)
        self.header_central_framel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_central_framel)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_central_framel)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/icons/airplay.svg"))

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.header_central_framel)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_central_framel)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        font2 = QFont()
        font2.setPointSize(8)
        self.header_right_frame.setFont(font2)
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minimize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setMinimumSize(QSize(40, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(200, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"background-color: rgb(0, 74, 109);")
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1, Qt.AlignLeft)

        self.cpu_info_btn = QPushButton(self.menu_frame)
        self.cpu_info_btn.setObjectName(u"cpu_info_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/zoom-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_info_btn.setIcon(icon4)
        self.cpu_info_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.cpu_info_btn, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1, Qt.AlignLeft)

        self.battry_info_btn = QPushButton(self.menu_frame)
        self.battry_info_btn.setObjectName(u"battry_info_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/battery-charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.battry_info_btn.setIcon(icon5)
        self.battry_info_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.battry_info_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.system_info_btn = QPushButton(self.menu_frame)
        self.system_info_btn.setObjectName(u"system_info_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.system_info_btn.setIcon(icon6)
        self.system_info_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.system_info_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.activity_info_btn = QPushButton(self.menu_frame)
        self.activity_info_btn.setObjectName(u"activity_info_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_info_btn.setIcon(icon7)
        self.activity_info_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.activity_info_btn, 3, 0, 1, 1, Qt.AlignLeft)

        self.label_11 = QLabel(self.menu_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMargin(5)

        self.gridLayout.addWidget(self.label_11, 3, 1, 1, 1, Qt.AlignLeft)

        self.storage_info_btn = QPushButton(self.menu_frame)
        self.storage_info_btn.setObjectName(u"storage_info_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/disc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_info_btn.setIcon(icon8)
        self.storage_info_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.storage_info_btn, 4, 0, 1, 1, Qt.AlignLeft)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMargin(5)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1, Qt.AlignLeft)

        self.sensors_info_btn = QPushButton(self.menu_frame)
        self.sensors_info_btn.setObjectName(u"sensors_info_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/thermometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sensors_info_btn.setIcon(icon9)
        self.sensors_info_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.sensors_info_btn, 5, 0, 1, 1, Qt.AlignLeft)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMargin(5)

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1, Qt.AlignLeft)

        self.network_info_btn = QPushButton(self.menu_frame)
        self.network_info_btn.setObjectName(u"network_info_btn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.network_info_btn.setIcon(icon10)
        self.network_info_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.network_info_btn, 6, 0, 1, 1, Qt.AlignLeft)

        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMargin(5)

        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_13.addWidget(self.menu_frame)


        self.horizontalLayout_12.addWidget(self.left_menu_cont_frame, 0, Qt.AlignLeft)

        self.main_body_content = QFrame(self.main_body_frame)
        self.main_body_content.setObjectName(u"main_body_content")
        self.main_body_content.setStyleSheet(u"background-color: rgb(97, 97, 97);")
        self.main_body_content.setFrameShape(QFrame.StyledPanel)
        self.main_body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_body_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_4 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cpu_info_frame = QFrame(self.cpu_and_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")

        self.gridLayout_2.addWidget(self.cpu_count, 0, 1, 1, 1)

        self.cpu_per = QLabel(self.cpu_info_frame)
        self.cpu_per.setObjectName(u"cpu_per")

        self.gridLayout_2.addWidget(self.cpu_per, 1, 1, 1, 1)

        self.label_17 = QLabel(self.cpu_info_frame)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_15 = QLabel(self.cpu_info_frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_13 = QLabel(self.cpu_info_frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.cpu_main_core = QLabel(self.cpu_info_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")

        self.gridLayout_2.addWidget(self.cpu_main_core, 2, 1, 1, 1)

        self.cpu_percentage = roundProgressBar(self.cpu_info_frame)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setMinimumSize(QSize(150, 150))
        self.cpu_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.cpu_percentage, 0, 2, 3, 1)


        self.verticalLayout_4.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.cpu_and_memory)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ram_info_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ram_usage_2 = QLabel(self.ram_info_frame)
        self.ram_usage_2.setObjectName(u"ram_usage_2")

        self.gridLayout_3.addWidget(self.ram_usage_2, 4, 1, 1, 1)

        self.label_19 = QLabel(self.ram_info_frame)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)

        self.used_ram = QLabel(self.ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")

        self.gridLayout_3.addWidget(self.used_ram, 2, 1, 1, 1)

        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_3.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_23 = QLabel(self.ram_info_frame)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)

        self.free_ram = QLabel(self.ram_info_frame)
        self.free_ram.setObjectName(u"free_ram")

        self.gridLayout_3.addWidget(self.free_ram, 3, 1, 1, 1)

        self.avilable_ram = QLabel(self.ram_info_frame)
        self.avilable_ram.setObjectName(u"avilable_ram")

        self.gridLayout_3.addWidget(self.avilable_ram, 1, 1, 1, 1)

        self.label_22 = QLabel(self.ram_info_frame)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 2, 0, 1, 1)

        self.label_21 = QLabel(self.ram_info_frame)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_24 = QLabel(self.ram_info_frame)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 4, 0, 1, 1)

        self.ram_percentage = spiralProgressBar(self.ram_info_frame)
        self.ram_percentage.setObjectName(u"ram_percentage")
        self.ram_percentage.setMinimumSize(QSize(150, 150))
        self.ram_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_3.addWidget(self.ram_percentage, 0, 2, 5, 1)


        self.verticalLayout_4.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battrey = QWidget()
        self.battrey.setObjectName(u"battrey")
        sizePolicy.setHeightForWidth(self.battrey.sizePolicy().hasHeightForWidth())
        self.battrey.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.battrey)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.battrey)
        self.label_43.setObjectName(u"label_43")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_43.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_43, 0, Qt.AlignBottom)

        self.frame = QFrame(self.battrey)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.battery_plugged = QLabel(self.frame)
        self.battery_plugged.setObjectName(u"battery_plugged")

        self.gridLayout_4.addWidget(self.battery_plugged, 3, 1, 1, 1)

        self.label_45 = QLabel(self.frame)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_4.addWidget(self.label_45, 1, 0, 1, 1)

        self.label_44 = QLabel(self.frame)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_4.addWidget(self.label_44, 0, 0, 1, 1)

        self.battery_charge = QLabel(self.frame)
        self.battery_charge.setObjectName(u"battery_charge")

        self.gridLayout_4.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.label_47 = QLabel(self.frame)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_4.addWidget(self.label_47, 3, 0, 1, 1)

        self.label_46 = QLabel(self.frame)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_4.addWidget(self.label_46, 2, 0, 1, 1)

        self.battery_status = QLabel(self.frame)
        self.battery_status.setObjectName(u"battery_status")

        self.gridLayout_4.addWidget(self.battery_status, 0, 1, 1, 1)

        self.battery_time_left = QLabel(self.frame)
        self.battery_time_left.setObjectName(u"battery_time_left")

        self.gridLayout_4.addWidget(self.battery_time_left, 2, 1, 1, 1)

        self.battery_usage = roundProgressBar(self.frame)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(150, 150))
        self.battery_usage.setMaximumSize(QSize(150, 150))

        self.gridLayout_4.addWidget(self.battery_usage, 2, 2, 2, 1)


        self.verticalLayout_7.addWidget(self.frame)

        self.stackedWidget.addWidget(self.battrey)
        self.system_information = QWidget()
        self.system_information.setObjectName(u"system_information")
        self.verticalLayout_5 = QVBoxLayout(self.system_information)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.system_information)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_37 = QLabel(self.frame_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.gridLayout_5.addWidget(self.label_37, 4, 2, 1, 1)

        self.label_36 = QLabel(self.frame_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.gridLayout_5.addWidget(self.label_36, 3, 2, 1, 1)

        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.gridLayout_5.addWidget(self.label_35, 2, 2, 1, 1)

        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.gridLayout_5.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.gridLayout_5.addWidget(self.label_30, 0, 0, 1, 1, Qt.AlignTop)

        self.system_system = QLabel(self.frame_2)
        self.system_system.setObjectName(u"system_system")
        self.system_system.setFont(font)

        self.gridLayout_5.addWidget(self.system_system, 1, 0, 1, 1)

        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.gridLayout_5.addWidget(self.label_32, 3, 0, 1, 1)

        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.gridLayout_5.addWidget(self.label_33, 4, 0, 1, 1)

        self.system_platform = QLabel(self.frame_2)
        self.system_platform.setObjectName(u"system_platform")

        self.gridLayout_5.addWidget(self.system_platform, 2, 1, 1, 1)

        self.system_version = QLabel(self.frame_2)
        self.system_version.setObjectName(u"system_version")

        self.gridLayout_5.addWidget(self.system_version, 3, 1, 1, 1)

        self.system_date = QLabel(self.frame_2)
        self.system_date.setObjectName(u"system_date")

        self.gridLayout_5.addWidget(self.system_date, 4, 1, 1, 1)

        self.system_processor = QLabel(self.frame_2)
        self.system_processor.setObjectName(u"system_processor")

        self.gridLayout_5.addWidget(self.system_processor, 2, 3, 1, 1)

        self.system_machine = QLabel(self.frame_2)
        self.system_machine.setObjectName(u"system_machine")

        self.gridLayout_5.addWidget(self.system_machine, 3, 3, 1, 1)

        self.system_time = QLabel(self.frame_2)
        self.system_time.setObjectName(u"system_time")
        font4 = QFont()
        font4.setBold(False)
        self.system_time.setFont(font4)

        self.gridLayout_5.addWidget(self.system_time, 4, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.system_information)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_6 = QVBoxLayout(self.activities)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.activities)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_52 = QLabel(self.frame_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_52)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.activity_search = QLineEdit(self.frame_6)
        self.activity_search.setObjectName(u"activity_search")

        self.horizontalLayout_15.addWidget(self.activity_search)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon11)

        self.horizontalLayout_15.addWidget(self.pushButton_4)


        self.horizontalLayout_14.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.activities)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_16.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.activities)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_17.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_17.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_17.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_17.addWidget(self.pushButton_8)


        self.verticalLayout_6.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activities)
        self.stroage = QWidget()
        self.stroage.setObjectName(u"stroage")
        self.verticalLayout_8 = QVBoxLayout(self.stroage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_53 = QLabel(self.stroage)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)

        self.verticalLayout_8.addWidget(self.label_53)

        self.storageTable = QTableWidget(self.stroage)
        if (self.storageTable.columnCount() < 9):
            self.storageTable.setColumnCount(9)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        self.storageTable.setObjectName(u"storageTable")

        self.verticalLayout_8.addWidget(self.storageTable)

        self.stackedWidget.addWidget(self.stroage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_9 = QVBoxLayout(self.sensors)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_54 = QLabel(self.sensors)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)

        self.verticalLayout_9.addWidget(self.label_54)

        self.sensorTable = QTableWidget(self.sensors)
        if (self.sensorTable.columnCount() < 6):
            self.sensorTable.setColumnCount(6)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        self.sensorTable.setObjectName(u"sensorTable")

        self.verticalLayout_9.addWidget(self.sensorTable)

        self.stackedWidget.addWidget(self.sensors)
        self.networks = QWidget()
        self.networks.setObjectName(u"networks")
        self.verticalLayout_10 = QVBoxLayout(self.networks)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea = QScrollArea(self.networks)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 344, 460))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_56 = QLabel(self.frame_9)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_56)

        self.net_stats_table = QTableWidget(self.frame_9)
        if (self.net_stats_table.columnCount() < 5):
            self.net_stats_table.setColumnCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        self.net_stats_table.setObjectName(u"net_stats_table")
        self.net_stats_table.setMinimumSize(QSize(150, 0))

        self.verticalLayout_13.addWidget(self.net_stats_table)


        self.verticalLayout_11.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_55 = QLabel(self.frame_10)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)

        self.verticalLayout_14.addWidget(self.label_55)

        self.net_io_table = QTableWidget(self.frame_10)
        if (self.net_io_table.columnCount() < 9):
            self.net_io_table.setColumnCount(9)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(8, __qtablewidgetitem36)
        self.net_io_table.setObjectName(u"net_io_table")
        self.net_io_table.setMinimumSize(QSize(150, 0))

        self.verticalLayout_14.addWidget(self.net_io_table)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_57 = QLabel(self.frame_11)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_57)

        self.net_addresses_table = QTableWidget(self.frame_11)
        if (self.net_addresses_table.columnCount() < 6):
            self.net_addresses_table.setColumnCount(6)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        self.net_addresses_table.setObjectName(u"net_addresses_table")
        self.net_addresses_table.setMinimumSize(QSize(150, 0))

        self.verticalLayout_12.addWidget(self.net_addresses_table)


        self.verticalLayout_11.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_58 = QLabel(self.frame_12)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font3)

        self.verticalLayout_15.addWidget(self.label_58)

        self.net_connections_table = QTableWidget(self.frame_12)
        if (self.net_connections_table.columnCount() < 7):
            self.net_connections_table.setColumnCount(7)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(6, __qtablewidgetitem49)
        self.net_connections_table.setObjectName(u"net_connections_table")
        self.net_connections_table.setMinimumSize(QSize(150, 0))

        self.verticalLayout_15.addWidget(self.net_connections_table)


        self.verticalLayout_11.addWidget(self.frame_12)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.networks)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_12.addWidget(self.main_body_content)

        self.right_frame = QFrame(self.main_body_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.right_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_12 = QLabel(self.right_frame)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Help = QPushButton(self.right_frame)
        self.Help.setObjectName(u"Help")

        self.verticalLayout_2.addWidget(self.Help)


        self.horizontalLayout_12.addWidget(self.right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(95, 95, 95);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.footer_frame_2 = QFrame(self.footer_frame)
        self.footer_frame_2.setObjectName(u"footer_frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.footer_frame_2.sizePolicy().hasHeightForWidth())
        self.footer_frame_2.setSizePolicy(sizePolicy1)
        self.footer_frame_2.setStyleSheet(u"background-color: rgb(91, 91, 91);")
        self.footer_frame_2.setFrameShape(QFrame.NoFrame)
        self.footer_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.footer_frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.footer_left_frame_2 = QFrame(self.footer_frame_2)
        self.footer_left_frame_2.setObjectName(u"footer_left_frame_2")
        self.footer_left_frame_2.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.footer_left_frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.footer_left_frame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.footer_left_frame_2)

        self.footer_right_frame_2 = QFrame(self.footer_frame_2)
        self.footer_right_frame_2.setObjectName(u"footer_right_frame_2")
        self.footer_right_frame_2.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.footer_right_frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_3 = QPushButton(self.footer_right_frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_10.addWidget(self.pushButton_3, 0, Qt.AlignRight)

        self.size_grip_2 = QFrame(self.footer_right_frame_2)
        self.size_grip_2.setObjectName(u"size_grip_2")
        sizePolicy1.setHeightForWidth(self.size_grip_2.sizePolicy().hasHeightForWidth())
        self.size_grip_2.setSizePolicy(sizePolicy1)
        self.size_grip_2.setMinimumSize(QSize(10, 10))
        self.size_grip_2.setMaximumSize(QSize(10, 10))
        self.size_grip_2.setFrameShape(QFrame.StyledPanel)
        self.size_grip_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.size_grip_2, 0, Qt.AlignBottom)


        self.horizontalLayout_8.addWidget(self.footer_right_frame_2)


        self.horizontalLayout_11.addWidget(self.footer_frame_2)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"System Infother", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_info_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.battry_info_btn.setText("")
        self.system_info_btn.setText("")
        self.activity_info_btn.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.storage_info_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Stroages", None))
        self.sensors_info_btn.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.network_info_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Networks", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU count", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ram_usage_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Total RAM", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.avilable_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"USed RAM", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Avilable RAM", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Charger", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Plugged in", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.system_system.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.pushButton_4.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Suspand", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Suspand", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Termminate", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Disk Partation", None))
        ___qtablewidgetitem8 = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem9 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem10 = self.storageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem11 = self.storageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Max File", None));
        ___qtablewidgetitem12 = self.storageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem13 = self.storageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem14 = self.storageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem15 = self.storageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Free Storage", None));
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem16 = self.sensorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem17 = self.sensorTable.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem18 = self.sensorTable.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem19 = self.sensorTable.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem20 = self.sensorTable.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem21 = self.net_stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem22 = self.net_stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem23 = self.net_stats_table.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem24 = self.net_stats_table.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Network IO Counter", None))
        ___qtablewidgetitem25 = self.net_io_table.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem26 = self.net_io_table.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Bytes Sent", None));
        ___qtablewidgetitem27 = self.net_io_table.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Bytes Received", None));
        ___qtablewidgetitem28 = self.net_io_table.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Packets Sent", None));
        ___qtablewidgetitem29 = self.net_io_table.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Packets Received", None));
        ___qtablewidgetitem30 = self.net_io_table.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ERR In", None));
        ___qtablewidgetitem31 = self.net_io_table.horizontalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ERR Out", None));
        ___qtablewidgetitem32 = self.net_io_table.horizontalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Drop IN", None));
        ___qtablewidgetitem33 = self.net_io_table.horizontalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Network Address", None))
        ___qtablewidgetitem34 = self.net_addresses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem35 = self.net_addresses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem36 = self.net_addresses_table.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Netmask", None));
        ___qtablewidgetitem37 = self.net_addresses_table.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Broadcast", None));
        ___qtablewidgetitem38 = self.net_addresses_table.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        ___qtablewidgetitem39 = self.net_connections_table.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem40 = self.net_connections_table.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem41 = self.net_connections_table.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem42 = self.net_connections_table.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem43 = self.net_connections_table.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem44 = self.net_connections_table.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem45 = self.net_connections_table.horizontalHeaderItem(6)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"code and designed by Manish khanal", None))
        self.Help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"version 1.0.1 | copyright cybercode.", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

