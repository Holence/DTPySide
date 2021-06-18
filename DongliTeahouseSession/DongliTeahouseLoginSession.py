from DongliTeahousePySideWheel.DongliTeahouseFunction import *
from DongliTeahousePySideWheel.DongliTeahouseFrame import DongliTeahouseDialog
from DongliTeahousePySideWheel.DongliTeahouseModule import DongliTeahouseLogin
from DongliTeahousePySideWheel import DongliTeahouseIcon

# Login 
class DongliTeahouseLoginSession(DongliTeahouseDialog):
	def __init__(self,locked_password):
		super().__init__(None,"Login")
		self.login=DongliTeahouseLogin(self)
		self.centralWidget.addWidget(self.login)
		self.setWindowTitle("Login")
		self.adjustSize()
		self.setFocus()
		self.login.lineEdit.setFocus()
		
		# 获取UserSetting.ini中的加密密码
		self.locked_password=locked_password
		
		#欢迎新用户
		if not self.locked_password:
			self.login.label.setPixmap(DongliTeahouseIcon.Happy().pixmap(QSize(28,28)))
	
	def accept(self):
		self.input_password=self.login.lineEdit.text()
		
		#新用户
		if not self.locked_password:
			self.login.label.setPixmap(DongliTeahouseIcon.Lock().pixmap(QSize(28,28)))
			Delay_Msecs(400)
			self.login.label.setPixmap(DongliTeahouseIcon.Unlock().pixmap(QSize(28,28)))
			Delay_Msecs(600)
			super().accept()
		
		elif Fernet_Decrypt(self.input_password,self.locked_password)==self.input_password:
			self.login.label.setPixmap(DongliTeahouseIcon.Lock().pixmap(QSize(28,28)))
			Delay_Msecs(400)
			self.login.label.setPixmap(DongliTeahouseIcon.Unlock().pixmap(QSize(28,28)))
			Delay_Msecs(600)
			super().accept()
		else:
			self.login.label.setPixmap(DongliTeahouseIcon.Unhappy().pixmap(QSize(28,28)))
	
	def reject(self):
		super().reject()