from DongliTeahousePySideWheel.DongliTeahouseFunction import *

# 其他窗口用的TitleBar Widget
from DongliTeahousePySideWheel.DongliTeahouseWidget.Ui_DongliTeahouseTitleBarCut import Ui_DongliTeahouseTitleBarCut
class DongliTeahouseTitleBarCut(Ui_DongliTeahouseTitleBarCut,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.PAPA=parent
		self.label_titlebar.setPapa(parent)
		self.initializeSignal()
	
	def initializeSignal(self):
		self.btn_close.clicked.connect(self.PAPA.close)
	
	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.label_titlebar.setText(title)