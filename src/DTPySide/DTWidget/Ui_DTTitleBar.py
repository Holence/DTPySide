# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTTitleBar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DTPySide.DT_rc

class Ui_DTTitleBar(object):
    def setupUi(self, DTTitleBar):
        if not DTTitleBar.objectName():
            DTTitleBar.setObjectName(u"DTTitleBar")
        DTTitleBar.resize(356, 42)
        DTTitleBar.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(DTTitleBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBarFrame = QFrame(DTTitleBar)
        self.TitleBarFrame.setObjectName(u"TitleBarFrame")
        self.TitleBarFrame.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.TitleBarFrame)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 3, 9, 3)
        self.title_icon = QPushButton(self.TitleBarFrame)
        self.title_icon.setObjectName(u"title_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_icon.sizePolicy().hasHeightForWidth())
        self.title_icon.setSizePolicy(sizePolicy)
        self.title_icon.setMinimumSize(QSize(36, 36))
        self.title_icon.setMaximumSize(QSize(36, 36))
        self.title_icon.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.title_icon)

        self.label_titlebar = QLabel(self.TitleBarFrame)
        self.label_titlebar.setObjectName(u"label_titlebar")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_titlebar.sizePolicy().hasHeightForWidth())
        self.label_titlebar.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_titlebar.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_titlebar)

        self.btn_minimize = QPushButton(self.TitleBarFrame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(24, 24))
        self.btn_minimize.setMaximumSize(QSize(24, 24))
        self.btn_minimize.setStyleSheet(u"")
        self.btn_minimize.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.TitleBarFrame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        sizePolicy.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy)
        self.btn_maximize.setMinimumSize(QSize(24, 24))
        self.btn_maximize.setMaximumSize(QSize(24, 24))
        self.btn_maximize.setStyleSheet(u"")
        self.btn_maximize.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.TitleBarFrame)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(24, 24))
        self.btn_close.setMaximumSize(QSize(24, 24))
        self.btn_close.setStyleSheet(u"")
        self.btn_close.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.TitleBarFrame)


        self.retranslateUi(DTTitleBar)

        QMetaObject.connectSlotsByName(DTTitleBar)
    # setupUi

    def retranslateUi(self, DTTitleBar):
        DTTitleBar.setWindowTitle(QCoreApplication.translate("DTTitleBar", u"DTTitleBar", None))
        self.label_titlebar.setText(QCoreApplication.translate("DTTitleBar", u"DT", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
    # retranslateUi

