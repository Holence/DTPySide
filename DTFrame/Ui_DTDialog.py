# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DTPySide.DTWidget.DTTitleBarCut import DTTitleBarCut


class Ui_DTDialog(object):
    def setupUi(self, DTDialog):
        if not DTDialog.objectName():
            DTDialog.setObjectName(u"DTDialog")
        DTDialog.resize(433, 332)
        DTDialog.setMinimumSize(QSize(0, 0))
        DTDialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(DTDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = DTTitleBarCut(DTDialog)
        self.TitleBar.setObjectName(u"TitleBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar.sizePolicy().hasHeightForWidth())
        self.TitleBar.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.TitleBar)

        self.centralWidget = QVBoxLayout()
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setContentsMargins(8, 10, 32, 25)

        self.verticalLayout.addLayout(self.centralWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 32, 25)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(DTDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Hack")
        font.setPointSize(9)
        self.buttonBox.setFont(font)
        self.buttonBox.setLayoutDirection(Qt.RightToLeft)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DTDialog)
        self.buttonBox.accepted.connect(DTDialog.accept)
        self.buttonBox.rejected.connect(DTDialog.reject)

        QMetaObject.connectSlotsByName(DTDialog)
    # setupUi

    def retranslateUi(self, DTDialog):
        DTDialog.setWindowTitle(QCoreApplication.translate("DTDialog", u"DTDialog", None))
    # retranslateUi

