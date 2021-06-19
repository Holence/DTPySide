from DTPySide.DTFunction import *

class DTSettingButton(QPushButton):
	def __init__(self,icon):
		super().__init__()
		self.setFixedSize(30,30)
		self.setIcon(icon)
		self.setIconSize(QSize(30,30))
		self.setFlat(True)