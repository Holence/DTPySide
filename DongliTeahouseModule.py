from DongliTeahousePySideWheel.DongliTeahouseWidget import *


# MainWindow用的TitleBar
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseTitleBarFull import Ui_DongliTeahouseTitleBarFull
class DongliTeahouseTitleBarFull(Ui_DongliTeahouseTitleBarFull,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.PAPA=parent
		self.label_titlebar.setPapa(parent)
		self.initializeSignal()
	
	def initializeSignal(self):
		self.btn_close.clicked.connect(self.PAPA.close)
		self.btn_maximize.clicked.connect(self.PAPA.windowToggleMaximized)
		self.btn_minimize.clicked.connect(self.PAPA.showMinimized)
		self.btn_menu.clicked.connect(lambda:show_ContextMenu_Beneath(self.PAPA.MainMenu(),self.btn_menu))

	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.label_titlebar.setText(title)


# 其他窗口用的TitleBar
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseTitleBarCut import Ui_DongliTeahouseTitleBarCut
class DongliTeahouseTitleBarCut(Ui_DongliTeahouseTitleBarCut,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.PAPA=parent
		self.label_titlebar.setPapa(parent)
		self.initializeSignal()
	
	def initializeSignal(self):
		self.btn_close.clicked.connect(self.PAPA.close)
	
	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.label_titlebar.setText(title)

# Dialog
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseDialog import Ui_DongliTeahouseDialog
class DongliTeahouseDialog(Ui_DongliTeahouseDialog,QDialog):
	def __init__(self,parent,title):
		if parent==None:
			super().__init__()
		else:
			super().__init__(parent)
		
		self.setupUi(self)
		
		# 无边框
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
		
		# 继承字体
		self.setAttribute(Qt.WA_WindowPropagation)
		
		# 缩放角
		self.setSizeGripEnabled(True)

		self.TitleBar.setWindowTitle(title)


# MessageBox
from DongliTeahousePySideWheel.ui.Ui_DongliTeahouseMessageBox import Ui_DongliTeahouseMessageBox
class DongliTeahouseMessageBox(Ui_DongliTeahouseMessageBox,QDialog):
	"传入title、messageText和icon的地址（建议使用DongliTeahouseMessageIcon的内置Icon）"

	def __init__(self,parent,title,messageText,icon=None):
		super().__init__(parent)
		self.setupUi(self)
		
		# 无边框
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
		
		# 继承字体
		self.setAttribute(Qt.WA_WindowPropagation)
		
		# 缩放角
		self.setSizeGripEnabled(True)
		
		self.TitleBar.setWindowTitle(title)
		self.label_message.setText(messageText)
		
		if icon!=None:
			icon_pic=icon.pixmap(QSize(64,64))
			self.label_icon.setPixmap(icon_pic)
		else:
			self.label_icon.hide()

		self.adjustSize()
		self.exec_()

# Login Module
from DongliTeahousePySideWheel.ui.Ui_Module_DongliTeahouseLogin import Ui_Module_DongliTeahouseLogin
class ModuleDongliTeahouseLogin(Ui_Module_DongliTeahouseLogin,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)


# Setting Module
from DongliTeahousePySideWheel.ui.Ui_ModuleDongliTeahouseSetting import Ui_Module_DongliTeahouseSetting
class Module_DongliTeahouseSetting(Ui_Module_DongliTeahouseSetting,QWidget):
	def __init__(self,parent):
		super().__init__()
		self.setupUi(self)
		self.PAPA=parent

		self.initializeWindow()
		self.initializeSignal()

	def initializeWindow(self):
		
		#加入第一页的menu button
		BasicInfoPageButton=DongliTeahouseSettingButton(QIcon(":/white/white_settings.svg"))
		self.addPageButton(BasicInfoPageButton,0)

		self.setFont(Font_Resize(self.PAPA.font(),0.8))
		self.lineEdit_password.setText(self.PAPA.password())
		self.lineEdit_font.setText(self.PAPA.font().key().split(",")[0])

	def initializeSignal(self):
		
		self.pushButton_password.clicked.connect(self.PasswordSetting)
		self.pushButton_font.clicked.connect(self.FontSetting)
	
	def PasswordSetting(self):
		try:
			self.PAPA.setPassword(self.lineEdit_password.text())
			self.PAPA.SaveAllEncryptData()
			DongliTeahouseMessageBox(self,"Information","Password reseted successfully!",DongliTeahouseMessageIcon.Information())
		except:
			DongliTeahouseMessageBox(self,"Warning","Error occur during password reseting!",DongliTeahouseMessageIcon.Error())

	def FontSetting(self):
		ok, font = QFontDialog.getFont(QFont(self.PAPA.font()), self)
		if ok:
			self.lineEdit_font.setText(font.key().split(",")[0])
			self.setFont(Font_Resize(font,0.8))
			self.PAPA.UserSetting.setValue("BasicInfo/Font",font)
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
	