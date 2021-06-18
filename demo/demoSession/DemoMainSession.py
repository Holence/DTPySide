from DongliTeahousePySideWheel.DongliTeahouseFunction import *
from DongliTeahousePySideWheel.DongliTeahouseSession import DongliTeahouseMainSession
from DongliTeahousePySideWheel.DongliTeahouseFrame import DongliTeahouseMessageBox
from DongliTeahousePySideWheel import DongliTeahouseIcon

from DongliTeahousePySideWheel.demo.demoSession.DemoSettingSession import DemoSettingSession
from DongliTeahousePySideWheel.demo.demoModule import DemoCentralWidget1,DemoMainWindow2

class DemoMainSession(DongliTeahouseMainSession):
	def __init__(self,app):
		super().__init__(app)
		
	def initializeWindow(self):
		super().initializeWindow()

		self.CentralWidget=DemoCentralWidget1(self)
		

		self.setCentralWidget(self.CentralWidget)
	

	def initializeMenu(self):
		self.addActionToMainMenu(self.CentralWidget.actionHello_World)
		
		self.actionSummonMainWindow2=QAction("MainWindow 2")
		self.actionSummonMainWindow2.setIcon(DongliTeahouseIcon.Happy())
		self.actionSummonMainWindow2.triggered.connect(self.summonMainWindow2)
		self.addActionToMainMenu(self.actionSummonMainWindow2)

		super().initializeMenu()

	def summonMainWindow2(self):
		self.MainWindow2=DemoMainWindow2(self)
		self.MainWindow2.initialize()
		self.MainWindow2.show()

	def setting(self):
		dlg=DemoSettingSession(self)
		dlg.exec_()