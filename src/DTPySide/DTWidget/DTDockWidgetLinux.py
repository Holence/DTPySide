from __future__ import annotations
from DTPySide import *

class DTDockWidgetLinux(QDockWidget):
	
	"""
	Because DTMainSession and DTMainWindow are based on DTWindow which is a QWidget not QMainWindow,
	so this DTDockWidget cannot dock to any DTWindow.
	
	Just use it as a tiny floating window.
	"""

	def eventFilter(self, watched, event) -> bool:
		# prevent docking by double click on edge
		if event.type()==QEvent.NonClientAreaMouseButtonDblClick:
			return True
		return False
	
	def __init__(self, title: str, parent: DTSession.DTMainSession, flags: Qt.WindowFlags = Qt.Window) -> None:
		super().__init__(parent, flags)
		self.setFloating(True)
		self.installEventFilter(self)

		self.app=self.parent().app

		self.setWindowTitle(title)
			
		# 不知道为什么大小会变掉
		def slot(v):
			if not v:
				self.Size=self.size()
			else:
				self.resize(self.Size.width(),self.Size.height())
		self.Size=self.size()
		self.visibilityChanged.connect(slot)

		self.show()
	