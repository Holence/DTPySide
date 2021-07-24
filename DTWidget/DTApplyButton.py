from __future__ import annotations
from DTPySide import *

class DTApplyButton(QPushButton):
	def __init__(self,parent):
		super().__init__(parent)
		self.setIcon(QIcon(":/icon/white/white_tool.svg"))
		self.setFlat(True)
		self.setIconSize(QSize(30,30))
		self.setFixedSize(36,36)