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
			return True,str(title)
		except:
			try:
				#YouTube的channel页面的标题竟然在body里面……
				title=html.xpath("/html/body/title/text()")
				title=urllib.parse.unquote(title[0],'utf-8')
				return True,str(title)
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
			if "http" not in icon_url:
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