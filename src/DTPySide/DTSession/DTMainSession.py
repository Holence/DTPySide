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

	def __init__(self, app):
		"""DTMainSession的构造函数

		Args:
			app (DTAPP): 保存传入的app指针
		"""
		
		super().__init__(app)

		self.haveTanslation=hasattr(self.app,"translation")
			
	
	def initialize(self):
		if self.haveTanslation==False and hasattr(self.app,"translation")==True:
			raise("You Must load the translation module before the construction of MainSession!")
		else:
			del self.haveTanslation
		
		self.initializeData()
		self.initializeWindow()
		self.restoreWindowStatus()

		self.initializeSignal()
		self.initializeMenu()
	
	def dataValidityCheck(self):
		return True
	
	def initializeData(self):
		if self.dataValidityCheck():
			self.loadData()
		else:
			DTFrame.DTMessageBox(self,"Error","Data is not valid!")
			self.app.quit()

	def restoreWindowStatus(self):
		"""MainSession中在这里恢复WindowStatu
		"""	
		
		try:
			self.resize(self.UserSetting().value("WindowStatus/Size"))
			self.move(self.UserSetting().value("WindowStatus/Pos"))
		except:
			self.resize(self.minimumWidth(),self.minimumHeight())
			self.adjustSize()
			MoveToCenterOfScreen(self)
	
	def initializeSignal(self):
		"""主窗体的action向function链接
		注意：需要拥有全局快捷键的action，需要addAction
		"""
		super().initializeSignal()
		
		self.actionExit.triggered.connect(self.quit)
		if self.app.isQuitOnClickX():
			self.TitleBar.btn_close.clicked.connect(self.quit)
		else:
			self.TitleBar.btn_close.clicked.connect(self.close)

		self.actionSetting.triggered.connect(self.setting)
		self.actionAbout.triggered.connect(self.about)
		self.actionBoss_Key.triggered.connect(self.bossComing)
		self.addAction(self.actionBoss_Key)

		if self.app.isBackupEnable():
			self.actionBackup.triggered.connect(self.backup)
	
	def initializeMenu(self):
		"制定menu"

		if self.app.isBackupEnable():
			self._MainMenu.addAction(self.actionBackup)
			self._MainMenu.addSeparator()
		
		################################################################

		self._MainMenu.addAction(self.actionSetting)
		self._MainMenu.addAction(self.actionAbout)
		self._MainMenu.addSeparator()
		
		################################################################
		
		self.__menu_view=QMenu(QCoreApplication.translate("DTMainWindow","View"),self) #这里不能用self.tr，因为如果被继承了，这里的self将会是子类，而在qm翻译文件的context中记录的是DTMainSWindow的翻译
		self.__menu_view.setIcon(IconFromCurrentTheme("eye.svg"))
		self.__menu_view.addAction(self.actionWindow_Toggle_Stay_on_Top)
		self.__menu_view.addAction(self.actionWindow_Toggle_Fullscreen)
		self.__menu_view.addAction(self.actionNormalize_Window)
		self.__menu_view.addAction(self.actionMinimize_Window)
		self.__menu_view.addAction(self.actionMaximize_Window)
		self.addMenuToMainMenu(self.__menu_view)
		
		self._MainMenu.addAction(self.actionBoss_Key)
		self._MainMenu.addAction(self.actionExit)
		
	def refresh(self):
		""""改变颜色后，可能有些依赖于app.color_list的颜色要更新，在这里添加对所有窗体的刷新操作"
		"""
		pass
	
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
						self.ResurrectionDlg=DTSession.DTLoginSession(self.UserSetting().value("BasicInfo/Password"))

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
		"""这里请用self.app.DataDir获取Data的路径
		"""
		pass

	def saveData(self):
		"""这里请用self.app.DataDir获取Data的路径
		"""
		pass
	
	def saveWindowStatus(self):
		self.UserSetting().setValue("WindowStatus/Size",self.size())
		self.UserSetting().setValue("WindowStatus/Pos",self.pos())
	
	def saveAllEncryptData(self):
		"saveData或者UserSetting中有加密的保存项目就要放到这里（更改密码的时候会调用这个函数）"
		if self.app.DataDir()!=None:
			self.app.setDataDir(self.app.DataDir())
		if self.app.isBackupEnable() and self.app.BackupDst()!=None:
			self.app.setBackupDst(self.app.BackupDst())
		
	def backup(self):
		# 可以implement这个函数，比如先保存一下

		class BackUpThread(QThread):
			def __init__(self, parent, data_dir, data_list):
				super().__init__(parent=parent)
				self.data_dir=data_dir
				self.data_list=data_list
			
			def run(self):
				if not os.path.exists(new_folder_dst):
					os.makedirs(new_folder_dst)
				for file in self.data_list:
					file_dst=os.path.join(new_folder_dst,file)
					shutil.copyfile(os.path.join(self.data_dir,file),file_dst)
		
		backup_dst=self.app.BackupDst()
		if backup_dst==None:
			DTFrame.DTMessageBox(self,"Warning","Please set backup dst first!",DTIcon.Warning())
		elif not os.path.exists(backup_dst):
			DTFrame.DTMessageBox(self,"Warning","Backup Dst %s does not exsit!"%backup_dst,DTIcon.Warning())
		else:
			new_folder_dst=os.path.join(backup_dst,WhatDayIsToday(1).toString("yyyyMMdd")).replace("/","\\")
			self.backup_thread=BackUpThread(self, self.app.DataDir(), self.app.DataList())
			self.backup_thread.finished.connect(self.backup_thread.deleteLater)
			self.backup_thread.finished.connect(lambda:self.app.showMessage("Information", "Data backup completed.", DTIcon.Information(), clicked_slot=lambda:os.popen("explorer /select,\"%s\""%new_folder_dst)))
			self.backup_thread.start()

	def about(self):
		about_text=""
		
		self.UserSetting().beginGroup("MetaData")
		for key in self.UserSetting().allKeys():
			about_text+="%s: %s\n"%(key,self.UserSetting().value(key))
		self.UserSetting().endGroup()

		DTFrame.DTMessageBox(self,"About",about_text[:-1],icon=DTIcon.Holo01())
	
	def setting(self):
		"请在继承的DTSettingSession中做到实时保存设定"
		
		from DTPySide import DTSession
		# 必须在这里再调用一次，如果不写的话，下面会说name 'DTSession' is not defined。不知道为什么啊啊啊，明明都在DTPySide的__init__中导入过了呀？！难道又是同级包内互相调用的问题，还是__feature__的annotation暂时还有bug？
		
		dlg=DTSession.DTSettingSession(self, self.app)
		dlg.exec_()
	
	def quit(self):
		self.saveWindowStatus()
		self.saveData()
		self.app.quit()