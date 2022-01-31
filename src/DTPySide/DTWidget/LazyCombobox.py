from __future__ import annotations
from DTPySide import *

class LazyCombobox(QComboBox):
	def __init__(self, parent):
		super().__init__(parent)
		self.setFocusPolicy(Qt.StrongFocus)

	def wheelEvent(self, event):
		event.ignore()