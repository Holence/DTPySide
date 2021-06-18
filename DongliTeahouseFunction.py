from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys,os
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