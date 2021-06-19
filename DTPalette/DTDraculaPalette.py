from PySide2.QtGui import QPalette,QColor
from PySide2.QtCore import Qt

class DTDraculaPalette(QPalette):
	"""Dracula palette for a Qt application meant to be used with the Fusion theme."""
	def __init__(self):
		super().__init__()

		self.setColor(QPalette.WindowText, QColor("#EBEBEB"))
		self.setColor(QPalette.ToolTipBase, QColor("#EBEBEB"))
		self.setColor(QPalette.ToolTipText, QColor("#EBEBEB"))
		self.setColor(QPalette.Text, QColor("#EBEBEB"))
		self.setColor(QPalette.ButtonText, QColor("#EBEBEB"))
		self.setColor(QPalette.HighlightedText, QColor("#EBEBEB"))
		self.setColor(QPalette.BrightText, QColor("#EBEBEB"))
		
		self.setColor(QPalette.Disabled, QPalette.WindowText, QColor("#7F7F7F"))
		self.setColor(QPalette.Disabled, QPalette.Text, QColor("#7F7F7F"))
		self.setColor(QPalette.Disabled, QPalette.ButtonText, QColor("#7F7F7F"))
		self.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor("#7F7F7F"))
		self.setColor(QPalette.Disabled, QPalette.Highlight, QColor("#7F7F7F"))

		self.setColor(QPalette.Button, QColor("#282C34"))
		self.setColor(QPalette.Base, QColor("#21252B"))
		self.setColor(QPalette.Dark, QColor("#1E2127"))
		self.setColor(QPalette.AlternateBase, QColor("#191A21"))
		self.setColor(QPalette.Shadow, QColor("#141414"))

		self.setColor(QPalette.Window, QColor("#282C34"))
		self.setColor(QPalette.Link, QColor("#BD93F9"))
		self.setColor(QPalette.Highlight, QColor("#BD93F9"))