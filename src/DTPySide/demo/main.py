from DTPySide import *

from DTPySide.demo.demoSession import DemoMainSession

def run():

	app=DTAPP(sys.argv)
	
	app.setAuthor("Holence")
	app.setApplicationName("DTPySide Demo")
	app.setLoginEnable(True)
	app.loadTranslation()
	app.setQuitOnClickX(True)
	mainsession=DemoMainSession(app)
	app.setMainSession(mainsession)
	# app.debugRun("123",True)
	app.run()

if __name__=="__main__":
	run()