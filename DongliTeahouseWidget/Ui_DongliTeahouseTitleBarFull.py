# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DongliTeahouseTitleBarFull.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DongliTeahousePySideWheel.DongliTeahouseWidget.DongliTeahouseTitleLabel import DongliTeahouseTitleLabel

import DongliTeahousePySideWheel.DongliTeahouse_rc

class Ui_DongliTeahouseTitleBarFull(object):
    def setupUi(self, DongliTeahouseTitleBarFull):
        if not DongliTeahouseTitleBarFull.objectName():
            DongliTeahouseTitleBarFull.setObjectName(u"DongliTeahouseTitleBarFull")
        DongliTeahouseTitleBarFull.resize(414, 38)
        DongliTeahouseTitleBarFull.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(40,40,40);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(30,30,30);\n"
"}")
        self.horizontalLayout = QHBoxLayout(DongliTeahouseTitleBarFull)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 2, 8, 0)
        self.btn_menu = QPushButton(DongliTeahouseTitleBarFull)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QSize(36, 36))
        self.btn_menu.setMaximumSize(QSize(36, 36))
        self.btn_menu.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/holoico_trans.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(36, 36))

        self.horizontalLayout.addWidget(self.btn_menu)

        self.label_titlebar = DongliTeahouseTitleLabel(DongliTeahouseTitleBarFull)
        self.label_titlebar.setObjectName(u"label_titlebar")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_titlebar.sizePolicy().hasHeightForWidth())
        self.label_titlebar.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_titlebar.setFont(font)
        self.label_titlebar.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_titlebar)

        self.btn_minimize = QPushButton(DongliTeahouseTitleBarFull)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(24, 24))
        self.btn_minimize.setMaximumSize(QSize(24, 24))
        self.btn_minimize.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/white/white_window-minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(DongliTeahouseTitleBarFull)
        self.btn_maximize.setObjectName(u"btn_maximize")
        sizePolicy.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy)
        self.btn_maximize.setMinimumSize(QSize(24, 24))
        self.btn_maximize.setMaximumSize(QSize(24, 24))
        self.btn_maximize.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/white/white_window-maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon2)
        self.btn_maximize.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(DongliTeahouseTitleBarFull)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(24, 24))
        self.btn_close.setMaximumSize(QSize(24, 24))
        self.btn_close.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/white/white_x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)
        self.btn_close.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_close)


        self.retranslateUi(DongliTeahouseTitleBarFull)

        QMetaObject.connectSlotsByName(DongliTeahouseTitleBarFull)
    # setupUi

    def retranslateUi(self, DongliTeahouseTitleBarFull):
        DongliTeahouseTitleBarFull.setWindowTitle(QCoreApplication.translate("DongliTeahouseTitleBarFull", u"Form", None))
        self.btn_menu.setText("")
        self.label_titlebar.setText(QCoreApplication.translate("DongliTeahouseTitleBarFull", u"DongliTeahouse", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
    # retranslateUi

