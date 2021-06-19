from DTPySide.DTFunction import *
from DTPySide.DTFrame import DTMessageBox
from DTPySide.DTWidget import DTSettingButton
from DTPySide import DTIcon

# Setting 
from DTPySide.DTModule.Ui_DTSetting import Ui_DTSetting
class DTSetting(Ui_DTSetting,QWidget):
	def __init__(self,Headquarter):
		super().__init__(Headquarter)
		self.setupUi(self)
		# 继承字体
		self.setAttribute(Qt.WA_WindowPropagation)
		
		self.Headquarter=Headquarter
		self.initializeWindow()
		self.initializeSignal()

	def initializeWindow(self):
		#加入第一页的menu button
		BasicInfoPageButton=DTSettingButton(QIcon(":/icon/white/white_settings.svg"))
		self.addPageButton(BasicInfoPageButton,0)
		
		self.lineEdit_font.setText(self.Headquarter.font().key().split(",")[0])
		
		if self.Headquarter.isLoginEnable():
			self.lineEdit_password.setText(self.Headquarter.password())
		else:
			self.lineEdit_password.hide()
			self.label_password.hide()
			self.pushButton_password.hide()
		
	def initializeSignal(self):
		self.pushButton_font.clicked.connect(self.FontSetting)
	
		if self.Headquarter.isLoginEnable():
			self.pushButton_password.clicked.connect(self.PasswordSetting)
	
	def PasswordSetting(self):
		
		try:
			self.Headquarter.setPassword(self.lineEdit_password.text())
			self.Headquarter.SaveAllEncryptData()
			DTMessageBox(self,"Information","Password reseted successfully!",DTIcon.Information())
		except:
			DTMessageBox(self,"Warning","Error occur during password reseting!",DTIcon.Error())

	def FontSetting(self):
		ok, font = QFontDialog.getFont(QFont(self.Headquarter.font()), self)
		if ok:
			self.lineEdit_font.setText(font.key().split(",")[0])
			self.Headquarter.UserSetting().setValue("BasicInfo/Font",font)
			self.Headquarter.updateFont()

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