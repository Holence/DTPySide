from __future__ import annotations
from DTPySide import *

# Setting
class DTSettingSession(DTFrame.DTDialog):
	def __init__(self, Headquarter, app):
		super().__init__(Headquarter,"Setting")
		
		# 不要按钮了，实时保存设置
		self.buttonBox.hide()
		self.centralWidget.setContentsMargins(QMargins(9,10,32,10))
		self.buttonBoxLayout.setContentsMargins(QMargins(0,0,32,0))
		
		self.__SettingModule=DTModule.DTSetting(Headquarter, app)
		self.setCentralWidget(self.__SettingModule)

		self.resize(self.minimumWidth(),self.minimumHeight())
		self.adjustSize()
		MoveToCenterOfScreen(self)

		self.setStyleSheet("QStackedWidget QPushButton{ min-height:36px }")
	
	def addButtonAndPage(self,button,qwidget):
		"传入一个button和stackwidget page中的QWidget，button将自动加入到ButtonMenu列表的队尾，并链接好跳转到该stackwidget page的信号"
		index=self.__SettingModule.appendStackPage(qwidget)
		self.__SettingModule.addPageButton(button,index)