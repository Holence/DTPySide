from DongliTeahousePySideWheel.DongliTeahouseWidget import *

# MainWindow用的TitleBar
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseTitleBarFull import Ui_DongliTeahouseTitleBarFull
class DongliTeahouseTitleBarFull(Ui_DongliTeahouseTitleBarFull,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.parent=parent
		self.label_titlebar.setPapa(parent)
		self.initializeSignal()
	
	def initializeSignal(self):
		self.btn_close.clicked.connect(self.parent.close)
		self.btn_maximize.clicked.connect(self.parent.windowToggleMaximized)
		self.btn_minimize.clicked.connect(self.parent.showMinimized)
		self.btn_menu.clicked.connect(lambda:show_ContextMenu_Beneath(self.parent.MainMenu(),self.btn_menu))

	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.label_titlebar.setText(title)

# 其他窗口用的TitleBar
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseTitleBarCut import Ui_DongliTeahouseTitleBarCut
class DongliTeahouseTitleBarCut(Ui_DongliTeahouseTitleBarCut,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.parent=parent
		self.label_titlebar.setPapa(parent)
		self.initializeSignal()
	
	def initializeSignal(self):
		self.btn_close.clicked.connect(self.parent.close)
	
	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.label_titlebar.setText(title)

# Dialog
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseDialog import Ui_DongliTeahouseDialog
class DongliTeahouseDialog(Ui_DongliTeahouseDialog,QDialog):
	def __init__(self,parent,title):
		super().__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
		QSizeGrip(self.SizeGrip)
		
		self.TitleBar.setWindowTitle(title)

# MessageBox
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseMessageBox import Ui_DongliTeahouseMessageBox
class DongliTeahouseMessageBox(Ui_DongliTeahouseMessageBox,QDialog):
	"传入title、messageText和icon的地址（建议使用DongliTeahouseMessageIcon的内置Icon）"

	def __init__(self,parent,title,messageText,icon=None):
		super().__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
		QSizeGrip(self.SizeGrip)
		
		self.TitleBar.setWindowTitle(title)
		self.label_message.setText(messageText)
		
		if icon!=None:
			icon_pic=icon.pixmap(QSize(64,64))
			self.label_icon.setPixmap(icon_pic)
		else:
			self.label_icon.hide()

		self.adjustSize()
		self.exec_()

# Mainwindow
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseMainWindow import Ui_DongliTeahouseMainWindow
class DongliTeahouseMainWindow(Ui_DongliTeahouseMainWindow,QMainWindow):
	"通过setCentralWidget来放入主功能区"

	quitApp=Signal()

	def closeEvent(self,event):
		super().closeEvent(event)
		self.dataSave()
		self.quitApp.emit()

	def __init__(self):
		super().__init__()

		self.__MainMenu=QMenu(self)
		self.__MetaData={}

		self.initializeMetaData()
		self.initializeData()
		self.initializeWindow()
		self.initializeSignal()
		self.initializeMenu()
		self.initializeTrayIcon()
		self.show()

	def initializeMetaData(self):
		self.__MetaData={
			"ProjectName":"DongliTeahouse's Project",
			"Version":"0.0.0.0",
			"Author":"鍵山狐",
			"Contact":"Holence08@gmail.com",
		}
	
	def initializeData(self):
		if self.dataValidityCheck():
			self.dataLoad()
		else:
			DongliTeahouseMessageBox(self,"Error","Data Error!")
			exit()
	
	def initializeWindow(self):
		self.TitleBar=DongliTeahouseTitleBarFull(self)
		self.setMenuWidget(self.TitleBar)
		
		self.setupUi(self)
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)

	def initializeSignal(self):
		"""
		主窗体的action向function链接
		注意：需要拥有全局快捷键的action，需要addAction
		"""

		self.actionSettings.triggered.connect(self.setting)
		self.actionAbout.triggered.connect(self.about)
		
		self.actionWindow_Toggle_Fullscreen.triggered.connect(self.windowToggleFullscreen)
		self.addAction(self.actionWindow_Toggle_Fullscreen)

		self.actionWindow_Toggle_Stay_on_Top.triggered.connect(self.windowToggleStayonTop)
		self.actionNormalize_Window.triggered.connect(self.showNormal)
		self.actionMaximize_Window.triggered.connect(self.showMaximized)
		self.actionMinimize_Window.triggered.connect(self.showMinimized)
		
		self.actionExit.triggered.connect(self.close)
		self.addAction(self.actionExit)
	
	def initializeMenu(self):
		"制定menu"
		
		self.__MainMenu.addAction(self.actionSettings)
		self.__MainMenu.addAction(self.actionAbout)
		self.__MainMenu.addSeparator()
		
		################################################################
		
		self.__MainMenu.addAction(self.actionWindow_Toggle_Fullscreen)
		self.__MainMenu.addAction(self.actionWindow_Toggle_Stay_on_Top)
		self.__MainMenu.addAction(self.actionNormalize_Window)
		self.__MainMenu.addAction(self.actionMinimize_Window)
		self.__MainMenu.addAction(self.actionMaximize_Window)
		self.__MainMenu.addSeparator()

		################################################################
		
		self.__MainMenu.addAction(self.actionExit)
		
	def initializeTrayIcon(self):
		"生成TrayIcon"

		self.TrayIcon=QSystemTrayIcon(self)
		
		self.TrayIcon.setIcon(QIcon(":/icon/holoico_trans.ico"))
		self.TrayIcon.activated.connect(self.windowResurrection)
		self.TrayIcon.setContextMenu(self.__MainMenu)
		
		self.TrayIcon.show()

	def windowToggleMaximized(self):
		"给TitleBar中的Maximize按钮用，切换主窗体Maximized和Normalized"
		
		if self.TitleBar.btn_maximize.isHidden():
			self.TitleBar.btn_maximize.show()
		if self.TitleBar.btn_minimize.isHidden():
			self.TitleBar.btn_minimize.show()
		
		if self.isMaximized():
			self.showNormal()
			self.TitleBar.btn_maximize.setIcon(QIcon(":/white/white_window-maximize.svg"))
		else:
			self.showMaximized()
			self.TitleBar.btn_maximize.setIcon(QIcon(":/white/white_window-restore.svg"))
	
	def windowResurrection(self,reason):
		"双击TrayIcon还原主窗体"

		if reason==QSystemTrayIcon.DoubleClick:
			self.showNormal()
	
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
	
	def dataValidityCheck(self):
		return True
		# return False

	def dataLoad(self):
		pass

	def dataSave(self):
		pass
	
	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.TitleBar.setWindowTitle(title)

	def setMetaData(self,ProjectName="DongliTeahouse's Project",Version="0.0.0.0",Author="鍵山狐",Contact="Holence08@gmail.com"):
		self.__MetaData={
			"ProjectName":ProjectName,
			"Version":Version,
			"Author":Author,
			"Contact":Contact
		}

	def MainMenu(self):
		return self.__MainMenu
	
	def addSeparatorToMainMenu(self):
		self.__MainMenu.addSeparator()

	def addActionToMainMenu(self,action):
		self.__MainMenu.addAction(action)
	
	def insertActionToMainMenu(self,fore_action,action):
		self.__MainMenu.insertAction(fore_action,action)
	
	def addMenuToMainMenu(self,menu):
		self.__MainMenu.addMenu(menu)
	
	def insertMenuToMainMenu(self,fore_action,menu):
		self.__MainMenu.insertMenu(fore_action,menu)

	def about(self):
		about_text=""
		for metadata_key in self.__MetaData.keys():
			about_text+="%s: %s\n"%(metadata_key,self.__MetaData[metadata_key])
		
		DongliTeahouseMessageBox(self,"About",about_text[:-1])
	
	def setting(self):
		pass