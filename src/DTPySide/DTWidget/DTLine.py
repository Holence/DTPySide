from __future__ import annotations
from DTPySide import *

class DTLine(QFrame):
	def __init__(self, parent, shape: QFrame.Shape = QFrame.HLine, shadow: QFrame.Shadow = QFrame.Sunken) -> None:
		super().__init__(parent)
		self.setFrameShape(shape)
		self.setFrameShadow(shadow)