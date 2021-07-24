from __future__ import annotations
from DTPySide import *

class DTSettingButton(QPushButton):
	def __init__(self,icon):
		super().__init__()
		self.setIcon(icon)
		self.setFlat(True)
		self.setIconSize(QSize(30,30))
		self.setFixedSize(36,36)