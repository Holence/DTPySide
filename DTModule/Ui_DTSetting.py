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

from DTPySide.DTWidget.DTApplyButton import DTApplyButton

import DTPySide.DT_rc

class Ui_DTSetting(object):
    def setupUi(self, DTSetting):
        if not DTSetting.objectName():
            DTSetting.setObjectName(u"DTSetting")
        DTSetting.resize(760, 529)
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
        self.scrollAreaWidgetContentsBasicInfo.setGeometry(QRect(0, 0, 732, 529))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContentsBasicInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 15, 0)
        self.pushButton_country = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_country.setObjectName(u"pushButton_country")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_country.sizePolicy().hasHeightForWidth())
        self.pushButton_country.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_country, 15, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 16, 1, 1, 1)

        self.label_country = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_country.setObjectName(u"label_country")

        self.gridLayout.addWidget(self.label_country, 14, 0, 1, 1)

        self.pushButton_password = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_password.setObjectName(u"pushButton_password")
        sizePolicy.setHeightForWidth(self.pushButton_password.sizePolicy().hasHeightForWidth())
        self.pushButton_password.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_password, 1, 1, 1, 1)

        self.pushButton_theme = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_theme.setObjectName(u"pushButton_theme")
        sizePolicy.setHeightForWidth(self.pushButton_theme.sizePolicy().hasHeightForWidth())
        self.pushButton_theme.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_theme, 11, 1, 1, 1)

        self.pushButton_font = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_font.setObjectName(u"pushButton_font")
        sizePolicy.setHeightForWidth(self.pushButton_font.sizePolicy().hasHeightForWidth())
        self.pushButton_font.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_font, 5, 1, 1, 1)

        self.label_password = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 0, 0, 1, 1)

        self.label_scale = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_scale.setObjectName(u"label_scale")

        self.gridLayout.addWidget(self.label_scale, 6, 0, 1, 1)

        self.pushButton_window_effect = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_window_effect.setObjectName(u"pushButton_window_effect")
        sizePolicy.setHeightForWidth(self.pushButton_window_effect.sizePolicy().hasHeightForWidth())
        self.pushButton_window_effect.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_window_effect, 9, 1, 1, 1)

        self.pushButton_scale = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_scale.setObjectName(u"pushButton_scale")
        sizePolicy.setHeightForWidth(self.pushButton_scale.sizePolicy().hasHeightForWidth())
        self.pushButton_scale.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_scale, 7, 1, 1, 1)

        self.lineEdit_backup = QLineEdit(self.scrollAreaWidgetContentsBasicInfo)
        self.lineEdit_backup.setObjectName(u"lineEdit_backup")
        self.lineEdit_backup.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_backup, 3, 0, 1, 1)

        self.lineEdit_font = QLineEdit(self.scrollAreaWidgetContentsBasicInfo)
        self.lineEdit_font.setObjectName(u"lineEdit_font")
        self.lineEdit_font.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_font, 5, 0, 1, 1)

        self.label_language = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_language.setObjectName(u"label_language")

        self.gridLayout.addWidget(self.label_language, 12, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.scrollAreaWidgetContentsBasicInfo)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 1, 0, 1, 1)

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

        self.gridLayout.addWidget(self.comboBox_window_effect, 9, 0, 1, 1)

        self.pushButton_language = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_language.setObjectName(u"pushButton_language")
        sizePolicy.setHeightForWidth(self.pushButton_language.sizePolicy().hasHeightForWidth())
        self.pushButton_language.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_language, 13, 1, 1, 1)

        self.comboBox_language = QComboBox(self.scrollAreaWidgetContentsBasicInfo)
        self.comboBox_language.setObjectName(u"comboBox_language")
        sizePolicy1.setHeightForWidth(self.comboBox_language.sizePolicy().hasHeightForWidth())
        self.comboBox_language.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_language, 13, 0, 1, 1)

        self.label_theme = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_theme.setObjectName(u"label_theme")

        self.gridLayout.addWidget(self.label_theme, 10, 0, 1, 1)

        self.pushButton_backup = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_backup.setObjectName(u"pushButton_backup")
        sizePolicy.setHeightForWidth(self.pushButton_backup.sizePolicy().hasHeightForWidth())
        self.pushButton_backup.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_backup, 3, 1, 1, 1)

        self.comboBox_theme = QComboBox(self.scrollAreaWidgetContentsBasicInfo)
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.setObjectName(u"comboBox_theme")
        sizePolicy1.setHeightForWidth(self.comboBox_theme.sizePolicy().hasHeightForWidth())
        self.comboBox_theme.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_theme, 11, 0, 1, 1)

        self.label_window_effect = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_window_effect.setObjectName(u"label_window_effect")

        self.gridLayout.addWidget(self.label_window_effect, 8, 0, 1, 1)

        self.comboBox_country = QComboBox(self.scrollAreaWidgetContentsBasicInfo)
        self.comboBox_country.setObjectName(u"comboBox_country")
        sizePolicy1.setHeightForWidth(self.comboBox_country.sizePolicy().hasHeightForWidth())
        self.comboBox_country.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_country, 15, 0, 1, 1)

        self.label_font = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_font.setObjectName(u"label_font")

        self.gridLayout.addWidget(self.label_font, 4, 0, 1, 1)

        self.spinBox_scale = QDoubleSpinBox(self.scrollAreaWidgetContentsBasicInfo)
        self.spinBox_scale.setObjectName(u"spinBox_scale")
        self.spinBox_scale.setDecimals(1)
        self.spinBox_scale.setMinimum(1.000000000000000)
        self.spinBox_scale.setMaximum(10.000000000000000)
        self.spinBox_scale.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.spinBox_scale, 7, 0, 1, 1)

        self.label_backup = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_backup.setObjectName(u"label_backup")

        self.gridLayout.addWidget(self.label_backup, 2, 0, 1, 1)

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
        self.label_country.setText(QCoreApplication.translate("DTSetting", u"Country", None))
        self.label_password.setText(QCoreApplication.translate("DTSetting", u"Password", None))
        self.label_scale.setText(QCoreApplication.translate("DTSetting", u"Scale (Change this according to your screen DPI)", None))
        self.label_language.setText(QCoreApplication.translate("DTSetting", u"Language", None))
        self.comboBox_window_effect.setItemText(0, QCoreApplication.translate("DTSetting", u"Normal", None))
        self.comboBox_window_effect.setItemText(1, QCoreApplication.translate("DTSetting", u"Aero", None))
        self.comboBox_window_effect.setItemText(2, QCoreApplication.translate("DTSetting", u"Acrylic", None))

        self.label_theme.setText(QCoreApplication.translate("DTSetting", u"Theme", None))
        self.comboBox_theme.setItemText(0, QCoreApplication.translate("DTSetting", u"Dracula", None))
        self.comboBox_theme.setItemText(1, QCoreApplication.translate("DTSetting", u"Dark", None))
        self.comboBox_theme.setItemText(2, QCoreApplication.translate("DTSetting", u"Light", None))

        self.label_window_effect.setText(QCoreApplication.translate("DTSetting", u"Window Effect", None))
        self.label_font.setText(QCoreApplication.translate("DTSetting", u"Font (font-size is fixed)", None))
        self.label_backup.setText(QCoreApplication.translate("DTSetting", u"Backup Dst", None))
    # retranslateUi

