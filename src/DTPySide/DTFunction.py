from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys, os, shutil, subprocess
import re
import copy
import time
import pickle
import json
import pypinyin
from send2trash import send2trash
from functools import partial
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import colour
import bz2, blosc
import typing

if sys.platform == "win32":
    from win32.lib import win32con
    from win32 import win32gui, win32api
    from win32com.shell import shell,shellcon
    PATH_PREFIX_LEN=8
if sys.platform=="linux":
    PATH_PREFIX_LEN=7

def ShowUp(window:QWidget):
    if window.isFullScreen():
        window.showFullScreen()
        if sys.platform == "win32":
            window.TitleBar.hide()
    else:
        window.showNormal()
        if sys.platform == "win32":
            window.TitleBar.show()
    
    if sys.platform == "win32":
        window.activateWindow()

def MoveToCenterOfScreen(widget:QWidget):
    """在initializeWindow中，setCentralWidget之后调用
    """
    scale=float(os.environ["QT_SCALE_FACTOR"])
    if sys.platform == "win32":
        widget.move(
            int((win32api.GetSystemMetrics(0)-widget.width()*scale)/scale)//2 ,
            int((win32api.GetSystemMetrics(1)-widget.height()*scale)/scale)//2
        )
    elif sys.platform == "linux":
        output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
        output = output.decode()
        w, h = map(int, output[:-1].split("x"))
        widget.move(
            int((w-widget.width()*scale)/scale)//2 ,
            int((h-widget.height()*scale)/scale)//2
        )

def IconFromCurrentTheme(name):
    return QIcon(":/icons/%s/%s"%(QIcon.themeName(),name))

def Clear_Layout(layout):
    for i in reversed(range(layout.count())):
        item=layout.itemAt(i)
        
        if item.spacerItem():
            layout.removeItem(item)
            del item
        else:
            item.widget().deleteLater()

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

##################################

def Fernet_Encrypt(password: str, data, iteration=100000):
    try:
        if type(data)!=bytes:
            data=pickle.dumps(data)
        
        salt=password.encode()[::-1]
        password=password.encode()
        kdf=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=iteration,backend=default_backend())
        key=base64.urlsafe_b64encode(kdf.derive(password))

        fer=Fernet(key)
        encrypt_data=fer.encrypt(data)
        
        return encrypt_data
    except:
        return False

def Fernet_Decrypt(password: str, data: bytes, iteration=100000):
    try:
        salt=password.encode()[::-1]
        password=password.encode()
        kdf=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=iteration,backend=default_backend())
        key=base64.urlsafe_b64encode(kdf.derive(password))
        
        fer=Fernet(key)
        decrypt_data=fer.decrypt(data)
        
        try:
            decrypt_data=pickle.loads(decrypt_data)
        except:
            pass

        return decrypt_data
    except:
        return False

