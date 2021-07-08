from __future__ import annotations
from DTPySide import *

# Dialog Module
from DTPySide.DTFrame.Ui_DTDialog import Ui_DTDialog
class DTDialog(Ui_DTDialog,QDialog):
	def __init__(self,parent,title):
		if parent==None:
			super().__init__()
		else:
			super().__init__(parent)
		
		self.setupUi(self)
		
		# 无边框
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
		
		# 继承字体
		self.setAttribute(Qt.WA_WindowPropagation,True)
		if 0.7*self.font().pointSize()>=9:
			self.buttonBox.setFont(Font_Resize(self.font(),0.7))
		
		# 缩放角
		self.setSizeGripEnabled(True)

		# 默认cancel
		self.buttonBox.button(QDialogButtonBox.Cancel).setDefault(True)

		self.TitleBar.setWindowTitle(title)
		self.TitleBar.setFull(False)
		self.TitleBar.updateWindowIcon()
		
		self.adjustSize()