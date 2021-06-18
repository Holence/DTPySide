from DongliTeahousePySideWheel.DongliTeahouseFunction import *

# MainWindow用的TitleBar Widget
from DongliTeahousePySideWheel.DongliTeahouseWidget.Ui_DongliTeahouseTitleBarFull import Ui_DongliTeahouseTitleBarFull
class DongliTeahouseTitleBarFull(Ui_DongliTeahouseTitleBarFull,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.PAPA=parent
		self.label_titlebar.setPapa(parent)
		self.initializeSignal()
	
	def initializeSignal(self):
		self.btn_close.clicked.connect(self.PAPA.close)
		self.btn_maximize.clicked.connect(self.PAPA.windowToggleMaximized)
		self.btn_minimize.clicked.connect(self.PAPA.showMinimized)
		self.btn_menu.clicked.connect(lambda:show_ContextMenu_Beneath(self.PAPA.MainMenu(),self.btn_menu))

	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.label_titlebar.setText(title)