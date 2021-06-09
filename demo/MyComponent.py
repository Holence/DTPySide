from DongliTeahousePySideWheel.DongliTeahouseTemplate import *

from DongliTeahousePySideWheel.demo.Ui_ModuleStackedWidgetSettingPage import Ui_ModuleStackedWidgetSettingPage
class ModuleStackedWidgetSettingPage(Ui_ModuleStackedWidgetSettingPage,QStackedWidget):
	def __init__(self,parent):
		super().__init__()
		self.setupUi(self)
		self.PAPA=parent
		self.initializeWindow()
		self.initializeSignal()
	
	def initializeWindow(self):
		self.lineEdit_homelabel.setText(self.PAPA.homelabel.text())
	
	def initializeSignal(self):
		self.lineEdit_homelabel.editingFinished.connect(self.setHomeLabel)
	
	def setHomeLabel(self):
		s=self.lineEdit_homelabel.text()
		self.PAPA.homelabel.setText(s)
		self.PAPA.UserSetting.setValue("HomePage/HomeLabel",s)
		

class MySettingDialog(DongliTeahouseSettingDialog):
	def __init__(self, parent):
		super().__init__(parent)
		self.SettingPages=ModuleStackedWidgetSettingPage(parent)
		
		MenuButton1=DongliTeahouseSettingButton(QIcon(":/white/white_at-sign.svg"))
		self.addButtonAndPage(MenuButton1,self.SettingPages.page_1)
		
		MenuButton2=DongliTeahouseSettingButton(QIcon(":/white/white_anchor.svg"))
		self.addButtonAndPage(MenuButton2,self.SettingPages.page_2)



class MainWindow(DongliTeahouseMainWindow):
	def __init__(self,app):
		super().__init__(app)

	def initializeWindow(self):
		super().initializeWindow()

		self.Form=QWidget()

		font=QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)

		self.homelabel=QLabel(self.UserSetting.value("HomePage/HomeLabel"))
		self.homelabel.setFont(font)

		self.homelabel.setAlignment(Qt.AlignCenter)

		self.horizontalLayout=QHBoxLayout(self.Form)
		self.horizontalLayout.addWidget(self.homelabel)
		
		self.setCentralWidget(self.Form)

	def initializeSignal(self):
		super().initializeSignal()

		self.actionHelloWorld=QAction("Hello World")
		self.actionHelloWorld.setIcon(DongliTeahouseMessageIcon.Holo())
		self.actionHelloWorld.triggered.connect(lambda:DongliTeahouseMessageBox(self,"Hello World","Hello! Welcome to DongliTeahouse.",DongliTeahouseMessageIcon.Heart()))
		self.addActionToMainMenu(self.actionHelloWorld)
		
		# 下面两句添加全局快捷键
		self.actionHelloWorld.setShortcut(QKeySequence(Qt.Key_F12))
		self.addAction(self.actionHelloWorld)

	def setting(self):
		dlg=MySettingDialog(self)
		dlg.exec_()