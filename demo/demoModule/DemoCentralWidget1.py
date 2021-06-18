from DongliTeahousePySideWheel.DongliTeahouseFunction import *
from DongliTeahousePySideWheel.DongliTeahouseFrame import DongliTeahouseMessageBox
from DongliTeahousePySideWheel import DongliTeahouseIcon


from DongliTeahousePySideWheel.demo.demoModule.Ui_DemoCentralWidget1 import Ui_DemoCentralWidget1
class DemoCentralWidget1(Ui_DemoCentralWidget1,QWidget):
    def __init__(self,Headquarter):
        super().__init__(Headquarter)
        self.setupUi(self)
        self.homelabel.setText(Headquarter.UserSetting().value("HomePage/HomeLabel"))

        self.actionHello_World.triggered.connect(lambda:DongliTeahouseMessageBox(self,"Hello World","Hello! Welcome to DongliTeahouse.",DongliTeahouseIcon.Heart()))