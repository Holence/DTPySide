from DTPySide.DTFunction import *
from DTPySide.DTWidget import DTSettingButton
from DTPySide.DTSession import DTSettingSession
from DTPySide.demo.demoModule import DemoSettingPage

class DemoSettingSession(DTSettingSession):
	def __init__(self, parent):
		super().__init__(parent)
		self.SettingPages=DemoSettingPage(parent)
		
		MenuButton1=DTSettingButton(QIcon(":/icon/white/white_at-sign.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page_1)
		
		MenuButton2=DTSettingButton(QIcon(":/icon/white/white_anchor.svg"))
		self.addButtonAndPage(MenuButton2,self.SettingPages.page_2)