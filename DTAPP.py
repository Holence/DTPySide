from DTPySide.DTFunction import *
from DTPySide.DTPalette import *
from DTPySide.DTStyle import *
from DTPySide.DTSession import DTLoginSession,DTMainSession
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

		self.setAttribute(Qt.AA_UseOpenGLES,True)
		self.setAttribute(Qt.AA_EnableHighDpiScaling,True)
		self.setAttribute(Qt.AA_UseHighDpiPixmaps,True)

		# 继承字体
		self.setAttribute(Qt.AA_UseStyleSheetPropagationInWidgetStyles,True)
		self.setQuitOnLastWindowClosed(False)
		

		super().__init__(args)
		self.UserSetting=QSettings("./UserSetting.ini",QSettings.IniFormat)

		self.setStyle("Fusion")
		# self.setWindowStyle((0,0))
		self.setWindowIcon(DTIcon.Holo1())

		
		self.setApplicationName("DT's Project")
		self.setApplicationVersion("0.0.0.0")
		self.setAuthor("鍵山狐")
		self.setOrganizationName("Dongli Teahouse")
		self.setOrganizationDomain("dongliteahouse.com")
		self.setContact("Holence08@gmail.com")
		
		self.setLoginEnable(True)
		self.__password=None
		self.__mainwindow=None


	def setWindowStyle(self,type:tuple):
		"""设置MainwWindow的Window Effect和Theme

		Args:
			type (tuple): (Window Effect : int, Theme : int)
			
			Window Effect : 0-Only shadow | 1-Areo | 2-Acrylic
			
			Theme ：0-Dracula | 1-Dark
		"""
		self.__WindowEffect=type[0]
		Theme=type[1]
		print(self.__WindowEffect,Theme)
		if Theme==0:
			if self.__WindowEffect==0:
				self.setPalette(DTDraculaPalette())
				self.setStyleSheet(DTDraculaNormalStyle)
			elif self.__WindowEffect==1 or self.__WindowEffect==2:
				self.setPalette(DTDraculaPalette())
				self.setStyleSheet(DTDraculaEffectStyle)
		if Theme==1:
			if self.__WindowEffect==0:
				self.setPalette(DTDarkPalette())
				self.setStyleSheet(DTDarkNormalStyle)
			elif self.__WindowEffect==1 or self.__WindowEffect==2:
				self.setPalette(DTDarkPalette())
				self.setStyleSheet(DTDarkEffectStyle)

	
	def getWindowEffect(self):
		return self.__WindowEffect
	
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
	
	def setMainSession(self,mainwindow:DTMainSession):
		self.__mainwindow=mainwindow
		self.__mainwindow.quitApp.connect(self.quit)
	
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
		self.__mainwindow.initialize()
		self.__mainwindow.show()
		sys.exit(self.exec_())

	def run(self):
		"""如果没有密码加密，需要setLoginEnable(False)
		"""		
		if self.__LoginEnable==True:
			self.__loginIn()
		
		self.__mainwindow.initialize()
		self.__mainwindow.show()
		sys.exit(self.exec_())