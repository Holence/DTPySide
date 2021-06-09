# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DongliTeahouseMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DongliTeahousePySideWheel.DongliTeahouse_rc

class Ui_DongliTeahouseMainWindow(object):
    def setupUi(self, DongliTeahouseMainWindow):
        if not DongliTeahouseMainWindow.objectName():
            DongliTeahouseMainWindow.setObjectName(u"DongliTeahouseMainWindow")
        DongliTeahouseMainWindow.resize(1280, 960)
        DongliTeahouseMainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamily(u"1529 Champ Fleury Pro")
        DongliTeahouseMainWindow.setFont(font)
        self.actionSetting = QAction(DongliTeahouseMainWindow)
        self.actionSetting.setObjectName(u"actionSetting")
        icon = QIcon()
        icon.addFile(u":/white/white_settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSetting.setIcon(icon)
        self.actionExit = QAction(DongliTeahouseMainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/white/white_log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionMaximize_Window = QAction(DongliTeahouseMainWindow)
        self.actionMaximize_Window.setObjectName(u"actionMaximize_Window")
        icon2 = QIcon()
        icon2.addFile(u":/white/white_window-maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMaximize_Window.setIcon(icon2)
        self.actionNormalize_Window = QAction(DongliTeahouseMainWindow)
        self.actionNormalize_Window.setObjectName(u"actionNormalize_Window")
        icon3 = QIcon()
        icon3.addFile(u":/white/white_window-restore.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNormalize_Window.setIcon(icon3)
        self.actionMinimize_Window = QAction(DongliTeahouseMainWindow)
        self.actionMinimize_Window.setObjectName(u"actionMinimize_Window")
        icon4 = QIcon()
        icon4.addFile(u":/white/white_window-minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMinimize_Window.setIcon(icon4)
        self.actionWindow_Toggle_Stay_on_Top = QAction(DongliTeahouseMainWindow)
        self.actionWindow_Toggle_Stay_on_Top.setObjectName(u"actionWindow_Toggle_Stay_on_Top")
        icon5 = QIcon()
        icon5.addFile(u":/white/white_arrow-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWindow_Toggle_Stay_on_Top.setIcon(icon5)
        self.actionWindow_Toggle_Fullscreen = QAction(DongliTeahouseMainWindow)
        self.actionWindow_Toggle_Fullscreen.setObjectName(u"actionWindow_Toggle_Fullscreen")
        icon6 = QIcon()
        icon6.addFile(u":/white/white_maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWindow_Toggle_Fullscreen.setIcon(icon6)
        self.actionAbout = QAction(DongliTeahouseMainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon7 = QIcon()
        icon7.addFile(u":/white/white_book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon7)
        self.actionBoss_Key = QAction(DongliTeahouseMainWindow)
        self.actionBoss_Key.setObjectName(u"actionBoss_Key")
        icon8 = QIcon()
        icon8.addFile(u":/white/white_users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBoss_Key.setIcon(icon8)
        self.centralwidget = QWidget(DongliTeahouseMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        DongliTeahouseMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(DongliTeahouseMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        DongliTeahouseMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DongliTeahouseMainWindow)

        QMetaObject.connectSlotsByName(DongliTeahouseMainWindow)
    # setupUi

    def retranslateUi(self, DongliTeahouseMainWindow):
        DongliTeahouseMainWindow.setWindowTitle(QCoreApplication.translate("DongliTeahouseMainWindow", u"DongliTeahouseMainWindow", None))
        self.actionSetting.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"Setting", None))
#if QT_CONFIG(tooltip)
        self.actionSetting.setToolTip(QCoreApplication.translate("DongliTeahouseMainWindow", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.actionExit.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("DongliTeahouseMainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionMaximize_Window.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"Maximize Window", None))
        self.actionNormalize_Window.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"Normalize Window", None))
        self.actionMinimize_Window.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"Minimize Window", None))
        self.actionWindow_Toggle_Stay_on_Top.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"Window Toggle Stay on Top", None))
        self.actionWindow_Toggle_Fullscreen.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"Window Toggle Fullscreen", None))
#if QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Fullscreen.setShortcut(QCoreApplication.translate("DongliTeahouseMainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"About", None))
        self.actionBoss_Key.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"Boss Key", None))
#if QT_CONFIG(shortcut)
        self.actionBoss_Key.setShortcut(QCoreApplication.translate("DongliTeahouseMainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

