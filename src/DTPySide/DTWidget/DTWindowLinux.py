from __future__ import annotations
from DTPySide import *

class DTWindowLinux(QWidget):
	
	def closeEvent(self, event):
		super().closeEvent(event)
	
	def show(self):
		super().show()
		if self.isMaximized():
			# 如果关掉的时候是最大化的话，再进行恢复show，就会有bug
			self.showNormal()
			self.showMaximized()
		else:
			ShowUp(self)

	def __init__(self, app:DTAPP, parent=None):
		super().__init__(parent=parent)
		self.app=app
		self.setWindowFlags(Qt.Window | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
	
	def reInitialize(self):
		self.setWindowFlags(Qt.Window | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
