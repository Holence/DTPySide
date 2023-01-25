from __future__ import annotations
from DTPySide import *


from ctypes import POINTER, Structure, c_bool, c_int, pointer, sizeof, WinDLL, byref, cast
from ctypes.wintypes import DWORD, HWND, ULONG, POINT, RECT, UINT , LONG, LPCVOID, MSG
from enum import Enum


class WINDOWCOMPOSITIONATTRIB(Enum):
	WCA_UNDEFINED = 0,
	WCA_NCRENDERING_ENABLED = 1,
	WCA_NCRENDERING_POLICY = 2,
	WCA_TRANSITIONS_FORCEDISABLED = 3,
	WCA_ALLOW_NCPAINT = 4,
	WCA_CAPTION_BUTTON_BOUNDS = 5,
	WCA_NONCLIENT_RTL_LAYOUT = 6,
	WCA_FORCE_ICONIC_REPRESENTATION = 7,
	WCA_EXTENDED_FRAME_BOUNDS = 8,
	WCA_HAS_ICONIC_BITMAP = 9,
	WCA_THEME_ATTRIBUTES = 10,
	WCA_NCRENDERING_EXILED = 11,
	WCA_NCADORNMENTINFO = 12,
	WCA_EXCLUDED_FROM_LIVEPREVIEW = 13,
	WCA_VIDEO_OVERLAY_ACTIVE = 14,
	WCA_FORCE_ACTIVEWINDOW_APPEARANCE = 15,
	WCA_DISALLOW_PEEK = 16,
	WCA_CLOAK = 17,
	WCA_CLOAKED = 18,
	WCA_ACCENT_POLICY = 19,
	WCA_FREEZE_REPRESENTATION = 20,
	WCA_EVER_UNCLOAKED = 21,
	WCA_VISUAL_OWNER = 22,
	WCA_LAST = 23


class ACCENT_STATE(Enum):
	""" 客户区状态枚举类 """
	ACCENT_DISABLED = 0,
	ACCENT_ENABLE_GRADIENT = 1,
	ACCENT_ENABLE_TRANSPARENTGRADIENT = 2,
	ACCENT_ENABLE_BLURBEHIND = 3,          # Aero效果
	ACCENT_ENABLE_ACRYLICBLURBEHIND = 4,   # 亚克力效果
	ACCENT_INVALID_STATE = 5


class ACCENT_POLICY(Structure):
	""" 设置客户区的具体属性 """

	_fields_ = [
		("AccentState",     DWORD),
		("AccentFlags",     DWORD),
		("GradientColor",   DWORD),
		("AnimationId",     DWORD),
	]


class WINDOWCOMPOSITIONATTRIBDATA(Structure):
	_fields_ = [
		("Attribute",   DWORD),
		# POINTER()接收任何ctypes类型，并返回一个指针类型
		("Data",        POINTER(ACCENT_POLICY)),
		("SizeOfData",  ULONG),
	]


class DWMNCRENDERINGPOLICY(Enum):
	DWMNCRP_USEWINDOWSTYLE = 0
	DWMNCRP_DISABLED = 1
	DWMNCRP_ENABLED = 2
	DWMNCRP_LAS = 3


class DWMWINDOWATTRIBUTE(Enum):
	DWMWA_NCRENDERING_ENABLED = 1
	DWMWA_NCRENDERING_POLICY = 2
	DWMWA_TRANSITIONS_FORCEDISABLED = 3
	DWMWA_ALLOW_NCPAINT = 4
	DWMWA_CAPTION_BUTTON_BOUNDS = 5
	DWMWA_NONCLIENT_RTL_LAYOUT = 6
	DWMWA_FORCE_ICONIC_REPRESENTATION = 7
	DWMWA_FLIP3D_POLICY = 8
	DWMWA_EXTENDED_FRAME_BOUNDS = 9
	DWMWA_HAS_ICONIC_BITMAP = 10
	DWMWA_DISALLOW_PEEK = 11
	DWMWA_EXCLUDED_FROM_PEEK = 12
	DWMWA_CLOAK = 13
	DWMWA_CLOAKED = 14
	DWMWA_FREEZE_REPRESENTATION = 25
	DWMWA_LAST = 16


class MARGINS(Structure):
	_fields_ = [
		("cxLeftWidth",     c_int),
		("cxRightWidth",    c_int),
		("cyTopHeight",     c_int),
		("cyBottomHeight",  c_int),
	]


class MINMAXINFO(Structure):
	_fields_ = [
		("ptReserved",      POINT),
		("ptMaxSize",       POINT),
		("ptMaxPosition",   POINT),
		("ptMinTrackSize",  POINT),
		("ptMaxTrackSize",  POINT),
	]


class PWINDOWPOS(Structure):
	_fields_ = [
		('hWnd',            HWND),
		('hwndInsertAfter', HWND),
		('x',               c_int),
		('y',               c_int),
		('cx',              c_int),
		('cy',              c_int),
		('flags',           UINT)
	]


class NCCALCSIZE_PARAMS(Structure):
	_fields_ = [
		('rgrc', RECT*3),
		('lppos', POINTER(PWINDOWPOS))
	]


