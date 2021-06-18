from DongliTeahousePySideWheel.DongliTeahouseFunction import *
from DongliTeahousePySideWheel.DongliTeahouseWidget import DongliTeahouseSettingButton
from DongliTeahousePySideWheel.DongliTeahouseSession import DongliTeahouseSettingSession
from DongliTeahousePySideWheel.demo.demoModule import DemoSettingPage

class DemoSettingSession(DongliTeahouseSettingSession):
	def __init__(self, parent):
		super().__init__(parent)
		self.SettingPages=DemoSettingPage(parent)
		
		MenuButton1=DongliTeahouseSettingButton(QIcon(":/icon/white/white_at-sign.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page_1)
		
		MenuButton2=DongliTeahouseSettingButton(QIcon(":/icon/white/white_anchor.svg"))
		self.addButtonAndPage(MenuButton2,self.SettingPages.page_2)