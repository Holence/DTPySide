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
		self.setQuitOnClickX(True)
		
		super().__init__(args)
		
		self.setStyle("Fusion")
		self.ThemeList=["Dracula","Dracula Customized","Brown","Green","Cyan","White"]
		self.initializeWindowStyle()
		
		self.TrayIcon=QSystemTrayIcon(self)

		self.setWindowIcon(DTIcon.HoloIcon1())
		self.setApplicationName("DTPySide Project")
		self.setApplicationVersion("0.0.0.0")
		self.setAuthor("鍵山狐")
		self.setOrganizationName("Dongli Teahouse")
		self.setOrganizationDomain("dongliteahouse.wordpress.com")
		self.setContact("Holence08@gmail.com")
		
		self.setDataList([])
		self.setLoginEnable(False)
		self.setBackupEnable(False)
	
	def initializeTrayIcon(self):
		"生成TrayIcon"
		
		self.TrayIcon.setIcon(self.windowIcon())
		self.TrayIcon.activated.connect(self.__mainsession.windowResurrection)
		self.TrayIcon.setContextMenu(self.__mainsession._MainMenu)
		
		self.TrayIcon.show()

	def initializeWindowStyle(self, refresh=False):
		"""生成color_list，并设置MainwWindow的Window Effect和Theme
		"""

		def changeColor(color_list,new_hue:float,new_saturation:float,new_luminance:float,contrast:float,reverse:bool):
			hue_offset=new_hue-colour.Color(color_list[1]).get_hue()
			sat_offset=new_saturation-0.5
			lum_offset=new_luminance-0.5

			if reverse:
				color=colour.Color(color_list[-1])
				r,g,b=color.get_rgb()
				r=1-r
				g=1-g
				b=1-b
				color=colour.Color()
				color.set_rgb((r,g,b))
				color_list[-1]=color.get_web()
			
			contrast=contrast-0.5
			std_lum=max(min(colour.Color(color_list[1]).get_luminance()+lum_offset,1),0)

			for i in range(len(color_list)):
				color=colour.Color(color_list[i])
				if new_hue!=-1:
					color.set_hue((color.get_hue()+hue_offset)%360)
				
				if i>=len(color_list)-3:
					new_saturation=max(min(color.get_saturation()+sat_offset*0.5,1),0)
					new_luminance=max(min(color.get_luminance()+lum_offset*0.5,1),0)
					new_luminance=max(min(new_luminance+(new_luminance-std_lum)*contrast*0.5,1),0)
				else:
					new_saturation=max(min(color.get_saturation()+sat_offset,1),0)
					new_luminance=max(min(color.get_luminance()+lum_offset,1),0)
					new_luminance=max(min(new_luminance+(new_luminance-std_lum)*contrast,1),0)
				
				color.set_saturation(new_saturation)
				color.set_luminance(new_luminance)
				
				color_list[i]=color.get_web()
			
			return color_list

		# DEEPDARK="#191A21" # Border和GroupBox、TitleBarFrame的Background
		# BACKGROUND="#21222C" # background
		# SOFTDARK="#282A36" # LineEdit、QPushButton的背景
		# DIM="#404257" # disable的文字、Itemview的item的背景
		# PRESSED = "#A67DB4" # Button Clicked 
		# FOCUSED="#8C6BBB" # Button Hover、text selection
		# TEXT="#E0E0E0" # 文字
		# ICONCOLOR="white" # 部分icon的颜色（暂未适配ui文件中指派的icon）
		
		white_or_black=["white","black"]
		theme=self.Theme()
		hue=self.Hue()
		saturation=self.Saturation()
		luminance=self.Luminance()
		contrast=self.Contrast()
		reverse=self.Reverse()

		if theme=="Dracula":
			self.color_list=["#191A21","#21222C","#282A36","#404257", "#A67DB4","#8C6BBB","#E0E0E0"]
			QIcon.setThemeName(white_or_black[reverse])
		elif theme=="Dracula Customized":
			self.color_list=["#202329","#282C34","#313341","#404257","#D7AAE6","#BD93F9","#EBEBEB"]
			QIcon.setThemeName(white_or_black[reverse])
		elif theme=="Brown":
			self.color_list=["#202020","#2A2A2A","#353535","#5c5c5c","#7AB6F3","#2A82DA","#FFFFFF"]
			QIcon.setThemeName(white_or_black[reverse])
		elif theme=="Green":
			self.color_list=["#17241F","#294137","#3F6151","#5D796C","#C6CA8F","#A5AD79","#EEF1E0"]
			QIcon.setThemeName(white_or_black[reverse])
		elif theme=="Cyan":
			self.color_list=["#2a3e63","#395693","#456eb8","#8099ce","#cbdbe7","#a1bdd2","#FFFFFF"]
			QIcon.setThemeName(white_or_black[reverse])
		elif theme=="White":
			self.color_list=["#aaaaaa","#ffffff","#dddddd","#9B9B9B","#eeeeee","#dae3ea","#333333"]
			QIcon.setThemeName(white_or_black[not reverse])
		
		if hue!=-1 or saturation!=0.5 or luminance!=0.5 or contrast!=0.5:
			self.color_list=changeColor(self.color_list,hue,saturation,luminance,contrast,reverse)

		self.setStyleSheet(DTStyleSheet(self.color_list, self.WindowEffect(), self.Font()))

		if refresh==True:
			self.__mainsession.refresh()

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
		if self.UserSetting().value("BasicInfo/Font")==None:
			font=QFont()
			font.setFamily("Meiryo UI")
			font.setPointSize(18)
			self.setFont(font)
		return self.UserSetting().value("BasicInfo/Font")
	
	def setFont(self, font:QFont):
		self.UserSetting().setValue("BasicInfo/Font",font)

	def Scale(self):
		if self.UserSetting().value("BasicInfo/Scale")==None or float(self.UserSetting().value("BasicInfo/Scale"))<1:
			self.setScale(1.0)
		return float(self.UserSetting().value("BasicInfo/Scale"))
	
	def setScale(self, scale:float):
		self.UserSetting().setValue("BasicInfo/Scale",str(scale))
	
	def WindowEffect(self):
		if self.UserSetting().value("BasicInfo/WindowEffect") not in ["Normal","Aero","Acrylic"]:
			self.setWindowEffect("Normal")
		elif sys.platform!="win32":
			self.setWindowEffect("Normal")
		return self.UserSetting().value("BasicInfo/WindowEffect")
	
	def setWindowEffect(self, WindowEffect:str):
		self.UserSetting().setValue("BasicInfo/WindowEffect",WindowEffect)
	
	def Theme(self):
		if self.UserSetting().value("BasicInfo/Theme") not in self.ThemeList:
			self.setTheme("Cyan")
		return self.UserSetting().value("BasicInfo/Theme")
	
	def setTheme(self, Theme:str):
		self.setHue(-1)
		self.setSaturation(0.5)
		self.setLuminance(0.5)
		self.setContrast(0.5)
		self.setReverse(False)
		self.UserSetting().setValue("BasicInfo/Theme",Theme)
	
	def Hue(self):
		if self.UserSetting().value("BasicInfo/Hue")==None:
			self.setHue(-1)
		else:
			Hue=float(self.UserSetting().value("BasicInfo/Hue"))
			if not 0<=Hue<=1 and Hue!=-1:
				self.setHue(-1)
		return float(self.UserSetting().value("BasicInfo/Hue"))
	
	def setHue(self, hue:float):
		self.UserSetting().setValue("BasicInfo/Hue",str(hue))

	def Saturation(self):
		if self.UserSetting().value("BasicInfo/Saturation")==None:
			self.setSaturation(0.5)
		else:
			Saturation=float(self.UserSetting().value("BasicInfo/Saturation"))
			if not 0<=Saturation<=1:
				self.setSaturation(0.5)
		return float(self.UserSetting().value("BasicInfo/Saturation"))
	
	def setSaturation(self, saturation:float):
		self.UserSetting().setValue("BasicInfo/Saturation",str(saturation))

	def Luminance(self):
		if self.UserSetting().value("BasicInfo/Luminance")==None:
			self.setLuminance(0.5)
		else:
			Luminance=float(self.UserSetting().value("BasicInfo/Luminance"))
			if not 0<=Luminance<=1:
				self.setLuminance(0.5)
		return float(self.UserSetting().value("BasicInfo/Luminance"))
	
	def setLuminance(self, luminance:float):
		self.UserSetting().setValue("BasicInfo/Luminance",str(luminance))
	
	def Contrast(self):
		if self.UserSetting().value("BasicInfo/Contrast")==None:
			self.setContrast(0.5)
		else:
			Contrast=float(self.UserSetting().value("BasicInfo/Contrast"))
			if not 0<=Contrast<=1:
				self.setContrast(0.5)
		return float(self.UserSetting().value("BasicInfo/Contrast"))
	
	def setContrast(self, contrast:float):
		self.UserSetting().setValue("BasicInfo/Contrast",str(contrast))

	def Reverse(self):
		if self.UserSetting().value("BasicInfo/Reverse")==None:
			self.setReverse(False)
		
		Reverse = self.UserSetting().value("BasicInfo/Reverse")
		Reverse = True if Reverse=="True" else False
		return Reverse

	def setReverse(self, reverse:bool):
		self.UserSetting().setValue("BasicInfo/Reverse",str(reverse))

	def Language(self):
		return self.UserSetting().value("BasicInfo/Language")
	
	def setLanguage(self, Language:str):
		self.UserSetting().setValue("BasicInfo/Language",Language)
	
	def Country(self):
		return self.UserSetting().value("BasicInfo/Country")
	
	def setCountry(self, Country:str):
		self.UserSetting().setValue("BasicInfo/Country",Country)

	def setApplicationName(self, str):
		super().setApplicationName(str)
		self.UserSetting().setValue("MetaData/ApplicationName",self.applicationName())
	
	def setApplicationVersion(self, str):
		super().setApplicationVersion(str)
		self.UserSetting().setValue("MetaData/ApplicationVersion",self.applicationVersion())
	
	def setOrganizationName(self, str):
		super().setOrganizationName(str)
		self.UserSetting().setValue("MetaData/OrganizationName",self.organizationName())
	
	def setOrganizationDomain(self, str):
		super().setOrganizationDomain(str)
		self.UserSetting().setValue("MetaData/OrganizationDomain",self.organizationDomain())

	def UserSetting(self):
		return self.__UserSetting

	def setQuitOnClickX(self, bool):
		self.__quit_on_click_x=bool
	
	def isQuitOnClickX(self):
		return self.__quit_on_click_x
	
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
			
			self.__data_dir=new_dir
			if self.isLoginEnable():
				self.UserSetting().setValue("BasicInfo/DataDir",Symmetric_Encrypt(self.password(), self.__data_dir, iteration=self.iteration()))
			else:
				self.UserSetting().setValue("BasicInfo/DataDir",self.__data_dir)
		else:
			DTFrame.DTMessageBox(None,"Error","Data Dir does not exsit!",DTIcon.Error())
	
	def DataDir(self):
		if self.UserSetting().value("BasicInfo/DataDir")==None:
			self.__data_dir=os.getcwd()
			if self.isLoginEnable():
				self.UserSetting().setValue("BasicInfo/DataDir",Symmetric_Encrypt(self.password(), self.__data_dir, iteration=self.iteration()))
			else:
				self.UserSetting().setValue("BasicInfo/DataDir",self.__data_dir)
		return self.__data_dir

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
		if self.DataList()==[] and bool==True:
			raise("Please setDataList before setBackEnable.")
		else:
			self.__BackupEnable=bool
	
	def setBackupDst(self, dst:str):
		"""设置面板中设置备份地址

		Args:
			dst (str): 备份的目的地
		"""
		if self.isBackupEnable():
			if os.path.exists(dst):
				self.__backup_dst=dst
				if self.isLoginEnable():
					self.UserSetting().setValue("BasicInfo/BackupDst",Symmetric_Encrypt(self.password(), self.__backup_dst, iteration=self.iteration()))
				else:
					self.UserSetting().setValue("BasicInfo/BackupDst",self.__backup_dst)
			else:
				DTFrame.DTMessageBox(None,"Error","Backup Dst does not exsit!",DTIcon.Error())
		else:
			raise("Please setBackupEnable before setBackupDst.")
	
	def BackupDst(self):
		return self.__backup_dst

	def password(self):
		return self.__password
	
	def setPassword(self, password):
		self.__password=password
		self.UserSetting().setValue("BasicInfo/Password",Symmetric_Encrypt(self.password(), self.password(), iteration=self.iteration()))

	def iteration(self):
		if self.UserSetting().value("BasicInfo/Iteration")==None or int(self.UserSetting().value("BasicInfo/Iteration"))<1:
			self.setIteration(48000)
		return int(self.UserSetting().value("BasicInfo/Iteration"))
	
	def setIteration(self, iteration):
		self.UserSetting().setValue("BasicInfo/Iteration", iteration)

	def author(self):
		return self.UserSetting().value("MetaData/Author")

	def setAuthor(self, author):
		self.UserSetting().setValue("MetaData/Author",author)
	
	def contact(self):
		return self.UserSetting().value("MetaData/Contact")

	def setContact(self, contact):
		self.UserSetting().setValue("MetaData/Contact",contact)
	
	def setMainSession(self, mainsession: DTSession.DTMainSession):
		self.__mainsession=mainsession
	
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
		self.__mainsession.close()
		self.exit()
		if self.isLoginEnable()==True:
			QProcess.startDetached(sys.executable, sys.argv+[str(Symmetric_Encrypt("9961", self.password(), iteration=self.iteration())), "9961"])
		else:
			QProcess.startDetached(sys.executable, sys.argv+["9961"])
	
	def __loginIn(self):
		locked_password=self.UserSetting().value("BasicInfo/Password")
		if locked_password:
			dlg=DTSession.DTLoginSession(locked_password, self.iteration())
		else:
			dlg=DTSession.DTLoginSession(locked_password, self.iteration(), "Register")
		
		if dlg.exec_()==0:
			self.quit()
			sys.exit()
		else:
			self.setPassword(dlg.input_password)
	
	def __loadEncryptedData(self):
		if self.isLoginEnable():
			self.__data_dir=Symmetric_Decrypt(self.password(), self.UserSetting().value("BasicInfo/DataDir"), iteration=self.iteration())
			if self.__data_dir==False:
				self.__data_dir=None
			self.__backup_dst=Symmetric_Decrypt(self.password(), self.UserSetting().value("BasicInfo/BackupDst"), iteration=self.iteration())
			if self.__backup_dst==False:
				self.__backup_dst=None
		else:
			self.__data_dir=self.UserSetting().value("BasicInfo/DataDir")
			self.__backup_dst=self.UserSetting().value("BasicInfo/BackupDst")
			
	def debugRun(self,password,loginEnable,show=True):
		
		self.setLoginEnable(loginEnable)
		
		# Restart
		if self.arguments()[-1]=="9961":
			if self.isLoginEnable()==True:
				# print("Args:",self.arguments())
				self.setPassword(Symmetric_Decrypt("9961", eval(self.arguments()[-2]), iteration=self.iteration()))
				# print("Restart Password:",self.password())

			self.__loadEncryptedData()
			
			self.initializeTrayIcon()
			self.__mainsession.initialize()
			self.__mainsession.show()

			self.exec_()
		
		# Normal
		else:
			self.setPassword(password)

			self.__loadEncryptedData()

			self.initializeTrayIcon()
			self.__mainsession.initialize()
			if show==True:
				self.__mainsession.show()

			self.exec_()

	def run(self,show=True):
		"""如果没有密码加密，需要setLoginEnable(False)
		"""

		# Restart
		if self.arguments()[-1]=="9961":
			if self.isLoginEnable()==True:
				# print("Args:",self.arguments())
				self.setPassword(Symmetric_Decrypt("9961", eval(self.arguments()[-2]), iteration=self.iteration()))
				# print("Restart Password:",self.password())

			self.__loadEncryptedData()

			self.initializeTrayIcon()
			self.__mainsession.initialize()
			self.__mainsession.show()

			self.exec_()
		
		# Normal
		else:
			if self.isLoginEnable()==True:
				self.__loginIn()
			
			self.__loadEncryptedData()
			
			self.initializeTrayIcon()
			self.__mainsession.initialize()
			if show==True:
				self.__mainsession.show()
			
			self.exec_()