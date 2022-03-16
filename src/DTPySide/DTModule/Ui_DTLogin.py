# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTLogin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DTPySide.DT_rc

class Ui_DTLogin(object):
    def setupUi(self, DTLogin):
        if not DTLogin.objectName():
            DTLogin.setObjectName(u"DTLogin")
        DTLogin.resize(221, 50)
        self.horizontalLayout = QHBoxLayout(DTLogin)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 10, 0, 15)
        self.label_lock = QLabel(DTLogin)
        self.label_lock.setObjectName(u"label_lock")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lock.sizePolicy().hasHeightForWidth())
        self.label_lock.setSizePolicy(sizePolicy)
        self.label_lock.setMinimumSize(QSize(28, 28))
        self.label_lock.setMaximumSize(QSize(28, 28))
        self.label_lock.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_lock)

        self.lineEdit = QLineEdit(DTLogin)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(180, 26))
        self.lineEdit.setMaximumSize(QSize(16777215, 28))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.retranslateUi(DTLogin)

        QMetaObject.connectSlotsByName(DTLogin)
    # setupUi

    def retranslateUi(self, DTLogin):
        DTLogin.setWindowTitle(QCoreApplication.translate("DTLogin", u"DTLogin", None))
        self.label_lock.setText("")
        self.lineEdit.setText("")
    # retranslateUi

