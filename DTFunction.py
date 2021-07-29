from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys, os, shutil
import re
import copy
import time
import requests
import urllib #淦！最新版的urllib3不支持代理。pip install urllib3==1.25.11就行了
from lxml import etree
import pickle
import json
import feedparser
import pypinyin
from functools import partial
from win32com.shell import shell,shellcon
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

def QDate_to_Str(date:QDate, mode="0"):
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

def Str_To_QDate(s:str, mode="0"):
	"""
	mode="0" : 20210101
	mode="0." : 2021.01.01
	mode="." : 2021.1.1
	"""
	if mode=="0":
		return QDate(int(s[:4]),int(s[4:6]),int(s[6:8]))
	elif mode=="0." or mode==".":
		date=s.split(".")
		year=date[0]
		month=date[1]
		day=date[2]
		return QDate(int(year),int(month),int(day))

def QDate_to_Tuple(date:QDate):
	return (date.year(),date.month(),date.day())

def WhatDayIsToday(mode=0):
	"""返回年月日

	Args:
		mode (int, optional):选择返回的类型。

		0：Tuple

		1: QDate
		
		"0": str: 20210101
		
		"0.": str: 2021.01.01
		
		".": str: 2021.1.1.
		
		Defaults to 0.
	"""
	today=time.localtime()
	if mode==0:
		return today.tm_year,today.tm_mon,today.tm_mday
	elif mode==1:
		return QDate(today.tm_year,today.tm_mon,today.tm_mday)
	elif mode in ["0","0.","."]:
		return QDate_to_Str(QDate(today.tm_year,today.tm_mon,today.tm_mday),mode)

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

def Json_Save(data,file_path):
	with open(file_path,"w",encoding="utf-8") as f:
		json.dump(data,f,ensure_ascii=False,indent=4)

def Json_Load(file_path):
	with open(file_path,"r",encoding="utf-8") as f:
		data=json.load(f)
	return data

def Str_to_AZ(input):
	
	def cn_to_az(last_name):
		rows = pypinyin.pinyin(last_name, style=pypinyin.NORMAL)
		return ''.join(row[0][0] for row in rows if len(row) > 0)

	def jp_to_az(i):
		jp1=["”","“","《","》","あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ"]
		jp2=["”","“","《","》","ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","サ","シ","ス","セ","ソ","タ","チ","ツ","テ","ト","ナ","ニ","ヌ","ネ","ノ","ハ","ヒ","フ","ヘ","ホ","マ","ミ","ム","メ","モ","ヤ","ユ","ヨ","ラ","リ","ル","レ","ロ","ワ","ヲ","ン","ガ","ギ","グ","ゲ","ゴ","ザ","ジ","ズ","ゼ","ゾ","ダ","ヂ","ヅ","デ","ド","バ","ビ","ブ","ベ","ボ","パ","ピ","プ","ペ","ポ"]
		az=["”","“","《","》","a","i","u","e","o","ka","ki","ku","ke","ko","sa","si","su","se","so","ta","ti","tu","te","to","na","ni","nu","ne","no","ha","hi","hu","he","ho","ma","mi","mu","me","mo","ya","yu","yo","ra","ri","ru","re","ro","wa","wo","n","ga","gi","gu","ge","go","za","ji","zu","ze","zo","da","di","du","de","do","ba","bi","bu","be","bo","pa","pi","pu","pe","po"]
		try:
			n=jp1.index(i)
			return az[n]
		except:
			try:
				n=jp2.index(i)
				return az[n]
			except:
				pass
				# print("%s	假名好像不完整\n"%i)
		return ""
	
	output=""
	
	#用unicode划分语言区
	for i in input:
		if re.match(r"[\u0000-\u007F]",i):#英
			output+=i.lower()
		elif re.match(r"[\u4E00-\u9FFF]",i):#中
			output+=cn_to_az(i[0])
		elif re.match(r"[\u0800-\u4DFF]",i):#日，\u4E00是中文的一
			output+=jp_to_az(i)
		# if re.match(r"[\uAC00-\uD7FF]",c)#韩
		else:
			output+=i
		
	return output

