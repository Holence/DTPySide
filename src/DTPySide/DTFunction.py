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
from win32.lib import win32con
from win32 import win32gui, win32api
from win32com.shell import shell,shellcon
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import colour

def IconFromCurrentTheme(name):
	return QIcon(":/icons/%s/%s"%(QIcon.themeName(),name))

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

def QDate_to_Tuple(date:QDate):
	return (date.year(),date.month(),date.day())

def WhatDayIsToday(mode):
	"""返回年月日

	Args:
		mode (int, optional):选择返回的类型。

		0：Tuple

		1: QDate
	"""
	today=time.localtime()
	if mode==0:
		return today.tm_year,today.tm_mon,today.tm_mday
	elif mode==1:
		return QDate(today.tm_year,today.tm_mon,today.tm_mday)

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

		if not os.path.exists(os.path.dirname(file_path)):
			os.makedirs(os.path.dirname(file_path))
		
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
	try:
		with open(file_path,"w",encoding="utf-8") as f:
			json.dump(data,f,ensure_ascii=False,indent=4)
		
		return True
	except:
		return False

def Json_Load(file_path):
	try:
		with open(file_path,"r",encoding="utf-8") as f:
			data=json.load(f)
		return data
	except:
		return False

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

def GetWebPageResponse(url,cookie="") -> requests.Response:
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		return response
	else:
		return None

def GetWebPageHTML(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		return response.text
	else:
		return None

def GetWebPageHeaders(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		return response.headers
	else:
		return None

def GetWebPageType(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		return response["Content-Type"]
	else:
		return None

def GetWebPageTitle(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		html=response.text
		try:
			tree=etree.HTML(html)
			title=tree.xpath(".//title/text()")[0]
			title=urllib.parse.unquote(title,'utf-8')
			return str(title)
		except:
			return None
	else:
		return None


def GetWebFavIcon(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	if response.ok:
		try:
			html=response.text
			tree=etree.HTML(html)
			icon_url=tree.xpath("//*[@rel='icon']/@href | //*[@rel='shortcut icon']/@href")[-1]
			if "http" not in icon_url:
				icon_url=urllib.parse.urljoin(url,icon_url)
			res=GetWebPageResponse(icon_url)
			if res!=None:
				return res.content
			else:
				return None
		except:
			return None
	else:
		return None

def GetWebPagePic(url,cookie=""):
	head={}
	head["cookie"]=cookie
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.143 (beta) Yowser/2.5 Safari/537.36'
	try:
		response=requests.get(url,headers=head,timeout=3)
	except:
		return None
	
	if response.ok:
		return response.content
	else:
		return None

def Delete_to_Recyclebin(dir):
	"删除成功返回True"
	result = shell.SHFileOperation((0,shellcon.FO_DELETE,dir,None, shellcon.FOF_SILENT | shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION,None,None))  #删除文件到回收站
	return result[0]==0

def Win32_Shellcopy(src, dest):
	"""
	Copy files and directories using Windows shell.

	:param src: Path or a list of paths to copy. Filename portion of a path
				(but not directory portion) can contain wildcards ``*`` and
				``?``.
	:param dst: destination directory.
	:returns: ``True`` if the operation completed successfully,
			  ``False`` if it was aborted by user (completed partially).
	:raises: ``WindowsError`` if anything went wrong. Typically, when source
			 file was not found.

	.. seealso:
		`SHFileperation on MSDN <http://msdn.microsoft.com/en-us/library/windows/desktop/bb762164(v=vs.85).aspx>`
	"""
	if isinstance(src, str):
		src = os.path.abspath(src)
	else:  # iterable
		src = '\0'.join(os.path.abspath(path) for path in src)

	result, aborted = shell.SHFileOperation((
		0,
		shellcon.FO_COPY,
		src,
		os.path.abspath(dest),
		shellcon.FOF_NOCONFIRMMKDIR,  # flags
		None,
		None))

	if not aborted and result != 0:
		# Note: raising a WindowsError with correct error code is quite
		# difficult due to SHFileOperation historical idiosyncrasies.
		# Therefore we simply pass a message.
		raise WindowsError('SHFileOperation failed: 0x%08x' % result)

	return not aborted

def Win32_Shellmove(src, dest):
	"""
	Move files and directories using Windows shell.

	:param src: Path or a list of paths to move. Filename portion of a path
				(but not directory portion) can contain wildcards ``*`` and
				``?``.
	:param dst: destination directory.
	:returns: ``True`` if the operation completed successfully,
			  ``False`` if it was aborted by user (completed partially).
	:raises: ``WindowsError`` if anything went wrong. Typically, when source
			 file was not found.

	.. seealso:
		`SHFileperation on MSDN <http://msdn.microsoft.com/en-us/library/windows/desktop/bb762164(v=vs.85).aspx>`
	"""
	if isinstance(src, str):
		src = os.path.abspath(src)
	else:  # iterable
		src = '\0'.join(os.path.abspath(path) for path in src)

	result, aborted = shell.SHFileOperation((
		0,
		shellcon.FO_MOVE,
		src,
		os.path.abspath(dest),
		shellcon.FOF_NOCONFIRMMKDIR,  # flags
		None,
		None))

	if not aborted and result != 0:
		# Note: raising a WindowsError with correct error code is quite
		# difficult due to SHFileOperation historical idiosyncrasies.
		# Therefore we simply pass a message.
		raise WindowsError('SHFileOperation failed: 0x%08x' % result)

	return not aborted
