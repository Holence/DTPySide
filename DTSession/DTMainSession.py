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
			app (DTAPP): 保存传入的app指针
		"""
		
		super().__init__(app)
	
	def initialize(self):
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
			pass
	
	def initializeSignal(self):
		"""主窗体的action向function链接
		注意：需要拥有全局快捷键的action，需要addAction
		"""
		super().initializeSignal()
		self.actionExit.triggered.connect(self.quitApp.emit)
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
		
		self.__menu_view=QMenu("View",self)
		self.__menu_view.setIcon(QIcon(":/icon/white/white_eye.svg"))
		self.__menu_view.addAction(self.actionWindow_Toggle_Stay_on_Top)
		self.__menu_view.addAction(self.actionWindow_Toggle_Fullscreen)
		self.__menu_view.addAction(self.actionNormalize_Window)
		self.__menu_view.addAction(self.actionMinimize_Window)
		self.__menu_view.addAction(self.actionMaximize_Window)
		self.addMenuToMainMenu(self.__menu_view)
		
		self._MainMenu.addAction(self.actionBoss_Key)
		self._MainMenu.addAction(self.actionExit)
		
	
	
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
		pass

	def saveData(self):
		pass
	
	def saveWindowStatus(self):
		self.UserSetting().setValue("WindowStatus/Size",self.size())
		self.UserSetting().setValue("WindowStatus/Pos",self.pos())
	
	def saveAllEncryptData(self):
		"saveData或者UserSetting中有加密的保存项目就要放到这里（更改密码的时候会调用这个函数）"
		pass
	
	def backup(self):
		# 可以implement这个函数，比如先保存一下

		class BackUpThread(QThread):
			def __init__(self, parent, backup_dst, backup_list):
				super().__init__(parent=parent)
				self.backup_dst=backup_dst
				self.backup_list=backup_list
			
			def run(self):
				new_folder_dst=os.path.join(self.backup_dst,WhatDayIsToday("0"))
				if not os.path.exists(new_folder_dst):
					os.makedirs(new_folder_dst)
				for url in self.backup_list:
					file_dst=os.path.join(new_folder_dst,os.path.basename(url))
					shutil.copyfile(url,file_dst)
		
		backup_dst=self.app.BackupDst()
		if backup_dst==False:
			DTFrame.DTMessageBox(self,"Warning","Please set backup dst first!",DTIcon.Warning())
		elif not os.path.exists(backup_dst):
			DTFrame.DTMessageBox(self,"Warning","Backup Dst %s does not exsit!"%backup_dst,DTIcon.Warning())
		else:
			self.backup_thread=BackUpThread(self,backup_dst,self.app.BackupList())
			self.backup_thread.finished.connect(self.backup_thread.deleteLater)
			self.backup_thread.finished.connect(lambda:self.app.TrayIcon.showMessage("Information","Data backup completed."))
			self.backup_thread.start()

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