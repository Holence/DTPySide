from DTPySide.DTFunction import *
from DTPySide.DTSession import DTMainSession
from DTPySide import DTIcon

from DTPySide.demo.demoSession.DemoSettingSession import DemoSettingSession
from DTPySide.demo.demoModule import DemoCentralWidget1
from DTPySide.demo.demoSession.DemoMainSession2 import DemoMainSession2

class DemoMainSession(DTMainSession):
	def __init__(self,app):
		super().__init__(app)
		
	def initializeWindow(self):
		super().initializeWindow()

		self.CentralWidget=DemoCentralWidget1(self)
		

		self.setCentralWidget(self.CentralWidget)
	

	def initializeMenu(self):
		self.addActionToMainMenu(self.CentralWidget.actionHello_World)
		
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
		dlg=DemoSettingSession(self)
		dlg.exec_()