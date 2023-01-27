from DTPySide import *

from DTPySide.demo.demoSession.DemoMainSession2 import DemoMainSession2
from DTPySide.demo.demoSession.DemoSettingSession import DemoSettingSession
from DTPySide.demo.demoModule import DemoCentralWidget1,WidgetGallery

class DemoMainSession(DTSession.DTMainSession):

	def closeEvent(self, event):
		self.dock_widget.close()
		super().closeEvent(event)
	
	def __init__(self,app):
		super().__init__(app)

	def initializeWindow(self):
		super().initializeWindow()

		self.Widget=DemoCentralWidget1(self)
		self.CentralWidget=WidgetGallery(self)
		self.CentralWidget.main_layout.addWidget(self.Widget)

		self.setCentralWidget(self.CentralWidget)

		self.dock_widget=DTWidget.DTDockWidget("A Floating TextEdit", self)
		self.lineedit=QTextEdit()
		self.dock_widget.setWidget(self.lineedit)
	
	def initializeSignal(self):
		super().initializeSignal()

		def slot():
			if self.dock_widget.isHidden():
				self.dock_widget.show()
				self.actionSwitchDock.setText("Hide DockWidget")
			else:
				self.dock_widget.hide()
				self.actionSwitchDock.setText("Show DockWidget")

		self.actionSwitchDock=QAction("Hide DockWidget")
		self.actionSwitchDock.setShortcut("F5")
		self.addAction(self.actionSwitchDock)
		self.actionSwitchDock.setIcon(IconFromCurrentTheme("slack.svg"))
		self.actionSwitchDock.triggered.connect(slot)

		self.actionSummonMainWindow2=QAction("MainWindow 2")
		self.actionSummonMainWindow2.setIcon(DTIcon.Happy())
		self.actionSummonMainWindow2.triggered.connect(self.summonMainWindow2)

	def initializeMenu(self):

		self.addActionToMainMenu(self.Widget.actionHello_World)
		self.addActionToMainMenu(self.actionSummonMainWindow2)
		self.addActionToMainMenu(self.actionSwitchDock)
		self.addSeparatorToMainMenu()

		super().initializeMenu()

	def summonMainWindow2(self):
		self.MainWindow2=DemoMainSession2(self)
		self.MainWindow2.initialize()
		self.MainWindow2.show()

	def setting(self):
		dlg=DemoSettingSession(self, self.app)
		dlg.exec_()