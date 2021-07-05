from DTPySide import DTAPP
from DTPySide.demo.demoSession import DemoMainSession
from DTPySide.DTPalette import DTDraculaPalette

from DTPySide.DTStyle import DTDraculaStyle
from DTPySide import DTIcon

def run():

	app=DTAPP([])
	app.setAuthor("Holence")
	app.setApplicationName("Dongli Teahouse PySide Demo")
	app.setApplicationVersion("1.0.0.0")
	app.setWindowIcon(DTIcon.Holo1())
	
	# app.setLoginEnable(False)
	
	mainsession=DemoMainSession(app)
	app.setMainSession(mainsession)
	
	app.setStyle("Fusion")
	app.setStyleSheet(DTDraculaStyle)
	app.setPalette(DTDraculaPalette())
	app.setWindowEffect("Aero")

	app.debugRun("123",True)
	# app.run()

if __name__=="__main__":
	run()