# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ModuleDongliTeahouseSetting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DongliTeahousePySideWheel.DongliTeahouse_rc

class Ui_Module_DongliTeahouseSetting(object):
    def setupUi(self, Module_DongliTeahouseSetting):
        if not Module_DongliTeahouseSetting.objectName():
            Module_DongliTeahouseSetting.setObjectName(u"Module_DongliTeahouseSetting")
        Module_DongliTeahouseSetting.resize(538, 383)
        self.horizontalLayout = QHBoxLayout(Module_DongliTeahouseSetting)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget_buttons = QListWidget(Module_DongliTeahouseSetting)
        self.listWidget_buttons.setObjectName(u"listWidget_buttons")
        self.listWidget_buttons.setMinimumSize(QSize(36, 0))
        self.listWidget_buttons.setMaximumSize(QSize(36, 16777215))
        self.listWidget_buttons.setStyleSheet(u"QListWidget {background: transparent;}")
        self.listWidget_buttons.setFrameShape(QFrame.NoFrame)
        self.listWidget_buttons.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_buttons.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_buttons.setProperty("showDropIndicator", False)
        self.listWidget_buttons.setDefaultDropAction(Qt.CopyAction)
        self.listWidget_buttons.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget_buttons.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget_buttons.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_buttons.setSpacing(3)

        self.horizontalLayout.addWidget(self.listWidget_buttons)

        self.stackedWidget = QStackedWidget(Module_DongliTeahouseSetting)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_basicinfo = QWidget()
        self.page_basicinfo.setObjectName(u"page_basicinfo")
        self.gridLayout = QGridLayout(self.page_basicinfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_password = QLineEdit(self.page_basicinfo)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 1, 0, 1, 1)

        self.pushButton_password = QPushButton(self.page_basicinfo)
        self.pushButton_password.setObjectName(u"pushButton_password")

        self.gridLayout.addWidget(self.pushButton_password, 1, 1, 1, 1)

        self.label_font = QLabel(self.page_basicinfo)
        self.label_font.setObjectName(u"label_font")

        self.gridLayout.addWidget(self.label_font, 2, 0, 1, 1)

        self.lineEdit_font = QLineEdit(self.page_basicinfo)
        self.lineEdit_font.setObjectName(u"lineEdit_font")
        self.lineEdit_font.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_font, 3, 0, 1, 1)

        self.label_password = QLabel(self.page_basicinfo)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 0, 0, 1, 1)

        self.pushButton_font = QPushButton(self.page_basicinfo)
        self.pushButton_font.setObjectName(u"pushButton_font")

        self.gridLayout.addWidget(self.pushButton_font, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_basicinfo)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Module_DongliTeahouseSetting)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Module_DongliTeahouseSetting)
    # setupUi

    def retranslateUi(self, Module_DongliTeahouseSetting):
        Module_DongliTeahouseSetting.setWindowTitle(QCoreApplication.translate("Module_DongliTeahouseSetting", u"Module_DongliTeahouseSetting", None))
        self.pushButton_password.setText(QCoreApplication.translate("Module_DongliTeahouseSetting", u"Apply", None))
        self.label_font.setText(QCoreApplication.translate("Module_DongliTeahouseSetting", u"Font", None))
        self.label_password.setText(QCoreApplication.translate("Module_DongliTeahouseSetting", u"Password", None))
        self.pushButton_font.setText(QCoreApplication.translate("Module_DongliTeahouseSetting", u"Font", None))
    # retranslateUi

