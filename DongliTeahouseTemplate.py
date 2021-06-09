from DongliTeahousePySideWheel.DongliTeahouseModule import *

# APP
class DongliTeahouseAPP(QApplication):
	def __init__(self,args):

		self.setAttribute(Qt.AA_UseOpenGLES)
		self.setAttribute(Qt.AA_EnableHighDpiScaling)
		self.setAttribute(Qt.AA_UseHighDpiPixmaps)

		super().__init__(args)

		self.setStyle("Fusion")
		self.setPalette(DongliTeahousePalette.MyDarkPalette())
		self.setWindowIcon(DongliTeahouseMessageIcon.Holo())
		self.setQuitOnLastWindowClosed(False)
		
		self.setApplicationName("DongliTeahouse's Project")
		self.setApplicationVersion("0.0.0.0")
		self.setOrganizationName("Dongli Teahouse")
		self.setOrganizationDomain("dongliteahouse.com")
		self.__author="鍵山狐"
		self.__contact="Holence08@gmail.com"

		self.checkIn()

	def setAuthor(self,author):
		self.__author=author
	
	def author(self):
		return self.__author
	
	def setContact(self,contact):
		self.__contact=contact
	
	def contact(self):
		return self.__contact
	
	def setMainWindow(self,mainwindow):
		self.mainwindow=mainwindow
		self.mainwindow.quitApp.connect(self.quit)
	
	def checkIn(self):
		self.password=None
		dlg=DongliTeahouseLogin(self)
		if dlg.exec_()==0:
			self.quit()
			exit()
		else:
			self.password=dlg.input_password
	
	def run(self):
		self.mainwindow.show()
		sys.exit(self.exec_())


# Login 
class DongliTeahouseLogin(DongliTeahouseDialog):
	def __init__(self,parent):
		super().__init__(None,"Login")
		
		self.login=ModuleDongliTeahouseLogin(self)
		self.centralWidget.addWidget(self.login)
		self.setWindowTitle("Login")
		self.adjustSize()
		self.setFocus()
		self.login.lineEdit.setFocus()
		
		# 获取UserSetting.ini中的加密密码
		self.UserSetting=QSettings("./UserSetting.ini",QSettings.IniFormat)
		self.lock_password=self.UserSetting.value("BasicInfo/Password")
		#欢迎新用户
		if self.lock_password==None:
			self.login.label.setPixmap(DongliTeahouseMessageIcon.Happy().pixmap(QSize(28,28)))
	
	def accept(self):
		self.input_password=self.login.lineEdit.text()
		
		#新用户
		if self.lock_password==None:
			self.login.label.setPixmap(DongliTeahouseMessageIcon.Lock().pixmap(QSize(28,28)))
			Delay_Msecs(400)
			self.login.label.setPixmap(DongliTeahouseMessageIcon.Unlock().pixmap(QSize(28,28)))
			Delay_Msecs(600)
			super().accept()
		
		elif Fernet_Decrypt(self.input_password,self.lock_password)==self.input_password:
			self.login.label.setPixmap(DongliTeahouseMessageIcon.Lock().pixmap(QSize(28,28)))
			Delay_Msecs(400)
			self.login.label.setPixmap(DongliTeahouseMessageIcon.Unlock().pixmap(QSize(28,28)))
			Delay_Msecs(600)
			super().accept()
		else:
			self.login.label.setPixmap(DongliTeahouseMessageIcon.Unhappy().pixmap(QSize(28,28)))
	
	def reject(self):
		super().reject()


