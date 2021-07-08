from __future__ import annotations
from DTPySide import *

DARK_DEEPDARK="rgb(35, 35, 35)"
DARK_BACKGROUND="rgb(53, 53, 53)"
DARK_SOFTDARK="rgb(42, 42, 42)"
DARK_BRIGHT="#5c5c5c"
DARK_HIGHLIGHT="rgb(42, 130, 218)"
DARK_WHITE="white"


DTDarkNormalStyle=f"""

#TitleBarFrame * {{
	background-color: {DARK_DEEPDARK};
}}
#TitleBarFrame {{
	background-color: {DARK_DEEPDARK};
}}
#TitleBarFrame #label_titlebar {{
	color: {DARK_WHITE};
}}

#DTMainWindow #centralWidget {{
	background-color: {DARK_BACKGROUND};
}}

#DTMainWindow #statusBar{{
	background-color: {DARK_SOFTDARK};
}}


QDialog {{
	border: 2px solid {DARK_DEEPDARK};
	border-radius: 1px;
}}

QPushButton {{
	font-family: "Hack";
}}


"""

###############################################################################################

DTDarkEffectStyle=f"""

* {{
	background-color: transparent;
}}

#TitleBarFrame * {{	
	background-color: {DARK_DEEPDARK};
}}
#TitleBarFrame {{	
	background-color: {DARK_DEEPDARK};
}}
#TitleBarFrame #label_titlebar {{
	color: {DARK_WHITE};
}}


#DTMainWindow #statusBar{{
	background-color: {DARK_SOFTDARK};
}}



/* 设置Window Effect后有些Palette会失效，得用stylesheet补足 */

QLineEdit, QDateTimeEdit, QSpinBox, QTextEdit, QPlainTextEdit, QTreeWidget, QTreeView, QProgressBar {{
	background-color: {DARK_SOFTDARK};
}}

/* QTabelView QTreeView 顶上的header*/
QHeaderView, QTableView QTableCornerButton::section{{
	background: {DARK_SOFTDARK};
}}


QSlider::groove{{
	height: 10px;
	background: {DARK_SOFTDARK};
    border: 1px solid transparent;
	border-radius: 6px;
}}

QSlider::handle {{
    background: {DARK_HIGHLIGHT};
    width: 20px;
	height: 12px;
    border: 1px solid {DARK_DEEPDARK};
    border-radius: 6px;
    margin: -2px 0; 
}}


QTabWidget::pane {{
	border: 1px solid {DARK_DEEPDARK};
	top:-1px; 
	background: {DARK_SOFTDARK};
}}
QTabBar::tab {{
	background: {DARK_BACKGROUND}; 
	border: 1px solid {DARK_DEEPDARK}; 
	padding: 15px;
}} 
QTabBar::tab:selected {{ 
	background: {DARK_SOFTDARK}; 
	margin-bottom: -1px; 
}}


QPushButton {{
	font-family: "Hack";
	background-color: {DARK_BACKGROUND};
}}

QToolButton {{
	font-family: "Hack";
	background-color: {DARK_BACKGROUND};
}}

QMenu {{
	background-color: {DARK_BACKGROUND};
	color: {DARK_WHITE};
}}
QMenu::item:selected {{
	background-color: {DARK_HIGHLIGHT};
}}


QDialog {{
	background-color: {DARK_BACKGROUND};
	border: 2px solid {DARK_DEEPDARK};
	border-radius: 1px;
}}

QToolTip {{
	color: {DARK_WHITE};
	background-color: {DARK_SOFTDARK};
}}

QComboBox {{
	background-color: {DARK_SOFTDARK};
}}

QComboBox::item:selected {{
	background-color: {DARK_HIGHLIGHT};
}}

QRadioButton {{
	color: {DARK_WHITE};
}}

QRadioButton::indicator {{
	width: 10px;
	height: 10px;
	border-radius: 7px;
}}

QRadioButton::indicator:checked {{
	background-color: {DARK_HIGHLIGHT};
	border: 2px solid {DARK_WHITE};
}}

QRadioButton::indicator:unchecked {{
	background-color: transparent;
	border: 2px solid {DARK_WHITE};
}}

QAbstractScrollArea::corner {{
    background: none;
    border: none;
}}

QScrollBar:vertical {{

	background: {DARK_SOFTDARK};
	width:15px;
	border-radius: 7px;
	margin: 0px 0px 0px 0px;
}}
QScrollBar::handle:vertical {{         

	min-height: 0px;
	border: 0px solid red;
	border-radius: 6px;
	background-color: {DARK_HIGHLIGHT};
}}
QScrollBar::add-line:vertical {{       
	height: 0px;
	subcontrol-position: bottom;
	subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
	height: 0 px;
	subcontrol-position: top;
	subcontrol-origin: margin;
}}

QScrollBar:horizontal {{

	background: {DARK_SOFTDARK};
	height:15px;
	border-radius: 7px;
	margin: 0px 0px 0px 0px;
}}
QScrollBar::handle:horizontal {{         

	min-width: 0px;
	border: 0px solid red;
	border-radius: 6px;
	background-color: {DARK_HIGHLIGHT};
}}
QScrollBar::add-line:horizontal {{       
	width: 0px;
	subcontrol-position: right;
	subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
	width: 0 px;
	subcontrol-position: left;
	subcontrol-origin: margin;
}}
"""