from DTPySide import *

from DTPySide.demo.demoModule.Ui_DemoCentralWidget1 import Ui_DemoCentralWidget1
class DemoCentralWidget1(Ui_DemoCentralWidget1,QWidget):
    def __init__(self,Headquarter):
        super().__init__(Headquarter)
        self.setupUi(self)
        
        try:
            self.homelabel.setText("HomeLabel's Text is: "+Headquarter.UserSetting().value("HomePage/HomeLabel"))
        except:
            pass
        
        # implement custom stylesheet
        self.homelabel.setStyleSheet('background:red')
        self.actionHello_World.triggered.connect(lambda:DTFrame.DTMessageBox(Headquarter,"Hello World","Hello! Welcome to Dongli Teahouse PySide.",DTIcon.Holo01()))