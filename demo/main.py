from DongliTeahousePySideWheel import DongliTeahouseAPP
from DongliTeahousePySideWheel.demo.demoSession import DemoMainSession

def run():

	app=DongliTeahouseAPP([])
	app.setAuthor("Holence")
	app.setApplicationName("Demo")
	
	# app.setLoginEnable(False)

	mainsession=DemoMainSession(app)
	app.setMainSession(mainsession)

	# app.debugRun("123",True)
	app.run()

if __name__=="__main__":
	run()