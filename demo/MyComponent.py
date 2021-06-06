from DongliTeahousePySideWheel.DongliTeahouseTemplate import *

from DongliTeahousePySideWheel.demo.Ui_ModuleSetting import Ui_ModuleSetting
class ModuleSetting(Ui_ModuleSetting,QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.pushButton_page1.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
		self.pushButton_page2.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))

class DialogSetting(DongliTeahouseDialog):
	def __init__(self, parent):
		super().__init__(parent, "Settings")
		self.setting=ModuleSetting()
		self.centralWidget.addWidget(self.setting)


class MainWindow(DongliTeahouseMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("DongliTeahouse Demo")
		self.setMetaData("DongliTeahouse Demo","0.0.0.1","Holence")

	def initializeWindow(self):
		super().initializeWindow()

		self.Form=QWidget()

		font=QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)

		self.label=QLabel("Home")
		self.label.setFont(font)

		self.label.setAlignment(Qt.AlignCenter)

		self.horizontalLayout=QHBoxLayout(self.Form)
		self.horizontalLayout.addWidget(self.label)
		
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
		dlg=DialogSetting(self)
		if dlg.exec_():
			print(dlg.setting.lineEdit.text())