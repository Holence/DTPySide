from DongliTeahousePySideWheel.DongliTeahouseFunction import *
from DongliTeahousePySideWheel.DongliTeahouseWidget import DongliTeahouseTitleBarFull
from DongliTeahousePySideWheel.DongliTeahouseFrame import DongliTeahouseMessageBox


# Mainwindow
from DongliTeahousePySideWheel.DongliTeahouseFrame.Ui_DongliTeahouseMainWindow import Ui_DongliTeahouseMainWindow
class DongliTeahouseMainWindow(Ui_DongliTeahouseMainWindow,QMainWindow):
	"DongliTeahouseMainWindow骨架，通过setCentralWidget来放入主功能区"
	
	def closeEvent(self, event):
		super().closeEvent(event)
		self.deleteLater()
	
	def __init__(self,app):
		super().__init__()
		self.app=app
		self._MainMenu=QMenu(self)

		self.TitleBar=DongliTeahouseTitleBarFull(self)
		self.setMenuWidget(self.TitleBar)
		
		self.setupUi(self)
		self.setWindowTitle(self.UserSetting().value("MetaData/ApplicationName"))
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)

	
	def initialize(self):
		self.initializeSignal()
		self.initializeMenu()

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
	
	def windowToggleMaximized(self):
		"给TitleBar中的Maximize按钮用，切换主窗体Maximized和Normalized"
		
		if self.TitleBar.btn_maximize.isHidden():
			self.TitleBar.btn_maximize.show()
		if self.TitleBar.btn_minimize.isHidden():
			self.TitleBar.btn_minimize.show()
		
		if self.isMaximized():
			self.showNormal()
			self.TitleBar.btn_maximize.setIcon(QIcon(":/icon/white/white_window-maximize.svg"))
		else:
			self.showMaximized()
			self.TitleBar.btn_maximize.setIcon(QIcon(":/icon/white/white_window-restore.svg"))

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
		self.TitleBar.setWindowTitle(title)

	def password(self):
		return self.app.password()
	
	def setPassword(self,password):
		self.app.setPassword(password)
	
	def UserSetting(self):
		return self.app.UserSetting