class WindowEffect:
	""" 调用windows api实现窗口效果 """

	def __init__(self):
		# 调用api
		self.user32 = WinDLL("user32")
		self.dwmapi = WinDLL("dwmapi")
		self.SetWindowCompositionAttribute = self.user32.SetWindowCompositionAttribute
		self.DwmExtendFrameIntoClientArea = self.dwmapi.DwmExtendFrameIntoClientArea
		self.DwmSetWindowAttribute = self.dwmapi.DwmSetWindowAttribute
		self.SetWindowCompositionAttribute.restype = c_bool
		self.DwmExtendFrameIntoClientArea.restype = LONG
		self.DwmSetWindowAttribute.restype = LONG
		self.SetWindowCompositionAttribute.argtypes = [
			c_int,
			POINTER(WINDOWCOMPOSITIONATTRIBDATA),
		]
		self.DwmSetWindowAttribute.argtypes = [c_int, DWORD, LPCVOID, DWORD]
		self.DwmExtendFrameIntoClientArea.argtypes = [c_int, POINTER(MARGINS)]
		# 初始化结构体
		self.accentPolicy = ACCENT_POLICY()
		self.winCompAttrData = WINDOWCOMPOSITIONATTRIBDATA()
		self.winCompAttrData.Attribute = WINDOWCOMPOSITIONATTRIB.WCA_ACCENT_POLICY.value[
			0
		]
		self.winCompAttrData.SizeOfData = sizeof(self.accentPolicy)
		self.winCompAttrData.Data = pointer(self.accentPolicy)

	def setAcrylicEffect(self, hWnd, gradientColor: str = "52557018", isEnableShadow: bool = True, animationId: int = 0):
		""" 给窗口开启Win10的亚克力效果34374620 52557018

		Parameter
		----------
		hWnd: int or `sip.voidptr`
			窗口句柄

		gradientColor: str
			十六进制亚克力混合色，对应rgba四个分量

		isEnableShadow: bool
			控制是否启用窗口阴影

		animationId: int
			控制磨砂动画
		
		拖动缓慢：去掉高级系统设置 -> 性能 -> 拖动时显示窗口内容 复选框的 √
		"""

		# 亚克力混合色
		gradientColor = (
			gradientColor[6:]
			+ gradientColor[4:6]
			+ gradientColor[2:4]
			+ gradientColor[:2]
		)
		gradientColor = DWORD(int(gradientColor, base=16))
		# 磨砂动画
		animationId = DWORD(animationId)
		# 窗口阴影
		accentFlags = DWORD(0x20 | 0x40 | 0x80 |
							0x100) if isEnableShadow else DWORD(0)
		self.accentPolicy.AccentState = ACCENT_STATE.ACCENT_ENABLE_ACRYLICBLURBEHIND.value[
			0
		]
		self.accentPolicy.GradientColor = gradientColor
		self.accentPolicy.AccentFlags = accentFlags
		self.accentPolicy.AnimationId = animationId
		# 开启亚克力
		self.SetWindowCompositionAttribute(hWnd, pointer(self.winCompAttrData))

	def setAeroEffect(self, hWnd):
		""" 给窗口开启Aero效果

		Parameter
		----------
		hWnd: int or `sip.voidptr`
			窗口句柄
		"""
		self.accentPolicy.AccentState = ACCENT_STATE.ACCENT_ENABLE_BLURBEHIND.value[0]
		# 开启Aero
		self.SetWindowCompositionAttribute(hWnd, pointer(self.winCompAttrData))

	def moveWindow(self, hWnd):
		""" 移动窗口

		Parameter
		----------
		hWnd: int or `sip.voidptr`
			窗口句柄
		"""
		win32gui.ReleaseCapture()
		win32api.SendMessage(
			hWnd, win32con.WM_SYSCOMMAND, win32con.SC_MOVE + win32con.HTCAPTION, 0
		)

	def addShadowEffect(self, hWnd):
		""" 给窗口添加阴影

		Parameter
		----------
		hWnd: int or `sip.voidptr`
			窗口句柄
		"""
		hWnd = int(hWnd)
		self.DwmSetWindowAttribute(
			hWnd,
			DWMWINDOWATTRIBUTE.DWMWA_NCRENDERING_POLICY.value,
			byref(c_int(DWMNCRENDERINGPOLICY.DWMNCRP_ENABLED.value)),
			4,
		)
		margins = MARGINS(-1, -1, -1, -1)
		self.DwmExtendFrameIntoClientArea(hWnd, byref(margins))

	def addWindowAnimation(self, hWnd):
		""" 打开窗口动画效果

		Parameters
		----------
		hWnd : int or `sip.voidptr`
			窗口句柄
		"""
		style = win32gui.GetWindowLong(hWnd, win32con.GWL_STYLE)
		win32gui.SetWindowLong(
			hWnd,
			win32con.GWL_STYLE,
			style
			# | win32con.WS_MAXIMIZEBOX
			# | win32con.WS_CAPTION
			# | win32con.CS_DBLCLKS
			# | win32con.WS_THICKFRAME,
			| win32con.WS_OVERLAPPEDWINDOW,
		)

		# 奶奶的不写WS_MAXIMIZEBOX、WS_CAPTION的话，拖动到顶端的最大化将会出现空隙
		# 但写了的话用Aero全透明就会出现windows自带的三个窗口title按钮，咋办呢？
		# 只能用亚克力Acrylic，或者用Aero的时候把Title设置为不透明好了……
		# 花了半个多小时的时间……