def List_Intersection(a:list, b:list) -> list:
	return list(set(a).intersection(set(b)))

def List_Union(a:list, b:list) -> list:
	return list(set(a).union(set(b)))

def List_Difference(a:list, b:list) -> list:
	return list(set(a).difference(set(b)))
	
def List_Symmetric_Difference(a:list, b:list) -> list:
	return list(set(a).symmetric_difference(set(b)))

def List_Intersection_Full(a:list, b:list) -> list:
	c=[]
	for i in a:
		if i in b:
			c.append(i)
	return c

def List_Union_Full(a:list, b:list) -> list:
	c=copy.deepcopy(a)
	for i in b:
		if i not in c:
			c.append(i)
	return c

def List_Difference_Full(a:list, b:list) -> list:
	c=[]
	for i in a:
		if i not in b:
			c.append(i)
	return c

def List_Symmetric_Difference_Full(a:list, b:list) -> list:
	c=[]
	for i in a:
		if i not in b:
			c.append(i)
	for i in b:
		if i not in a:
			c.append(i)
	return c

def GetWebPageResponse(url,cookie=""):
	head={}

	if cookie!="":
		head["cookie"]=cookie
	
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	
	try:
		# response=requests.get(url,headers=head,timeout=3)#
		response=requests.get(url,headers=head,timeout=3)
		return True,response
	except Exception as e:
		return False,e

def GetWebPageInfo(url="",cookie="",response=None):
	if response==None:
		status,response=GetWebPageResponse(url,cookie)
	else:
		status=True
	
	if status==True:
		return True,response.raw.info()
	else:
		return False,response

def GetWebPageType(url="",cookie="",response=None):
	if response==None:
		status,response=GetWebPageInfo(url,cookie)
	else:
		status=True
	
	if status==True:
		return status,response["Content-Type"]
	else:
		return False,response

def GetWebPageHTML(url="",cookie="",response=None):
	if response==None:
		status,response=GetWebPageResponse(url,cookie)
	else:
		status=True
	
	if status==True:
		if response.encoding!="GB2312" and response.encoding!="GBK":
			response.encoding='utf-8'
		else:
			response.encoding="GBK"
		return True,response.text
	else:
		return False,response

def GetWebPageTitle(url="",cookie="",response=None):
	"成功的话返回(True,title)，失败的话返回(False,Exception)，其中如果Title中包含url编码（比如|对应的是%7C），自动解析成utf-8编码"
	if response==None:
		status,html=GetWebPageHTML(url,cookie)
	else:
		status,html=GetWebPageHTML(response=response)

	
	if status==True:
		try:
			html=etree.HTML(html)
			title=html.xpath("/html/head/title/text()")
			title=urllib.parse.unquote(title[0],'utf-8')
			return True,title
		except:
			try:
				#YouTube的channel页面的标题竟然在body里面……
				title=html.xpath("/html/body/title/text()")
				title=urllib.parse.unquote(title[0],'utf-8')
				return True,title
			except Exception as e:
				return False,e
	else:
		return False,html


def GetWebFavIcon(url="",cookie="",response=None):
	if response==None:
		status,html=GetWebPageHTML(url,cookie)
	else:
		status,html=GetWebPageHTML(response=response)

	if status==True:
		try:
			html=etree.HTML(html)
			icon_url=html.xpath("//*[@rel='icon']/@href")[0]
			icon_url=urllib.parse.urljoin(url,icon_url)
			status,icon=GetWebPagePic(icon_url)
			
			return status,icon
		except:
			try:
				icon_url=html.xpath("//*[@rel='shortcut icon']/@href")[0]
				icon_url=urllib.parse.urljoin(url,icon_url)
				status,icon=GetWebPagePic(icon_url)
				
				return status,icon
			except Exception as e:
				return False,e
	else:
		return False,html

