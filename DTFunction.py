from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys, os
import re
import pickle
from functools import partial
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



def Clear_Layout(layout):
	for i in reversed(range(layout.count())): 
		layout.takeAt(i).widget().deleteLater()

def Font_Resize(font,resize_ratio):
	new_font=QFont(font)
	fontsize=font.pointSize()
	fontsize=int(fontsize*resize_ratio)
	new_font.setPointSize(fontsize)
	return new_font

def Delay_Msecs(msecs):
	"传入int类型的延迟毫秒数msecs"
	dieTime= QTime.currentTime().addMSecs(msecs)
	while QTime.currentTime() < dieTime:
		QCoreApplication.processEvents(QEventLoop.AllEvents, 100)

def QDate_to_Str(date,mode="0"):
	"""
	mode="0" : 20210101
	mode="0." : 2021.01.01
	mode="." : 2021.1.1

	"""
	if mode=="0":
		return "%04d%02d%02d"%(date.year(),date.month(),date.day())
	elif mode=="0.":
		return "%04d.%02d.%02d"%(date.year(),date.month(),date.day())
	elif mode==".":
		return "%d.%d.%d"%(date.year(),date.month(),date.day())

def Str_To_QDate(s):
	return QDate(int(s[:4]),int(s[4:6]),int(s[6:8]))

def Generate_ConicalGradientColor(colorList,cube_width):
	n=len(colorList)
	if n==0:
		return QColor("#5B1803")
	
	angle=0
	delta=1/n
	colors=[]
	for i in range(n):
		colors.append((angle,colorList[i]))
		colors.append((angle+delta-0.01,colorList[i]))
		angle+=delta

	color=QConicalGradient(cube_width/2,cube_width/2,90)
	color.setStops(colors)
	return color

def show_ContextMenu_Beneath(menu,btn):
	btn_pos=btn.pos()
	btn_height=btn.height()
	btn_pos+=QPoint(0,btn_height)
	true_pos=btn.parentWidget().mapToGlobal(btn_pos)
	menu.exec_(true_pos)

def show_ContextMenu_Right(menu,btn):
	btn_pos=btn.pos()
	btn_height=btn.height()
	btn_pos+=QPoint(btn_height,0)
	true_pos=btn.parentWidget().mapToGlobal(btn_pos)
	menu.exec_(true_pos)

def Generate_Key(password):
	"""
	根据password生成一个固定的salt，用salt生成一个PBKDF2，用PBKDF2和password生成key
	所以给定一个固定的password，将返回那个固定的key。
	"""
	salt=password.encode()[::-1]
	password=password.encode()
	kdf=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,backend=default_backend())
	key=base64.urlsafe_b64encode(kdf.derive(password))
	return key

def Fernet_Encrypt_Save(password,data,file_path):
	try:
		data=pickle.dumps(data)
		key=Generate_Key(password)

		fer=Fernet(key)
		encrypt_data=fer.encrypt(data)

		with open(file_path,"wb") as f:
			f.write(encrypt_data)
		
		return True
	except:
		return False

def Fernet_Decrypt_Load(password,file_path):
	try:
		key=Generate_Key(password)
	
		with open(file_path,"rb") as f:
			data=f.read()
		
		fer=Fernet(key)
		decrypt_data=fer.decrypt(data)
		decrypt_data=pickle.loads(decrypt_data)

		return decrypt_data
	except:
		return False

def Fernet_Encrypt(password,data):
	try:
		data=pickle.dumps(data)
		key=Generate_Key(password)

		fer=Fernet(key)
		encrypt_data=fer.encrypt(data)
		
		return encrypt_data
	except:
		return False

def Fernet_Decrypt(password,data):
	try:
		key=Generate_Key(password)
		
		fer=Fernet(key)
		decrypt_data=fer.decrypt(data)
		decrypt_data=pickle.loads(decrypt_data)

		return decrypt_data
	except:
		return False


##############################################################################################

