from __future__ import annotations
from DTPySide import *

# APP
class DTAPP(QApplication):
	"""DTAPP注释


	Args:
		QApplication ([type]): [description]
	"""
	
	def __init__(self, args):

		self.__UserSetting=QSettings("./UserSetting.ini",QSettings.IniFormat)
		
		# 添加缩放大小的环境变量
		os.environ["QT_SCALE_FACTOR"] = str(self.Scale())

		# 设置图片缩放质量
		self.setAttribute(Qt.AA_UseOpenGLES,True)
		# self.setAttribute(Qt.AA_EnableHighDpiScaling,True)
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
		
		self.TrayIcon=QSystemTrayIcon(self)

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
		
		self.setStyleSheet(DTStyleSheet(self.Theme(), self.Hue(), self.Saturation(), self.Luminance(), self.Contrast(), self.Reverse(), self.WindowEffect(), self.Font()))
	
	def hasTanslation(self):
		return hasattr(self,"translation")

	def loadTranslation(self, translation_module=DTTranslation):
		"""请在构造MainSession之前调用这个函数，因为MainSession中的文字会用translate来请求translation
		
		设置translation的module（请复制DTTranslation文件夹到自己的项目中，先翻译自己项目里的文本，之后再在lrelease的时候与合并qm文件）。
		
		如果不调用这个函数，App默认为无translation，设置菜单中也不会有语言和地区的选项

		Args:
			translation_module (module, optional): Defaults to DTTranslation.
		"""		
		
		self.translation_module=translation_module

		if self.Language() not in translation_module.Language_Dict:
			self.setLanguage("English")
		if self.Country() not in translation_module.Country_Dict:
			self.setCountry("World")
		
		language=self.Language()
		country=self.Country()
		
		# set QLocale
		QLocale.setDefault(QLocale(translation_module.Language_Dict[language][0],translation_module.Country_Dict[country]))

		# load .qm file
		self.translation=QTranslator()
		self.translation.load(translation_module.Language_Dict[language][1])
		self.installTranslator(self.translation)
	
	def Font(self) -> QFont:
		if self.__UserSetting.value("BasicInfo/Font")==None:
			font=QFont()
			font.setFamily("Meiryo UI")
			font.setPointSize(18)
			self.setFont(font)
		return self.__UserSetting.value("BasicInfo/Font")
	
	def setFont(self, font:QFont):
		self.__UserSetting.setValue("BasicInfo/Font",font)

	def Scale(self):
		if self.__UserSetting.value("BasicInfo/Scale")==None or float(self.__UserSetting.value("BasicInfo/Scale"))<1:
			self.setScale(1.0)
		return float(self.__UserSetting.value("BasicInfo/Scale"))
	
	def setScale(self, scale:float):
		self.__UserSetting.setValue("BasicInfo/Scale",str(scale))
	
	def WindowEffect(self):
		if self.__UserSetting.value("BasicInfo/WindowEffect") not in ["Normal","Aero","Acrylic"]:
			self.setWindowEffect("Normal")
		return self.__UserSetting.value("BasicInfo/WindowEffect")
	
	def setWindowEffect(self, WindowEffect:str):
		self.__UserSetting.setValue("BasicInfo/WindowEffect",WindowEffect)
	
	def Theme(self):
		if self.__UserSetting.value("BasicInfo/Theme") not in self.ThemeList:
			self.setTheme("Dracula")
		return self.__UserSetting.value("BasicInfo/Theme")
	
	def setTheme(self, Theme:str):
		self.setHue(-1)
		self.setSaturation(0.5)
		self.setLuminance(0.5)
		self.setContrast(0.5)
		self.setReverse(False)
		self.__UserSetting.setValue("BasicInfo/Theme",Theme)
	
	def Hue(self):
		if self.__UserSetting.value("BasicInfo/Hue")==None:
			self.setHue(-1)
		else:
			Hue=float(self.__UserSetting.value("BasicInfo/Hue"))
			if not 0<=Hue<=1 and Hue!=-1:
				self.setHue(-1)
		return float(self.__UserSetting.value("BasicInfo/Hue"))
	
	def setHue(self, hue:float):
		self.__UserSetting.setValue("BasicInfo/Hue",str(hue))

	def Saturation(self):
		if self.__UserSetting.value("BasicInfo/Saturation")==None:
			self.setSaturation(0.5)
		else:
			Saturation=float(self.__UserSetting.value("BasicInfo/Saturation"))
			if not 0<=Saturation<=1:
				self.setSaturation(0.5)
		return float(self.__UserSetting.value("BasicInfo/Saturation"))
	
	def setSaturation(self, saturation:float):
		self.__UserSetting.setValue("BasicInfo/Saturation",str(saturation))

	def Luminance(self):
		if self.__UserSetting.value("BasicInfo/Luminance")==None:
			self.setLuminance(0.5)
		else:
			Luminance=float(self.__UserSetting.value("BasicInfo/Luminance"))
			if not 0<=Luminance<=1:
				self.setLuminance(0.5)
		return float(self.__UserSetting.value("BasicInfo/Luminance"))
	
	def setLuminance(self, luminance:float):
		self.__UserSetting.setValue("BasicInfo/Luminance",str(luminance))
	
	def Contrast(self):
		if self.__UserSetting.value("BasicInfo/Contrast")==None:
			self.setContrast(0.5)
		else:
			Contrast=float(self.__UserSetting.value("BasicInfo/Contrast"))
			if not 0<=Contrast<=1:
				self.setContrast(0.5)
		return float(self.__UserSetting.value("BasicInfo/Contrast"))
	
	def setContrast(self, contrast:float):
		self.__UserSetting.setValue("BasicInfo/Contrast",str(contrast))

	def Reverse(self):
		if self.__UserSetting.value("BasicInfo/Reverse")==None:
			self.setReverse(False)
		
		Reverse = self.__UserSetting.value("BasicInfo/Reverse")
		Reverse = True if Reverse=="True" else False
		return Reverse

	def setReverse(self, reverse:bool):
		self.__UserSetting.setValue("BasicInfo/Reverse",str(reverse))

	def Language(self):
		return self.__UserSetting.value("BasicInfo/Language")
	
	def setLanguage(self, Language:str):
		self.__UserSetting.setValue("BasicInfo/Language",Language)
	
	def Country(self):
		return self.__UserSetting.value("BasicInfo/Country")
	
	def setCountry(self, Country:str):
		self.__UserSetting.setValue("BasicInfo/Country",Country)

	def setApplicationName(self, str):
		super().setApplicationName(str)
		self.__UserSetting.setValue("MetaData/ApplicationName",self.applicationName())
	
	def setApplicationVersion(self, str):
		super().setApplicationVersion(str)
		self.__UserSetting.setValue("MetaData/ApplicationVersion",self.applicationVersion())
	
	def setOrganizationName(self, str):
		super().setOrganizationName(str)
		self.__UserSetting.setValue("MetaData/OrganizationName",self.organizationName())
	
	def setOrganizationDomain(self, str):
		super().setOrganizationDomain(str)
		self.__UserSetting.setValue("MetaData/OrganizationDomain",self.organizationDomain())

	def UserSetting(self):
		return self.__UserSetting

	def isLoginEnable(self):
		return self.__LoginEnable
	
	def setLoginEnable(self, bool=True):
		self.__LoginEnable=bool
	
	def setDataDir(self, new_dir:str):
		if os.path.exists(new_dir):
			old_dir=self.DataDir()
			try:
				for file in self.DataList():		
					old_file_dir=os.path.join(old_dir,file)
					file_dst=os.path.join(new_dir,file)
					shutil.move(old_file_dir,file_dst)
			except Exception as e:
				DTFrame.DTMessageBox(None,"Error",e,DTIcon.Error())
			self.__UserSetting.setValue("BasicInfo/DataDir",Fernet_Encrypt(self.__password,new_dir))
		else:
			DTFrame.DTMessageBox(None,"Error","Data Dir does not exsit!",DTIcon.Error())
	
	def DataDir(self):
		if self.__UserSetting.value("BasicInfo/DataDir")==None:
			self.__UserSetting.setValue("BasicInfo/DataDir",Fernet_Encrypt(self.__password,os.getcwd()))
		
		return Fernet_Decrypt(self.__password,self.__UserSetting.value("BasicInfo/DataDir"))

	def setDataList(self, data_list:list):
		"""程序中对app设置，data文件列表（应该是DataDir下的文件，与load、save、backup相关）

		Args:
			data_list (list): data文件列表
		"""
		self.__DataList=data_list
	
	def DataList(self):
		return self.__DataList
	
	def isBackupEnable(self):
		return self.__BackupEnable
	
	def setBackupEnable(self, bool=True):
		"""设置是否开启备份功能，备份文件的列表即为main中setDataList设置的文件列表

		Args:
			bool (bool, optional): Defaults to True.
		"""		
		self.__BackupEnable=bool
	
	def setBackupDst(self, dst:str):
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
			raise("Please setBackupEnable before setBackupDst.")
	
	def BackupDst(self):
		return Fernet_Decrypt(self.__password,self.__UserSetting.value("BasicInfo/BackupDst"))

	def password(self):
		return self.__password
	
	def setPassword(self, password):
		self.__password=password
		self.__UserSetting.setValue("BasicInfo/Password",Fernet_Encrypt(self.__password,self.__password))

	def author(self):
		return self.__UserSetting.value("MetaData/Author")

	def setAuthor(self, author):
		self.__UserSetting.setValue("MetaData/Author",author)
	
	def contact(self):
		return self.__UserSetting.value("MetaData/Contact")

	def setContact(self, contact):
		self.__UserSetting.setValue("MetaData/Contact",contact)
	
	def setMainSession(self, mainsession: DTSession.DTMainSession):
		self.__mainsession=mainsession
		self.__mainsession.quitApp.connect(self.quit)
	
	def showMessage(self, title:str, msg:str, icon:QIcon, msecs:int=1000, clicked_slot=None):
		self.TrayIcon.showMessage(title, msg, icon, msecs)
		try:
			self.TrayIcon.messageClicked.disconnect() # 取消所有的信号槽，如果之前没有连接信号，这里会报错，所以加了个try
		except:
			pass
		self.TrayIcon.messageClicked.connect(clicked_slot)

	def restart(self):
		self.__mainsession.saveWindowStatus()
		self.__mainsession.saveData()
		self.exit()
		if self.__LoginEnable==True:
			QProcess.startDetached(sys.executable, sys.argv+[str(Fernet_Encrypt("9961",self.password())), "9961"])
		else:
			QProcess.startDetached(sys.executable, sys.argv+["9961"])
	
	def __loginIn(self):
		dlg=DTSession.DTLoginSession(self.__UserSetting.value("BasicInfo/Password"))
		if dlg.exec_()==0:
			self.quit()
			sys.exit()
		else:
			self.setPassword(dlg.input_password)
	
	def debugRun(self,password,loginEnable,show=True):
		
		self.setLoginEnable(loginEnable)
		
		# Restart
		if self.arguments()[-1]=="9961":
			if self.__LoginEnable==True:
				# print("Args:",self.arguments())
				self.setPassword(Fernet_Decrypt("9961", eval(self.arguments()[-2])))
				# print("Restart Password:",self.password())

			self.__mainsession.initialize()
			self.__mainsession.show()
			
			self.initializeTrayIcon()
			self.exec_()
		
		# Normal
		else:
			self.setPassword(password)

			self.__mainsession.initialize()
			if show==True:
				self.__mainsession.show()
			
			self.initializeTrayIcon()
			self.exec_()

	def run(self,show=True):
		"""如果没有密码加密，需要setLoginEnable(False)
		"""

		# Restart
		if self.arguments()[-1]=="9961":
			if self.__LoginEnable==True:
				# print("Args:",self.arguments())
				self.setPassword(Fernet_Decrypt("9961", eval(self.arguments()[-2])))
				# print("Restart Password:",self.password())

			self.__mainsession.initialize()
			self.__mainsession.show()
			
			self.initializeTrayIcon()
			self.exec_()
		
		# Normal
		else:
			if self.__LoginEnable==True:
				self.__loginIn()
			
			self.__mainsession.initialize()
			if show==True:
				self.__mainsession.show()
			
			self.initializeTrayIcon()
			
			self.exec_()