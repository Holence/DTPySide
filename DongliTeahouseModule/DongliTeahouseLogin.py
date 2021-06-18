from DongliTeahousePySideWheel.DongliTeahouseFunction import *

# Login 
from DongliTeahousePySideWheel.DongliTeahouseModule.Ui_DongliTeahouseLogin import Ui_DongliTeahouseLogin
class DongliTeahouseLogin(Ui_DongliTeahouseLogin,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)