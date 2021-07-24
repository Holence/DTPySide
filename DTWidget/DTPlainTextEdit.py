from __future__ import annotations
from DTPySide import *

class DTPlainTextEdit(QPlainTextEdit):
	"""
	A TextEdit editor that sends editingFinished events 
	when the text was changed and focus is lost.
	"""

	editingFinished = Signal()
	receivedFocus = Signal()
	# edited=Signal()
	# returnPressed=Signal()

	def __init__(self, parent):
		super().__init__(parent)
		# self.setTabChangesFocus( True )

	def focusInEvent(self, event):
		super().focusInEvent(event)
		self.receivedFocus.emit()

	def focusOutEvent(self, event):
		super().focusOutEvent(event)
		self.editingFinished.emit()
	
	# def keyPressEvent(self,event):
	# 	super().keyPressEvent( event )
	# 	if event.key()==Qt.Key_Return:
	# 		self.returnPressed.emit()
	# 	self.edited.emit()
		