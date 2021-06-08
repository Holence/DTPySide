from DongliTeahousePySideWheel.DongliTeahouseWidget import *


# Login Module
from DongliTeahousePySideWheel.ui.Ui_Module_DongliTeahouseLogin import Ui_Module_DongliTeahouseLogin
class ModuleDongliTeahouseLogin(Ui_Module_DongliTeahouseLogin,QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)


# Setting Module
from DongliTeahousePySideWheel.ui.Ui_ModuleDongliTeahouseSetting import Ui_Module_DongliTeahouseSetting
class Module_DongliTeahouseSetting(Ui_Module_DongliTeahouseSetting,QWidget):
	def __init__(self,parent):
		super().__init__()
		self.setupUi(self)
		self.parent=parent

		self.initializeWindow()
		self.initializeSignal()

	def initializeWindow(self):
		
		#加入第一页的menu button
		BasicInfoPageButton=DongliTeahouseSettingButton(QIcon(":/white/white_settings.svg"))
		self.addPageButton(BasicInfoPageButton,0)

		self.setFont(Font_Resize(self.parent.font(),0.8))
		self.lineEdit_password.setText(self.parent.password())
		self.lineEdit_font.setText(self.parent.font().key().split(",")[0])

	def initializeSignal(self):
		
		self.pushButton_password.clicked.connect(lambda:self.parent.setPassword(self.lineEdit_password.text()))
		self.pushButton_font.clicked.connect(self.FontSetting)
	
	def FontSetting(self):
		ok, font = QFontDialog.getFont(QFont(self.parent.font()), self)
		if ok:
			self.lineEdit_font.setText(font.key().split(",")[0])
			self.setFont(Font_Resize(font,0.8))
			self.parent.UserSetting.setValue("BasicInfo/Font",font)
			self.parent.updateFont()

	def appendStackPage(self,page):
		index=self.stackedWidget.addWidget(page)
		return index

	def addPageButton(self,button,index):
		"传入一个按钮，自动加入到ButtonMenu列表的队尾，并链接好跳转到该位置的stackwidget page的信号"
		button.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(index))
		item=QListWidgetItem()
		
		item.setSizeHint(QSize(36,36))

		# 就是这个鬼头东西
		# 如果不设置一下
		# 右键列表空白处时就会出现一个标识QListWidgetItem的小长方形
		# 它和button的大小不一致，就暴露了马脚
		# 找了半个小时才找到……

		self.listWidget_buttons.addItem(item)
		self.listWidget_buttons.setItemWidget(item,button)
	