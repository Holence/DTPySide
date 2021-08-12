from __future__ import annotations
from DTPySide import *

# APP
class DTAPP(QApplication):
	"""DTAPP注释


	Args:
		QApplication ([type]): [description]
	"""
	
	def __init__(self,args):
		
		self.__UserSetting=QSettings("./UserSetting.ini",QSettings.IniFormat)
		
		# 添加缩放大小的环境变量
		os.environ["QT_SCALE_FACTOR"] = str(self.Scale())

		# 设置图片缩放质量
		self.setAttribute(Qt.AA_UseOpenGLES,True)
		self.setAttribute(Qt.AA_EnableHighDpiScaling,True)
		self.setAttribute(Qt.AA_UseHighDpiPixmaps,True)
		
		# 设置字体缩放质量
		# QLibraryInfo will load qt.conf from one of the following locations:
		#	1. :/qt/etc/qt.conf using the resource system
		#	2. on macOS, in the Resource directory inside the application bundle, for example assistant.app/Contents/Resources/qt.conf
		#	3. in the directory containing the application executable, i.e. QCoreApplication::applicationDirPath() + QDir::separator() + "qt.conf"
		# 
		# print(self.applicationDirPath()+QDir.separator()) to see where the qt.conf should be placed
		# 新建一个qt.conf写下下面的设置 would cause the Windows platform plugin to use the FreeType font engine.
		# [Platforms]
		# WindowsArguments = fontengine=freetype
		# 这样字体也就不会有锯齿啦~
		#
		# （用Python解释器跑的时候，self.applicationDirPath()==D:/Program/Python，也就是python.exe的根目录
		# 如果这时候把qt.conf放到D:/Program/Python，会影响对相应组件的加载与打包（即使设置了Prefix等路径也不行）
		# 
		# 所以在解释的时候就不放qt.conf，而是在打包后，把qt.conf放在main.exe的目录下
		# （如果用了WebEngine的话，还要复制一份resource、translation和QtWebEngineProcess.exe到根目录）

		# 继承stylesheet
		self.setAttribute(Qt.AA_UseStyleSheetPropagationInWidgetStyles,True)
		
		# BossKey隐藏主窗口后不退出QApp
		self.setQuitOnLastWindowClosed(False)
		
		super().__init__(args)

		self.setStyle("Fusion")
		self.ThemeList=["Dracula","Dracula2","Brown","Green","Cyan","White"]
		self.initializeWindowStyle()
		self.loadTranslation()
		self.TrayIcon=QSystemTrayIcon(self)
		self.__password=None
		self.__mainsession=None

		self.setWindowIcon(DTIcon.HoloIcon1())
		self.setApplicationName("DT's Project")
		self.setApplicationVersion("0.0.0.0")
		self.setAuthor("鍵山狐")
		self.setOrganizationName("Dongli Teahouse")
		self.setOrganizationDomain("www.dongliteahouse.com")
		self.setContact("Holence08@gmail.com")
		
		self.setLoginEnable(False)
		self.setBackupEnable(False)
	
	def initializeTrayIcon(self):
		"生成TrayIcon"
		
		self.TrayIcon.setIcon(self.windowIcon())
		self.TrayIcon.activated.connect(self.__mainsession.windowResurrection)
		self.TrayIcon.setContextMenu(self.__mainsession._MainMenu)
		
		self.TrayIcon.show()

	def initializeWindowStyle(self):
		"""设置MainwWindow的Window Effect和Theme
		"""
		
		WindowEffect=self.WindowEffect()
		Theme=self.Theme()
		Hue=self.Hue()
		Font=self.Font()
		
		self.setStyleSheet(DTStyleSheet(Theme, Hue, WindowEffect,Font))
	
	def loadTranslation(self):

		if self.Language() not in DTTranslation.Language_Dict:
			self.setLanguage("English")
		if self.Country() not in DTTranslation.Country_Dict:
			self.setCountry("World")
		
		language=self.Language()
		country=self.Country()
		
		# set QLocale
		QLocale.setDefault(QLocale(DTTranslation.Language_Dict[language][0],DTTranslation.Country_Dict[country]))

		# load .qm file
		self.translation=QTranslator()
		self.translation.load(DTTranslation.Language_Dict[language][1])
		self.installTranslator(self.translation)
	
	def Font(self) -> QFont:
		if self.__UserSetting.value("BasicInfo/Font")==None:
			font=QFont()
			font.setFamily("Meiryo UI")
			font.setPointSize(18)
			self.setFont(font)
		return self.__UserSetting.value("BasicInfo/Font")
	
	def setFont(self,font:QFont):
		self.__UserSetting.setValue("BasicInfo/Font",font)

	def Scale(self):
		if self.__UserSetting.value("BasicInfo/Scale")==None or float(self.__UserSetting.value("BasicInfo/Scale"))<1 or float(self.__UserSetting.value("BasicInfo/Scale"))>5:
			self.setScale(1.0)
		return float(self.__UserSetting.value("BasicInfo/Scale"))
	
	def setScale(self,scale:float):
		self.__UserSetting.setValue("BasicInfo/Scale",str(scale))
	
	def WindowEffect(self):
		if self.__UserSetting.value("BasicInfo/WindowEffect") not in ["Normal","Aero","Acrylic"]:
			self.setWindowEffect("Acrylic")
		return self.__UserSetting.value("BasicInfo/WindowEffect")
	
	def setWindowEffect(self, WindowEffect:str):
		self.__UserSetting.setValue("BasicInfo/WindowEffect",WindowEffect)
	
	def Theme(self):
		if self.__UserSetting.value("BasicInfo/Theme") not in self.ThemeList:
			self.setTheme("Dracula")
		return self.__UserSetting.value("BasicInfo/Theme")
	
	def setTheme(self,Theme:str):
		self.setHue(-1)
		self.__UserSetting.setValue("BasicInfo/Theme",Theme)
	
	def Hue(self):
		if self.__UserSetting.value("BasicInfo/Hue")==None:
			self.setHue(-1)
		else:
			Hue=float(self.__UserSetting.value("BasicInfo/Hue"))
			if not 0<=Hue<=1 and Hue!=-1:
				self.setHue(-1)
		return float(self.__UserSetting.value("BasicInfo/Hue"))
	
	def setHue(self,hue:float):
		self.__UserSetting.setValue("BasicInfo/Hue",str(hue))

	def Language(self):
		return self.__UserSetting.value("BasicInfo/Language")
	
	def setLanguage(self,Language:str):
		self.__UserSetting.setValue("BasicInfo/Language",Language)
	
	def Country(self):
		return self.__UserSetting.value("BasicInfo/Country")
	
	def setCountry(self,Country:str):
		self.__UserSetting.setValue("BasicInfo/Country",Country)

	def setApplicationName(self,str):
		super().setApplicationName(str)
		self.__UserSetting.setValue("MetaData/ApplicationName",self.applicationName())
	
	def setApplicationVersion(self,str):
		super().setApplicationVersion(str)
		self.__UserSetting.setValue("MetaData/ApplicationVersion",self.applicationVersion())
	
	def setOrganizationName(self,str):
		super().setOrganizationName(str)
		self.__UserSetting.setValue("MetaData/OrganizationName",self.organizationName())
	
	def setOrganizationDomain(self,str):
		super().setOrganizationDomain(str)
		self.__UserSetting.setValue("MetaData/OrganizationDomain",self.organizationDomain())

	def UserSetting(self):
		return self.__UserSetting

	def isLoginEnable(self):
		return self.__LoginEnable
	
	def setLoginEnable(self,bool=True):
		self.__LoginEnable=bool
	
	def isBackupEnable(self):
		return self.__BackupEnable
	
	def setBackupEnable(self,bool=True):
		"""设置是否开启备份功能

		Args:
			bool (bool, optional): Defaults to True.
		"""		
		self.__BackupEnable=bool
		self.setBackupList([])
	
	def setBackupDst(self,dst:str):
		"""设置面板中设置备份地址

		Args:
			dst (str): 备份的目的地
		"""
		if self.isBackupEnable():
			if os.path.exists(dst):
				self.__UserSetting.setValue("BasicInfo/BackupDst",Fernet_Encrypt(self.__password,dst))
			else:
				DTFrame.DTMessageBox(None,"Error","Backup Dst does not exsit!",DTIcon.Error())
		else:
			raise("Please setBackupEnable before setBackupList.")
	
	def BackupDst(self):
		return Fernet_Decrypt(self.__password,self.__UserSetting.value("BasicInfo/BackupDst"))

	def setBackupList(self,backup_list:list):
		"""程序中对app设置，要备份的文件的url列表

		Args:
			backup_list (list): 要备份的文件的url列表
		"""
		self.__BackupList=backup_list
	
	def BackupList(self):
		return self.__BackupList

	def password(self):
		return self.__password
	
	def setPassword(self,password):
		self.__password=password
		self.__UserSetting.setValue("BasicInfo/Password",Fernet_Encrypt(self.__password,self.__password))

	def author(self):
		return self.__UserSetting.value("MetaData/Author")

	def setAuthor(self,author):
		self.__UserSetting.setValue("MetaData/Author",author)
	
	def contact(self):
		return self.__UserSetting.value("MetaData/Contact")

	def setContact(self,contact):
		self.__UserSetting.setValue("MetaData/Contact",contact)
	
	def setMainSession(self,mainsession: DTSession.DTMainSession):
		self.__mainsession=mainsession
		self.__mainsession.quitApp.connect(self.quit)
	
	def __loginIn(self):
		dlg=DTSession.DTLoginSession(self.__UserSetting.value("BasicInfo/Password"))
		if dlg.exec_()==0:
			self.quit()
			sys.exit()
		else:
			self.setPassword(dlg.input_password)
	
	def debugRun(self,password,loginEnable,show=True):
		self.setLoginEnable(loginEnable)
		self.setPassword(password)

		self.__mainsession.initialize()
		if show==True:
			self.__mainsession.show()
		
		self.initializeTrayIcon()
		sys.exit(self.exec_())

	def run(self,show=True):
		"""如果没有密码加密，需要setLoginEnable(False)
		"""
		if self.__LoginEnable==True:
			self.__loginIn()
		
		self.__mainsession.initialize()
		if show==True:
			self.__mainsession.show()
		
		self.initializeTrayIcon()
		sys.exit(self.exec_())