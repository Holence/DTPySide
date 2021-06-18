# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DongliTeahouseLogin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DongliTeahousePySideWheel.DongliTeahouse_rc

class Ui_DongliTeahouseLogin(object):
    def setupUi(self, DongliTeahouseLogin):
        if not DongliTeahouseLogin.objectName():
            DongliTeahouseLogin.setObjectName(u"DongliTeahouseLogin")
        DongliTeahouseLogin.resize(207, 38)
        self.horizontalLayout = QHBoxLayout(DongliTeahouseLogin)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 10, 0, 0)
        self.label = QLabel(DongliTeahouseLogin)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(28, 28))
        self.label.setPixmap(QPixmap(u":/icon/white/white_lock.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(DongliTeahouseLogin)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(165, 24))
        font = QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.retranslateUi(DongliTeahouseLogin)

        QMetaObject.connectSlotsByName(DongliTeahouseLogin)
    # setupUi

    def retranslateUi(self, DongliTeahouseLogin):
        DongliTeahouseLogin.setWindowTitle(QCoreApplication.translate("DongliTeahouseLogin", u"DongliTeahouseLogin", None))
        self.label.setText("")
    # retranslateUi

