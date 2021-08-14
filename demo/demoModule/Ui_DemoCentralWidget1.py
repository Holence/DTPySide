# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DemoCentralWidget1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DTPySide.DT_rc

class Ui_DemoCentralWidget1(object):
    def setupUi(self, DemoCentralWidget1):
        if not DemoCentralWidget1.objectName():
            DemoCentralWidget1.setObjectName(u"DemoCentralWidget1")
        DemoCentralWidget1.resize(400, 300)
        self.actionHello_World = QAction(DemoCentralWidget1)
        self.actionHello_World.setObjectName(u"actionHello_World")
        icon = QIcon()
        icon.addFile(u":/icons/icon/holoicon1.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHello_World.setIcon(icon)
        self.horizontalLayout = QHBoxLayout(DemoCentralWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.homelabel = QLabel(DemoCentralWidget1)
        self.homelabel.setObjectName(u"homelabel")
        font = QFont()
        font.setPointSize(24)
        self.homelabel.setFont(font)
        self.homelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.homelabel)


        self.retranslateUi(DemoCentralWidget1)

        QMetaObject.connectSlotsByName(DemoCentralWidget1)
    # setupUi

    def retranslateUi(self, DemoCentralWidget1):
        DemoCentralWidget1.setWindowTitle(QCoreApplication.translate("DemoCentralWidget1", u"DemoCentralWidget1", None))
        self.actionHello_World.setText(QCoreApplication.translate("DemoCentralWidget1", u"Hello World", None))
        self.homelabel.setText("")
    # retranslateUi

