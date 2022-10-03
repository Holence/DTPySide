# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DTPySide.DTWidget.DTTitleBar import DTTitleBar

import DTPySide.DT_rc

class Ui_DTMainWindow(object):
    def setupUi(self, DTMainWindow):
        if not DTMainWindow.objectName():
            DTMainWindow.setObjectName(u"DTMainWindow")
        DTMainWindow.resize(1278, 960)
        self.actionSetting = QAction(DTMainWindow)
        self.actionSetting.setObjectName(u"actionSetting")
        self.actionExit = QAction(DTMainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionMaximize_Window = QAction(DTMainWindow)
        self.actionMaximize_Window.setObjectName(u"actionMaximize_Window")
        self.actionNormalize_Window = QAction(DTMainWindow)
        self.actionNormalize_Window.setObjectName(u"actionNormalize_Window")
        self.actionMinimize_Window = QAction(DTMainWindow)
        self.actionMinimize_Window.setObjectName(u"actionMinimize_Window")
        self.actionWindow_Toggle_Stay_on_Top = QAction(DTMainWindow)
        self.actionWindow_Toggle_Stay_on_Top.setObjectName(u"actionWindow_Toggle_Stay_on_Top")
        self.actionWindow_Toggle_Fullscreen = QAction(DTMainWindow)
        self.actionWindow_Toggle_Fullscreen.setObjectName(u"actionWindow_Toggle_Fullscreen")
        self.actionAbout = QAction(DTMainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionBoss_Key = QAction(DTMainWindow)
        self.actionBoss_Key.setObjectName(u"actionBoss_Key")
        self.actionBackup = QAction(DTMainWindow)
        self.actionBackup.setObjectName(u"actionBackup")
        self.actionSecure_Mode = QAction(DTMainWindow)
        self.actionSecure_Mode.setObjectName(u"actionSecure_Mode")
        self.verticalLayout = QVBoxLayout(DTMainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = DTTitleBar(DTMainWindow)
        self.TitleBar.setObjectName(u"TitleBar")

        self.verticalLayout.addWidget(self.TitleBar)

        self.centralWidget = QFrame(DTMainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralwidget = QVBoxLayout(self.centralWidget)
        self.centralwidget.setSpacing(0)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.centralWidget)

        self.statusBar = QLabel(DTMainWindow)
        self.statusBar.setObjectName(u"statusBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy1)
        self.statusBar.setMinimumSize(QSize(0, 20))
        self.statusBar.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.statusBar)


        self.retranslateUi(DTMainWindow)

        QMetaObject.connectSlotsByName(DTMainWindow)
    # setupUi

    def retranslateUi(self, DTMainWindow):
        DTMainWindow.setWindowTitle(QCoreApplication.translate("DTMainWindow", u"DTMainWindow", None))
        self.actionSetting.setText(QCoreApplication.translate("DTMainWindow", u"Setting", None))
#if QT_CONFIG(tooltip)
        self.actionSetting.setToolTip(QCoreApplication.translate("DTMainWindow", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.actionExit.setText(QCoreApplication.translate("DTMainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("DTMainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionMaximize_Window.setText(QCoreApplication.translate("DTMainWindow", u"Maximize Window", None))
        self.actionNormalize_Window.setText(QCoreApplication.translate("DTMainWindow", u"Normalize Window", None))
        self.actionMinimize_Window.setText(QCoreApplication.translate("DTMainWindow", u"Minimize Window", None))
        self.actionWindow_Toggle_Stay_on_Top.setText(QCoreApplication.translate("DTMainWindow", u"Window Toggle Stay on Top", None))
#if QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Stay_on_Top.setShortcut(QCoreApplication.translate("DTMainWindow", u"F12", None))
#endif // QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Fullscreen.setText(QCoreApplication.translate("DTMainWindow", u"Window Toggle Fullscreen", None))
#if QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Fullscreen.setShortcut(QCoreApplication.translate("DTMainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("DTMainWindow", u"About", None))
        self.actionBoss_Key.setText(QCoreApplication.translate("DTMainWindow", u"Boss Key", None))
#if QT_CONFIG(shortcut)
        self.actionBoss_Key.setShortcut(QCoreApplication.translate("DTMainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionBackup.setText(QCoreApplication.translate("DTMainWindow", u"Backup", None))
        self.actionSecure_Mode.setText(QCoreApplication.translate("DTMainWindow", u"Secure Mode", None))
#if QT_CONFIG(tooltip)
        self.actionSecure_Mode.setToolTip(QCoreApplication.translate("DTMainWindow", u"If turned on, open window from tray icon will need password.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

