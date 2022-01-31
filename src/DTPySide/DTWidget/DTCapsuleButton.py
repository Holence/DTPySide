from __future__ import annotations
from DTPySide import *

class DTCapsuleButton(QLabel):
	clicked=Signal()
	def __init__(self,parent,text,color):
		super().__init__(parent)
		self.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed)
		
		self.setText(text)
		self.adjustSize()
		
		self.setStyleSheet(""" 
			QLabel {
				color: white;
				background-color: %s;
				border: 1px solid %s;
				border-radius: 12px;
			}
		"""%(color,color))

		# SET DROP SHADOW
		shadow = QGraphicsDropShadowEffect(self)
		shadow.setBlurRadius(0.8)
		shadow.setXOffset(4)
		shadow.setYOffset(4)
		shadow.setColor(QColor("#252525"))
		self.setGraphicsEffect(shadow)
	
	def mouseReleaseEvent(self,event):
		super().mouseReleaseEvent(event)
		if event.button()==Qt.LeftButton:
			self.clicked.emit()
	
	# Clear_Layout时调用deleteLater删除DTCapsuleButton，但shadow消不干净，那就setGraphicsEffect为空
	def deleteLater(self):
		super().deleteLater()
		self.setGraphicsEffect(None)
