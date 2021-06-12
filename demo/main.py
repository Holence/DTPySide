from DongliTeahousePySideWheel.demo.MyComponent import *

def run():

	app=DongliTeahouseAPP([])
	app.setAuthor("Holence")
	app.setApplicationName("Demo")
	# app.setLoginEnable(False)

	window=MainWindow(app)
	app.setMainWindow(window)

	app.run()

if __name__=="__main__":
	run()