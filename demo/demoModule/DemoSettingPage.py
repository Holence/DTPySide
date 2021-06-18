from DongliTeahousePySideWheel.DongliTeahouseFunction import *

from DongliTeahousePySideWheel.demo.demoModule.Ui_DemoSettingPage import Ui_DemoSettingPage
class DemoSettingPage(Ui_DemoSettingPage,QStackedWidget):
	def __init__(self,Headquarter):
		super().__init__()
		self.setupUi(self)
		self.Headquarter=Headquarter
		self.initializeWindow()
		self.initializeSignal()
	
	def initializeWindow(self):
		self.lineEdit_homelabel.setText(self.Headquarter.UserSetting().value("HomePage/HomeLabel"))
	
	def initializeSignal(self):
		self.lineEdit_homelabel.editingFinished.connect(self.setHomeLabel)
	
	def setHomeLabel(self):
		s=self.lineEdit_homelabel.text()
		self.Headquarter.CentralWidget.homelabel.setText(s)
		self.Headquarter.UserSetting().setValue("HomePage/HomeLabel",s)