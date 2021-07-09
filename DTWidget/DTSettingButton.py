from __future__ import annotations
from DTPySide import *

class DTSettingButton(QPushButton):
	def __init__(self,icon,font_size:int):
		super().__init__()
		btn_size=int(font_size*2)
		icon_size=int(btn_size*0.8)
		self.setFixedSize(btn_size,btn_size)
		self.setIcon(icon)
		self.setIconSize(QSize(icon_size,icon_size))
		self.setFlat(True)