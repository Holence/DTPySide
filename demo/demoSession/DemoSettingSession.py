from DTPySide import *

from DTPySide.demo.demoModule import DemoSettingPage
class DemoSettingSession(DTSession.DTSettingSession):
	def __init__(self, Headquarter, app):
		super().__init__(Headquarter ,app)
		self.SettingPages=DemoSettingPage(Headquarter)
		
		MenuButton1=DTWidget.DTSettingButton(QIcon(":/icon/white/white_at-sign.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page_1)
		
		MenuButton2=DTWidget.DTSettingButton(QIcon(":/icon/white/white_anchor.svg"))
		self.addButtonAndPage(MenuButton2,self.SettingPages.page_2)