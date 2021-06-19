from DTPySide.DTFunction import *

# MainWindow用的TitleBar Widget
from DTPySide.DTWidget.Ui_DTTitleBarFull import Ui_DTTitleBarFull
class DTTitleBarFull(Ui_DTTitleBarFull,QWidget):
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
		self.btn_maximize.clicked.connect(self.Headquarter.windowToggleMaximized)
		self.btn_minimize.clicked.connect(self.Headquarter.showMinimized)
		self.title_icon.clicked.connect(lambda:show_ContextMenu_Beneath(self.Headquarter.MainMenu(),self.title_icon))

	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.label_titlebar.setText(title)