from __future__ import annotations
from DTPySide import *

# Setting 
from DTPySide.DTModule.Ui_DTSetting import Ui_DTSetting
class DTSetting(Ui_DTSetting,QWidget):
	def __init__(self, Headquarter:DTSession.DTMainSession, app:DTAPP):
		super().__init__(Headquarter)
		self.setupUi(self)
		# 继承字体
		self.setAttribute(Qt.WA_WindowPropagation,True)
		
		self.Headquarter=Headquarter
		self.app=app

		self.initializeWindow()
		self.initializeSignal()

		self.listWidget_buttons.setFixedWidth(int(self.font().pointSize()*2.4))
		
		

	def initializeWindow(self):
		
		#加入第一页的menu button
		BasicInfoPageButton=DTWidget.DTSettingButton(QIcon(":/icon/white/white_settings.svg"),self.font().pointSize())
		self.addPageButton(BasicInfoPageButton,0)
		
		self.lineEdit_font.setText(self.Headquarter.font().key().split(",")[0])
		
		if self.app.isLoginEnable():
			self.lineEdit_password.setText(self.app.password())
		else:
			self.lineEdit_password.hide()
			self.label_password.hide()
			self.pushButton_password.hide()
		

		self.comboBox_window_effect.setCurrentIndex(["Normal","Aero","Acrylic"].index(self.app.WindowEffect()))
		self.comboBox_theme.setCurrentIndex(["Dracula","Dark","Light"].index(self.app.Theme()))


		self.setMinimumSize(500,350)
		
	def initializeSignal(self):
		self.pushButton_font.clicked.connect(self.FontSetting)
	
		if self.app.isLoginEnable():
			self.pushButton_password.clicked.connect(self.PasswordSetting)
		
		self.pushButton_window_effect.clicked.connect(self.WindowEffectSetting)
		self.pushButton_theme.clicked.connect(self.ThemeSetting)
	
		

	def PasswordSetting(self):
		
		try:
			self.app.setPassword(self.lineEdit_password.text())
			self.Headquarter.SaveAllEncryptData()
			DTFrame.DTMessageBox(self,"Information","Password reseted successfully!",DTIcon.Information())
		except:
			DTFrame.DTMessageBox(self,"Warning","Error occur during password reseting!",DTIcon.Error())

	def FontSetting(self):
		ok, font = QFontDialog.getFont(QFont(self.Headquarter.font()), self)
		if ok:
			self.lineEdit_font.setText(font.key().split(",")[0])
			self.app.UserSetting().setValue("BasicInfo/Font",font)
			self.Headquarter.updateFont()
			DTFrame.DTMessageBox(self,"Information","Please restart the application manually for better experience.")

	def WindowEffectSetting(self):
		
		self.app.setWindowEffect(self.comboBox_window_effect.currentText())
		DTFrame.DTMessageBox(self,"Information","Window Effet changed to %s successfullt! Please restart the application manually to repaint."%self.app.WindowEffect())

	def ThemeSetting(self):
		
		self.app.setTheme(self.comboBox_theme.currentText())
		DTFrame.DTMessageBox(self,"Information","Theme changed to %s successfullt! Please restart the application manually to repaint."%self.app.Theme())
		

	def appendStackPage(self,page):
		index=self.stackedWidget.addWidget(page)
		return index

	def addPageButton(self,button,index):
		"传入一个按钮，自动加入到ButtonMenu列表的队尾，并链接好跳转到该位置的stackwidget page的信号"
		button.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(index))
		item=QListWidgetItem()
		
		font_size=self.font().pointSize()*2
		item.setSizeHint(QSize(font_size,font_size))

		# 就是这个鬼头东西
		# 如果不设置一下
		# 右键列表空白处时就会出现一个标识QListWidgetItem的小长方形
		# 它和button的大小不一致，就暴露了马脚
		# 找了半个小时才找到……

		self.listWidget_buttons.addItem(item)
		self.listWidget_buttons.setItemWidget(item,button)