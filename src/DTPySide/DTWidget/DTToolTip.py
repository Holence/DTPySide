from __future__ import annotations
from DTPySide import *

class DTToolTip(QLabel):
	def __init__(self, parent, tooltip):
		super().__init__(tooltip,parent)
		
		self.setStyleSheet(""" 
			QLabel {
				background-color: #0C0B0B;	
				color: #E6E6E6;
				padding-left: 10px;
				padding-right: 10px;
				border: 1px solid #0C0B0B;
				border-radius: 12px;
				border-left: 3px solid #FF6265;
			}
		""")
		
		self.adjustSize()

		# SET OPACITY
		opacity = QGraphicsOpacityEffect(self)
		opacity.setOpacity(0.85)
		self.setGraphicsEffect(opacity)
