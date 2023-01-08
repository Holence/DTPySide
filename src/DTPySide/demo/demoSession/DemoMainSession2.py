from DTPySide import *

from DTPySide.demo.demoModule import DemoCentralWidget2
class DemoMainSession2(DTFrame.DTMainWindow):
    
    def __init__(self,Headquarter):
        super().__init__(Headquarter.app)
        self.CentralWidget=DemoCentralWidget2(Headquarter)
        self.setCentralWidget(self.CentralWidget)
        MoveToCenterOfScreen(self)
        self.setWindowTitle("Demo Window 2")
