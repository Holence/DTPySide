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
        icon = QIcon()
        icon.addFile(u":/icon/white/white_settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSetting.setIcon(icon)
        self.actionExit = QAction(DTMainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/icon/white/white_log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionMaximize_Window = QAction(DTMainWindow)
        self.actionMaximize_Window.setObjectName(u"actionMaximize_Window")
        icon2 = QIcon()
        icon2.addFile(u":/icon/white/white_window-maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMaximize_Window.setIcon(icon2)
        self.actionNormalize_Window = QAction(DTMainWindow)
        self.actionNormalize_Window.setObjectName(u"actionNormalize_Window")
        icon3 = QIcon()
        icon3.addFile(u":/icon/white/white_window-restore.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNormalize_Window.setIcon(icon3)
        self.actionMinimize_Window = QAction(DTMainWindow)
        self.actionMinimize_Window.setObjectName(u"actionMinimize_Window")
        icon4 = QIcon()
        icon4.addFile(u":/icon/white/white_window-minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMinimize_Window.setIcon(icon4)
        self.actionWindow_Toggle_Stay_on_Top = QAction(DTMainWindow)
        self.actionWindow_Toggle_Stay_on_Top.setObjectName(u"actionWindow_Toggle_Stay_on_Top")
        icon5 = QIcon()
        icon5.addFile(u":/icon/white/white_arrow-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWindow_Toggle_Stay_on_Top.setIcon(icon5)
        self.actionWindow_Toggle_Fullscreen = QAction(DTMainWindow)
        self.actionWindow_Toggle_Fullscreen.setObjectName(u"actionWindow_Toggle_Fullscreen")
        icon6 = QIcon()
        icon6.addFile(u":/icon/white/white_maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWindow_Toggle_Fullscreen.setIcon(icon6)
        self.actionAbout = QAction(DTMainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon7 = QIcon()
        icon7.addFile(u":/icon/white/white_book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon7)
        self.actionBoss_Key = QAction(DTMainWindow)
        self.actionBoss_Key.setObjectName(u"actionBoss_Key")
        icon8 = QIcon()
        icon8.addFile(u":/icon/white/white_users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBoss_Key.setIcon(icon8)
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
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.statusBar.setFont(font)
        self.statusBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

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
        self.actionWindow_Toggle_Fullscreen.setText(QCoreApplication.translate("DTMainWindow", u"Window Toggle Fullscreen", None))
#if QT_CONFIG(shortcut)
        self.actionWindow_Toggle_Fullscreen.setShortcut(QCoreApplication.translate("DTMainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("DTMainWindow", u"About", None))
        self.actionBoss_Key.setText(QCoreApplication.translate("DTMainWindow", u"Boss Key", None))
#if QT_CONFIG(shortcut)
        self.actionBoss_Key.setShortcut(QCoreApplication.translate("DTMainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.statusBar.setText("")
    # retranslateUi

