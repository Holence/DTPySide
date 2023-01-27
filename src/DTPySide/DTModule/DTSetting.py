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
			self.spinBox_iteration.setValue(self.app.iteration())
		else:
			self.lineEdit_password.hide()
			self.label_password.hide()
			self.spinBox_iteration.hide()
			self.label_iteration.hide()
		
		if self.app.DataList()!=[]:
			self.lineEdit_data_dir.setText(self.app.DataDir())
			
			if self.app.isBackupEnable():
				dst=self.app.BackupDst()
				if dst==None:
					self.lineEdit_backup.setText("")
				else:
					self.lineEdit_backup.setText(dst)
			else:
				self.label_backup.hide()
				self.lineEdit_backup.hide()
				self.pushButton_backup.hide()
		
		else:
			self.lineEdit_data_dir.hide()
			self.label_data_dir.hide()
			self.pushButton_data_dir.hide()
			self.label_backup.hide()
			self.lineEdit_backup.hide()
			self.pushButton_backup.hide()

		# font
		self.pushButton_font.setText(self.app.Font().key().split(",")[0])
		self.pushButton_font.setStyleSheet("font-family:%s; min-height:26px; max-height:26px;"%self.app.Font().key().split(",")[0])

		# scale
		self.spinBox_scale.setValue(self.app.Scale())

		# window effect
		if sys.platform=="win32":
			self.comboBox_window_effect.setCurrentIndex(["Normal","Aero","Acrylic"].index(self.app.WindowEffect()))
		else:
			self.label_window_effect.hide()
			self.comboBox_window_effect.hide()
		
		# theme
		self.comboBox_theme.addItems(self.app.ThemeList)
		self.comboBox_theme.setCurrentIndex(self.app.ThemeList.index(self.app.Theme()))

		# color
		self.setStyleSheet("""
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
		QSlider::add-page{
			background:transparent;
		}
		QSlider::sub-page{
			background: transparent;
		}
		""")
		# hue
		self.slider_Hue.setValue(int(self.app.Hue()*self.slider_Hue.maximum()))
		self.slider_Hue.setStyleSheet("""
		QSlider::groove{
			background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));
		}
		""")
		self.pushButton_hue_reset.setStyleSheet("QPushButton{ min-height:16px; max-height:16px; min-width:16px; max-width:16px; icon-size:12px; }")
		self.pushButton_hue_reset.setIcon(IconFromCurrentTheme("corner-down-left.svg"))
		# saturation
		self.slider_saturation.setValue(int(self.app.Saturation()*self.slider_saturation.maximum()))
		self.updateSaturationSlider()
		self.pushButton_saturation_reset.setStyleSheet("QPushButton{ min-height:16px; max-height:16px; min-width:16px; max-width:16px; icon-size:12px; }")
		self.pushButton_saturation_reset.setIcon(IconFromCurrentTheme("corner-down-left.svg"))
		# luminance
		self.slider_luminance.setValue(int(self.app.Luminance()*self.slider_luminance.maximum()))
		self.slider_luminance.setStyleSheet("""
		QSlider::groove{
			background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
		}
		""")
		self.pushButton_luminance_reset.setStyleSheet("QPushButton{ min-height:16px; max-height:16px; min-width:16px; max-width:16px; icon-size:12px; }")
		self.pushButton_luminance_reset.setIcon(IconFromCurrentTheme("corner-down-left.svg"))

		self.slider_contrast.setValue(int(self.app.Contrast()*self.slider_contrast.maximum()))
		self.slider_contrast.setStyleSheet("""
		QSlider::groove{
			background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));
		}
		""")
		self.pushButton_contrast_reset.setStyleSheet("QPushButton{ min-height:16px; max-height:16px; min-width:16px; max-width:16px; icon-size:12px; }")
		self.pushButton_contrast_reset.setIcon(IconFromCurrentTheme("corner-down-left.svg"))
		
		self.updateColorPreview()

		if self.app.Reverse():
			self.checkBox_reverse.setCheckState(Qt.Checked)

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
			self.pushButton_iteration.clicked.connect(self.IterationSetting)
		
		self.pushButton_data_dir.clicked.connect(self.DataDirSetting)
		
		if self.app.isBackupEnable():
			self.pushButton_backup.clicked.connect(self.BackupSetting)
		
		self.pushButton_scale.clicked.connect(self.ScaleSetting)
		
		if sys.platform=="win32":
			self.comboBox_window_effect.currentIndexChanged.connect(self.WindowEffectSetting)
		
		self.comboBox_theme.currentIndexChanged.connect(self.ThemeSetting)
		
		self.pushButton_color.clicked.connect(self.ColorSetting)

		def slotColorPreview():
			self.updateColorPreview()
			self.updateSaturationSlider()
		
		self.slider_Hue.sliderMoved.connect(slotColorPreview)
		self.slider_saturation.sliderMoved.connect(slotColorPreview)
		self.slider_luminance.sliderMoved.connect(slotColorPreview)

		self.pushButton_hue_reset.clicked.connect(self.HueReset)
		self.pushButton_saturation_reset.clicked.connect(self.SaturationReset)
		self.pushButton_luminance_reset.clicked.connect(self.LuminanceReset)
		self.pushButton_contrast_reset.clicked.connect(self.ContrastReset)
		
		self.checkBox_reverse.stateChanged.connect(self.ReverseSetting)
	
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

	def IterationSetting(self):
		
		try:
			self.app.setIteration(self.spinBox_iteration.value())
			self.app.setPassword(self.lineEdit_password.text())
			self.Headquarter.saveAllEncryptData()
			DTFrame.DTMessageBox(self,"Information","Iteration seted to \"%s\" successfully!"%self.app.iteration(),DTIcon.Information())
		except:
			DTFrame.DTMessageBox(self,"Warning","Error occur during password reseting!",DTIcon.Error())

	def DataDirSetting(self):
		dlg=QFileDialog(self)
		data_dir=dlg.getExistingDirectory()
		if data_dir:

			warning_list=[]
			for file in self.app.DataList():
				if file in os.listdir(data_dir):
					warning_list.append(file)
			
			flag=True
			if warning_list!=[]:
				if DTFrame.DTConfirmBox(
					self,
					"Warning",
					"There are already files with the same names in the new Data Dir: \n\n%s\n\nDo you want to overwrite them?"%data_dir,
					icon=DTIcon.Warning(),
					detail="\n".join(warning_list)
				).exec_():
					flag=True
				else:
					flag=False
			
			if flag==True:
				self.app.setDataDir(data_dir)
				self.lineEdit_data_dir.setText(self.app.DataDir())
				DTFrame.DTMessageBox(self,"Information","Data Dir changed to\n\n \"%s\" \n\nsuccessfully!"%self.app.DataDir(),DTIcon.Information())

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
		self.app.restart()
	
	def updateColorPreview(self):
		if self.app.Hue()==-1 and self.slider_Hue.value()==0:
			self.label_color_preview.setStyleSheet("background:black")
			return
		c=colour.Color()
		c.set_hue(float(self.slider_Hue.value()/self.slider_Hue.maximum()))
		c.set_saturation(float(self.slider_saturation.value()/self.slider_saturation.maximum()))
		c.set_luminance(float(self.slider_luminance.value()/self.slider_luminance.maximum()))
		color=c.get_web()
		self.label_color_preview.setStyleSheet("background:%s"%color)

	def updateSaturationSlider(self):
		if self.app.Hue()==-1 and self.slider_Hue.value()==0:
			self.slider_saturation.setStyleSheet("""
			QSlider::groove{
				background:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));
			}
			""")
			return
		c=colour.Color()
		c.set_hue(float(self.slider_Hue.value()/self.slider_Hue.maximum()))	
		c.set_luminance(0.5)
		c.set_saturation(1.0)
		r,g,b=list(map(lambda x:int(x*255),c.get_rgb()))
		self.slider_saturation.setStyleSheet("""
		QSlider::groove{
			background:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(%s, %s, %s, 255));
		}
		"""%(r,g,b))

	def ColorSetting(self):
		if self.app.Hue()==-1 and self.slider_Hue.value()==0:
			pass
		else:
			self.app.setHue(float(self.slider_Hue.value()/self.slider_Hue.maximum()))
		self.app.setSaturation(float(self.slider_saturation.value()/self.slider_saturation.maximum()))
		self.app.setLuminance(float(self.slider_luminance.value()/self.slider_luminance.maximum()))
		self.app.setContrast(float(self.slider_contrast.value()/self.slider_contrast.maximum()))
		self.app.initializeWindowStyle(refresh=True)

	def HueReset(self):
		self.app.setHue(-1)
		self.slider_Hue.setValue(0)
		self.app.initializeWindowStyle(refresh=True)
		self.updateColorPreview()
		self.updateSaturationSlider()
	
	def SaturationReset(self):
		self.app.setSaturation(0.5)
		self.slider_saturation.setValue(int(self.slider_saturation.maximum()/2))
		self.app.initializeWindowStyle(refresh=True)
	
	def LuminanceReset(self):
		self.app.setLuminance(0.5)
		self.slider_luminance.setValue(int(self.slider_luminance.maximum()/2))
		self.app.initializeWindowStyle(refresh=True)
	
	def ContrastReset(self):
		self.app.setContrast(0.5)
		self.slider_contrast.setValue(int(self.slider_contrast.maximum()/2))
		self.app.initializeWindowStyle(refresh=True)

	def ReverseSetting(self):
		dlg=DTFrame.DTConfirmBox(self,"Warning","You want to change text and icon from dark to light (or from light to dark)?\n\nApp will restart after the change.")
		if dlg.exec_():
			if self.checkBox_reverse.checkState()==Qt.Checked:
				self.app.setReverse(True)
			else:
				self.app.setReverse(False)
			self.app.restart()
	
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