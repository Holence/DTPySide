from DongliTeahousePySideWheel import DongliTeahouseMessageIcon
from DongliTeahousePySideWheel import DongliTeahousePalette
from DongliTeahousePySideWheel.DongliTeahouseFunction import *

class DongliTeahouseSettingButton(QPushButton):
	def __init__(self,icon):
		super().__init__()
		self.setFixedSize(36,36)
		self.setIcon(icon)
		self.setIconSize(QSize(36,36))
		self.setFlat(True)

class DongliTeahouseTitleLabel(QLabel):
	def  __init__(self,parent):
		super(DongliTeahouseTitleLabel,self).__init__(parent)
		self.__press_pos = QPoint()
		
		#原理不明，重定义事件函数吗？
		self.mouseDoubleClickEvent = self.dobleClickMaximizeRestore

	def setPapa(self,PAPA):
		"拖动与双击要去改变主窗体的状态，而在MyTitleBar的setupUI给进来的parent是MyTitleBar，不是主窗体，所以要手动设置PAPA"
		self.PAPA=PAPA
	
	def mousePressEvent(self, event):
		super(DongliTeahouseTitleLabel, self).mousePressEvent( event )
		if event.button() == Qt.LeftButton:
			self.__press_pos = event.pos()

	def mouseReleaseEvent(self, event):
		super(DongliTeahouseTitleLabel, self).mouseReleaseEvent( event )
		if event.button() == Qt.LeftButton:
			self.__press_pos = QPoint()

	def mouseMoveEvent(self, event):
		super(DongliTeahouseTitleLabel, self).mouseMoveEvent( event )
		if not self.__press_pos.isNull():
			#全屏还移动就会出问题
			if not self.PAPA.isFullScreen() and not self.PAPA.isMaximized():
				self.PAPA.move(self.PAPA.pos() + (event.pos() - self.__press_pos))
		
	def dobleClickMaximizeRestore(self,event):
		"双击切换最大化"
		if hasattr(self.PAPA,"windowToggleMaximized") and event.type() == QEvent.MouseButtonDblClick and event.button()==Qt.LeftButton:
			QTimer.singleShot(50, self.PAPA.windowToggleMaximized)

class WeekCube(QGraphicsRectItem):
	def __init__(self,begin,now,colorList,parent):
		super().__init__(0,0,10,10)
		self.parent=parent
		self.now=now

		weeks=int(begin.daysTo(now)/7)
		y=weeks//52*15
		x=weeks%52*15
		self.setPos(float(x),float(y))
		
		#竟然可以直接略过QBrush？！
		# self.setBrush(QBrush(QColor("#FF6265")))
		# self.setBrush(QColor("#FF6265"))
		self.color=Generate_ConicalGradientColor(colorList)
		self.setBrush(self.color)
		self.setAcceptHoverEvents(True)
	
	def hoverEnterEvent(self,event):
		super().hoverEnterEvent(event)
		pen=QPen()
		pen.setWidth(2)
		self.setPen(pen)
	
	def hoverLeaveEvent(self,event):
		super().hoverLeaveEvent(event)
		pen=QPen()
		pen.setWidth(0)
		self.setPen(pen)
	
	def mousePressEvent(self,event):
		super().mousePressEvent(event)
