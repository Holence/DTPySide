from __future__ import annotations
from DTPySide import *

# Dialog
from DTPySide.DTFrame.Ui_DTDialogLinux import Ui_DTDialogLinux
class DTDialogLinux(Ui_DTDialogLinux,QDialog):
	def __init__(self, parent, title):
		
		if parent==None:
			# Login
			super().__init__()
		else:
			super().__init__(parent)

		self.setupUi(self)
		
		# 现在有全局stylesheet和AA_UseStyleSheetPropagationInWidgetStyles了，就不用一个个写继承字体了
		# Makes a toplevel window inherit font, palette and locale from its parent.
		# self.setAttribute(Qt.WA_WindowPropagation,True)
		
		# 缩放角
		self.setSizeGripEnabled(True)

		self.setWindowTitle(title)

		# 默认cancel
		# self.setDefaultButton(QDialogButtonBox.Cancel)
		self.setDefaultButton(QDialogButtonBox.Ok)
		
		self.adjustSize()
		MoveToCenterOfScreen(self)

	def setCentralWidget(self, widget):
		self.centralWidget.addWidget(widget)
	
	def setButtonBox(self,btns:QDialogButtonBox.StandardButton):
		self.buttonBox.setStandardButtons(btns)

	def setDefaultButton(self,btn:QDialogButtonBox.StandardButton):
		self.buttonBox.button(btn).setDefault(True)