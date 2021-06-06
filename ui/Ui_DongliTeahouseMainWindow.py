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
        font.setFamily(u"Hack")
        font.setPointSize(11)
        DongliTeahouseMainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/holoico_trans.ico", QSize(), QIcon.Normal, QIcon.Off)
        DongliTeahouseMainWindow.setWindowIcon(icon)
        self.actionSettings = QAction(DongliTeahouseMainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        icon1 = QIcon()
        icon1.addFile(u":/white/white_settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionExit = QAction(DongliTeahouseMainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        icon2.addFile(u":/white/white_log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionMaximize_Window = QAction(DongliTeahouseMainWindow)
        self.actionMaximize_Window.setObjectName(u"actionMaximize_Window")
        icon3 = QIcon()
        icon3.addFile(u":/white/white_window-maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMaximize_Window.setIcon(icon3)
        self.actionNormalize_Window = QAction(DongliTeahouseMainWindow)
        self.actionNormalize_Window.setObjectName(u"actionNormalize_Window")
        icon4 = QIcon()
        icon4.addFile(u":/white/white_window-restore.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNormalize_Window.setIcon(icon4)
        self.actionMinimize_Window = QAction(DongliTeahouseMainWindow)
        self.actionMinimize_Window.setObjectName(u"actionMinimize_Window")
        icon5 = QIcon()
        icon5.addFile(u":/white/white_window-minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMinimize_Window.setIcon(icon5)
        self.actionWindow_Toggle_Stay_on_Top = QAction(DongliTeahouseMainWindow)
        self.actionWindow_Toggle_Stay_on_Top.setObjectName(u"actionWindow_Toggle_Stay_on_Top")
        icon6 = QIcon()
        icon6.addFile(u":/white/white_arrow-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWindow_Toggle_Stay_on_Top.setIcon(icon6)
        self.actionWindow_Toggle_Fullscreen = QAction(DongliTeahouseMainWindow)
        self.actionWindow_Toggle_Fullscreen.setObjectName(u"actionWindow_Toggle_Fullscreen")
        icon7 = QIcon()
        icon7.addFile(u":/white/white_maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWindow_Toggle_Fullscreen.setIcon(icon7)
        self.actionAbout = QAction(DongliTeahouseMainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon8 = QIcon()
        icon8.addFile(u":/white/white_book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon8)
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
        self.actionSettings.setText(QCoreApplication.translate("DongliTeahouseMainWindow", u"Settings", None))
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
    # retranslateUi

