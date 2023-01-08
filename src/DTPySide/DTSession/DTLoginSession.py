from __future__ import annotations
from DTPySide import *

# Login 
class DTLoginSession(DTFrame.DTDialog):
	def __init__(self, locked_password, iteration, title="Login"):
		super().__init__(None,title)
		self.iteration=iteration

		self.__LoginModule=DTModule.DTLogin(self)
		self.centralWidget.setContentsMargins(QMargins(9,10,32,10))
		self.setCentralWidget(self.__LoginModule)
		self.adjustSize()
		MoveToCenterOfScreen(self)

		self.setWindowTitle(title)
		self.buttonBox.button(QDialogButtonBox.Ok).setDefault(True)

		# 获取UserSetting.ini中的加密密码
		self.locked_password=locked_password
		
		#欢迎新用户
		if not self.locked_password:
			self.__LoginModule.label_lock.setPixmap(DTIcon.Happy().pixmap(QSize(64,64)))
		
		self.setFocus()
		self.__LoginModule.lineEdit.setFocus()
	
	def accept(self):

		self.__LoginModule.lineEdit.setReadOnly(True)
		self.buttonBox.setEnabled(False)
		self.input_password=self.__LoginModule.lineEdit.text()
		
		#新用户
		if not self.locked_password:
			self.__LoginModule.label_lock.setPixmap(DTIcon.Lock().pixmap(QSize(64,64)))
			Delay_Msecs(300)
			self.__LoginModule.label_lock.setPixmap(DTIcon.Unlock().pixmap(QSize(64,64)))
			Delay_Msecs(400)
			super().accept()
		
		elif Symmetric_Decrypt(self.input_password, self.locked_password, iteration=self.iteration)==self.input_password:
			self.__LoginModule.label_lock.setPixmap(DTIcon.Lock().pixmap(QSize(64,64)))
			Delay_Msecs(300)
			self.__LoginModule.label_lock.setPixmap(DTIcon.Unlock().pixmap(QSize(64,64)))
			Delay_Msecs(400)
			super().accept()
		else:
			self.__LoginModule.label_lock.setPixmap(DTIcon.Unhappy().pixmap(QSize(64,64)))
			self.__LoginModule.lineEdit.setReadOnly(False)
			self.buttonBox.setEnabled(True)
	
	def reject(self):
		super().reject()