class DTWindowWin32(QWidget):
	BORDER_WIDTH = 5

	def closeEvent(self, event):
		super().closeEvent(event)
	
	def show(self):
		super().show()
		if self.isMaximized():
			# 如果关掉的时候是最大化的话，再进行恢复show，就会有bug
			self.showNormal()
			self.showMaximized()
		else:
			ShowUp(self)

	def __init__(self, app:DTAPP, parent=None):
		super().__init__(parent=parent)
		self.app=app
		
		self.__monitor_info = None

		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
		self.initializeWindowEffect()
	
	def reInitialize(self):
		self.__monitor_info = None

		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
		self.initializeWindowEffect()
	
	def initializeWindowEffect(self):
		"""设置窗口效果，Normal 或 Aero 或 Acrylic
		"""

		self.windowEffect = WindowEffect()
		self.windowEffect.addWindowAnimation(self.winId())
		
		window_effect=self.app.WindowEffect()

		if window_effect=="Normal":
			# Normal
			self.windowEffect.addShadowEffect(self.winId())
		
		elif window_effect=="Aero":
			# Aero
			self.windowEffect.setAeroEffect(self.winId())
			self.windowEffect.addShadowEffect(self.winId())
			
		elif window_effect=="Acrylic":
			# Acrylic
			self.windowEffect.setAcrylicEffect(self.winId())
	
	
	def isWindowMaximized(self, hWnd) -> bool:
		""" 判断窗口是否最大化 """
		# 返回指定窗口的显示状态以及被恢复的、最大化的和最小化的窗口位置，返回值为元组
		windowPlacement = win32gui.GetWindowPlacement(hWnd)
		if not windowPlacement:
			return False
		return windowPlacement[1] == win32con.SW_MAXIMIZE

	def nativeEvent(self, eventType, message):
		""" 处理windows消息 """
		try:
			scale=self.app.Scale()
			msg = MSG.from_address(message.__int__())
			if msg.message == win32con.WM_NCHITTEST and not self.isWindowMaximized(msg.hWnd):
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
				if self.isWindowMaximized(msg.hWnd):
					self.monitorNCCALCSIZE(msg)
					
					#变成最大化
					try:
						self.TitleBar.btn_maximize.setIcon(self.TitleBar.restore_icon)
					except:
						pass
				else:
					
					#变成正常
					try:
						self.TitleBar.btn_maximize.setIcon(self.TitleBar.maximize_icon)
					except:
						pass
				return True, 0
			
			elif msg.message == win32con.WM_GETMINMAXINFO:
				# 窗口移动
				if self.isWindowMaximized(msg.hWnd):
					window_rect = win32gui.GetWindowRect(msg.hWnd)
					if not window_rect:
						return False, 0
					# 获取显示器句柄
					monitor = win32api.MonitorFromRect(window_rect)
					if not monitor:
						return False, 0
					# 获取显示器信息
					monitor_info = win32api.GetMonitorInfo(monitor)
					monitor_rect = monitor_info['Monitor']
					work_area = monitor_info['Work']
					# 将lParam转换为MINMAXINFO指针
					info = cast(msg.lParam, POINTER(MINMAXINFO)).contents
					# 调整窗口大小
					info.ptMaxSize.x = work_area[2] - work_area[0]
					info.ptMaxSize.y = work_area[3] - work_area[1]
					info.ptMaxTrackSize.x = info.ptMaxSize.x
					info.ptMaxTrackSize.y = info.ptMaxSize.y
					# 修改左上角坐标
					info.ptMaxPosition.x = abs(window_rect[0] - monitor_rect[0])
					info.ptMaxPosition.y = abs(window_rect[1] - monitor_rect[1])
					return True, 1
			
			return QWidget.nativeEvent(self, eventType, message)

		except:
			pass

	def monitorNCCALCSIZE(self, msg: MSG):
		"""放大到全屏"""

		monitor = win32api.MonitorFromWindow(msg.hWnd)
		# 如果没有保存显示器信息就直接返回，否则接着调整窗口大小
		if monitor is None and not self.__monitor_info:
			return
		elif monitor is not None:
			self.__monitor_info = win32api.GetMonitorInfo(monitor)
		# 调整窗口大小
		params = cast(msg.lParam, POINTER(NCCALCSIZE_PARAMS)).contents
		params.rgrc[0].left = self.__monitor_info['Work'][0]
		params.rgrc[0].top = self.__monitor_info['Work'][1]
		params.rgrc[0].right = self.__monitor_info['Work'][2]
		params.rgrc[0].bottom = self.__monitor_info['Work'][3]