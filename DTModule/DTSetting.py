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
		BasicInfoPageButton=DTWidget.DTSettingButton(IconFromCurrentTheme("settings.svg"))
		self.addPageButton(BasicInfoPageButton,0)
		
		
		if self.app.isLoginEnable():
			self.lineEdit_password.setText(self.app.password())
		else:
			self.lineEdit_password.hide()
			self.label_password.hide()
		
		if self.app.isBackupEnable():
			dst=self.app.BackupDst()
			if dst==False:
				self.lineEdit_backup.setText("")
			else:
				self.lineEdit_backup.setText(dst)
		else:
			self.label_backup.hide()
			self.lineEdit_backup.hide()
			self.pushButton_backup.hide()
		
		self.pushButton_font.setText(self.app.Font().key().split(",")[0])
		self.pushButton_font.setStyleSheet("font-family:%s"%self.app.Font().key().split(",")[0])

		self.spinBox_scale.setValue(self.app.Scale())
		self.comboBox_window_effect.setCurrentIndex(["Normal","Aero","Acrylic"].index(self.app.WindowEffect()))
		
		self.comboBox_theme.addItems(self.app.ThemeList)
		self.comboBox_theme.setCurrentIndex(self.app.ThemeList.index(self.app.Theme()))
		self.slider_Hue.setValue(int(self.app.Hue()*360))
		self.slider_Hue.setStyleSheet("""
		QSlider{
			padding-left:10px;
			padding-right:10px;
			height: 36px;
		}
		QSlider::groove:horizontal {
			height: 24px;
			border: none;
			border-radius: 6px;
		}
		QSlider::handle {
			height: 28px;
		}
		QSlider::groove{
			background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));
		}
		QSlider::add-page{
			background:transparent;
		}
		QSlider::sub-page{
			background: transparent;
		}
		""")
		self.pushButton_hue_reset.setStyleSheet("QPushButton{ min-height:16px; max-height:16px; min-width:16px; max-width:16px; icon-size:12px; }")
		self.pushButton_hue_reset.setIcon(IconFromCurrentTheme("corner-down-left.svg"))
		
		if self.app.hasTanslation():
			self.comboBox_language.addItems(self.app.translation_module.Language_Dict.keys())
			self.comboBox_country.addItems(self.app.translation_module.Country_Dict.keys())
			self.comboBox_language.setCurrentText(self.app.Language())
			self.comboBox_country.setCurrentText(self.app.Country())
		else:
			self.comboBox_language.hide()
			self.label_language.hide()
			self.comboBox_country.hide()
			self.label_country.hide()

		self.setMinimumSize(800,550)
		
	def initializeSignal(self):
		self.pushButton_font.clicked.connect(self.FontSetting)
	
		if self.app.isLoginEnable():
			self.lineEdit_password.editingFinished.connect(self.PasswordSetting)
		
		if self.app.isBackupEnable():
			self.pushButton_backup.clicked.connect(self.BackupSetting)
		
		self.pushButton_scale.clicked.connect(self.ScaleSetting)
		self.comboBox_window_effect.currentIndexChanged.connect(self.WindowEffectSetting)
		self.comboBox_theme.currentIndexChanged.connect(self.ThemeSetting)
		self.pushButton_hue.clicked.connect(self.HueSetting)
		self.pushButton_hue_reset.clicked.connect(self.HueReset)
	
		if self.app.hasTanslation():
			self.comboBox_language.currentIndexChanged.connect(self.LanguageSetting)
			self.comboBox_country.currentIndexChanged.connect(self.CountrySetting)

	def PasswordSetting(self):
		
		try:
			self.app.setPassword(self.lineEdit_password.text())
			self.Headquarter.saveAllEncryptData()
			DTFrame.DTMessageBox(self,"Information","Password reseted to \"%s\" successfully!"%self.app.password(),DTIcon.Information())
		except:
			DTFrame.DTMessageBox(self,"Warning","Error occur during password reseting!",DTIcon.Error())

	def BackupSetting(self):
		dlg=QFileDialog(self)
		backup_dst=dlg.getExistingDirectory()
		if backup_dst:
			self.app.setBackupDst(backup_dst)
			self.lineEdit_backup.setText(self.app.BackupDst())
			DTFrame.DTMessageBox(self,"Information","Backup Dst changed to\n\n \"%s\" \n\nsuccessfully!"%self.app.BackupDst(),DTIcon.Information())
	
	def FontSetting(self):
		ok, font = QFontDialog.getFont(self.app.Font(), self)
		if ok:
			self.app.setFont(font)
			# DTFrame.DTMessageBox(self,"Information","Font changed to \"%s\" successfully!\n\nApp will be restart for better experience."%self.app.Font().key().split(",")[0],DTIcon.Information())
			self.app.restart()
			
	
	def ScaleSetting(self):
		self.app.setScale(round(self.spinBox_scale.value(),1))
		# DTFrame.DTMessageBox(self,"Information","Scale changed to \"%s\" successfully!\n\nApp will be restart for better experience."%self.app.Scale(),DTIcon.Information())
		self.app.restart()

	def WindowEffectSetting(self):
		self.app.setWindowEffect(self.comboBox_window_effect.currentText())
		# DTFrame.DTMessageBox(self,"Information","Window Effet changed to \"%s\" successfully!\n\nApp will be restart for better experience."%self.app.WindowEffect(),DTIcon.Information())
		self.app.restart()

	def ThemeSetting(self):
		self.app.setTheme(self.comboBox_theme.currentText())
		self.slider_Hue.setValue(0)
		# DTFrame.DTMessageBox(self,"Information","Theme changed to \"%s\" successfully!\n\nApp will be restart for better experience."%self.app.Theme(),DTIcon.Information())
		self.app.restart()
	
	def HueSetting(self):
		self.app.setHue(float(self.slider_Hue.value()/360))
		self.app.initializeWindowStyle()
	
	def HueReset(self):
		self.app.setHue(-1)
		self.slider_Hue.setValue(0)
		self.app.initializeWindowStyle()

	def LanguageSetting(self):
		self.app.setLanguage(self.comboBox_language.currentText())
		# DTFrame.DTMessageBox(self,"Information","Language changed to \"%s\" successfully!\n\nApp will be restart for better experience."%self.app.Language(),DTIcon.Information())
		self.app.restart()

	def CountrySetting(self):
		self.app.setCountry(self.comboBox_country.currentText())
		# DTFrame.DTMessageBox(self,"Information","Country changed to \"%s\" successfully!\n\nApp will be restart for better experience."%self.app.Country(),DTIcon.Information())
		self.app.restart()
	
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