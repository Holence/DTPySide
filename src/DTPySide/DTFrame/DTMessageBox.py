from __future__ import annotations
from DTPySide import *

# MessageBox Module
from DTPySide.DTFrame.Ui_DTMessageBox import Ui_DTMessageBox
from DTPySide.DTFrame.DTDialog import DTDialog

class MessageModule(Ui_DTMessageBox,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)

class DTMessageBox(DTDialog):
	def __init__(self,parent,title,text,icon=None,detail=""):
		super().__init__(parent,title)
		self.module=MessageModule(self)
		self.setCentralWidget(self.module)

		self.module.label_text.setText(text)
		# self.module.label_text.setOpenExternalLinks(True)

		if detail=="":
			self.module.textBrowser.hide()
		else:
			self.module.textBrowser.setText(detail)
			self.module.textBrowser.setStyleSheet('font-family:"微软雅黑"; font-size:12pt;')

		self.setButtonBox(QDialogButtonBox.Ok)
		self.setDefaultButton(QDialogButtonBox.Ok)

		if icon!=None:
			icon_pic=icon.pixmap(QSize(64,64))
			self.module.label_icon.setPixmap(icon_pic)
		else:
			self.module.label_icon.hide()
			self.module.horizontalLayout.setContentsMargins(30,10,0,5)

		self.adjustSize()
		MoveToCenterOfScreen(self)

		self.exec_()

class DTConfirmBox(DTDialog):
	def __init__(self,parent,title,text,icon=None,detail=""):
		super().__init__(parent, title)
		self.module=MessageModule(self)
		self.setCentralWidget(self.module)

		self.module.label_text.setText(text)

		if detail=="":
			self.module.textBrowser.hide()
		else:
			self.module.textBrowser.setText(detail)
			self.module.textBrowser.setStyleSheet('font-family:"微软雅黑"; font-size:12pt;')

		if icon!=None:
			icon_pic=icon.pixmap(QSize(64,64))
			self.module.label_icon.setPixmap(icon_pic)
		else:
			self.module.label_icon.setVisible(False)
			self.module.horizontalLayout.setContentsMargins(45,10,0,5)

		self.adjustSize()
		MoveToCenterOfScreen(self)