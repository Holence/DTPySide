from DongliTeahousePySideWheel import DongliTeahouseIcon
from DongliTeahousePySideWheel import DongliTeahousePalette
from DongliTeahousePySideWheel.DongliTeahouseFunction import *

class DongliTeahouseCapsuleButton(QLabel):
	clicked=Signal()
	def __init__(self,parent,text,color):
		super().__init__(parent)
		self.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed)
		
		# setStyleSheet会自动清空font，这里还得手动set一下
		self.setText(text)
		self.setFont(parent.font())
		self.adjustSize()
		
		self.setStyleSheet(""" 
			QLabel {
				color: white;
				background-color: %s;
				border-radius: %spx;
				border: 1px solid %s;
			}
		"""%(color,int(self.height()/2),color))

		# SET DROP SHADOW
		shadow = QGraphicsDropShadowEffect(self)
		shadow.setBlurRadius(0.8)
		shadow.setXOffset(4)
		shadow.setYOffset(4)
		shadow.setColor(QColor("#252525"))
		self.setGraphicsEffect(shadow)
	
	def mouseReleaseEvent(self,event):
		super().mouseReleaseEvent(event)
		if event.button()==Qt.LeftButton:
			self.clicked.emit()
	
	# Clear_Layout时调用deleteLater删除DongliTeahouseCapsuleButton，但shadow消不干净，那就setGraphicsEffect为空
	def deleteLater(self):
		super().deleteLater()
		self.setGraphicsEffect(None)

class DongliTeahouseToolTip(QLabel):
	def __init__(self, parent, tooltip):
		super().__init__(tooltip,parent)
		
		self.setFont(parent.font())
		
		self.setStyleSheet(""" 
			QLabel {
				background-color: #0C0B0B;	
				color: #E6E6E6;
				padding-left: 10px;
				padding-right: 10px;
				border-radius: %spx;
				border: 1px solid #0C0B0B;
				border-left: 3px solid #FF6265;
			}
		"""%int(self.height()/2))

		self.adjustSize()

		# SET OPACITY
		opacity = QGraphicsOpacityEffect(self)
		opacity.setOpacity(0.85)
		self.setGraphicsEffect(opacity)

class DongliTeahouseSettingButton(QPushButton):
	def __init__(self,icon):
		super().__init__()
		self.setFixedSize(30,30)
		self.setIcon(icon)
		self.setIconSize(QSize(30,30))
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
