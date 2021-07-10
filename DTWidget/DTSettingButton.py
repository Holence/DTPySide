from __future__ import annotations
from DTPySide import *

class DTSettingButton(QPushButton):
	def __init__(self,icon):
		super().__init__()
		self.setIcon(icon)
		self.setFlat(True)