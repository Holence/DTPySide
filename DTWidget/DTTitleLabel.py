from DTPySide.DTFunction import *

class DTTitleLabel(QLabel):
	def  __init__(self,parent):
		super().__init__(parent)
		self.__press_pos = QPoint()
		
		#原理不明，重定义事件函数吗？
		self.mouseDoubleClickEvent = self.dobleClickMaximizeRestore

	def setHeadquarter(self,Headquarter):
		"拖动与双击要去改变主窗体的状态，而在MyTitleBar的setupUI给进来的parent是MyTitleBar，不是主窗体，所以要手动设置Headquarter"
		self.Headquarter=Headquarter
	
	def mousePressEvent(self, event):
		super(DTTitleLabel, self).mousePressEvent( event )
		if event.button() == Qt.LeftButton:
			self.__press_pos = event.pos()

	def mouseReleaseEvent(self, event):
		super(DTTitleLabel, self).mouseReleaseEvent( event )
		if event.button() == Qt.LeftButton:
			self.__press_pos = QPoint()

	def mouseMoveEvent(self, event):
		super(DTTitleLabel, self).mouseMoveEvent( event )
		if not self.__press_pos.isNull():
			#全屏还移动就会出问题
			if not self.Headquarter.isFullScreen() and not self.Headquarter.isMaximized():
				self.Headquarter.move(self.Headquarter.pos() + (event.pos() - self.__press_pos))
		
	def dobleClickMaximizeRestore(self,event):
		"双击切换最大化"
		if hasattr(self.Headquarter,"windowToggleMaximized") and event.type() == QEvent.MouseButtonDblClick and event.button()==Qt.LeftButton:
			QTimer.singleShot(50, self.Headquarter.windowToggleMaximized)