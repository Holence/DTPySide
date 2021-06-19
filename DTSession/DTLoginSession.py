from DTPySide.DTFunction import *
from DTPySide.DTFrame import DTDialog
from DTPySide.DTModule import DTLogin
from DTPySide import DTIcon

# Login 
class DTLoginSession(DTDialog):
	def __init__(self,locked_password):
		super().__init__(None,"Login")
		self.login=DTLogin(self)
		self.centralWidget.addWidget(self.login)
		self.setWindowTitle("Login")
		self.adjustSize()
		self.setFocus()
		self.login.lineEdit.setFocus()

		self.buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
		
		# 获取UserSetting.ini中的加密密码
		self.locked_password=locked_password
		
		#欢迎新用户
		if not self.locked_password:
			self.login.label.setPixmap(DTIcon.Happy().pixmap(QSize(28,28)))
	
	def accept(self):
		self.input_password=self.login.lineEdit.text()
		
		#新用户
		if not self.locked_password:
			self.login.label.setPixmap(DTIcon.Lock().pixmap(QSize(28,28)))
			Delay_Msecs(400)
			self.login.label.setPixmap(DTIcon.Unlock().pixmap(QSize(28,28)))
			Delay_Msecs(600)
			super().accept()
		
		elif Fernet_Decrypt(self.input_password,self.locked_password)==self.input_password:
			self.login.label.setPixmap(DTIcon.Lock().pixmap(QSize(28,28)))
			Delay_Msecs(400)
			self.login.label.setPixmap(DTIcon.Unlock().pixmap(QSize(28,28)))
			Delay_Msecs(600)
			super().accept()
		else:
			self.login.label.setPixmap(DTIcon.Unhappy().pixmap(QSize(28,28)))
	
	def reject(self):
		super().reject()