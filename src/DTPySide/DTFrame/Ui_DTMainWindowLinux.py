# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTMainWindowLinux.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DTPySide.DT_rc

class Ui_DTMainWindowLinux(object):
    def setupUi(self, DTMainWindowLinux):
        if not DTMainWindowLinux.objectName():
            DTMainWindowLinux.setObjectName(u"DTMainWindowLinux")
        DTMainWindowLinux.resize(1278, 960)
        self.actionSetting = QAction(DTMainWindowLinux)
        self.actionSetting.setObjectName(u"actionSetting")
        self.actionExit = QAction(DTMainWindowLinux)
        self.actionExit.setObjectName(u"actionExit")
        self.actionMaximize_Window = QAction(DTMainWindowLinux)
        self.actionMaximize_Window.setObjectName(u"actionMaximize_Window")
        self.actionNormalize_Window = QAction(DTMainWindowLinux)
        self.actionNormalize_Window.setObjectName(u"actionNormalize_Window")
        self.actionMinimize_Window = QAction(DTMainWindowLinux)
        self.actionMinimize_Window.setObjectName(u"actionMinimize_Window")
        self.actionWindow_Toggle_Stay_on_Top = QAction(DTMainWindowLinux)
        self.actionWindow_Toggle_Stay_on_Top.setObjectName(u"actionWindow_Toggle_Stay_on_Top")
        self.actionWindow_Toggle_Fullscreen = QAction(DTMainWindowLinux)
        self.actionWindow_Toggle_Fullscreen.setObjectName(u"actionWindow_Toggle_Fullscreen")
        self.actionAbout = QAction(DTMainWindowLinux)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionBoss_Key = QAction(DTMainWindowLinux)
        self.actionBoss_Key.setObjectName(u"actionBoss_Key")
        self.actionBackup = QAction(DTMainWindowLinux)
        self.actionBackup.setObjectName(u"actionBackup")
        self.actionSecure_Mode = QAction(DTMainWindowLinux)
        self.actionSecure_Mode.setObjectName(u"actionSecure_Mode")
        self.verticalLayout = QVBoxLayout(DTMainWindowLinux)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralWidget = QFrame(DTMainWindowLinux)
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

        self.statusBar = QLabel(DTMainWindowLinux)
        self.statusBar.setObjectName(u"statusBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy1)
        self.statusBar.setMinimumSize(QSize(0, 20))
        self.statusBar.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.statusBar)


        self.retranslateUi(DTMainWindowLinux)

        QMetaObject.connectSlotsByName(DTMainWindowLinux)
    # setupUi

    def retranslateUi(self, DTMainWindowLinux):
        DTMainWindowLinux.setWindowTitle(QCoreApplication.translate("DTMainWindowLinux", u"DTMainWindow", None))
        self.actionSetting.setText(QCoreApplication.translate("DTMainWindowLinux", u"Setting", None))
#if QT_CONFIG(tooltip)
        self.actionSetting.setToolTip(QCoreApplication.translate("DTMainWindowLinux", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.actionExit.setText(QCoreApplication.translate("DTMainWindowLinux", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("DTMainWindowLinux", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionMaximize_Window.setText(QCoreApplication.translate("DTMainWindowLinux", u"Maximize Window", None))
        self.actionNormalize_Window.setText(QCoreApplication.translate("DTMainWindowLinux", u"Normalize Window", None))
        self.actionMinimize_Window.setText(QCoreApplication.translate("DTMainWindowLinux", u"Minimize Window", None))
        self.actionWindow_Toggle_Stay_on_Top.setText(QCoreApplication.translate("DTMainWindowLinux", u"Window Toggle Stay on Top", None))
#if QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Stay_on_Top.setShortcut(QCoreApplication.translate("DTMainWindowLinux", u"F12", None))
#endif // QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Fullscreen.setText(QCoreApplication.translate("DTMainWindowLinux", u"Window Toggle Fullscreen", None))
#if QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Fullscreen.setShortcut(QCoreApplication.translate("DTMainWindowLinux", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("DTMainWindowLinux", u"About", None))
        self.actionBoss_Key.setText(QCoreApplication.translate("DTMainWindowLinux", u"Boss Key", None))
#if QT_CONFIG(shortcut)
        self.actionBoss_Key.setShortcut(QCoreApplication.translate("DTMainWindowLinux", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionBackup.setText(QCoreApplication.translate("DTMainWindowLinux", u"Backup", None))
        self.actionSecure_Mode.setText(QCoreApplication.translate("DTMainWindowLinux", u"Secure Mode", None))
#if QT_CONFIG(tooltip)
        self.actionSecure_Mode.setToolTip(QCoreApplication.translate("DTMainWindowLinux", u"If turned on, open window from tray icon will need password.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

