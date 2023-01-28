from __future__ import annotations
from DTPySide import *

# Mainwindow
from DTPySide.DTFrame.Ui_DTMainWindowLinux import Ui_DTMainWindowLinux
class DTMainWindowLinux(Ui_DTMainWindowLinux,DTWidget.DTWindow):
	"DTMainWindow骨架，通过setCentralWidget来放入主功能区"
	
	def __init__(self, app:DTAPP):
		super().__init__(app)
		self.setupUi(self)
		self.app=app
		self._MainMenu=QMenu(self)
	
	def initialize(self):
		self.initializeWindow()
		self.initializeSignal()
		self.initializeMenu()

	def initializeWindow(self):
		self.setWindowTitle(self.app.applicationName())

		self.actionSetting.setIcon(IconFromCurrentTheme("settings.svg"))
		self.actionExit.setIcon(IconFromCurrentTheme("log-out.svg"))
		self.actionMaximize_Window.setIcon(IconFromCurrentTheme("window-maximize.svg"))
		self.actionNormalize_Window.setIcon(IconFromCurrentTheme("window-restore.svg"))
		self.actionMinimize_Window.setIcon(IconFromCurrentTheme("window-minimize.svg"))
		self.actionWindow_Toggle_Stay_on_Top.setIcon(IconFromCurrentTheme("arrow-up.svg"))
		self.actionWindow_Toggle_Fullscreen.setIcon(IconFromCurrentTheme("maximize.svg"))
		self.actionAbout.setIcon(IconFromCurrentTheme("book.svg"))
		self.actionBoss_Key.setIcon(IconFromCurrentTheme("users.svg"))
		self.actionBackup.setIcon(IconFromCurrentTheme("cloud.svg"))
		self.actionSecure_Mode.setIcon(IconFromCurrentTheme("toggle-left.svg"))
	
	def initializeSignal(self):	
		"""主窗体的action向function链接
		注意：需要拥有全局快捷键的action，需要addAction
		"""
		
		def slot():
			self._MainMenu.exec_(self.centralWidget.mapToGlobal(self.centralWidget.pos()))
		self.actionShowMenu=QAction("Show Menu")
		self.actionShowMenu.setShortcut("Ctrl+M")
		self.actionShowMenu.triggered.connect(slot)
		self.addAction(self.actionShowMenu)
	
		self.actionWindow_Toggle_Fullscreen.triggered.connect(self.windowToggleFullscreen)
		self.addAction(self.actionWindow_Toggle_Fullscreen)

		self.actionWindow_Toggle_Stay_on_Top.triggered.connect(self.windowToggleStayonTop)
		self.addAction(self.actionWindow_Toggle_Stay_on_Top)

		self.actionNormalize_Window.triggered.connect(self.windowShowNormal)
		self.actionMaximize_Window.triggered.connect(self.showMaximized)
		self.actionMinimize_Window.triggered.connect(self.showMinimized)

		self.actionExit.triggered.connect(self.close)
		self.addAction(self.actionExit)

	def initializeMenu(self):
		"制定menu"
		
		self.__menu_view=QMenu(QCoreApplication.translate("DTMainWindow","View"),self) #这里不能用self.tr，因为如果被继承了，这里的self将会是子类，而在qm翻译文件的context中记录的是DTMainSWindow的翻译
		self.__menu_view.setIcon(IconFromCurrentTheme("eye.svg"))
		self.__menu_view.addAction(self.actionWindow_Toggle_Stay_on_Top)
		self.__menu_view.addAction(self.actionWindow_Toggle_Fullscreen)
		self.__menu_view.addAction(self.actionNormalize_Window)
		self.__menu_view.addAction(self.actionMinimize_Window)
		self.__menu_view.addAction(self.actionMaximize_Window)
		self.addMenuToMainMenu(self.__menu_view)

		self.addActionToMainMenu(self.actionExit)
	
	def MainMenu(self):
		return self._MainMenu
	
	def addSeparatorToMainMenu(self):
		self._MainMenu.addSeparator()
	
	def insertSeparatorToMainMenu(self, fore_action):
		self._MainMenu.insertSeparator(fore_action)

	def addActionToMainMenu(self,action):
		self._MainMenu.addAction(action)
	
	def insertActionToMainMenu(self,fore_action,action):
		self._MainMenu.insertAction(fore_action,action)
	
	def addMenuToMainMenu(self,menu):
		self._MainMenu.addMenu(menu)
	
	def insertMenuToMainMenu(self,fore_action,menu):
		self._MainMenu.insertMenu(fore_action,menu)
	
	def windowShowNormal(self):
		self.showNormal()
		self.resize(self.minimumWidth(),self.minimumHeight())
		MoveToCenterOfScreen(self)

	def windowToggleStayonTop(self):
		"切换主窗体的置顶与否"

		if bool(self.windowFlags() & Qt.WindowStaysOnTopHint):
			self.setWindowFlag(Qt.WindowStaysOnTopHint,False)
			# 貌似设置了置顶后缩放就侦测不到了，手动重置一下
			self.reInitialize()
		else:
			self.setWindowFlag(Qt.WindowStaysOnTopHint,True)
		
		if self.isFullScreen():
			self.showFullScreen()
		else:
			self.show()
		
	
	def windowToggleFullscreen(self):
		"切换主窗体的全屏与否"
		
		if self.isFullScreen():
			self.showNormal()
		else:
			self.showFullScreen()
	
	def setStatusTip(self, tip:str):
		self.statusBar.setText(tip)
	
	def password(self):
		return self.app.password()
	
	def setPassword(self,password):
		self.app.setPassword(password)
	
	def iteration(self):
		return self.app.iteration()
	
	def setIteration(self,iteration):
		self.app.setIteration(iteration)
	
	def UserSetting(self):
		return self.app.UserSetting()

	def setCentralWidget(self,widget):
		
		self.centralwidget.addWidget(widget,Qt.AlignCenter)