from ctypes import POINTER, Structure,  c_bool, c_int, pointer, sizeof, WinDLL, byref, cast
from ctypes.wintypes import DWORD, HWND, ULONG, POINT, RECT, UINT , LONG, LPCVOID, MSG
from win32.lib import win32con
from win32 import win32gui, win32api
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

	def setAcrylicEffect(self, hWnd, gradientColor: str = "FFFFFF20", isEnableShadow: bool = True, animationId: int = 0):
		""" 给窗口开启Win10的亚克力效果

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

##############################################################################################

def Generate_StyleSheet(theme:str, window_effect:str, font:QFont):
	
	font_size=font.pointSize()
	font_family=font.family()

	stylesheet=""

	if theme=="Dracula":
		DEEPDARK="#242830" # Border和GroupBox、TitleBarFrame的Background
		BACKGROUND="#282C34" # background
		SOFTDARK="#3A414D" # LineEdit的背景
		DIM="#696969" # disable的文字
		PRESSED = "#D7AAE6" # Button Clicked
		FOCUSED="#BD93F9" # Button Hover
		TEXT="#EBEBEB" # 文字

	elif theme=="Dark":
		DEEPDARK="#232323"
		BACKGROUND="#2A2A2A"
		SOFTDARK="#353535"
		DIM="#5c5c5c"
		PRESSED = "#7AB6F3"
		FOCUSED="#2A82DA"
		TEXT="#FFFFFF"
	
	elif theme=="Light":
		DEEPDARK="#8972CC"
		BACKGROUND="#A796DB"
		SOFTDARK="#B9B5FF"
		DIM="#D8C2FF"
		PRESSED = "#ECCAFF"
		FOCUSED="#E2C6FF"
		TEXT="#2D2730"
	
	if window_effect=="Normal":
		stylesheet+=f"""
			* {{
				background: {BACKGROUND};
			}}
		"""
		pass
	else:
		stylesheet+=f"""
			* {{
				background: transparent;
			}}

			QDialog{{
				background-color: {BACKGROUND};
			}}
		"""
	

	stylesheet+=f"""

	QWidget
	{{
		color: {TEXT};
		font-family: {font_family};
	}}

	QDialog {{
		border: 2px solid {DEEPDARK};
		border-radius: 1px;
	}}

	#DTMainWindow #statusBar{{
		background-color: {SOFTDARK};
	}}

	#DTLogin #label_lock{{
		min-width: {int(font_size*1.5)}px;
		max-width: {int(font_size*1.5)}px;
		min-height: {int(font_size*1.5)}px;
		max-height: {int(font_size*1.5)}px;
	}}

	/* TitleBar */

	#TitleBarFrame{{
		min-width: {font_size*8}px;
	}}
	#TitleBarFrame #label_titlebar{{
		font-size: {int(font_size*1.2)}pt;
		font-weight: bold;
	}}

	#TitleBarFrame QPushButton {{
		border: none;
		background-color: transparent;	
		icon-size: {int(font_size*1.4)}px;
		min-width: {int(font_size*1.4)}px;
		max-width: {int(font_size*1.4)}px;
		min-height: {int(font_size*1.4)}px;
		max-height: {int(font_size*1.4)}px;
	}}

	#TitleBarFrame QPushButton:hover{{
		background-color: {BACKGROUND};
		border-style: solid;
		border-radius: 4px;
	}}
	#TitleBarFrame QPushButton:pressed {{
		background-color: {SOFTDARK};
		border-style: solid;
		border-radius: 4px;
	}}

	
	#TitleBarFrame #title_icon{{
		icon-size: {int(font_size*2)}px;
		min-width: {int(font_size*2)}px;
		max-width: {int(font_size*2)}px;
		min-height: {int(font_size*2)}px;
		max-height: {int(font_size*2)}px;
	}}
	#TitleBarFrame #title_icon:hover{{
		background-color: rgba(0, 0, 0, 0);
	}}
	#TitleBarFrame #title_icon:pressed {{
		background-color: rgba(0, 0, 0, 0);
	}}
	
	#TitleBarFrame #btn_close:hover{{
		background-color: rgb(232, 17, 35);
		border-style: solid;
		border-radius: 4px;
	}}
	#TitleBarFrame #btn_close:pressed {{
		background-color: rgb(241, 112, 122);
		border-style: solid;
		border-radius: 4px;
	}}
	#TitleBarFrame * {{
		background-color: {DEEPDARK};
	}}
	#TitleBarFrame {{
		background-color: {DEEPDARK};
	}}

	/* ---------------------------------------- */

	QFrame{{
		color: {TEXT};
	}}
	QMainWindow::separator{{
		border: 1px solid {DEEPDARK};
		width: 4px;
		height: 4px;
	}}
	QMainWindow::separator:hover{{
		background: {FOCUSED};
	}}
	QSplitter::handle{{
		border: 1px solid {DEEPDARK};
		width: 4px;
		height: 4px;
	}}
	QSplitter::handle:hover{{
		/*splitter->handle(1)->setAttribute(Qt::WA_Hover, true);才生效*/
		border-color: {FOCUSED};
	}}
	QSplitter::handle:pressed{{
		border-color: {PRESSED};
	}}
	QSizeGrip{{
		background-color: none;
	}}
	


	/* MenuBar Menu */
	QMenuBar {{
		background-color: {BACKGROUND};
		spacing: 1px;
		border-bottom: 1px solid {DEEPDARK};
	}}

	QMenuBar::item{{
		background: transparent;
		padding: 1px 8px;
	}}

	QMenuBar::item:selected{{
		background: {FOCUSED};
		border: 1px solid {FOCUSED};
	}}

	QMenuBar::item:pressed{{
		background: {PRESSED};
		border: 1px solid {PRESSED};
		padding-top: 4px;
	}}

	QMenu {{
		background-color: {BACKGROUND};
		border: 1px solid {DEEPDARK};
		margin: 1px;
		padding: 1px;
	}}

	QMenu::item{{
		padding: 2px 25px 2px 15px;
		border: 1px solid transparent;
		margin: 1px;
		font-size: {int(font_size*0.7)}pt;
	}}
	QMenu::icon {{
		width: 15px;
		height: 15px;
		padding:5px;
		border-right: 1px inset {DEEPDARK};
	}}

	QMenu::item:selected {{
		border-color: {DEEPDARK};
		background: {FOCUSED};
	}}

	QMenu::separator {{
		height: 1px;
		background: {DEEPDARK};
		margin: 0 5px;
	}}

	QMenu::indicator {{/*checked 的√*/
		width: 13px;
		height: 13px;
		padding:2px;
	}}
	QMenu::icon:checked {{ /* appearance of a 'checked' icon */
		background: {FOCUSED};
		border: 1px inset {PRESSED};
		border-radius: 3px;
		padding: 2px;
	}}


	/* ToolBar StatusBar */

	QToolBar {{
		background: {BACKGROUND};
		spacing: 1px;
		padding: 1px;
		border-bottom: 1px solid {DEEPDARK};
	}}

	QStatusBar{{
		background: transparent;
		border-top:1px solid {DEEPDARK};
	}}

	QStatusBar::item {{
		margin: 2px 0;
		border-left: 1px solid {DEEPDARK};
	}}

	QStatusBar QLabel{{
		background: transparent;
		margin: 0  2px;
	}}

	QStatusBar QPushButton{{
		background: transparent;
		margin: 0  2px;
	}}

	QStatusBar QPushButton:hover{{
		background: {FOCUSED};
		margin: 0  2px;
	}}


	/* Label */

	QLabel {{
		background: transparent;
		border: 1px solid transparent;
	}}

	QToolTip {{
		background: {SOFTDARK};
		color: {TEXT}
	}}


	/* TextBox */

	QLineEdit {{
		background: {SOFTDARK};
		selection-background-color: {FOCUSED};
		border: 1px solid {DEEPDARK};
		border-radius: 2px;
		height: {int(font_size*1.5)}px;
	}}


	QLineEdit:focus{{
		border-color: {FOCUSED};
	}}
	
	QLineEdit[echoMode="2"]{{
		lineedit-password-character: 9679; /*字符的ascii码35 88等 */
	}}

	QLineEdit:read-only {{
		color: {DIM};
	}}

	QLineEdit:disabled{{
		color: {DIM};
	}}

	QTextEdit, QPlainTextEdit{{
		background-color: {SOFTDARK};
		selection-background-color:{FOCUSED};
		border: 1px solid {DEEPDARK};
	}}
	QTextEdit:focus, QPlainTextEdit:focus{{
		border-color: {FOCUSED};
	}}

	/* Button */


	QPushButton {{
		border: 1px solid {DEEPDARK};
		border-radius: 3px;
		background-color: {SOFTDARK};
		font-family: "Hack";
		font-size: {int(font_size*0.7)}pt;
	}}

	QPushButton:hover{{
		background-color: {FOCUSED};
		border-color: {PRESSED};
	}}

	QPushButton:pressed
	{{
		border-width: 1px;
		background-color: {PRESSED};
		border-color: {DEEPDARK};
	}}

	QPushButton:focus, QPushButton:default {{
		border-color: {FOCUSED};
	}}

	QDialogButtonBox QPushButton{{
		font-size: {int(font_size*0.7)}pt;
		min-width: {int(font_size*4)}px;
		min-height: {int(font_size*1.5)}px;
	}}
	
	QToolButton {{
		font-family: "Hack";
		font-size: {int(font_size*0.7)}pt;
		height: {int(font_size*1.8)}px;
	}}
	QToolButton,QToolButton:unchecked {{
		/* ToolBar里的按钮和带下拉菜单的按钮 */
		border: 1px solid transparent;
		border-radius: 3px;
		background-color: {SOFTDARK};
		margin: 1px;
	}}
	QToolButton:checked{{
		background-color: {FOCUSED};
		border-color: {PRESSED};
	}}
	QToolButton:hover{{
		background-color: {FOCUSED};
		border-color: {PRESSED};
	}}

	QToolButton:pressed,QToolButton:checked:hover{{
		background-color: {PRESSED};
		border-color: {FOCUSED};
	}}
	QToolButton:checked:pressed{{
		background-color: {FOCUSED};
	}}

	/* only for MenuButtonPopup */
	QToolButton[popupMode="1"]{{
		padding-left: 1px;
		padding-right: 15px;
		border: 1px solid {DEEPDARK};
		min-height: 15px;
		background-color: {SOFTDARK};
	}}
	QToolButton[popupMode="1"]:hover{{
		background-color: {FOCUSED};
		border-color: {PRESSED};
	}}
	QToolButton[popupMode="1"]:pressed{{
		border-width: 1px;
		background-color: {PRESSED};
		border-color: {DEEPDARK};
	}}
	QToolButton::menu-button {{
		border: 1px solid {DEEPDARK};
		border-top-right-radius: 2px;
		border-bottom-right-radius: 2px;
		width: 16px;
	}}

	QRadioButton{{
		background: transparent;
		font-family: "Hack";
		font-size: {int(font_size*0.7)}pt;
	}}
	QRadioButton::indicator {{
		width: 10px;
		height: 10px;
		border: 2px solid {TEXT};
		border-radius: 7px;
	}}
	QRadioButton::indicator:checked {{
		background: {FOCUSED};
	}}
	QRadioButton::indicator:unchecked {{
		background: transparent;
	}}

	QCheckBox{{
		font-family: "Hack";
		font-size: {int(font_size*0.7)}pt;
		background: transparent;
	}}
	QCheckBox::indicator {{
		width: 10px;
		height: 10px;
		border: 2px solid {TEXT};
		border-radius: 7px;
	}}
	QCheckBox::indicator:checked {{
		background-color: {FOCUSED};
	}}
	QCheckBox::indicator:unchecked {{
		background-color: transparent;
	}}
	QCheckBox::indicator:indeterminate {{
		background-color: {FOCUSED};
		border-radius: 2px;
	}}



	/* ComboBox */

	QComboBox{{
		background-color: {SOFTDARK};
		border: 1px solid {DEEPDARK};
	}}
	QComboBox:focus{{
		border-color: {FOCUSED};
	}}
	QComboBox:on {{
		/* shift the text when the popup opens */
		padding-top: 2px;
		padding-left: 2px;
	}}
	QComboBox::item {{
		height: {font_size*2}px;
		font-size: {font_size}pt;
		
	}}
	QComboBox::item:selected {{
		background-color: {FOCUSED};
	}}
	

	/* SpinBox DateTime */

	QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit{{
		background-color: {SOFTDARK};
		border-top-right-radius: 5px;
		border-bottom-right-radius: 5px;
		selection-background-color: {FOCUSED};
	}}
	QSpinBox:focus, QDoubleSpinBox:focus, QDateEdit:focus, QTimeEdit:focus, QDateTimeEdit:focus{{
		border: 1px solid {DEEPDARK};
		border-color: {FOCUSED};
	}}

	QSpinBox::up-button, QDoubleSpinBox::up-button, QDateEdit::up-button, QTimeEdit::up-button, QDateTimeEdit::up-button{{
		background-color: {SOFTDARK};
		subcontrol-origin: border;
		subcontrol-position: top right;
		width: {font_size}px;
		border: 1px solid {DEEPDARK};
		border-top-right-radius: 5px;
		margin-top: 1px;
		margin-right: 1px;
	}}
	QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed, QDateEdit::up-button:pressed, QTimeEdit::up-button:pressed, QDateTimeEdit::up-button:pressed {{
		background-color: {FOCUSED};
	}}
	QSpinBox::up-arrow, QDoubleSpinBox::up-arrow, QDateEdit::up-arrow, QTimeEdit::up-arrow, QDateTimeEdit::up-arrow{{
		image: url(:/icon/white/white_chevron-up.svg);
	}}

	QSpinBox::down-button, QDoubleSpinBox::down-button, QDateEdit::down-button, QTimeEdit::down-button, QDateTimeEdit::down-button{{
		background-color: {SOFTDARK};
		subcontrol-origin: border;
		subcontrol-position: bottom right;
		width: {font_size}px;
		border: 1px solid {DEEPDARK};
		border-bottom-right-radius: 5px;
		margin-bottom: 1px;
		margin-right: 1px;
	}}
	QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed, QDateEdit::down-button:pressed, QTimeEdit::down-button:pressed, QDateTimeEdit::down-button:pressed {{
		background-color: {FOCUSED};
	}}
	QSpinBox::down-arrow, QDoubleSpinBox::down-arrow, QDateEdit::down-arrow, QTimeEdit::down-arrow, QDateTimeEdit::down-arrow{{
		image: url(:/icon/white/white_chevron-down.svg);
	}}
	


	/* Slider ProgressBar */

	QProgressBar {{
		background-color: {SOFTDARK};
		border: 1px solid {DEEPDARK};
		border-radius: 4px;
		text-align: center;
	}}

	QProgressBar::chunk {{
		background-color: {FOCUSED};
	}}

	QSlider{{
		background: transparent;
		min-height: 14px;
		min-width: 14px;
	}}
	
	QSlider::handle {{
		background: {FOCUSED};
		border: 1px solid {DEEPDARK};
		border-radius: 6px;
	}}

	QSlider::groove:horizontal {{
		height: 12px;
	}}
	QSlider::handle:horizontal{{
		width: 12px;
		height: 14px;
		margin: -7px;
	}}

	QSlider::groove:vertical{{
		width: 12px;
	}}
	QSlider::handle:vertical{{
		width: 14px;
		height: 12px;
		margin: -7px;
	}}
	
	QSlider::add-page{{
		/*还没有滑上去的地方*/
		background:{SOFTDARK};
	}}
	QSlider::sub-page{{
		/*已经划过的从地方*/                            
		background: {FOCUSED};
	}}


	/* ScrollBar */

	QScrollBar{{
		background-color: {SOFTDARK};
		border: 1px solid {DEEPDARK};
		border-radius: 5px;
		padding: 1px;
		height: 10px;
		width: 10px;
	}}
	QScrollBar::handle{{
		border-radius: 3px;
		background: {FOCUSED};
		min-width: 16px;
		min-height: 16px;
	}}
	QScrollBar::handle:hover {{
		background: {PRESSED};
	}}
	QScrollBar::add-line, QScrollBar::sub-line,
	QScrollBar::add-page, QScrollBar::sub-page {{
		width: 0px;
		background: transparent;
	}}
	QScrollArea{{
		border: none;
	}}

	/* DockWidget*/

	QDockWidget, QDockWidget > QWidget /*not work*/
	{{
		border-color: {DEEPDARK}; /*qt bug*/
		background: transparent;
	}}
	QDockWidget::title {{
		border-bottom: 1px solid {DEEPDARK};
		text-align: left;
		padding: 6px;
	}}


	/* GroupBox */

	QGroupBox {{
		background-color: {DEEPDARK};
		border: 1px solid {DEEPDARK};
		border-radius: 4px;
		margin-top: 2em;
	}}
	QGroupBox::title {{
		subcontrol-origin: margin;
		subcontrol-position: top left;
		left: 1em;

	}}

	/* ToolBox */

	QToolBox{{
		border: 1px solid {DEEPDARK};
	}}
	QToolBox::tab {{
		background: {SOFTDARK};
		border: 1px solid {DEEPDARK};
		border-radius: 1px;
	}}
	QToolBox::tab:hover {{
		background-color: {FOCUSED};
		border-color: transparent;
	}}
	QToolBox::tab:pressed {{
		background-color: {PRESSED};
		border-color: transparent;
	}}
	QToolBox::tab:selected {{
		font-weight: bold;
		border-color: {FOCUSED};
	}}


	/* TabWidget */

	QTabWidget{{
		margin-top:10px;
	}}
	QTabWidget::pane{{
		border: 1px solid {DEEPDARK};
	}}
	QTabWidget::tab-bar {{
		left: 0px;
	}}
	QTabBar::tab {{
		background: {SOFTDARK};
		border: 1px solid {DEEPDARK};
		padding: 3px 5px;    
	}}
	QTabBar::tab:hover {{
		background: {FOCUSED};
		border-color: transparent;
	}}
	QTabBar::tab:selected {{
		background: {FOCUSED};
		border-color: {PRESSED};
	}}
	QTabBar::tab:pressed {{
		background: {PRESSED};
		border-color: transparent;
	}}
	QTabBar::tab:focus {{
		border-color: {FOCUSED};
	}}
	QTabBar::tab:top{{
		margin-top: 3px;
		border-bottom: transparent;
		margin-right: 1px;
	}}
	QTabBar::tab:bottom{{
		margin-bottom: 3px;
		border-top: transparent;
		margin-right: 1px;
	}}
	QTabBar::tab:left{{
		border-right: transparent;
		margin-bottom: 1px;
	}}
	QTabBar::tab:right{{
		border-left: transparent;
		margin-bottom: 1px;
	}}


	/* QHeaderView for list table */

	QHeaderView {{
		border: none;
		margin: 0px;
		padding: 0px;
	}}
	QHeaderView::section, QTableCornerButton::section {{
		/*设置表头属性*/ /*表格左上角小框框*/
		background-color: {SOFTDARK};
		padding: 0 3px;
		border-right: 1px solid {DEEPDARK};
		border-bottom: 1px solid {DEEPDARK};
		border-radius: 0px;
	}}
	QHeaderView::section:hover, QTableCornerButton::section:hover{{
		background-color: {FOCUSED};
	}}
	QHeaderView::section:pressed{{
		background-color: {PRESSED};
	}}
	QHeaderView::section:checked {{
		background-color: {FOCUSED};
	}}


	/* QTableWidget */

	QTableWidget, QTableView
	{{
		gridline-color: {DEEPDARK}; /*表格中的网格线条颜色*/
		background: {BACKGROUND};
		alternate-background-color: {FOCUSED};
		selection-background-color:{FOCUSED}; /*鼠标选中时背景色*/
		border:1px solid {DEEPDARK}; /*边框线的宽度、颜色*/
	}}
	QTableView::item, QTabWidget::item{{
		background: transparent;
		outline-style: none;
		border: none;
	}}

	QTableView::item:hover {{
		background: {FOCUSED};
		border: 1px solid {FOCUSED};
	}}

	QTableView::item:selected {{
		background: {FOCUSED};
		color: {TEXT};
	}}

	QTableView::item:selected:active {{
		background: {FOCUSED};
	}}

	QTableWidget QComboBox{{
		margin: 2px;
		border: none;
	}}

	QListView, QTreeView, QTableView {{
		border:1px solid {DEEPDARK};
	}}
	QListView::item:hover, QTreeView::item:hover, QTableView::item:hover {{
		background: transparent;
	}}
	QListView::item:selected , QTreeView::item:selected, QTableView::item:selected {{
		background: {FOCUSED};
	}}
	QTreeView::branch:selected{{
		background: {FOCUSED};
	}}

	"""

	return stylesheet

