from __future__ import annotations
from DTPySide import *

# Login 
from DTPySide.DTModule.Ui_DTLogin import Ui_DTLogin
class DTLogin(Ui_DTLogin,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.label_lock.setPixmap(IconFromCurrentTheme("lock.svg").pixmap(24,24))
		