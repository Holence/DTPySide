from DTPySide import *

from DTPySide.demo.demoModule.Ui_DemoCentralWidget2 import Ui_DemoCentralWidget2
class DemoCentralWidget2(Ui_DemoCentralWidget2,QWidget):
    def __init__(self,Headquarter):
        super().__init__(Headquarter)
        self.setupUi(self)
        
        self.homelabel.setText("Your password is "+Headquarter.password())