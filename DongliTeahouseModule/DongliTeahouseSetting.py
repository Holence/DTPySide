from DongliTeahousePySideWheel.DongliTeahouseFrame import DongliTeahouseMessageBox
from DongliTeahousePySideWheel.DongliTeahouseWidget import DongliTeahouseSettingButton
from DongliTeahousePySideWheel.DongliTeahouseFunction import *
from DongliTeahousePySideWheel import DongliTeahouseIcon

# Setting 
from DongliTeahousePySideWheel.DongliTeahouseModule.Ui_DongliTeahouseSetting import Ui_DongliTeahouseSetting
class DongliTeahouseSetting(Ui_DongliTeahouseSetting,QWidget):
	def __init__(self,parent):
		super().__init__()
		self.setupUi(self)
		self.PAPA=parent

		self.initializeWindow()
		self.initializeSignal()

	def initializeWindow(self):
		#加入第一页的menu button
		BasicInfoPageButton=DongliTeahouseSettingButton(QIcon(":/icon/white/white_settings.svg"))
		self.addPageButton(BasicInfoPageButton,0)
		
		self.setFont(Font_Resize(self.PAPA.font(),0.8))
		self.lineEdit_font.setText(self.PAPA.font().key().split(",")[0])
		
		if self.PAPA.isLoginEnable():
			self.lineEdit_password.setText(self.PAPA.password())
		else:
			self.lineEdit_password.hide()
			self.label_password.hide()
			self.pushButton_password.hide()
		
	def initializeSignal(self):
		self.pushButton_font.clicked.connect(self.FontSetting)
	
		if self.PAPA.isLoginEnable():
			self.pushButton_password.clicked.connect(self.PasswordSetting)
	
	def PasswordSetting(self):
		
		try:
			self.PAPA.setPassword(self.lineEdit_password.text())
			self.PAPA.SaveAllEncryptData()
			DongliTeahouseMessageBox(self,"Information","Password reseted successfully!",DongliTeahouseIcon.Information())
		except:
			DongliTeahouseMessageBox(self,"Warning","Error occur during password reseting!",DongliTeahouseIcon.Error())

	def FontSetting(self):
		ok, font = QFontDialog.getFont(QFont(self.PAPA.font()), self)
		if ok:
			self.lineEdit_font.setText(font.key().split(",")[0])
			self.setFont(Font_Resize(font,0.8))
			self.PAPA.UserSetting().setValue("BasicInfo/Font",font)
			self.PAPA.updateFont()

	def appendStackPage(self,page):
		index=self.stackedWidget.addWidget(page)
		return index

	def addPageButton(self,button,index):
		"传入一个按钮，自动加入到ButtonMenu列表的队尾，并链接好跳转到该位置的stackwidget page的信号"
		button.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(index))
		item=QListWidgetItem()
		
		item.setSizeHint(QSize(30,30))

		# 就是这个鬼头东西
		# 如果不设置一下
		# 右键列表空白处时就会出现一个标识QListWidgetItem的小长方形
		# 它和button的大小不一致，就暴露了马脚
		# 找了半个小时才找到……

		self.listWidget_buttons.addItem(item)
		self.listWidget_buttons.setItemWidget(item,button)