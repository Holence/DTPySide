# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTDialogLinux.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DTDialogLinux(object):
    def setupUi(self, DTDialogLinux):
        if not DTDialogLinux.objectName():
            DTDialogLinux.setObjectName(u"DTDialogLinux")
        DTDialogLinux.resize(433, 314)
        DTDialogLinux.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(DTDialogLinux)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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

        self.buttonBox = QDialogButtonBox(DTDialogLinux)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setLayoutDirection(Qt.RightToLeft)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.buttonBoxLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.buttonBoxLayout)


        self.retranslateUi(DTDialogLinux)
        self.buttonBox.accepted.connect(DTDialogLinux.accept)
        self.buttonBox.rejected.connect(DTDialogLinux.reject)

        QMetaObject.connectSlotsByName(DTDialogLinux)
    # setupUi

    def retranslateUi(self, DTDialogLinux):
        DTDialogLinux.setWindowTitle(QCoreApplication.translate("DTDialogLinux", u"DTDialog", None))
    # retranslateUi

