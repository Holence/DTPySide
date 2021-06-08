# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Module_DongliTeahouseLogin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DongliTeahousePySideWheel.DongliTeahouse_rc

class Ui_Module_DongliTeahouseLogin(object):
    def setupUi(self, Module_DongliTeahouseLogin):
        if not Module_DongliTeahouseLogin.objectName():
            Module_DongliTeahouseLogin.setObjectName(u"Module_DongliTeahouseLogin")
        Module_DongliTeahouseLogin.resize(207, 38)
        self.horizontalLayout = QHBoxLayout(Module_DongliTeahouseLogin)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 10, 0, 0)
        self.label = QLabel(Module_DongliTeahouseLogin)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(28, 28))
        self.label.setPixmap(QPixmap(u":/white/white_lock.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Module_DongliTeahouseLogin)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(165, 24))
        font = QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.retranslateUi(Module_DongliTeahouseLogin)

        QMetaObject.connectSlotsByName(Module_DongliTeahouseLogin)
    # setupUi

    def retranslateUi(self, Module_DongliTeahouseLogin):
        Module_DongliTeahouseLogin.setWindowTitle(QCoreApplication.translate("Module_DongliTeahouseLogin", u"Module_DongliTeahouseLogin", None))
        self.label.setText("")
    # retranslateUi

