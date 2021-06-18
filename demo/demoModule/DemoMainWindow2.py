from DongliTeahousePySideWheel.demo.demoModule.DemoCentralWidget2 import DemoCentralWidget2

from DongliTeahousePySideWheel.DongliTeahouseFrame import DongliTeahouseMainWindow
class DemoMainWindow2(DongliTeahouseMainWindow):
    def __init__(self,Headquarter):
        super().__init__(Headquarter.app)
        self.CentralWidget=DemoCentralWidget2(Headquarter)
        self.setCentralWidget(self.CentralWidget)