import os

base=os.getcwd()

uiPath=base

os.chdir(uiPath)
for i in os.listdir("./"):
	name=os.path.splitext(i)[0]
	ext=os.path.splitext(i)[1]
	if ext==".ui":
		os.system("pyside2-uic %s.ui -o %s.py"%(name,name))
		with open("%s.py"%name,"r+",encoding="utf-8") as f:
			s=f.read()
			s=s.replace("import DongliTeahouse_rc","import DongliTeahousePySideWheel.DongliTeahouse_rc")
			s=s.replace("from DongliTeahouse","from DongliTeahousePySideWheel.DongliTeahouse")
			f.seek(0)
			f.write(s)