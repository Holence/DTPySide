# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTMessageBox.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DTPySide.DT_rc

class Ui_DTMessageBox(object):
    def setupUi(self, DTMessageBox):
        if not DTMessageBox.objectName():
            DTMessageBox.setObjectName(u"DTMessageBox")
        DTMessageBox.resize(528, 123)
        self.horizontalLayout = QHBoxLayout(DTMessageBox)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_icon = QLabel(DTMessageBox)
        self.label_icon.setObjectName(u"label_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy)
        self.label_icon.setMinimumSize(QSize(64, 64))
        self.label_icon.setMaximumSize(QSize(64, 64))
        self.label_icon.setScaledContents(True)
        self.label_icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_icon)

        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_text = QLabel(DTMessageBox)
        self.label_text.setObjectName(u"label_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_text.sizePolicy().hasHeightForWidth())
        self.label_text.setSizePolicy(sizePolicy1)
        self.label_text.setMinimumSize(QSize(0, 0))
        self.label_text.setTextFormat(Qt.AutoText)
        self.label_text.setScaledContents(False)
        self.label_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_text.setWordWrap(True)
        self.label_text.setMargin(0)
        self.label_text.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_2.addWidget(self.label_text)

        self.textBrowser = QTextBrowser(DTMessageBox)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(400, 50))

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(DTMessageBox)

        QMetaObject.connectSlotsByName(DTMessageBox)
    # setupUi

    def retranslateUi(self, DTMessageBox):
        DTMessageBox.setWindowTitle(QCoreApplication.translate("DTMessageBox", u"DTMessageBox", None))
        self.label_icon.setText("")
        self.label_text.setText("")
    # retranslateUi

