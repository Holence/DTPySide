from DTPySide import *

from DTPySide.demo.demoSession.DemoMainSession2 import DemoMainSession2
from DTPySide.demo.demoSession.DemoSettingSession import DemoSettingSession
from DTPySide.demo.demoModule import DemoCentralWidget1,WidgetGallery

class DemoMainSession(DTSession.DTMainSession):
	def __init__(self,app):
		super().__init__(app)
		
	def initializeWindow(self):
		super().initializeWindow()

		self.Widget=DemoCentralWidget1(self)
		# self.Widget=WidgetGallery(self)

		self.setCentralWidget(self.Widget)
	

	def initializeMenu(self):
		self.addActionToMainMenu(self.Widget.actionHello_World)
		
		self.actionSummonMainWindow2=QAction("MainWindow 2")
		self.actionSummonMainWindow2.setIcon(DTIcon.Happy())
		self.actionSummonMainWindow2.triggered.connect(self.summonMainWindow2)
		self.addActionToMainMenu(self.actionSummonMainWindow2)

		super().initializeMenu()

	def summonMainWindow2(self):
		self.MainWindow2=DemoMainSession2(self)
		self.MainWindow2.initialize()
		self.MainWindow2.show()

	def setting(self):
		dlg=DemoSettingSession(self, self.app)
		dlg.exec_()