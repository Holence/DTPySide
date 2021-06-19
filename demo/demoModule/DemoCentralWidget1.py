from DTPySide.DTFunction import *
from DTPySide.DTFrame import DTMessageBox
from DTPySide import DTIcon


from DTPySide.demo.demoModule.Ui_DemoCentralWidget1 import Ui_DemoCentralWidget1
class DemoCentralWidget1(Ui_DemoCentralWidget1,QWidget):
    def __init__(self,Headquarter):
        super().__init__(Headquarter)
        self.setupUi(self)
        
        self.homelabel.setText(Headquarter.UserSetting().value("HomePage/HomeLabel"))

        self.actionHello_World.triggered.connect(lambda:DTMessageBox(Headquarter,"Hello World","Hello! Welcome to Dongli Teahouse PySide.",DTIcon.Heart()))