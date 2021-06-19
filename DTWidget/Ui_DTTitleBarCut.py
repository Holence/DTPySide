# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTTitleBarCut.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DTPySide.DTWidget.DTTitleLabel import DTTitleLabel

import DTPySide.DT_rc

class Ui_DTTitleBarCut(object):
    def setupUi(self, DTTitleBarCut):
        if not DTTitleBarCut.objectName():
            DTTitleBarCut.setObjectName(u"DTTitleBarCut")
        DTTitleBarCut.resize(405, 40)
        DTTitleBarCut.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(DTTitleBarCut)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBarFrame = QFrame(DTTitleBarCut)
        self.TitleBarFrame.setObjectName(u"TitleBarFrame")
        self.TitleBarFrame.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.TitleBarFrame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 3, 8, 3)
        self.title_icon = QPushButton(self.TitleBarFrame)
        self.title_icon.setObjectName(u"title_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_icon.sizePolicy().hasHeightForWidth())
        self.title_icon.setSizePolicy(sizePolicy)
        self.title_icon.setMinimumSize(QSize(36, 36))
        self.title_icon.setMaximumSize(QSize(36, 36))
        self.title_icon.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/holoicon1.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.title_icon.setIcon(icon)
        self.title_icon.setIconSize(QSize(36, 36))

        self.horizontalLayout_2.addWidget(self.title_icon)

        self.label_titlebar = DTTitleLabel(self.TitleBarFrame)
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

        self.horizontalLayout_2.addWidget(self.label_titlebar)

        self.btn_close = QPushButton(self.TitleBarFrame)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(24, 24))
        self.btn_close.setMaximumSize(QSize(24, 24))
        self.btn_close.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/white/white_x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.TitleBarFrame)


        self.retranslateUi(DTTitleBarCut)

        QMetaObject.connectSlotsByName(DTTitleBarCut)
    # setupUi

    def retranslateUi(self, DTTitleBarCut):
        DTTitleBarCut.setWindowTitle(QCoreApplication.translate("DTTitleBarCut", u"Form", None))
        self.title_icon.setText("")
        self.label_titlebar.setText(QCoreApplication.translate("DTTitleBarCut", u"DT", None))
        self.btn_close.setText("")
    # retranslateUi

