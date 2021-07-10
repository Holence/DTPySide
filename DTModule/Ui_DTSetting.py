# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTSetting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DTPySide.DT_rc

class Ui_DTSetting(object):
    def setupUi(self, DTSetting):
        if not DTSetting.objectName():
            DTSetting.setObjectName(u"DTSetting")
        DTSetting.resize(734, 449)
        self.horizontalLayout = QHBoxLayout(DTSetting)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_buttons = QVBoxLayout()
        self.verticalLayout_buttons.setObjectName(u"verticalLayout_buttons")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_buttons.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_buttons)

        self.stackedWidget = QStackedWidget(DTSetting)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_basicinfo = QWidget()
        self.page_basicinfo.setObjectName(u"page_basicinfo")
        self.horizontalLayout_2 = QHBoxLayout(self.page_basicinfo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaBasicInfo = QScrollArea(self.page_basicinfo)
        self.scrollAreaBasicInfo.setObjectName(u"scrollAreaBasicInfo")
        self.scrollAreaBasicInfo.setFrameShape(QFrame.NoFrame)
        self.scrollAreaBasicInfo.setWidgetResizable(True)
        self.scrollAreaWidgetContentsBasicInfo = QWidget()
        self.scrollAreaWidgetContentsBasicInfo.setObjectName(u"scrollAreaWidgetContentsBasicInfo")
        self.scrollAreaWidgetContentsBasicInfo.setGeometry(QRect(0, 0, 706, 449))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContentsBasicInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 15, 0)
        self.pushButton_window_effect = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_window_effect.setObjectName(u"pushButton_window_effect")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_window_effect.sizePolicy().hasHeightForWidth())
        self.pushButton_window_effect.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_window_effect, 7, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 11, 1, 1, 1)

        self.pushButton_password = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_password.setObjectName(u"pushButton_password")
        sizePolicy.setHeightForWidth(self.pushButton_password.sizePolicy().hasHeightForWidth())
        self.pushButton_password.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_password, 1, 1, 1, 1)

        self.pushButton_theme = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_theme.setObjectName(u"pushButton_theme")
        sizePolicy.setHeightForWidth(self.pushButton_theme.sizePolicy().hasHeightForWidth())
        self.pushButton_theme.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_theme, 9, 1, 1, 1)

        self.lineEdit_font = QLineEdit(self.scrollAreaWidgetContentsBasicInfo)
        self.lineEdit_font.setObjectName(u"lineEdit_font")
        self.lineEdit_font.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_font, 3, 0, 1, 1)

        self.label_password = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 0, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.scrollAreaWidgetContentsBasicInfo)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 1, 0, 1, 1)

        self.label_font = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_font.setObjectName(u"label_font")

        self.gridLayout.addWidget(self.label_font, 2, 0, 1, 1)

        self.label_scale = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_scale.setObjectName(u"label_scale")

        self.gridLayout.addWidget(self.label_scale, 4, 0, 1, 1)

        self.label_window_effect = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_window_effect.setObjectName(u"label_window_effect")

        self.gridLayout.addWidget(self.label_window_effect, 6, 0, 1, 1)

        self.comboBox_window_effect = QComboBox(self.scrollAreaWidgetContentsBasicInfo)
        self.comboBox_window_effect.addItem("")
        self.comboBox_window_effect.addItem("")
        self.comboBox_window_effect.addItem("")
        self.comboBox_window_effect.setObjectName(u"comboBox_window_effect")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_window_effect.sizePolicy().hasHeightForWidth())
        self.comboBox_window_effect.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_window_effect, 7, 0, 1, 1)

        self.label_theme = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_theme.setObjectName(u"label_theme")

        self.gridLayout.addWidget(self.label_theme, 8, 0, 1, 1)

        self.comboBox_theme = QComboBox(self.scrollAreaWidgetContentsBasicInfo)
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.setObjectName(u"comboBox_theme")
        sizePolicy1.setHeightForWidth(self.comboBox_theme.sizePolicy().hasHeightForWidth())
        self.comboBox_theme.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_theme, 9, 0, 1, 1)

        self.pushButton_font = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_font.setObjectName(u"pushButton_font")
        sizePolicy.setHeightForWidth(self.pushButton_font.sizePolicy().hasHeightForWidth())
        self.pushButton_font.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_font, 3, 1, 1, 1)

        self.spinBox_scale = QDoubleSpinBox(self.scrollAreaWidgetContentsBasicInfo)
        self.spinBox_scale.setObjectName(u"spinBox_scale")
        self.spinBox_scale.setDecimals(1)
        self.spinBox_scale.setMinimum(1.000000000000000)
        self.spinBox_scale.setMaximum(10.000000000000000)
        self.spinBox_scale.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.spinBox_scale, 5, 0, 1, 1)

        self.pushButton_scale = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_scale.setObjectName(u"pushButton_scale")
        sizePolicy.setHeightForWidth(self.pushButton_scale.sizePolicy().hasHeightForWidth())
        self.pushButton_scale.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_scale, 5, 1, 1, 1)

        self.scrollAreaBasicInfo.setWidget(self.scrollAreaWidgetContentsBasicInfo)

        self.horizontalLayout_2.addWidget(self.scrollAreaBasicInfo)

        self.stackedWidget.addWidget(self.page_basicinfo)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(DTSetting)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DTSetting)
    # setupUi

    def retranslateUi(self, DTSetting):
        DTSetting.setWindowTitle(QCoreApplication.translate("DTSetting", u"DTSetting", None))
        self.pushButton_window_effect.setText(QCoreApplication.translate("DTSetting", u"Apply", None))
        self.pushButton_password.setText(QCoreApplication.translate("DTSetting", u"Apply", None))
        self.pushButton_theme.setText(QCoreApplication.translate("DTSetting", u"Apply", None))
        self.label_password.setText(QCoreApplication.translate("DTSetting", u"Password", None))
        self.label_font.setText(QCoreApplication.translate("DTSetting", u"Font (Recommended fontsize: [16,18])", None))
        self.label_scale.setText(QCoreApplication.translate("DTSetting", u"Scale (Change this according to your screen DPI)", None))
        self.label_window_effect.setText(QCoreApplication.translate("DTSetting", u"Window Effect", None))
        self.comboBox_window_effect.setItemText(0, QCoreApplication.translate("DTSetting", u"Normal", None))
        self.comboBox_window_effect.setItemText(1, QCoreApplication.translate("DTSetting", u"Aero", None))
        self.comboBox_window_effect.setItemText(2, QCoreApplication.translate("DTSetting", u"Acrylic", None))

        self.label_theme.setText(QCoreApplication.translate("DTSetting", u"Theme", None))
        self.comboBox_theme.setItemText(0, QCoreApplication.translate("DTSetting", u"Dracula", None))
        self.comboBox_theme.setItemText(1, QCoreApplication.translate("DTSetting", u"Dark", None))
        self.comboBox_theme.setItemText(2, QCoreApplication.translate("DTSetting", u"Light", None))

        self.pushButton_font.setText(QCoreApplication.translate("DTSetting", u"Font", None))
        self.pushButton_scale.setText(QCoreApplication.translate("DTSetting", u"Apply", None))
    # retranslateUi

