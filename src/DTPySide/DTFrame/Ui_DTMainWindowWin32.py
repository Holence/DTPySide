# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTMainWindowWin32.ui'
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

class Ui_DTMainWindowWin32(object):
    def setupUi(self, DTMainWindowWin32):
        if not DTMainWindowWin32.objectName():
            DTMainWindowWin32.setObjectName(u"DTMainWindowWin32")
        DTMainWindowWin32.resize(1278, 960)
        self.actionSetting = QAction(DTMainWindowWin32)
        self.actionSetting.setObjectName(u"actionSetting")
        self.actionExit = QAction(DTMainWindowWin32)
        self.actionExit.setObjectName(u"actionExit")
        self.actionMaximize_Window = QAction(DTMainWindowWin32)
        self.actionMaximize_Window.setObjectName(u"actionMaximize_Window")
        self.actionNormalize_Window = QAction(DTMainWindowWin32)
        self.actionNormalize_Window.setObjectName(u"actionNormalize_Window")
        self.actionMinimize_Window = QAction(DTMainWindowWin32)
        self.actionMinimize_Window.setObjectName(u"actionMinimize_Window")
        self.actionWindow_Toggle_Stay_on_Top = QAction(DTMainWindowWin32)
        self.actionWindow_Toggle_Stay_on_Top.setObjectName(u"actionWindow_Toggle_Stay_on_Top")
        self.actionWindow_Toggle_Fullscreen = QAction(DTMainWindowWin32)
        self.actionWindow_Toggle_Fullscreen.setObjectName(u"actionWindow_Toggle_Fullscreen")
        self.actionAbout = QAction(DTMainWindowWin32)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionBoss_Key = QAction(DTMainWindowWin32)
        self.actionBoss_Key.setObjectName(u"actionBoss_Key")
        self.actionBackup = QAction(DTMainWindowWin32)
        self.actionBackup.setObjectName(u"actionBackup")
        self.actionSecure_Mode = QAction(DTMainWindowWin32)
        self.actionSecure_Mode.setObjectName(u"actionSecure_Mode")
        self.verticalLayout = QVBoxLayout(DTMainWindowWin32)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = DTTitleBar(DTMainWindowWin32)
        self.TitleBar.setObjectName(u"TitleBar")

        self.verticalLayout.addWidget(self.TitleBar)

        self.centralWidget = QFrame(DTMainWindowWin32)
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

        self.statusBar = QLabel(DTMainWindowWin32)
        self.statusBar.setObjectName(u"statusBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy1)
        self.statusBar.setMinimumSize(QSize(0, 20))
        self.statusBar.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.statusBar)


        self.retranslateUi(DTMainWindowWin32)

        QMetaObject.connectSlotsByName(DTMainWindowWin32)
    # setupUi

    def retranslateUi(self, DTMainWindowWin32):
        DTMainWindowWin32.setWindowTitle(QCoreApplication.translate("DTMainWindowWin32", u"DTMainWindow", None))
        self.actionSetting.setText(QCoreApplication.translate("DTMainWindowWin32", u"Setting", None))
#if QT_CONFIG(tooltip)
        self.actionSetting.setToolTip(QCoreApplication.translate("DTMainWindowWin32", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.actionExit.setText(QCoreApplication.translate("DTMainWindowWin32", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("DTMainWindowWin32", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionMaximize_Window.setText(QCoreApplication.translate("DTMainWindowWin32", u"Maximize Window", None))
        self.actionNormalize_Window.setText(QCoreApplication.translate("DTMainWindowWin32", u"Normalize Window", None))
        self.actionMinimize_Window.setText(QCoreApplication.translate("DTMainWindowWin32", u"Minimize Window", None))
        self.actionWindow_Toggle_Stay_on_Top.setText(QCoreApplication.translate("DTMainWindowWin32", u"Window Toggle Stay on Top", None))
#if QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Stay_on_Top.setShortcut(QCoreApplication.translate("DTMainWindowWin32", u"F12", None))
#endif // QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Fullscreen.setText(QCoreApplication.translate("DTMainWindowWin32", u"Window Toggle Fullscreen", None))
#if QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Fullscreen.setShortcut(QCoreApplication.translate("DTMainWindowWin32", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("DTMainWindowWin32", u"About", None))
        self.actionBoss_Key.setText(QCoreApplication.translate("DTMainWindowWin32", u"Boss Key", None))
#if QT_CONFIG(shortcut)
        self.actionBoss_Key.setShortcut(QCoreApplication.translate("DTMainWindowWin32", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionBackup.setText(QCoreApplication.translate("DTMainWindowWin32", u"Backup", None))
        self.actionSecure_Mode.setText(QCoreApplication.translate("DTMainWindowWin32", u"Secure Mode", None))
#if QT_CONFIG(tooltip)
        self.actionSecure_Mode.setToolTip(QCoreApplication.translate("DTMainWindowWin32", u"If turned on, open window from tray icon will need password.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

