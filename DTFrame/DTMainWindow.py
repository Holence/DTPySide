from DTPySide.DTFunction import *
from DTPySide.DTWidget import DTTitleBarFull, DTEdge

# Mainwindow
from DTPySide.DTFrame.Ui_DTMainWindow import Ui_DTMainWindow
class DTMainWindow(Ui_DTMainWindow,QMainWindow):
	"DTMainWindow骨架，通过setCentralWidget来放入主功能区"
	
	def closeEvent(self, event):
		super().closeEvent(event)
		self.deleteLater()
	
	def resizeEvent(self, event):
		# Update Size Grips
		self.left_grip.setGeometry(0, 10, 10, self.height())
		self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
		self.top_grip.setGeometry(0, 0, self.width(), 10)
		self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

	def __init__(self,app):
		super().__init__()
		self.app=app
		self._MainMenu=QMenu(self)

		self.TitleBar=DTTitleBarFull(self)
		self.setMenuWidget(self.TitleBar)

		self.setupUi(self)
		self.setWindowTitle(self.UserSetting().value("MetaData/ApplicationName"))
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
		
	
	def initialize(self):
		self.initializeWindow()
		self.restoreWindowStatus()
		self.initializeEdge()

		self.initializeSignal()
		self.initializeMenu()

	def initializeWindow(self):
		
		pass
	
	def restoreWindowStatus(self):
		pass
	
	def initializeEdge(self):
		"""制定四边+四角的SizeGrip
		"""		
		self.left_grip = DTEdge(self, Qt.LeftEdge, True)
		self.right_grip = DTEdge(self, Qt.RightEdge, True)
		self.top_grip = DTEdge(self, Qt.TopEdge, True)
		self.bottom_grip = DTEdge(self, Qt.BottomEdge, True)
	
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
			self.left_grip.show()
			self.right_grip.show()
			self.top_grip.show()
			self.bottom_grip.show()
		else:
			self.showMaximized()
			self.TitleBar.btn_maximize.setIcon(QIcon(":/icon/white/white_window-restore.svg"))
			self.left_grip.hide()
			self.right_grip.hide()
			self.top_grip.hide()
			self.bottom_grip.hide()

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