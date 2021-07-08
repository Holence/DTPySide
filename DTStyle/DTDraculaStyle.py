from __future__ import annotations
from DTPySide import *

DRACULA_DEEPDARK="#21252B"
DRACULA_BACKGROUND="#282C34"
DRACULA_SOFTDARK="#30353F"
DRACULA_BRIGHT="#5c5c5c"
DRACULA_HIGHLIGHT="#BD93F9"
DRACULA_WHITE="#EBEBEB"


DTDraculaNormalStyle=f"""

#TitleBarFrame * {{
	background-color: {DRACULA_DEEPDARK};
}}
#TitleBarFrame {{
	background-color: {DRACULA_DEEPDARK};
}}
#TitleBarFrame #label_titlebar {{
	color: {DRACULA_WHITE};
}}

#DTMainWindow #centralWidget {{
	background-color: {DRACULA_BACKGROUND};
}}

#DTMainWindow #statusBar{{
	background-color: {DRACULA_SOFTDARK};
}}


QDialog {{
	border: 2px solid {DRACULA_DEEPDARK};
	border-radius: 1px;
}}

QPushButton {{
	font-family: "Hack";
}}


"""

###############################################################################################

DTDraculaEffectStyle=f"""

* {{
	background-color: transparent;
}}

#TitleBarFrame * {{	
	background-color: {DRACULA_DEEPDARK};
}}
#TitleBarFrame {{	
	background-color: {DRACULA_DEEPDARK};
}}
#TitleBarFrame #label_titlebar {{
	color: {DRACULA_WHITE};
}}


#DTMainWindow #statusBar{{
	background-color: {DRACULA_SOFTDARK};
}}



/* 设置Window Effect后有些Palette会失效，得用stylesheet补足 */

QLineEdit, QDateTimeEdit, QSpinBox, QTextEdit, QPlainTextEdit, QTreeWidget, QTreeView, QProgressBar {{
	background-color: {DRACULA_SOFTDARK};
}}

/* QTabelView QTreeView 顶上的header*/
QHeaderView, QTableView QTableCornerButton::section{{
	background: {DRACULA_SOFTDARK};
}}


QSlider::groove{{
	height: 10px;
	background: {DRACULA_SOFTDARK};
    border: 1px solid transparent;
	border-radius: 6px;
}}

QSlider::handle {{
    background: {DRACULA_HIGHLIGHT};
    width: 20px;
	height: 12px;
    border: 1px solid {DRACULA_DEEPDARK};
    border-radius: 6px;
    margin: -2px 0; 
}}


QTabWidget::pane {{
	border: 1px solid {DRACULA_DEEPDARK};
	top:-1px; 
	background: {DRACULA_SOFTDARK};
}}
QTabBar::tab {{
	background: {DRACULA_BACKGROUND}; 
	border: 1px solid {DRACULA_DEEPDARK}; 
	padding: 15px;
}} 
QTabBar::tab:selected {{ 
	background: {DRACULA_SOFTDARK}; 
	margin-bottom: -1px; 
}}


QPushButton {{
	font-family: "Hack";
	background-color: {DRACULA_BACKGROUND};
}}

QToolButton {{
	font-family: "Hack";
	background-color: {DRACULA_BACKGROUND};
}}

QMenu {{
	background-color: {DRACULA_BACKGROUND};
	color: {DRACULA_WHITE};
}}
QMenu::item:selected {{
	background-color: {DRACULA_HIGHLIGHT};
}}


QDialog {{
	background-color: {DRACULA_BACKGROUND};
	border: 2px solid {DRACULA_DEEPDARK};
	border-radius: 1px;
}}

QToolTip {{
	color: {DRACULA_WHITE};
	background-color: {DRACULA_SOFTDARK};
}}

QComboBox {{
	background-color: {DRACULA_SOFTDARK};
}}

QComboBox::item:selected {{
	background-color: {DRACULA_HIGHLIGHT};
}}

QRadioButton {{
	color: {DRACULA_WHITE};
}}

QRadioButton::indicator {{
	width: 10px;
	height: 10px;
	border-radius: 7px;
}}

QRadioButton::indicator:checked {{
	background-color: {DRACULA_HIGHLIGHT};
	border: 2px solid {DRACULA_WHITE};
}}

QRadioButton::indicator:unchecked {{
	background-color: transparent;
	border: 2px solid {DRACULA_WHITE};
}}

QAbstractScrollArea::corner {{
    background: none;
    border: none;
}}

QScrollBar:vertical {{

	background: {DRACULA_SOFTDARK};
	width:15px;
	border-radius: 7px;
	margin: 0px 0px 0px 0px;
}}
QScrollBar::handle:vertical {{         

	min-height: 0px;
	border: 0px solid red;
	border-radius: 6px;
	background-color: {DRACULA_HIGHLIGHT};
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

	background: {DRACULA_SOFTDARK};
	height:15px;
	border-radius: 7px;
	margin: 0px 0px 0px 0px;
}}
QScrollBar::handle:horizontal {{         

	min-width: 0px;
	border: 0px solid red;
	border-radius: 6px;
	background-color: {DRACULA_HIGHLIGHT};
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