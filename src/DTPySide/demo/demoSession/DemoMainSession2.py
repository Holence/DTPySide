from DTPySide import *

from DTPySide.demo.demoModule import DemoCentralWidget2
class DemoMainSession2(DTFrame.DTMainWindow):
    def __init__(self,Headquarter):
        super().__init__(Headquarter.app)
        self.CentralWidget=DemoCentralWidget2(Headquarter)
        self.setCentralWidget(self.CentralWidget)
        self.setGeometry(Headquarter.x()+50,Headquarter.y()+50,Headquarter.width()-100,Headquarter.height()-100)
        self.setWindowTitle("Demo Window 2")