from __future__ import annotations
from DTPySide import *

class DTApplyButton(QPushButton):
	def __init__(self,parent):
		super().__init__(parent)
		self.setIcon(IconFromCurrentTheme("tool.svg"))
		self.setFlat(True)
		self.setStyleSheet("""
			border: none;
			icon-size: 22px;
			max-height: 26px;
			min-height: 26px;
			min-width: 26px;
			max-width: 26px;
		""")