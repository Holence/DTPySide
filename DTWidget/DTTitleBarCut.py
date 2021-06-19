from DTPySide.DTFunction import *

# 其他窗口用的TitleBar Widget
from DTPySide.DTWidget.Ui_DTTitleBarCut import Ui_DTTitleBarCut
class DTTitleBarCut(Ui_DTTitleBarCut,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.Headquarter=parent
		self.label_titlebar.setHeadquarter(parent)
		
		# windowIcon是自动继承的，直接设置就好了
		self.title_icon.setIcon(self.windowIcon())
		
		self.initializeSignal()

	def initializeSignal(self):
		self.btn_close.clicked.connect(self.Headquarter.close)
	
	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.label_titlebar.setText(title)