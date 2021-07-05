from DTPySide.DTFunction import *

from DTPySide.DTWidget import DTWindow

# Mainwindow
from DTPySide.DTFrame.Ui_DTMainWindow import Ui_DTMainWindow
class DTMainWindow(Ui_DTMainWindow,DTWindow):
	"DTMainWindow骨架，通过setCentralWidget来放入主功能区"
	
	def __init__(self,app):
		super().__init__()
		self.app=app
		self._MainMenu=QMenu(self)

		self.setupUi(self)
		
		self.TitleBar.setFull(True)
		self.setWindowTitle(self.UserSetting().value("MetaData/ApplicationName"))

	def initialize(self):
		self.initializeWindow()
		self.restoreWindowStatus()

		self.initializeSignal()
		self.initializeMenu()

	def initializeWindow(self):
		
		pass
	
	def restoreWindowStatus(self):
		pass
	
	def initializeSignal(self):	
		"""主窗体的action向function链接
		注意：需要拥有全局快捷键的action，需要addAction
		"""
		self.actionWindow_Toggle_Fullscreen.triggered.connect(self.windowToggleFullscreen)
		self.addAction(self.actionWindow_Toggle_Fullscreen)

		self.actionWindow_Toggle_Stay_on_Top.triggered.connect(self.windowToggleStayonTop)
		self.actionNormalize_Window.triggered.connect(self.windowShowNormal)
		self.actionMaximize_Window.triggered.connect(self.showMaximized)
		self.actionMinimize_Window.triggered.connect(self.showMinimized)

		self.actionExit.triggered.connect(self.close)
		self.addAction(self.actionExit)

	def initializeMenu(self):
		"制定menu"
		
		self._MainMenu.addAction(self.actionWindow_Toggle_Fullscreen)
		self._MainMenu.addAction(self.actionWindow_Toggle_Stay_on_Top)
		self._MainMenu.addAction(self.actionNormalize_Window)
		self._MainMenu.addAction(self.actionMinimize_Window)
		self._MainMenu.addAction(self.actionMaximize_Window)
		self._MainMenu.addSeparator()

		################################################################
		
		self._MainMenu.addAction(self.actionExit)
	
	def MainMenu(self):
		return self._MainMenu
	
	def addSeparatorToMainMenu(self):
		self._MainMenu.addSeparator()

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
		self.setGeometry(self.x(),self.y(),1200,900)

	def windowToggleStayonTop(self):
		"切换主窗体的置顶与否"

		if bool(self.windowFlags() & Qt.WindowStaysOnTopHint):
			self.setWindowFlag(Qt.WindowStaysOnTopHint,False)
		else:
			self.setWindowFlag(Qt.WindowStaysOnTopHint,True)
		
		if self.isFullScreen():
			self.showFullScreen()
		else:
			self.showNormal()
	
	def windowToggleFullscreen(self):
		"切换主窗体的全屏与否"

		if self.isFullScreen():
			self.showNormal()
			self.TitleBar.btn_maximize.show()
			self.TitleBar.btn_minimize.show()
		else:
			self.showFullScreen()
			self.TitleBar.btn_maximize.hide()
			self.TitleBar.btn_minimize.hide()

	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		try:
			self.TitleBar.setWindowTitle(title)
		except:
			pass

	def password(self):
		return self.app.password()
	
	def setPassword(self,password):
		self.app.setPassword(password)
	
	def UserSetting(self):
		return self.app.UserSetting



	def setCentralWidget(self,widget):
		# 奶奶的，这里本来偷懒，在ui文件中用了一个QWidget占位
		# 这里就写了self.centralwidget=widget直接暴力替换
		# 结果把TitleBar区域的判定搞坏掉了
		# TitleBar的mousePressEvent、mouseMoveEvent等事件在左上角的一个区域内都侦测不到了
		# 花了我将近两个小时才捉出这只虫子……
		
		self.centralwidget.addWidget(widget)