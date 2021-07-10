from __future__ import annotations
from DTPySide import *

# MessageBox Module
from DTPySide.DTFrame.Ui_DTMessageBox import Ui_DTMessageBox
class DTMessageBox(Ui_DTMessageBox,QDialog):
	"传入title、messageText和icon的地址（建议使用DTIcon的内置Icon）"

	def __init__(self,parent,title,messageText,icon=None):
		super().__init__(parent)
		self.setupUi(self)
		
		# 无边框
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
		
		# 现在有全局stylesheet和AA_UseStyleSheetPropagationInWidgetStyles了，就不用一个个写继承字体了
		# Makes a toplevel window inherit font, palette and locale from its parent.
		# self.setAttribute(Qt.WA_WindowPropagation,True)
		
		# 缩放角
		self.setSizeGripEnabled(True)
		
		self.TitleBar.setWindowTitle(title)
		self.TitleBar.setFull(False)
		self.TitleBar.updateWindowIcon()

		self.label_message.setText(messageText)
		
		if icon!=None:
			icon_pic=icon.pixmap(QSize(64,64))
			self.label_icon.setPixmap(icon_pic)
		else:
			self.label_icon.hide()

		self.adjustSize()
		self.exec_()