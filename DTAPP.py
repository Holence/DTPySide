from __future__ import annotations
from DTPySide import *


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
		self.__UserSetting=QSettings("./UserSetting.ini",QSettings.IniFormat)

		self.setStyle("Fusion")
		self.setWindowStyle()
		self.setWindowIcon(DTIcon.Holo1())

		
		self.setApplicationName("DT's Project")
		self.setApplicationVersion("0.0.0.0")
		self.setAuthor("鍵山狐")
		self.setOrganizationName("Dongli Teahouse")
		self.setOrganizationDomain("dongliteahouse.com")
		self.setContact("Holence08@gmail.com")
		
		self.setLoginEnable(True)
		self.__password=None
		self.__mainsession=None


	def setWindowStyle(self):
		"""设置MainwWindow的Window Effect和Theme

		Args:
			WindowEffect: Normal (only shadow) | Aero | Acrylic
			Theme: Dracula | Dark | Light
		"""
		
		WindowEffect=self.__UserSetting.value("BasicInfo/WindowEffect")
		
		if WindowEffect!="Normal" and WindowEffect!="Aero" and WindowEffect!="Acrylic":
			self.__UserSetting.setValue("BasicInfo/WindowEffect","Normal")
			WindowEffect=self.__UserSetting.value("BasicInfo/WindowEffect")

		Theme=self.__UserSetting.value("BasicInfo/Theme")
		if Theme!="Dracula" and Theme!="Dark" and Theme!="Light":
			self.__UserSetting.setValue("BasicInfo/Theme","Dracula")
			Theme=self.__UserSetting.value("BasicInfo/Theme")

		
		font=self.UserSetting().value("BasicInfo/Font")
		self.setStyleSheet(Generate_StyleSheet(Theme, WindowEffect, font))
		
	
	def WindowEffect(self):
		return self.__UserSetting.value("BasicInfo/WindowEffect")
	
	def setWindowEffect(self, WindowEffect:str):
		self.__UserSetting.setValue("BasicInfo/WindowEffect",WindowEffect)
	
	def Theme(self):
		return self.__UserSetting.value("BasicInfo/Theme")
	
	def setTheme(self,Theme:str):
		self.__UserSetting.setValue("BasicInfo/Theme",Theme)

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
		dlg=DTSession.DTLoginSession(self,self.__UserSetting.value("BasicInfo/Password"))
		if dlg.exec_()==0:
			self.quit()
			exit()
		else:
			self.setPassword(dlg.input_password)
	
	def debugRun(self,password,loginEnable):
		self.setLoginEnable(loginEnable)
		self.setPassword(password)
		self.__mainsession.initialize()
		self.__mainsession.show()
		sys.exit(self.exec_())

	def run(self):
		"""如果没有密码加密，需要setLoginEnable(False)
		"""		
		if self.__LoginEnable==True:
			self.__loginIn()
		
		self.__mainsession.initialize()
		self.__mainsession.show()
		sys.exit(self.exec_())