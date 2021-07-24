from __future__ import annotations
from DTPySide import *

# Setting 
from DTPySide.DTModule.Ui_DTSetting import Ui_DTSetting
class DTSetting(Ui_DTSetting,QWidget):
	def __init__(self, Headquarter:DTSession.DTMainSession, app:DTAPP):
		super().__init__(Headquarter)
		self.setupUi(self)
		
		self.Headquarter=Headquarter
		self.app=app

		self.initializeWindow()
		self.initializeSignal()
		
		

	def initializeWindow(self):
		
		#加入第一页的menu button
		BasicInfoPageButton=DTWidget.DTSettingButton(QIcon(":/icon/white/white_settings.svg"))
		self.addPageButton(BasicInfoPageButton,0)
		
		self.lineEdit_font.setText(self.app.Font().key().split(",")[0])
		
		if self.app.isLoginEnable():
			self.lineEdit_password.setText(self.app.password())
		else:
			self.lineEdit_password.hide()
			self.label_password.hide()
			self.pushButton_password.hide()
		

		self.spinBox_scale.setValue(self.app.Scale())
		self.comboBox_window_effect.setCurrentIndex(["Normal","Aero","Acrylic"].index(self.app.WindowEffect()))
		self.comboBox_theme.setCurrentIndex(["Dracula","Dark","Light"].index(self.app.Theme()))
		
		import DTPySide.DTTranslation as DTTranslation

		self.comboBox_language.addItems(DTTranslation.Language_Dict.keys())
		self.comboBox_country.addItems(DTTranslation.Country_Dict.keys())
		self.comboBox_language.setCurrentText(self.app.Language())
		self.comboBox_country.setCurrentText(self.app.Country())


		self.setMinimumSize(800,550)
		
	def initializeSignal(self):
		self.pushButton_font.clicked.connect(self.FontSetting)
	
		if self.app.isLoginEnable():
			self.pushButton_password.clicked.connect(self.PasswordSetting)
		
		self.pushButton_scale.clicked.connect(self.ScaleSetting)
		self.pushButton_window_effect.clicked.connect(self.WindowEffectSetting)
		self.pushButton_theme.clicked.connect(self.ThemeSetting)
		self.pushButton_language.clicked.connect(self.LanguageSetting)
		self.pushButton_country.clicked.connect(self.CountrySetting)
	
		

	def PasswordSetting(self):
		
		try:
			self.app.setPassword(self.lineEdit_password.text())
			self.Headquarter.saveAllEncryptData()
			DTFrame.DTMessageBox(self,"Information","Password reseted to \"%s\" successfully!"%self.app.password(),DTIcon.Information())
		except:
			DTFrame.DTMessageBox(self,"Warning","Error occur during password reseting!",DTIcon.Error())

	def FontSetting(self):
		ok, font = QFontDialog.getFont(self.app.Font(), self)
		if ok:
			self.lineEdit_font.setText(font.key().split(",")[0])
			self.app.setFont(font)
			self.app.initializeWindowStyle()
			DTFrame.DTMessageBox(self,"Information","Font changed to \"%s\" successfully!"%self.app.Font().key().split(",")[0],DTIcon.Information())
	
	def ScaleSetting(self):
		self.app.setScale(round(self.spinBox_scale.value(),1))
		DTFrame.DTMessageBox(self,"Information","Scale changed to \"%s\" successfully!\n\nPlease restart the application manually to apply the setting."%self.app.Scale(),DTIcon.Information())

	def WindowEffectSetting(self):
		
		self.app.setWindowEffect(self.comboBox_window_effect.currentText())
		self.app.initializeWindowStyle()
		DTFrame.DTMessageBox(self,"Information","Window Effet changed to \"%s\" successfully!\n\nPlease restart the application manually for better expeirence."%self.app.WindowEffect(),DTIcon.Information())

	def ThemeSetting(self):
		
		self.app.setTheme(self.comboBox_theme.currentText())
		self.app.initializeWindowStyle()
		DTFrame.DTMessageBox(self,"Information","Theme changed to \"%s\" successfully!"%self.app.Theme(),DTIcon.Information())
		
	def LanguageSetting(self):
		self.app.setLanguage(self.comboBox_language.currentText())
		DTFrame.DTMessageBox(self,"Information","Language changed to \"%s\" successfully!\n\nPlease restart the application manually for better expeirence."%self.app.Language(),DTIcon.Information())

	def CountrySetting(self):
		self.app.setCountry(self.comboBox_country.currentText())
		DTFrame.DTMessageBox(self,"Information","Country changed to \"%s\" successfully!"%self.app.Country(),DTIcon.Information())
	
	def appendStackPage(self,page):
		index=self.stackedWidget.addWidget(page)
		return index

	def addPageButton(self,button,index):
		"传入一个按钮，自动加入到ButtonMenu列表的队尾，并链接好跳转到该位置的stackwidget page的信号"
		
		button.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(index))
		self.verticalLayout_buttons.insertWidget(self.verticalLayout_buttons.count()-1,button)
		
		###################################
		# 以前还费劲用listwidget装载pushbutton，明明用layout这么方便，就是却不会用……
		# item=QListWidgetItem()
		# 
		# font_size=self.font().pointSize()*4
		# item.setSizeHint(QSize(font_size,font_size))
		# 
		# # 就是这个鬼头东西
		# # 如果不设置一下
		# # 右键列表空白处时就会出现一个标识QListWidgetItem的小长方形
		# # 它和button的大小不一致，就暴露了马脚
		# # 找了半个小时才找到……
		# 
		# self.listWidget_buttons.addItem(item)
		# self.listWidget_buttons.setItemWidget(item,button)
		###################################