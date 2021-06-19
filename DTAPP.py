from DTPySide.DTFunction import *
from DTPySide.DTPalette import DTDraculaPalette
from DTPySide.DTStyle import DTDraculaStyle
from DTPySide.DTSession import DTLoginSession
from DTPySide import DTIcon

# APP
class DTAPP(QApplication):
	"""DTAPP注释


	Args:
		QApplication ([type]): [description]
	"""
	
	def __init__(self,args):
		"""asd

		Args:
			args (asd): asddas
		"""

		self.setAttribute(Qt.AA_UseOpenGLES)
		self.setAttribute(Qt.AA_EnableHighDpiScaling)
		self.setAttribute(Qt.AA_UseHighDpiPixmaps)

		# 继承字体
		self.setAttribute(Qt.AA_UseStyleSheetPropagationInWidgetStyles)
		

		super().__init__(args)
		self.UserSetting=QSettings("./UserSetting.ini",QSettings.IniFormat)

		self.setStyle("Fusion")
		self.setStyleSheet(DTDraculaStyle)
		self.setPalette(DTDraculaPalette())

		self.setWindowIcon(DTIcon.Holo1())
		self.setQuitOnLastWindowClosed(False)
		
		self.setApplicationName("DT's Project")
		self.setApplicationVersion("0.0.0.0")
		self.setAuthor("鍵山狐")
		self.setOrganizationName("Dongli Teahouse")
		self.setOrganizationDomain("dongliteahouse.com")
		self.setContact("Holence08@gmail.com")
		
		self.setLoginEnable(True)
		self.__password=None
	
	def setApplicationName(self,str):
		super().setApplicationName(str)
		self.UserSetting.setValue("MetaData/ApplicationName",self.applicationName())
	
	def setApplicationVersion(self,str):
		super().setApplicationVersion(str)
		self.UserSetting.setValue("MetaData/ApplicationVersion",self.applicationVersion())
	
	def setOrganizationName(self,str):
		super().setOrganizationName(str)
		self.UserSetting.setValue("MetaData/OrganizationName",self.organizationName())
	
	def setOrganizationDomain(self,str):
		super().setOrganizationDomain(str)
		self.UserSetting.setValue("MetaData/OrganizationDomain",self.organizationDomain())

	def isLoginEnable(self):
		return self.__LoginEnable
	
	def setLoginEnable(self,bool=True):
		self.__LoginEnable=bool

	def password(self):
		return self.__password
	
	def setPassword(self,password):
		self.__password=password
		self.UserSetting.setValue("BasicInfo/Password",Fernet_Encrypt(self.__password,self.__password))

	def author(self):
		return self.__author

	def setAuthor(self,author):
		self.__author=author
		self.UserSetting.setValue("MetaData/Author",self.author())
	
	def contact(self):
		return self.__contact

	def setContact(self,contact):
		self.__contact=contact
		self.UserSetting.setValue("MetaData/Contact",self.contact())
	
	def setMainSession(self,mainwindow):
		self.mainwindow=mainwindow
		self.mainwindow.quitApp.connect(self.quit)
	
	def __loginIn(self):
		dlg=DTLoginSession(self.UserSetting.value("BasicInfo/Password"))
		if dlg.exec_()==0:
			self.quit()
			exit()
		else:
			self.setPassword(dlg.input_password)
	
	def debugRun(self,password,loginEnable):
		self.setLoginEnable(loginEnable)
		self.setPassword(password)
		self.mainwindow.initialize()
		self.mainwindow.show()
		sys.exit(self.exec_())

	def run(self):
		if self.__LoginEnable==True:
			self.__loginIn()
		
		self.mainwindow.initialize()
		self.mainwindow.show()
		sys.exit(self.exec_())