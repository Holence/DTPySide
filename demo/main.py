from DongliTeahousePySideWheel.demo.MyComponent import *

def run():

	app=QApplication(sys.argv)

	app.setStyle("Fusion")
	app.setPalette(DongliTeahousePalette.MyDarkPalette())
	app.setQuitOnLastWindowClosed(False)

	window=MainWindow()
	window.quitApp.connect(app.quit)

	sys.exit(app.exec_())