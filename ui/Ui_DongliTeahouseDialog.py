# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DongliTeahouseDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DongliTeahousePySideWheel.DongliTeahouseTemplate import DongliTeahouseTitleBarCut


class Ui_DongliTeahouseDialog(object):
    def setupUi(self, DongliTeahouseDialog):
        if not DongliTeahouseDialog.objectName():
            DongliTeahouseDialog.setObjectName(u"DongliTeahouseDialog")
        DongliTeahouseDialog.resize(655, 500)
        DongliTeahouseDialog.setMinimumSize(QSize(600, 500))
        font = QFont()
        font.setFamily(u"Hack")
        font.setPointSize(11)
        DongliTeahouseDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(DongliTeahouseDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = DongliTeahouseTitleBarCut(DongliTeahouseDialog)
        self.TitleBar.setObjectName(u"TitleBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar.sizePolicy().hasHeightForWidth())
        self.TitleBar.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.TitleBar)

        self.centralWidget = QVBoxLayout()
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setContentsMargins(50, 20, 32, 30)

        self.verticalLayout.addLayout(self.centralWidget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.SizeGrip = QFrame(DongliTeahouseDialog)
        self.SizeGrip.setObjectName(u"SizeGrip")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SizeGrip.sizePolicy().hasHeightForWidth())
        self.SizeGrip.setSizePolicy(sizePolicy1)
        self.SizeGrip.setMinimumSize(QSize(16, 16))
        self.SizeGrip.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.SizeGrip, 1, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(DongliTeahouseDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Hack")
        font1.setPointSize(9)
        self.buttonBox.setFont(font1)
        self.buttonBox.setLayoutDirection(Qt.RightToLeft)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(DongliTeahouseDialog)
        self.buttonBox.accepted.connect(DongliTeahouseDialog.accept)
        self.buttonBox.rejected.connect(DongliTeahouseDialog.reject)

        QMetaObject.connectSlotsByName(DongliTeahouseDialog)
    # setupUi

    def retranslateUi(self, DongliTeahouseDialog):
        DongliTeahouseDialog.setWindowTitle(QCoreApplication.translate("DongliTeahouseDialog", u"DongliTeahouseDialog", None))
    # retranslateUi

