import os
import shutil


def deepin(base):
	
	base=os.path.abspath(base)
	os.chdir(base)

	for i in os.listdir("./"):
		if os.path.isdir(i):
			deepin(i)
			os.chdir(base)
		else:
			ext=os.path.splitext(i)[1]
			if ext==".ui":
				ui_list.append(" "+os.path.abspath(i))

ui_list=[]
base=os.getcwd()
deepin(base)
os.system("lupdate %s -ts translation.ts"%("".join(ui_list)))