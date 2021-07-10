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
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
		
		# 现在有全局stylesheet和AA_UseStyleSheetPropagationInWidgetStyles了，就不用一个个写继承字体了
		# Makes a toplevel window inherit font, palette and locale from its parent.
		# self.setAttribute(Qt.WA_WindowPropagation,True)
		
		# 缩放角
		self.setSizeGripEnabled(True)

		# 默认cancel
		self.buttonBox.button(QDialogButtonBox.Cancel).setDefault(True)

		self.TitleBar.setWindowTitle(title)
		self.TitleBar.setFull(False)
		self.TitleBar.updateWindowIcon()
		
		self.adjustSize()