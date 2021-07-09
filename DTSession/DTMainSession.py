from __future__ import annotations
from DTPySide import *

class DTMainSession(DTFrame.DTMainWindow):
	"""DTAPP的主程序
	通过DTAPP.setMainSession(DTMainSession)传入DTAPP
	相当于Qt程序最初的QMainWindow

	Args:
		DTMainWindow (这是啥): 这里要填啥

	Returns:
		没有return: 这里要填啥
	"""	
	
	quitApp=Signal()

	def closeEvent(self,event):
		super().closeEvent(event)
		self.saveWindowStatus()
		self.saveData()
		self.quitApp.emit()
	
		
	def __init__(self, app):
		"""DTMainSession的构造函数

		Args:
			app (DTAPP): 保存传入的app指针，用于调用app的UserSetting和Password
		"""
		
		super().__init__(app)
	
	def initialize(self):
		self.initializeData()
		self.initializeWindow() 
		self.restoreWindowStatus()

		self.initializeSignal()
		self.initializeMenu()
		self.initializeTrayIcon()
	
	def dataValidityCheck(self):
		return True
	
	def initializeData(self):
		if self.dataValidityCheck():
			self.loadData()
		else:
			DTFrame.DTMessageBox(self,"Error","Data Error!")
			exit()

	def restoreWindowStatus(self):
		"""MainSession中在这里恢复WindowStatu
		"""	

		self.updateFont()
		
		try:
			self.resize(self.UserSetting().value("WindowStatus/Size"))
			self.move(self.UserSetting().value("WindowStatus/Pos"))
		except:
			pass
	
	def initializeSignal(self):	
		"""主窗体的action向function链接
		注意：需要拥有全局快捷键的action，需要addAction
		"""

		self.actionSetting.triggered.connect(self.setting)
		self.actionAbout.triggered.connect(self.about)
		
		self.actionWindow_Toggle_Fullscreen.triggered.connect(self.windowToggleFullscreen)
		self.addAction(self.actionWindow_Toggle_Fullscreen)

		self.actionWindow_Toggle_Stay_on_Top.triggered.connect(self.windowToggleStayonTop)
		self.actionNormalize_Window.triggered.connect(self.windowShowNormal)
		self.actionMaximize_Window.triggered.connect(self.showMaximized)
		self.actionMinimize_Window.triggered.connect(self.showMinimized)
		
		self.actionBoss_Key.triggered.connect(self.bossComing)
		self.addAction(self.actionBoss_Key)

		self.actionExit.triggered.connect(self.close)
		self.addAction(self.actionExit)
	
	def initializeMenu(self):
		"制定menu"
		
		self._MainMenu.addAction(self.actionSetting)
		self._MainMenu.addAction(self.actionAbout)
		self._MainMenu.addSeparator()
		
		################################################################
		
		self._MainMenu.addAction(self.actionWindow_Toggle_Fullscreen)
		self._MainMenu.addAction(self.actionWindow_Toggle_Stay_on_Top)
		self._MainMenu.addAction(self.actionNormalize_Window)
		self._MainMenu.addAction(self.actionMinimize_Window)
		self._MainMenu.addAction(self.actionMaximize_Window)
		self._MainMenu.addSeparator()

		################################################################
		
		self._MainMenu.addAction(self.actionBoss_Key)
		self._MainMenu.addAction(self.actionExit)
		
	def initializeTrayIcon(self):
		"生成TrayIcon"

		self.TrayIcon=QSystemTrayIcon(self)
		
		self.TrayIcon.setIcon(QIcon(":/icon/holoicon1.ico"))
		self.TrayIcon.activated.connect(self.windowResurrection)
		self.TrayIcon.setContextMenu(self._MainMenu)
		
		self.TrayIcon.show()
	
	def windowResurrection(self,reason):
		"双击TrayIcon还原主窗体"
		
		from DTPySide import DTSession
		# 必须在这里再调用一次，如果不写的话，下面会说name 'DTSession' is not defined。不知道为什么啊啊啊，明明都在DTPySide的__init__中导入过了呀？！难道又是同级包内互相调用的问题，还是__feature__的annotation暂时还有bug？

		if reason==QSystemTrayIcon.DoubleClick:
			if self.isHidden():
				# 有Login选项
				if self.app.isLoginEnable():

					# 还未出现Login界面
					if not hasattr(self,"ResurrectionDlg"):
						self.ResurrectionDlg=DTSession.DTLoginSession(self.app,self.UserSetting().value("BasicInfo/Password"))

						#成功登回
						if self.ResurrectionDlg.exec_():
							self.showNormal()
							# 恢复self._MainMenu里的其他action
							for action in self._MainMenu.actions()[:-1]:
								action.setVisible(True)
						
						del self.ResurrectionDlg
					
					# 已经有Login界面了
					else:
						pass
				
				# 无Login选项
				else:
					self.showNormal()
			
			# 
			else:
				self.showNormal()
	
	def bossComing(self):
		self.hide()
		
		if self.app.isLoginEnable():
			# Boss键后只显示退出键，self._MainMenu里的其他action隐藏掉
			for action in self._MainMenu.actions()[:-1]:
				action.setVisible(False)
	
	def loadData(self):
		pass

	def saveData(self):
		pass
	
	def saveWindowStatus(self):
		self.UserSetting().setValue("WindowStatus/Size",self.size())
		self.UserSetting().setValue("WindowStatus/Pos",self.pos())
	
	def SaveAllEncryptData(self):
		"saveData或者UserSetting中有加密的保存项目就要放到这里（除了对密码的加密已经操作过了）"
		pass

	def updateFont(self):
		"""使用了AA_UseStyleSheetPropagationInWidgetStyles继承字体与stylesheet，用主窗体控制全局的字体
		"""

		self.setFont(self.UserSetting().value("BasicInfo/Font"))
			

	def about(self):
		about_text=""
		
		self.UserSetting().beginGroup("MetaData")
		for key in self.UserSetting().allKeys():
			about_text+="%s: %s\n"%(key,self.UserSetting().value(key))
		self.UserSetting().endGroup()

		DTFrame.DTMessageBox(self,"About",about_text[:-1])
	
	def setting(self):
		"请在继承的DTSettingSession中做到实时保存设定"
		
		from DTPySide import DTSession 
		# 必须在这里再调用一次，如果不写的话，下面会说name 'DTSession' is not defined。不知道为什么啊啊啊，明明都在DTPySide的__init__中导入过了呀？！难道又是同级包内互相调用的问题，还是__feature__的annotation暂时还有bug？
		
		dlg=DTSession.DTSettingSession(self, self.app)
		dlg.exec_()