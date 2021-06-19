from DTPySide import DTAPP
from DTPySide.demo.demoSession import DemoMainSession
from DTPySide.DTPalette import DTBrightPalette
from DTPySide import DTIcon

def run():

	app=DTAPP([])
	app.setAuthor("Holence")
	app.setApplicationName("Dongli Teahouse PySide Demo")
	app.setApplicationVersion("1.0.0.0")
	app.setWindowIcon(DTIcon.Holo1())
	
	# app.setLoginEnable(False)
	# app.setPalette(DTBrightPalette())

	mainsession=DemoMainSession(app)
	app.setMainSession(mainsession)

	# app.debugRun("123",True)
	app.run()

if __name__=="__main__":
	run()