def GetWebPagePic(url="",cookie="",response=None):
	if response==None:
		status,response=GetWebPageResponse(url,cookie)
	else:
		status=True
	
	if status==True:
		return True,response.content
	else:
		return False,response

def Delete_to_Recyclebin(dir):
	"删除成功返回True"
	result = shell.SHFileOperation((0,shellcon.FO_DELETE,dir,None, shellcon.FOF_SILENT | shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION,None,None))  #删除文件到回收站
	return result[0]==0

##############################################################################################

from ctypes import POINTER, Structure, c_bool, c_int, pointer, sizeof, WinDLL, byref, cast
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

##############################################################################################

def Generate_StyleSheet(theme:str, window_effect:str, font:QFont):
	
	# font_size=18
	font_family=font.family()

	stylesheet=""

	if theme=="Dracula":
		# DEEPDARK="#202329" # Border和GroupBox、TitleBarFrame的Background 242830
		# BACKGROUND="#282C34" # background
		# SOFTDARK="#313341" # LineEdit的背景 3A414D
		# DIM="#696969" # disable的文字
		# PRESSED = "#A67DB4" # Button Clicked D7AAE6
		# FOCUSED="#8C6BBB" # Button Hover BD93F9
		# TEXT="#EBEBEB" # 文字
		# ICONCOLOR="white"

		DEEPDARK="#191A21" # Border和GroupBox、TitleBarFrame的Background
		BACKGROUND="#21222C" # background
		SOFTDARK="#282A36" # LineEdit的背景
		DIM="#404257" # disable的文字 6272A4
		PRESSED = "#A67DB4" # Button Clicked 
		FOCUSED="#8C6BBB" # Button Hover 
		TEXT="#E0E0E0" # 文字
		ICONCOLOR="white"

	elif theme=="Dark":
		DEEPDARK="#232323"
		BACKGROUND="#2A2A2A"
		SOFTDARK="#353535"
		DIM="#5c5c5c"
		PRESSED = "#7AB6F3"
		FOCUSED="#2A82DA"
		TEXT="#FFFFFF"
		ICONCOLOR="white"
	
	elif theme=="Light":
		DEEPDARK="#8972CC"
		BACKGROUND="#A796DB"
		SOFTDARK="#B9B5FF"
		DIM="#D8C2FF"
		PRESSED = "#ECCAFF"
		FOCUSED="#E2C6FF"
		TEXT="#2D2730"
		ICONCOLOR="black"
	
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
		font-size: 18pt;
		selection-background-color: {FOCUSED};
		selection-color: {TEXT};
	}}
	QWidget::item:active, QWidget::item:!active
	{{
		color: {TEXT};
	}}
	
	QWidget:disabled
	{{
		color: {DIM};
	}}

	QDialog {{
		border: 2px solid {DEEPDARK};
		border-radius: 1px;
	}}

	#DTMainWindow #statusBar{{
		background-color: {SOFTDARK};
		font-family: "Hack";
		font-size: 9pt;
	}}
	/* TitleBar */

	DTLogin QLineEdit {{
		font-size: 12pt;
	}}
	
	#TitleBarFrame #label_titlebar {{
		font-family: "Segoe UI";
		font-size: 20pt;
	}}
	#TitleBarFrame QPushButton {{
		border: none;
		background-color: transparent;
		max-height: 24px;
		min-height: 24px;
		min-width: 24px;
		max-width: 24px;
	}}

	#TitleBarFrame QPushButton:hover{{
		background-color: {SOFTDARK};
		border-style: solid;
		border-radius: 4px;
	}}
	#TitleBarFrame QPushButton:pressed {{
		background-color: {DIM};
		border-style: solid;
		border-radius: 4px;
	}}

	#TitleBarFrame #title_icon{{
		icon-size: 36px;
		max-height: 36px;
		min-height: 36px;
		min-width: 36px;
		max-width: 36px;
	}}
	#TitleBarFrame #title_icon:hover{{
		background-color: transparent;
	}}
	#TitleBarFrame #title_icon:pressed {{
		background-color: transparent;
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

	QSplitter{{
		background: transparent;
	}}
	
	QScrollBar::add-line {{
	height: 0px;
	}}
	QScrollBar::sub-line {{
	height: 0px;
	}}
	QScrollBar::add-page, QScrollBar::sub-page {{
	height: 0px;
	}}

	QSplitter::handle{{
		border: 1px solid transparent;
		border-radius: 7px;
	}}
	QSplitter::handle:horizontal{{
		width: 12px;
		image: url(:/icon/{ICONCOLOR}/{ICONCOLOR}_more-vertical.svg);
	}}
	QSplitter::handle:vertical{{
		height: 12px;
		image: url(:/icon/{ICONCOLOR}/{ICONCOLOR}_more-horizontal.svg);
	}}
	QSplitter::handle:hover{{
		background: {SOFTDARK};
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
		border: 1px solid {DEEPDARK};
	}}

	QMenuBar::item:pressed{{
		background: {PRESSED};
		border: 1px solid {DEEPDARK};
		padding-top: 4px;
	}}

	QMenu {{
		font-family: "Hack";
		font-size: 12pt;
		background-color: {BACKGROUND};
		border: 1px solid {DEEPDARK};
		margin: 1px;
		padding: 1px;
	}}

	QMenu::item{{
		padding: 2px 25px 2px 15px;
		border: 1px solid transparent;
		margin: 1px;
	}}
	QMenu::item:disabled{{
		color: {DIM};
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
		height: 2px;
		background: {DEEPDARK};
	}}

	QMenu::indicator {{/*checked 的√*/
		width: 13px;
		height: 13px;
		padding:2px;
	}}
	QMenu::icon:checked {{ /* appearance of a 'checked' icon */
		background: {FOCUSED};
		border: 1px inset {DEEPDARK};
		border-radius: 3px;
		padding: 2px;
	}}


	/* ToolBar */

	QToolBar {{
		background: {BACKGROUND};
		spacing: 1px;
		padding: 1px;
		border-bottom: 1px solid {DEEPDARK};
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
		border: 1px solid {DEEPDARK};
		border-radius: 6px;
		height: 36px;
	}}


	QLineEdit:focus{{
		border-color: {FOCUSED};
	}}

	QLineEdit:read-only {{
		color: {DIM};
	}}

	QTextEdit, QPlainTextEdit{{
		background-color: {SOFTDARK};
		border: 1px solid {DEEPDARK};
	}}
	QTextEdit:focus, QPlainTextEdit:focus{{
		border-color: {FOCUSED};
	}}

	QTextBrowser:focus{{
		border-color: {DEEPDARK};
	}}

	/* Button */


	QPushButton {{
		border: 1px solid {DEEPDARK};
		border-radius: 3px;
		background-color: {SOFTDARK};
		font-family: "Hack";
		font-size: 12pt;
		min-height: 27px;
	}}

	QPushButton:hover{{
		background-color: {FOCUSED};
		border-color: {DEEPDARK};
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
		min-width: 72px;
	}}
	
	QToolButton {{
		font-family: "Hack";
		font-size: 12pt;
		height: 27px;
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
		border-color: {DEEPDARK};
	}}
	QToolButton:hover{{
		background-color: {FOCUSED};
		border-color: {DEEPDARK};
	}}

	QToolButton:pressed,QToolButton:checked:hover{{
		background-color: {PRESSED};
		border-color: {DEEPDARK};
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
		border-color: {DEEPDARK};
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
		font-size: 12pt;
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
		font-size: 12pt;
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
		border-radius: 6px;
		height: 36px;
	}}
	QComboBox:focus{{
		border-color: {DEEPDARK};
	}}
	QComboBox QAbstractItemView{{
		background-color: {DEEPDARK};
	}}
	QComboBox::drop-down{{
		background-color: {SOFTDARK};
		border: 1px solid {DEEPDARK};
		border-top-right-radius: 6px;
		border-bottom-right-radius: 6px;
		subcontrol-origin: padding;
		subcontrol-position: top right;
		width: 18px;
		margin: 1px;
	}}
	QComboBox::drop-down:pressed{{
		background-color: {FOCUSED};
	}}
	QComboBox::down-arrow{{
		image: url(:/icon/{ICONCOLOR}/{ICONCOLOR}_chevron-down.svg);
	}}
	

	/* SpinBox DateTime */

	QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit{{
		font-family: "Hack";
		background-color: {SOFTDARK};
		border-radius: 6px;
		height: 36px;
	}}
	QSpinBox:focus, QDoubleSpinBox:focus, QDateEdit:focus, QTimeEdit:focus, QDateTimeEdit:focus{{
		border: 1px solid {FOCUSED};
	}}

	QSpinBox::up-button, QDoubleSpinBox::up-button, QDateEdit::up-button, QTimeEdit::up-button, QDateTimeEdit::up-button{{
		background-color: {SOFTDARK};
		subcontrol-origin: border;
		subcontrol-position: top right;
		width: 18px;
		border: 1px solid {DEEPDARK};
		border-top-right-radius: 6px;
		margin-top: 1px;
		margin-right: 1px;
	}}
	QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed, QDateEdit::up-button:pressed, QTimeEdit::up-button:pressed, QDateTimeEdit::up-button:pressed {{
		background-color: {FOCUSED};
	}}
	QSpinBox::up-arrow, QDoubleSpinBox::up-arrow, QDateEdit::up-arrow, QTimeEdit::up-arrow, QDateTimeEdit::up-arrow{{
		image: url(:/icon/{ICONCOLOR}/{ICONCOLOR}_chevron-up.svg);
	}}

	QSpinBox::down-button, QDoubleSpinBox::down-button, QDateEdit::down-button, QTimeEdit::down-button, QDateTimeEdit::down-button{{
		background-color: {SOFTDARK};
		subcontrol-origin: border;
		subcontrol-position: bottom right;
		width: 18px;
		border: 1px solid {DEEPDARK};
		border-bottom-right-radius: 6px;
		margin-bottom: 1px;
		margin-right: 1px;
	}}
	QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed, QDateEdit::down-button:pressed, QTimeEdit::down-button:pressed, QDateTimeEdit::down-button:pressed {{
		background-color: {FOCUSED};
	}}
	QSpinBox::down-arrow, QDoubleSpinBox::down-arrow, QDateEdit::down-arrow, QTimeEdit::down-arrow, QDateTimeEdit::down-arrow{{
		image: url(:/icon/{ICONCOLOR}/{ICONCOLOR}_chevron-down.svg);
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
		width: 16px;
		height: 16px;
		background-color: {SOFTDARK};
		border: 1px solid transparent;
		border-radius: 7px;
		padding: 1px;
	}}
	QScrollBar::handle{{
		border-radius: 5px;
		background: {FOCUSED};
	}}
	QScrollBar::handle:hover {{
		background: {PRESSED};
	}}
	QScrollBar::add-line, QScrollBar::sub-line,
	QScrollBar::add-page, QScrollBar::sub-page {{
		background: transparent;
	}}
	QScrollArea{{
		border: none;
	}}
	QAbstractScrollArea::corner {{
		background: transparent;
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
		margin-top:1em;
	}}
	QGroupBox::title {{
		subcontrol-origin: margin;
		subcontrol-position: top left;
	}}

	/* ToolBox */

	QToolBox{{
		border: 1px solid {DEEPDARK};
	}}
	QToolBox::tab {{
		font-family: "Hack";
		font-size: 12pt;
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
		border-color: {DEEPDARK};
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
		font-family: "Hack";
		font-size: 12pt;
		background: {SOFTDARK};
		border: 1px solid {DEEPDARK};
	}}
	QTabBar::tab:hover {{
		background: {FOCUSED};
		border-color: transparent;
	}}
	QTabBar::tab:selected {{
		background: {FOCUSED};
		border-color: {DEEPDARK};
	}}
	QTabBar::tab:pressed {{
		background: {PRESSED};
		border-color: transparent;
	}}
	QTabBar::tab:focus {{
		border-color: {DEEPDARK};
	}}
	QTabBar::tab:top{{
		border-bottom: transparent;
	}}
	QTabBar::tab:bottom{{
		border-top: transparent;
	}}
	QTabBar::tab:left{{
		border-right: transparent;
	}}
	QTabBar::tab:right{{
		border-left: transparent;
	}}


	/* QHeaderView for list table */

	QAbstractItemView, QAbstractItemView QLineEdit {{
		font-family: "Hack";
		font-size: 12pt;
		background-color: {SOFTDARK};
	}}
	
	QHeaderView {{
		border: none;

	}}
	QHeaderView::section, QTableCornerButton::section {{
		/*设置表头属性*/ /*表格左上角小框框*/
		background-color: {DIM};
		padding-top: 5px;
		border-right: 1px solid {DEEPDARK};
		border-bottom: 1px solid {DEEPDARK};
		border-radius: 0px;
	}}
	QHeaderView::section:hover, QTableCornerButton::section:hover{{
		background-color: {DIM};
	}}
	QHeaderView::section:pressed{{
		background-color: {DIM};
	}}
	QHeaderView::section:checked {{
		background-color: {DIM};
	}}


	/* QTableWidget */

	QTableWidget, QTableView
	{{
		gridline-color: {DEEPDARK}; /*表格中的网格线条颜色*/
		alternate-background-color: {FOCUSED};
		border:1px solid {DEEPDARK}; /*边框线的宽度、颜色*/
	}}
	QListView::item, QTreeView::item, QTableView::item{{
		background: {DIM};
		outline-style: none;
		border-left: 2px solid {PRESSED};
	}}

	QTableView::item:selected:active {{
		background: {FOCUSED};
	}}

	QTableWidget QComboBox{{
		margin: 2px;
		border: none;
	}}

	QListView{{
		font-family: {font_family};
		border:1px solid {DEEPDARK};
	}}
	QTreeView, QTableView {{
		border:1px solid {DEEPDARK};
	}}
	QListView::item:hover, QTreeView::item:hover, QTableView::item:hover {{
		background: {FOCUSED};
	}}
	QListView::item:selected , QTreeView::item:selected, QTableView::item:selected {{
		background: {FOCUSED};
		color: {TEXT};
	}}
	QTreeView::branch{{
		
	}}
	QTreeView::branch:selected{{
		
	}}


	QFontDialog {{
		min-width: 900px;
		min-height: 700px;
	}}
	QFontDialog * {{
		font-size: 17px;
	}}
	
	/* QCalendar */

	/* header row */
	QCalendarWidget QWidget {{
		font-family: "Hack";
		font-size: 12pt;
		alternate-background-color: {SOFTDARK};
	}}
	
	/* normal days */
	QCalendarWidget QAbstractItemView:enabled
	{{
		background-color: {BACKGROUND};
	}}
	
	"""

	return stylesheet

# QStatusBar{{
# 	background: transparent;
# 	border-top:1px solid {DEEPDARK};
# }}

# QStatusBar::item {{
# 	margin: 2px 0;
# 	border-left: 1px solid {DEEPDARK};
# }}

# QStatusBar QLabel{{
# 	background: transparent;
# 	margin: 0  2px;
# }}

# QStatusBar QPushButton{{
# 	background: transparent;
# 	margin: 0  2px;
# }}

# QStatusBar QPushButton:hover{{
# 	background: {FOCUSED};
# 	margin: 0  2px;
# }}