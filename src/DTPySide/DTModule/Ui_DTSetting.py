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
from DTPySide.DTWidget import LazyCombobox

import DTPySide.DT_rc

class Ui_DTSetting(object):
    def setupUi(self, DTSetting):
        if not DTSetting.objectName():
            DTSetting.setObjectName(u"DTSetting")
        DTSetting.resize(1008, 730)
        self.horizontalLayout = QHBoxLayout(DTSetting)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_buttons = QVBoxLayout()
        self.verticalLayout_buttons.setObjectName(u"verticalLayout_buttons")
        self.verticalSpacer_buttons = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_buttons.addItem(self.verticalSpacer_buttons)


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
        self.scrollAreaWidgetContentsBasicInfo.setGeometry(QRect(0, 0, 980, 730))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContentsBasicInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 15, 0)
        self.verticalLayout_color = QVBoxLayout()
        self.verticalLayout_color.setSpacing(0)
        self.verticalLayout_color.setObjectName(u"verticalLayout_color")
        self.verticalLayout_color.setContentsMargins(-1, 34, -1, 5)
        self.label_color_preview = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_color_preview.setObjectName(u"label_color_preview")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_color_preview.sizePolicy().hasHeightForWidth())
        self.label_color_preview.setSizePolicy(sizePolicy)
        self.label_color_preview.setMinimumSize(QSize(26, 26))
        self.label_color_preview.setMaximumSize(QSize(26, 26))
        self.label_color_preview.setAlignment(Qt.AlignCenter)

        self.verticalLayout_color.addWidget(self.label_color_preview)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_color.addItem(self.verticalSpacer_2)

        self.pushButton_color = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_color.setObjectName(u"pushButton_color")
        sizePolicy.setHeightForWidth(self.pushButton_color.sizePolicy().hasHeightForWidth())
        self.pushButton_color.setSizePolicy(sizePolicy)

        self.verticalLayout_color.addWidget(self.pushButton_color)


        self.gridLayout.addLayout(self.verticalLayout_color, 16, 1, 1, 1)

        self.pushButton_scale = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_scale.setObjectName(u"pushButton_scale")
        sizePolicy.setHeightForWidth(self.pushButton_scale.sizePolicy().hasHeightForWidth())
        self.pushButton_scale.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_scale, 11, 1, 1, 1)

        self.label_font = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_font.setObjectName(u"label_font")

        self.gridLayout.addWidget(self.label_font, 8, 0, 1, 1)

        self.lineEdit_data_dir = QLineEdit(self.scrollAreaWidgetContentsBasicInfo)
        self.lineEdit_data_dir.setObjectName(u"lineEdit_data_dir")
        self.lineEdit_data_dir.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_data_dir, 5, 0, 1, 1)

        self.label_window_effect = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_window_effect.setObjectName(u"label_window_effect")

        self.gridLayout.addWidget(self.label_window_effect, 12, 0, 1, 1)

        self.label_backup = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_backup.setObjectName(u"label_backup")

        self.gridLayout.addWidget(self.label_backup, 6, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.scrollAreaWidgetContentsBasicInfo)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 1, 0, 1, 1)

        self.label_data_dir = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_data_dir.setObjectName(u"label_data_dir")

        self.gridLayout.addWidget(self.label_data_dir, 4, 0, 1, 1)

        self.comboBox_theme = LazyCombobox(self.scrollAreaWidgetContentsBasicInfo)
        self.comboBox_theme.setObjectName(u"comboBox_theme")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_theme.sizePolicy().hasHeightForWidth())
        self.comboBox_theme.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_theme, 15, 0, 1, 1)

        self.label_theme = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_theme.setObjectName(u"label_theme")

        self.gridLayout.addWidget(self.label_theme, 14, 0, 1, 1)

        self.pushButton_backup = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_backup.setObjectName(u"pushButton_backup")
        sizePolicy.setHeightForWidth(self.pushButton_backup.sizePolicy().hasHeightForWidth())
        self.pushButton_backup.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_backup, 7, 1, 1, 1)

        self.spinBox_scale = QDoubleSpinBox(self.scrollAreaWidgetContentsBasicInfo)
        self.spinBox_scale.setObjectName(u"spinBox_scale")
        self.spinBox_scale.setDecimals(1)
        self.spinBox_scale.setMinimum(1.000000000000000)
        self.spinBox_scale.setMaximum(10.000000000000000)
        self.spinBox_scale.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.spinBox_scale, 11, 0, 1, 1)

        self.pushButton_data_dir = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_data_dir.setObjectName(u"pushButton_data_dir")
        sizePolicy.setHeightForWidth(self.pushButton_data_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_data_dir.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_data_dir, 5, 1, 1, 1)

        self.comboBox_window_effect = LazyCombobox(self.scrollAreaWidgetContentsBasicInfo)
        self.comboBox_window_effect.addItem("")
        self.comboBox_window_effect.addItem("")
        self.comboBox_window_effect.addItem("")
        self.comboBox_window_effect.setObjectName(u"comboBox_window_effect")
        sizePolicy1.setHeightForWidth(self.comboBox_window_effect.sizePolicy().hasHeightForWidth())
        self.comboBox_window_effect.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_window_effect, 13, 0, 1, 1)

        self.label_language = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_language.setObjectName(u"label_language")

        self.gridLayout.addWidget(self.label_language, 17, 0, 1, 1)

        self.label_country = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_country.setObjectName(u"label_country")

        self.gridLayout.addWidget(self.label_country, 19, 0, 1, 1)

        self.comboBox_language = LazyCombobox(self.scrollAreaWidgetContentsBasicInfo)
        self.comboBox_language.setObjectName(u"comboBox_language")
        sizePolicy1.setHeightForWidth(self.comboBox_language.sizePolicy().hasHeightForWidth())
        self.comboBox_language.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_language, 18, 0, 1, 1)

        self.label_iteration = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_iteration.setObjectName(u"label_iteration")

        self.gridLayout.addWidget(self.label_iteration, 2, 0, 1, 1)

        self.comboBox_country = LazyCombobox(self.scrollAreaWidgetContentsBasicInfo)
        self.comboBox_country.setObjectName(u"comboBox_country")
        sizePolicy1.setHeightForWidth(self.comboBox_country.sizePolicy().hasHeightForWidth())
        self.comboBox_country.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_country, 20, 0, 1, 1)

        self.lineEdit_backup = QLineEdit(self.scrollAreaWidgetContentsBasicInfo)
        self.lineEdit_backup.setObjectName(u"lineEdit_backup")
        self.lineEdit_backup.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_backup, 7, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 4, 3, 1, 1)

        self.label_contrast = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_contrast.setObjectName(u"label_contrast")

        self.gridLayout_2.addWidget(self.label_contrast, 6, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 6, 3, 1, 1)

        self.slider_Hue = QSlider(self.scrollAreaWidgetContentsBasicInfo)
        self.slider_Hue.setObjectName(u"slider_Hue")
        self.slider_Hue.setMaximum(360)
        self.slider_Hue.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider_Hue, 1, 1, 1, 3)

        self.slider_contrast = QSlider(self.scrollAreaWidgetContentsBasicInfo)
        self.slider_contrast.setObjectName(u"slider_contrast")
        self.slider_contrast.setMaximum(500)
        self.slider_contrast.setPageStep(1)
        self.slider_contrast.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider_contrast, 7, 1, 1, 3)

        self.slider_saturation = QSlider(self.scrollAreaWidgetContentsBasicInfo)
        self.slider_saturation.setObjectName(u"slider_saturation")
        self.slider_saturation.setMaximum(500)
        self.slider_saturation.setPageStep(1)
        self.slider_saturation.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider_saturation, 3, 1, 1, 3)

        self.label_luminance = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_luminance.setObjectName(u"label_luminance")

        self.gridLayout_2.addWidget(self.label_luminance, 4, 1, 1, 1)

        self.pushButton_hue_reset = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_hue_reset.setObjectName(u"pushButton_hue_reset")
        sizePolicy.setHeightForWidth(self.pushButton_hue_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_hue_reset.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pushButton_hue_reset, 0, 2, 1, 1)

        self.pushButton_luminance_reset = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_luminance_reset.setObjectName(u"pushButton_luminance_reset")
        sizePolicy.setHeightForWidth(self.pushButton_luminance_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_luminance_reset.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pushButton_luminance_reset, 4, 2, 1, 1)

        self.pushButton_saturation_reset = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_saturation_reset.setObjectName(u"pushButton_saturation_reset")
        sizePolicy.setHeightForWidth(self.pushButton_saturation_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_saturation_reset.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pushButton_saturation_reset, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.slider_luminance = QSlider(self.scrollAreaWidgetContentsBasicInfo)
        self.slider_luminance.setObjectName(u"slider_luminance")
        self.slider_luminance.setMaximum(500)
        self.slider_luminance.setPageStep(1)
        self.slider_luminance.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider_luminance, 5, 1, 1, 3)

        self.label_saturation = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_saturation.setObjectName(u"label_saturation")

        self.gridLayout_2.addWidget(self.label_saturation, 2, 1, 1, 1)

        self.label_hue = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_hue.setObjectName(u"label_hue")

        self.gridLayout_2.addWidget(self.label_hue, 0, 1, 1, 1)

        self.pushButton_contrast_reset = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_contrast_reset.setObjectName(u"pushButton_contrast_reset")
        sizePolicy.setHeightForWidth(self.pushButton_contrast_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_contrast_reset.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pushButton_contrast_reset, 6, 2, 1, 1)

        self.checkBox_reverse = QCheckBox(self.scrollAreaWidgetContentsBasicInfo)
        self.checkBox_reverse.setObjectName(u"checkBox_reverse")

        self.gridLayout_2.addWidget(self.checkBox_reverse, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 16, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 21, 1, 1, 1)

        self.label_scale = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_scale.setObjectName(u"label_scale")

        self.gridLayout.addWidget(self.label_scale, 10, 0, 1, 1)

        self.label_password = QLabel(self.scrollAreaWidgetContentsBasicInfo)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 0, 0, 1, 1)

        self.pushButton_font = QPushButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_font.setObjectName(u"pushButton_font")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_font.sizePolicy().hasHeightForWidth())
        self.pushButton_font.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_font, 9, 0, 1, 1)

        self.spinBox_iteration = QSpinBox(self.scrollAreaWidgetContentsBasicInfo)
        self.spinBox_iteration.setObjectName(u"spinBox_iteration")
        self.spinBox_iteration.setMinimum(1)
        self.spinBox_iteration.setMaximum(1000000000)
        self.spinBox_iteration.setSingleStep(10000)
        self.spinBox_iteration.setValue(48000)

        self.gridLayout.addWidget(self.spinBox_iteration, 3, 0, 1, 1)

        self.pushButton_iteration = DTApplyButton(self.scrollAreaWidgetContentsBasicInfo)
        self.pushButton_iteration.setObjectName(u"pushButton_iteration")
        sizePolicy.setHeightForWidth(self.pushButton_iteration.sizePolicy().hasHeightForWidth())
        self.pushButton_iteration.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_iteration, 3, 1, 1, 1)

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
        self.label_color_preview.setText("")
        self.label_font.setText(QCoreApplication.translate("DTSetting", u"Font (font-size is fixed)", None))
        self.label_window_effect.setText(QCoreApplication.translate("DTSetting", u"Window Effect", None))
        self.label_backup.setText(QCoreApplication.translate("DTSetting", u"Backup Dst", None))
        self.label_data_dir.setText(QCoreApplication.translate("DTSetting", u"Data Dir", None))
        self.label_theme.setText(QCoreApplication.translate("DTSetting", u"Theme", None))
        self.comboBox_window_effect.setItemText(0, QCoreApplication.translate("DTSetting", u"Normal", None))
        self.comboBox_window_effect.setItemText(1, QCoreApplication.translate("DTSetting", u"Aero", None))
        self.comboBox_window_effect.setItemText(2, QCoreApplication.translate("DTSetting", u"Acrylic", None))

        self.label_language.setText(QCoreApplication.translate("DTSetting", u"Language", None))
        self.label_country.setText(QCoreApplication.translate("DTSetting", u"Country", None))
        self.label_iteration.setText(QCoreApplication.translate("DTSetting", u"Iteration", None))
        self.label_contrast.setText(QCoreApplication.translate("DTSetting", u"Contrast", None))
        self.label_luminance.setText(QCoreApplication.translate("DTSetting", u"Luminance", None))
        self.pushButton_hue_reset.setText("")
        self.pushButton_luminance_reset.setText("")
        self.pushButton_saturation_reset.setText("")
        self.label_saturation.setText(QCoreApplication.translate("DTSetting", u"Saturation", None))
        self.label_hue.setText(QCoreApplication.translate("DTSetting", u"Hue", None))
        self.pushButton_contrast_reset.setText("")
        self.checkBox_reverse.setText(QCoreApplication.translate("DTSetting", u"Reverse", None))
        self.label_scale.setText(QCoreApplication.translate("DTSetting", u"Scale (Change this according to your screen DPI)", None))
        self.label_password.setText(QCoreApplication.translate("DTSetting", u"Password", None))
    # retranslateUi

