# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DemoCentralWidget2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DTPySide.DT_rc

class Ui_DemoCentralWidget2(object):
    def setupUi(self, DemoCentralWidget2):
        if not DemoCentralWidget2.objectName():
            DemoCentralWidget2.setObjectName(u"DemoCentralWidget2")
        DemoCentralWidget2.resize(400, 300)
        self.actionHello_World = QAction(DemoCentralWidget2)
        self.actionHello_World.setObjectName(u"actionHello_World")
        icon = QIcon()
        icon.addFile(u":/icons/icon/holoicon2.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHello_World.setIcon(icon)
        self.horizontalLayout = QHBoxLayout(DemoCentralWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.homelabel = QLabel(DemoCentralWidget2)
        self.homelabel.setObjectName(u"homelabel")
        self.homelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.homelabel)


        self.retranslateUi(DemoCentralWidget2)

        QMetaObject.connectSlotsByName(DemoCentralWidget2)
    # setupUi

    def retranslateUi(self, DemoCentralWidget2):
        DemoCentralWidget2.setWindowTitle(QCoreApplication.translate("DemoCentralWidget2", u"DemoCentralWidget2", None))
        self.actionHello_World.setText(QCoreApplication.translate("DemoCentralWidget2", u"Hello World", None))
        self.homelabel.setText("")
    # retranslateUi

