# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTDialogWin32.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DTPySide.DTWidget.DTTitleBar import DTTitleBar


class Ui_DTDialogWin32(object):
    def setupUi(self, DTDialogWin32):
        if not DTDialogWin32.objectName():
            DTDialogWin32.setObjectName(u"DTDialogWin32")
        DTDialogWin32.resize(433, 314)
        DTDialogWin32.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(DTDialogWin32)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = DTTitleBar(DTDialogWin32)
        self.TitleBar.setObjectName(u"TitleBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar.sizePolicy().hasHeightForWidth())
        self.TitleBar.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.TitleBar)

        self.centralWidget = QHBoxLayout()
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setContentsMargins(41, 10, 32, 15)

        self.verticalLayout.addLayout(self.centralWidget)

        self.buttonBoxLayout = QHBoxLayout()
        self.buttonBoxLayout.setSpacing(0)
        self.buttonBoxLayout.setObjectName(u"buttonBoxLayout")
        self.buttonBoxLayout.setContentsMargins(-1, -1, 32, 25)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonBoxLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(DTDialogWin32)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        self.buttonBox.setLayoutDirection(Qt.RightToLeft)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.buttonBoxLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.buttonBoxLayout)


        self.retranslateUi(DTDialogWin32)
        self.buttonBox.accepted.connect(DTDialogWin32.accept)
        self.buttonBox.rejected.connect(DTDialogWin32.reject)

        QMetaObject.connectSlotsByName(DTDialogWin32)
    # setupUi

    def retranslateUi(self, DTDialogWin32):
        DTDialogWin32.setWindowTitle(QCoreApplication.translate("DTDialogWin32", u"DTDialog", None))
    # retranslateUi

