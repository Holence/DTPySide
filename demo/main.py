from DTPySide import DTAPP
from DTPySide.demo.demoSession import DemoMainSession
from DTPySide import DTIcon

def run():

	app=DTAPP([])
	
	app.setAuthor("Holence")
	app.setApplicationName("Dongli Teahouse PySide Demo")
	app.setApplicationVersion("1.0.0.0")
	app.setWindowIcon(DTIcon.Holo2())
	
	app.setWindowStyle((2,0))
	# app.setWindowStyle((2,1))

	mainsession=DemoMainSession(app)
	app.setMainSession(mainsession)
	
	# app.debugRun("123",True)
	app.run()
	

if __name__=="__main__":
	run()