# Mainwindow
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseMainWindow import Ui_DongliTeahouseMainWindow
class DongliTeahouseMainWindow(Ui_DongliTeahouseMainWindow,QMainWindow):
	"通过setCentralWidget来放入主功能区"

	quitApp=Signal()

	def closeEvent(self,event):
		super().closeEvent(event)
		self.dataSave()
		self.quitApp.emit()

	def __init__(self,app):
		super().__init__()
		self.__MainMenu=QMenu(self)
		self.UserSetting=QSettings("./UserSetting.ini",QSettings.IniFormat)
		self.setPassword(app.password)

		self.initializeMetaData(app)
		self.initializeData()
		self.initializeWindow()
		self.initializeSignal()
		self.initializeMenu()
		self.initializeTrayIcon()

	def initializeMetaData(self,app):

		self.UserSetting.beginGroup("MetaData")
		self.UserSetting.setValue("ApplicationName",app.applicationName())
		self.UserSetting.setValue("Author",app.author())
		self.UserSetting.setValue("ApplicationVersion",app.applicationVersion())
		self.UserSetting.setValue("OrganizationName",app.organizationName())
		self.UserSetting.setValue("OrganizationDomain",app.organizationDomain())
		self.UserSetting.setValue("Contact",app.contact())
		self.UserSetting.endGroup()
		
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
		self.updateFont()
		self.setWindowTitle(self.UserSetting.value("MetaData/ApplicationName"))
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)

	def initializeSignal(self):
		"""
		主窗体的action向function链接
		注意：需要拥有全局快捷键的action，需要addAction
		"""

		self.actionSetting.triggered.connect(self.setting)
		self.actionAbout.triggered.connect(self.about)
		
		self.actionWindow_Toggle_Fullscreen.triggered.connect(self.windowToggleFullscreen)
		self.addAction(self.actionWindow_Toggle_Fullscreen)

		self.actionWindow_Toggle_Stay_on_Top.triggered.connect(self.windowToggleStayonTop)
		self.actionNormalize_Window.triggered.connect(self.showNormal)
		self.actionMaximize_Window.triggered.connect(self.showMaximized)
		self.actionMinimize_Window.triggered.connect(self.showMinimized)
		
		self.actionBoss_Key.triggered.connect(self.bossComing)
		self.addAction(self.actionBoss_Key)

		self.actionExit.triggered.connect(self.close)
		self.addAction(self.actionExit)
	
	def initializeMenu(self):
		"制定menu"
		
		self.__MainMenu.addAction(self.actionSetting)
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
		
		self.__MainMenu.addAction(self.actionBoss_Key)
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
			if self.isHidden():
				if not hasattr(self,"ResurrectionDlg"):
					self.ResurrectionDlg=DongliTeahouseLogin(self)
					
					#成功登回
					if self.ResurrectionDlg.exec_():
						self.showNormal()
						# 恢复self.__MainMenu里的其他action
						for action in self.__MainMenu.actions()[:-1]:
							action.setVisible(True)
					
					del self.ResurrectionDlg
				else:
					pass
			else:
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
	
	def bossComing(self):
		self.hide()
		
		# Boss键后只显示退出键，self.__MainMenu里的其他action隐藏掉
		for action in self.__MainMenu.actions()[:-1]:
			action.setVisible(False)

	def dataValidityCheck(self):
		return True

	def dataLoad(self):
		pass

	def dataSave(self):
		pass
	
	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.TitleBar.setWindowTitle(title)

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

	def password(self):
		return self.__Password
	
	def setPassword(self,password):
		self.__Password=password
		self.UserSetting.setValue("BasicInfo/Password",Fernet_Encrypt(self.__Password,self.__Password))
	
	def SaveAllEncryptData(self):
		"设置密码后将调用这个函数，对所有加密文件的内容覆写，比如dataSave或者UserSetting中有加密的保存项目就要放到这里（除了对密码的加密已经操作过了）"
		pass

	def updateFont(self):
		self.setFont(self.UserSetting.value("BasicInfo/Font"))

	def about(self):
		about_text=""
		
		self.UserSetting.beginGroup("MetaData")
		for key in self.UserSetting.allKeys():
			about_text+="%s: %s\n"%(key,self.UserSetting.value(key))
		self.UserSetting.endGroup()

		DongliTeahouseMessageBox(self,"About",about_text[:-1])
	
	def setting(self):
		"请在继承的DongliTeahouseSettingDialog中做到实时保存设定"
		
		# dlg=DongliTeahouseSettingDialog(self)
		# dlg.exec_()
		pass


# Setting
class DongliTeahouseSettingDialog(DongliTeahouseDialog):
	def __init__(self,parent):
		super().__init__(parent,"Setting")
		
		# 不要按钮了，实时保存设置
		# self.buttonBox.removeButton(self.buttonBox.button(QDialogButtonBox.Cancel))
		self.buttonBox.clear()
		self.centralWidget.setContentsMargins(QMargins(8,10,32,0))
		self.horizontalLayout.setContentsMargins(QMargins(0,0,32,0))

		self.__settingModule=Module_DongliTeahouseSetting(parent)
		self.centralWidget.addWidget(self.__settingModule)
	
	def addButtonAndPage(self,button,qwidget):
		"传入一个button和stackwidget page中的QWidget，button将自动加入到ButtonMenu列表的队尾，并链接好跳转到该stackwidget page的信号"
		index=self.__settingModule.appendStackPage(qwidget)
		self.__settingModule.addPageButton(button,index)