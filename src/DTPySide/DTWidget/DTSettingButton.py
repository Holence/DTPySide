from __future__ import annotations
from DTPySide import *

class DTSettingButton(QPushButton):
	def __init__(self,icon):
		super().__init__()
		self.setIcon(icon)
		self.setFlat(True)
		self.setStyleSheet("""
			border: none;
			icon-size: 22px;
			max-height: 26px;
			min-height: 26px;
			min-width: 26px;
			max-width: 26px;
		""")