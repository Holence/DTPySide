from __future__ import annotations
from DTPySide import *
from ctypes.wintypes import MSG

class DTDockWidgetWin32(QDockWidget):
	
	"""
	Because DTMainSession and DTMainWindow are based on DTWindow which is a QWidget not QMainWindow,
	so this DTDockWidget cannot dock to any DTWindow.
	
	Just use it as a tiny floating window.
	"""

	BORDER_WIDTH = 5

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
	
		from DTPySide.DTWidget.DTTitleBar import DTTitleBar
		self.TitleBar=DTTitleBar(self)
		self.TitleBar.setWindowTitle(title)
		self.TitleBar.setFull(False)
		self.TitleBar.title_icon.hide()
		self.TitleBar.btn_close.clicked.connect(self.hide)
		self.setTitleBarWidget(self.TitleBar)
			
		# 不知道为什么大小会变掉
		def slot(v):
			if not v:
				self.Size=self.size()
			else:
				self.resize(self.Size.width(),self.Size.height())
		self.Size=self.size()
		self.visibilityChanged.connect(slot)

		self.show()
	
	def nativeEvent(self, eventType, message):
		""" 处理windows消息 """
		try:
			scale=self.app.Scale()
			msg = MSG.from_address(message.__int__())
			if msg.message == win32con.WM_NCHITTEST:
				# 鼠标在窗口中移动

				# 解决多屏下会出现鼠标一直为拖动状态的问题
				
				xPos = (win32api.LOWORD(msg.lParam) -
						self.frameGeometry().x()*scale) % 65536
				yPos = win32api.HIWORD(msg.lParam) - self.frameGeometry().y()*scale
				w, h = self.width()*scale, self.height()*scale
				
				lx = xPos -4 < self.BORDER_WIDTH
				rx = xPos +4 > w - self.BORDER_WIDTH
				ty = yPos -4 < self.BORDER_WIDTH
				by = yPos +4 > h - self.BORDER_WIDTH
				
				if lx and ty:
					return True, win32con.HTTOPLEFT
				elif rx and by:
					return True, win32con.HTBOTTOMRIGHT
				elif rx and ty:
					return True, win32con.HTTOPRIGHT
				elif lx and by:
					return True, win32con.HTBOTTOMLEFT
				elif ty:
					return True, win32con.HTTOP
				elif by:
					return True, win32con.HTBOTTOM
				elif lx:
					return True, win32con.HTLEFT
				elif rx:
					return True, win32con.HTRIGHT
			
			elif msg.message == win32con.WM_NCCALCSIZE:
				# 窗口缩放大小
				return True, 0
			
			return QWidget.nativeEvent(self, eventType, message)

		except Exception as e:
			pass
		