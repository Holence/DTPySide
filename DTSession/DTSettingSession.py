from DTPySide.DTFunction import *
from DTPySide.DTFrame import DTDialog
from DTPySide.DTModule import DTSetting

# Setting
class DTSettingSession(DTDialog):
	def __init__(self,parent):
		super().__init__(parent,"Setting")
		
		# 不要按钮了，实时保存设置
		# self.buttonBox.removeButton(self.buttonBox.button(QDialogButtonBox.Cancel))
		self.buttonBox.clear()
		self.centralWidget.setContentsMargins(QMargins(8,10,32,0))
		self.horizontalLayout.setContentsMargins(QMargins(0,0,32,0))
		
		self.__settingModule=DTSetting(parent)
		self.centralWidget.addWidget(self.__settingModule)
	
	def addButtonAndPage(self,button,qwidget):
		"传入一个button和stackwidget page中的QWidget，button将自动加入到ButtonMenu列表的队尾，并链接好跳转到该stackwidget page的信号"
		index=self.__settingModule.appendStackPage(qwidget)
		self.__settingModule.addPageButton(button,index)