def AES_Encrypt(password: str, data, iteration=48000):
    try:
        if type(data)!=bytes:
            data=pickle.dumps(data)
        
        # generate password
        salt = os.urandom(16)
        iv = os.urandom(16)
        kdf = PBKDF2HMAC(hashes.SHA512(), 32, salt, iteration, backend=default_backend())
        password = kdf.derive(password.encode())

        # pad data
        padder = PKCS7(128).padder()
        data = padder.update(data) + padder.finalize()

        # encrypt
        cipher = Cipher(algorithms.AES(password), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypt_data = encryptor.update(data) + encryptor.finalize()

        encrypt_data = base64.b64encode(salt + encrypt_data + iv)

        return encrypt_data
    except:
        return False

def AES_Decrypt(password: str, data, iteration=48000):
    try:
        # re-generate password from
        encrypted_obj = base64.b64decode(data)
        salt = encrypted_obj[0:16]
        iv = encrypted_obj[-16:]
        cypher_text = encrypted_obj[16:-16]
        kdf = PBKDF2HMAC(hashes.SHA512(), 32, salt, iteration, backend=default_backend())
        password = kdf.derive(password.encode())

        # decrypt
        cipher = Cipher(algorithms.AES(password), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_text = decryptor.update(cypher_text) + decryptor.finalize()

        # remove padding
        unpadder = PKCS7(128).unpadder()
        decrypt_data = unpadder.update(padded_text) + unpadder.finalize()
        
        try:
            decrypt_data=pickle.loads(decrypt_data)
        except:
            pass

        return decrypt_data
    except:
        return False

def Symmetric_Encrypt(password: str, data, mode=None, iteration=48000):
    if mode==None:
        return AES_Encrypt(password, data, iteration)
    else:
        if mode=="Fernet":
            return Fernet_Encrypt(password, data, iteration)
        if mode=="AES":
            return AES_Encrypt(password, data, iteration)

def Symmetric_Decrypt(password: str, data, mode=None, iteration=48000):
    if mode==None:
        res = AES_Decrypt(password, data, iteration)
        if res is False:
            return Fernet_Decrypt(password, data, iteration)
        else:
            return res
    else:
        if mode=="Fernet":
            return Fernet_Decrypt(password, data, iteration)
        if mode=="AES":
            return AES_Decrypt(password, data, iteration)

def Symmetric_Encrypt_Save(password: str, data, file_path, mode=None, iteration=48000):
    try:
        if mode==None:
            enc_data=AES_Encrypt(password, data, iteration)
        else:
            if mode=="Fernet":
                enc_data=Fernet_Encrypt(password, data, iteration)
            if mode=="AES":
                enc_data=AES_Encrypt(password, data, iteration)
        
        if not os.path.exists(os.path.dirname(os.path.abspath(file_path))):
            os.makedirs(os.path.dirname(file_path))
        
        with open(file_path,"wb") as f:
            f.write(blosc.compress(enc_data, cname="zlib"))
        
        return True
    except Exception as e:
        return False

def Symmetric_Decrypt_Load(password: str, file_path, mode=None, iteration=48000):
    try:
        try:
            with open(file_path,"rb") as f:
                data=blosc.decompress(f.read())
        except:
            # 兼容旧版
            try:
                with bz2.open(file_path,"rb") as f:
                    data=f.read()
            except:
                with open(file_path,"rb") as f:
                    data=f.read()
        
        if mode==None:
            decrypt_data = AES_Decrypt(password, data, iteration)
            if decrypt_data is False:
                decrypt_data = Fernet_Decrypt(password, data, iteration)
        else:
            if mode=="Fernet":
                decrypt_data = Fernet_Decrypt(password, data, iteration)
            if mode=="AES":
                decrypt_data = AES_Decrypt(password, data, iteration)

        return decrypt_data
    except:
        return False
    

def Json_Save(data, file_path):
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

def Base64_Encode(thing, width=40, encoding_for_str="utf-8") -> str:
    if type(thing)==bytes:
        res=base64.b64encode(thing).decode("ascii")
    elif type(thing)==str:
        res=base64.b64encode(bytes(thing, encoding_for_str)).decode("ascii")
    else:
        res=base64.b64encode(pickle.dumps(thing)).decode("ascii")

    if type(width)==int:
        return "\n".join([ res[i:i+width] for i in range(0, len(res), width)])
    else:
        return res

def Base64_Decode(base64_s: str, TYPE: typing.Union[str,bytes,object], encoding_for_str="utf-8") -> str:
    res=base64.b64decode(base64_s.strip().replace("\n","").encode("ascii"))
    if TYPE==bytes:
        return res
    elif TYPE==str:
        return res.decode(encoding_for_str)
    elif TYPE==object:
        return pickle.loads(res)
    else:
        return res

def Base64_Encode_Save(thing, file_path, width=40, encoding_for_str="utf-8"):
    with open(file_path, "w") as f:
        f.write(Base64_Encode(thing, width, encoding_for_str))

def Base64_Decode_Load(file_path, TYPE: typing.Union[str,bytes,object], encoding_for_str="utf-8"):
    with open(file_path, "r") as f:
        res=Base64_Decode(f.read(), TYPE, encoding_for_str)
    return res

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

##################################

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

##################################

def Delete_to_Recyclebin(dir):
    "删除成功返回True"
    if sys.platform=="win32":
        dir=dir.replace("/","\\")
    try:
        send2trash(dir)
        return True
    except:
        return False

def Shell_Copy_File(src, dest):
    """
    无法返回覆盖还是跳过，请提前自行判断是否会有冲突！
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
    if sys.platform == "win32":
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
    elif sys.platform == "linux":
        if not os.path.exists(os.path.join(dest, os.path.basename(src))):
            src=src.replace("'","'\\''")
            dest=dest.replace("'","'\\''")
            os.system(f"cp -r '{src}' '{dest}'")
        else:
            src=src.replace("'","'\\''")
            dest=dest.replace("'","'\\''")
            cmd=f" cp -i -r '{src}' '{dest}' -v"
            os.system("gnome-terminal -- %s"%cmd)

def Shell_Move_File(src, dest):
    """
    无法返回覆盖还是跳过，请提前自行判断是否会有冲突！
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
    if sys.platform == "win32":
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
    elif sys.platform == "linux":
        if not os.path.exists(os.path.join(dest, os.path.basename(src))):
            src=src.replace("'","'\\''")
            dest=dest.replace("'","'\\''")
            os.system(f"mv '{src}' '{dest}'")
        else:
            src=src.replace("'","'\\''")
            dest=dest.replace("'","'\\''")
            cmd=f" mv -i '{src}' '{dest}' -v"
            os.system("gnome-terminal -- %s"%cmd)

def Open_Explorer(url, select: bool):
    if sys.platform=="win32":
        if select:
            os.popen("explorer /select,\"%s\""%url.replace("/","\\"))
        else:
            os.startfile(url)
    elif sys.platform=="linux":
        if select:
            os.popen("nautilus -s \"%s\""%url)
        else:
            os.popen("xdg-open \"%s\""%url)

def Open_Website(url):
    if sys.platform=="win32":
        os.system("start explorer \"https://www.google.com/search?q=%s\""%url)
    elif sys.platform=="linux":
        os.system("xdg-open \"https://www.google.com/search?q=%s\""%url)
