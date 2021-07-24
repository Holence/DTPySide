from __future__ import annotations
from DTPySide import *

# Login 
class DTLoginSession(DTFrame.DTDialog):
	def __init__(self,locked_password):
		super().__init__(None,"Login")
		self.__LoginModule=DTModule.DTLogin(self)
		self.setCentralWidget(self.__LoginModule)
		self.setWindowTitle("Login")

		self.buttonBox.button(QDialogButtonBox.Ok).setDefault(True)

		# 获取UserSetting.ini中的加密密码
		self.locked_password=locked_password
		
		#欢迎新用户
		if not self.locked_password:
			self.__LoginModule.label_lock.setPixmap(DTIcon.Happy().pixmap(QSize(64,64)))
		
		self.setFocus()
		self.__LoginModule.lineEdit.setFocus()
	
	def accept(self):
		self.input_password=self.__LoginModule.lineEdit.text()
		
		#新用户
		if not self.locked_password:
			self.__LoginModule.label_lock.setPixmap(DTIcon.Lock().pixmap(QSize(64,64)))
			Delay_Msecs(400)
			self.__LoginModule.label_lock.setPixmap(DTIcon.Unlock().pixmap(QSize(64,64)))
			Delay_Msecs(600)
			super().accept()
		
		elif Fernet_Decrypt(self.input_password,self.locked_password)==self.input_password:
			self.__LoginModule.label_lock.setPixmap(DTIcon.Lock().pixmap(QSize(64,64)))
			Delay_Msecs(400)
			self.__LoginModule.label_lock.setPixmap(DTIcon.Unlock().pixmap(QSize(64,64)))
			Delay_Msecs(600)
			super().accept()
		else:
			self.__LoginModule.label_lock.setPixmap(DTIcon.Unhappy().pixmap(QSize(64,64)))
	
	def reject(self):
		super().reject()