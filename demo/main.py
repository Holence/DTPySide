from DTPySide import *

from DTPySide.demo.demoSession import DemoMainSession

def run():

	app=DTAPP(sys.argv)
	
	app.setAuthor("Holence")
	app.setApplicationName("Dongli Teahouse PySide Demo")
	app.setLoginEnable(True)
	app.loadTranslation()
	mainsession=DemoMainSession(app)
	app.setMainSession(mainsession)
	# app.debugRun("123",True)
	app.run()

if __name__=="__main__":
	run()