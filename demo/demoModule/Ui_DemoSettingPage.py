# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DemoSettingPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DemoSettingPage(object):
    def setupUi(self, DemoSettingPage):
        if not DemoSettingPage.objectName():
            DemoSettingPage.setObjectName(u"DemoSettingPage")
        DemoSettingPage.resize(483, 369)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 483, 369))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 15, 0)
        self.lineEdit_homelabel = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_homelabel.setObjectName(u"lineEdit_homelabel")

        self.gridLayout.addWidget(self.lineEdit_homelabel, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.label_homelabel = QLabel(self.scrollAreaWidgetContents)
        self.label_homelabel.setObjectName(u"label_homelabel")

        self.gridLayout.addWidget(self.label_homelabel, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        DemoSettingPage.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        DemoSettingPage.addWidget(self.page_2)

        self.retranslateUi(DemoSettingPage)

        QMetaObject.connectSlotsByName(DemoSettingPage)
    # setupUi

    def retranslateUi(self, DemoSettingPage):
        DemoSettingPage.setWindowTitle(QCoreApplication.translate("DemoSettingPage", u"DemoSettingPage", None))
        self.label_homelabel.setText(QCoreApplication.translate("DemoSettingPage", u"Home Label", None))
        self.label.setText(QCoreApplication.translate("DemoSettingPage", u"This is Custome Setting Page2.", None))
    # retranslateUi

