from DongliTeahousePySideWheel.DongliTeahouseFunction import *

# MessageBox Module
from DongliTeahousePySideWheel.DongliTeahouseFrame.Ui_DongliTeahouseMessageBox import Ui_DongliTeahouseMessageBox
class DongliTeahouseMessageBox(Ui_DongliTeahouseMessageBox,QDialog):
	"传入title、messageText和icon的地址（建议使用DongliTeahouseIcon的内置Icon）"

	def __init__(self,parent,title,messageText,icon=None):
		super().__init__(parent)
		self.setupUi(self)
		
		# 无边框
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
		
		# 继承字体
		self.setAttribute(Qt.WA_WindowPropagation)
		if 0.7*self.font().pointSize()>=9:
			self.buttonBox.setFont(Font_Resize(self.font(),0.7))
		
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