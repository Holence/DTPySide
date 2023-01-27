from __future__ import annotations
from DTPySide import *

class DTStyleSheet(str):
	def __new__(cls, color_list, window_effect:str, font:QFont):
		
		# font_size=18
		font_family=font.family()

		DEEPDARK,BACKGROUND,SOFTDARK,DIM,PRESSED,FOCUSED,TEXT=color_list
		
		ICONCOLOR=QIcon.themeName()

		stylesheet=""

		if window_effect=="Normal":
			stylesheet+=f"""
				* {{
					background: {BACKGROUND};
				}}
			"""
			pass
		else:
			stylesheet+=f"""
				* {{
					background: transparent;
				}}

				QDialog{{
					background-color: {BACKGROUND};
				}}
			"""
		

		stylesheet+=f"""

		QWidget
		{{
			color: {TEXT};
			font-family: {font_family};
			font-size: 14pt;
			selection-background-color: {FOCUSED};
			selection-color: {TEXT};
		}}
		QWidget::item:active, QWidget::item:!active
		{{
			color: {TEXT};
		}}
		
		QWidget:disabled
		{{
			color: {DIM};
		}}

		QDialog {{
			border: 2px solid {DEEPDARK};
			border-radius: 2px;
		}}

		#DTMainWindowWin32 #statusBar, #DTMainWindowLinux #statusBar{{
			background-color: {SOFTDARK};
			font-family: "微软雅黑";
			font-size: 9pt;
		}}

		/* Login */
		DTLoginSession QLineEdit {{
			font-size: 12pt;
		}}

		DTLoginSession DTTitleBar QLabel {{
			font-family: "Segoe UI";
			font-size: 20pt;
		}}

		DTLoginSession DTTitleBar #title_icon{{
			icon-size: 36px;
			max-height: 36px;
			min-height: 36px;
			min-width: 36px;
			max-width: 36px;
		}}
		
		/* TitleBar */
		DTTitleBar QLabel {{
			font-family: "Segoe UI";
			font-size: 20px;
		}}
		
		DTTitleBar QPushButton {{
			border: none;
			background-color: transparent;
			max-height: 24px;
			min-height: 24px;
			min-width: 24px;
			max-width: 24px;
		}}

		DTTitleBar QPushButton:hover{{
			background-color: {SOFTDARK};
			border-style: solid;
			border-radius: 4px;
		}}
		DTTitleBar QPushButton:pressed {{
			background-color: {DIM};
			border-style: solid;
			border-radius: 4px;
		}}

		DTTitleBar #title_icon{{
			icon-size: 26px;
			max-height: 26px;
			min-height: 26px;
			min-width: 26px;
			max-width: 26px;
		}}
		DTTitleBar #title_icon:hover{{
			background-color: transparent;
		}}
		DTTitleBar #title_icon:pressed {{
			background-color: transparent;
		}}
		
		DTTitleBar #btn_close:hover{{
			background-color: rgb(232, 17, 35);
			border-style: solid;
			border-radius: 4px;
		}}
		DTTitleBar #btn_close:pressed {{
			background-color: rgb(241, 112, 122);
			border-style: solid;
			border-radius: 4px;
		}}
		DTTitleBar * {{
			background-color: {DEEPDARK};
		}}
		DTTitleBar {{
			background-color: {DEEPDARK};
		}}

		/* ---------------------------------------- */

		QFrame{{
			color: {TEXT};
		}}
		QMainWindow::separator{{
			border: 1px solid {DEEPDARK};
			width: 4px;
			height: 4px;
		}}
		QMainWindow::separator:hover{{
			background: {FOCUSED};
		}}

		QSplitter{{
			background: transparent;
		}}

		QSplitter::handle{{
			border: 1px solid transparent;
			margin: 2px;
			border-radius: 6px;
		}}
		QSplitter::handle:horizontal{{
			width: 6px;
			image: url(:/icons/{ICONCOLOR}/more-vertical.svg);
		}}
		QSplitter::handle:vertical{{
			height: 6px;
			image: url(:/icons/{ICONCOLOR}/more-horizontal.svg);
		}}
		QSplitter::handle:hover{{
			background: {SOFTDARK};
		}}
		

		QSizeGrip{{
			background-color: none;
		}}

		/* MenuBar Menu */
		QMenuBar {{
			background-color: {BACKGROUND};
			font-size: 10pt;
			spacing: 1px;
			border-bottom: 1px solid {DEEPDARK};
		}}

		QMenuBar::item{{
			background: transparent;
			font-size: 10pt;
			padding: 1px 8px;
		}}

		QMenuBar::item:selected{{
			background: {FOCUSED};
			border: 1px solid {DEEPDARK};
		}}

		QMenuBar::item:pressed{{
			background: {PRESSED};
			border: 1px solid {DEEPDARK};
			padding-top: 4px;
		}}

		QMenu {{
			font-family: "微软雅黑";
			font-size: 10pt;
			background-color: {BACKGROUND};
			margin: 1px;
			padding: 1px;
		}}

		QMenu::item{{
			font-family: "微软雅黑";
			font-size: 10pt;
			padding: 2px 25px 2px 15px;
			border: 1px solid transparent;
			margin: 1px;
		}}
		QMenu::item:disabled{{
			color: {DIM};
		}}
		QMenu::icon {{
			width: 15px;
			height: 15px;
			padding:5px;
			border-right: 1px inset {DEEPDARK};
		}}

		QMenu::item:selected {{
			border-color: {DEEPDARK};
			background: {FOCUSED};
		}}

		QMenu::separator {{
			height: 2px;
			background: {DEEPDARK};
		}}

		QMenu::indicator {{/*checked 的√*/
			width: 13px;
			height: 13px;
			padding:2px;
		}}
		QMenu::icon:checked {{ /* appearance of a 'checked' icon */
			background: {FOCUSED};
			border: 1px inset {DEEPDARK};
			border-radius: 3px;
			padding: 2px;
		}}


		/* ToolBar */

		QToolBar {{
			background: {BACKGROUND};
			spacing: 1px;
			padding: 1px;
			border-bottom: 1px solid {DEEPDARK};
		}}


		/* Label */

		QLabel {{
			background: transparent;
		}}

		QToolTip {{
			background: {SOFTDARK};
			color: {TEXT};
			font-family: {font_family};
			font-size: 11pt;
		}}


		/* TextBox */
		
		QLineEdit {{
			background: {SOFTDARK};
			font-size: 12pt;
			border-radius: 6px;
			height: 26px;
		}}


		QLineEdit:focus{{
			border: 1px solid;
			border-color: {FOCUSED};
		}}

		QLineEdit:read-only {{
			color: {DIM};
		}}

		QTextEdit, QPlainTextEdit, QTextBrowser{{
			border-radius: 6px;
			font-size: 14pt;
			background-color: {SOFTDARK};
		}}
		QTextEdit:focus, QPlainTextEdit:focus, QTextBrowser:focus{{
			border: 1px solid;
			border-color: {FOCUSED};
		}}

		/* Button */


		QPushButton {{
			border: 1px solid transparent;
			border-radius: 3px;
			background-color: {SOFTDARK};
			font-family: {font_family}; /*"微软雅黑";*/
			font-size: 12pt;
			min-height: 26px;
		}}

		QPushButton:hover{{
			background-color: {FOCUSED};
			border-color: {FOCUSED};
		}}

		QPushButton:pressed
		{{
			background-color: {PRESSED};
			border-color: {FOCUSED};
		}}

		QPushButton:focus, QPushButton:default {{
			border-color: {FOCUSED};
		}}

		QDialogButtonBox QPushButton{{
			min-width: 72px;
		}}
		
		QToolButton {{
			font-family: {font_family}; /*"微软雅黑";*/
			font-size: 12pt;
			height: 27px;
		}}
		QToolButton,QToolButton:unchecked {{
			/* ToolBar里的按钮和带下拉菜单的按钮 */
			border: 1px solid transparent;
			border-radius: 3px;
			background-color: {SOFTDARK};
			margin: 1px;
		}}
		QToolButton:checked{{
			background-color: {FOCUSED};
			border-color: {DEEPDARK};
		}}
		QToolButton:hover{{
			background-color: {FOCUSED};
			border-color: {DEEPDARK};
		}}

		QToolButton:pressed,QToolButton:checked:hover{{
			background-color: {PRESSED};
			border-color: {DEEPDARK};
		}}
		QToolButton:checked:pressed{{
			background-color: {FOCUSED};
		}}

		/* only for MenuButtonPopup */
		QToolButton[popupMode="1"]{{
			padding-left: 1px;
			padding-right: 15px;
			border: 1px solid {DEEPDARK};
			min-height: 15px;
			background-color: {SOFTDARK};
		}}
		QToolButton[popupMode="1"]:hover{{
			background-color: {FOCUSED};
			border-color: {DEEPDARK};
		}}
		QToolButton[popupMode="1"]:pressed{{
			border-width: 1px;
			background-color: {PRESSED};
			border-color: {DEEPDARK};
		}}
		QToolButton::menu-button {{
			border: 1px solid {DEEPDARK};
			border-top-right-radius: 2px;
			border-bottom-right-radius: 2px;
			width: 16px;
		}}

		QRadioButton{{
			background: transparent;
			font-family: {font_family}; /*"微软雅黑";*/
			font-size: 12pt;
		}}
		QRadioButton::indicator {{
			width: 10px;
			height: 10px;
			border: 2px solid {TEXT};
			border-radius: 7px;
		}}
		QRadioButton::indicator:checked {{
			background: {FOCUSED};
		}}
		QRadioButton::indicator:unchecked {{
			background: transparent;
		}}

		QCheckBox{{
			font-family: {font_family}; /*"微软雅黑";*/
			font-size: 12pt;
			background: transparent;
		}}
		QCheckBox::indicator {{
			width: 10px;
			height: 10px;
			border: 2px solid {TEXT};
			border-radius: 7px;
		}}
		QCheckBox::indicator:checked {{
			background-color: {FOCUSED};
		}}
		QCheckBox::indicator:unchecked {{
			background-color: transparent;
		}}
		QCheckBox::indicator:indeterminate {{
			background-color: {FOCUSED};
			border-radius: 2px;
		}}

		

		/* ComboBox */

		QComboBox{{
			background-color: {SOFTDARK};
			border-radius: 6px;
			font-size: 12pt;
			height: 26px;
		}}
		QComboBox:focus{{
			border: 1px solid;
			border-color: {FOCUSED};
		}}
		QComboBox QAbstractItemView{{
			background-color: {DEEPDARK};
		}}
		QComboBox::drop-down{{
			background-color: {SOFTDARK};
			border: 1px solid transparent;
			border-top-right-radius: 6px;
			border-bottom-right-radius: 6px;
			subcontrol-origin: padding;
			subcontrol-position: top right;
			width: 18px;
			margin: 1px;
		}}
		QComboBox::drop-down:pressed{{
			background-color: {FOCUSED};
		}}
		QComboBox::down-arrow{{
			image: url(:/icons/{ICONCOLOR}/chevron-down.svg);
		}}
		

		/* SpinBox DateTime */

		QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit{{
			font-family: {font_family}; /*"微软雅黑";*/
			background-color: {SOFTDARK};
			font-size: 12pt;
			border-radius: 6px;
			height: 26px;
		}}
		QSpinBox:focus, QDoubleSpinBox:focus, QDateEdit:focus, QTimeEdit:focus, QDateTimeEdit:focus{{
			border: 1px solid {FOCUSED};
		}}

		QSpinBox::up-button, QDoubleSpinBox::up-button, QDateEdit::up-button, QTimeEdit::up-button, QDateTimeEdit::up-button{{
			background-color: {SOFTDARK};
			subcontrol-origin: border;
			subcontrol-position: top right;
			width: 18px;
			border: 2px ridge transparent;
			border-top-right-radius: 6px;
			margin-top: 1px;
			margin-right: 1px;
		}}
		QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed, QDateEdit::up-button:pressed, QTimeEdit::up-button:pressed, QDateTimeEdit::up-button:pressed {{
			background-color: {FOCUSED};
		}}
		QSpinBox::up-arrow, QDoubleSpinBox::up-arrow, QDateEdit::up-arrow, QTimeEdit::up-arrow, QDateTimeEdit::up-arrow{{
			image: url(:/icons/{ICONCOLOR}/chevron-up.svg);
		}}

		QSpinBox::down-button, QDoubleSpinBox::down-button, QDateEdit::down-button, QTimeEdit::down-button, QDateTimeEdit::down-button{{
			background-color: {SOFTDARK};
			subcontrol-origin: border;
			subcontrol-position: bottom right;
			width: 18px;
			border: 2px ridge transparent;
			border-bottom-right-radius: 6px;
			margin-bottom: 1px;
			margin-right: 1px;
		}}
		QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed, QDateEdit::down-button:pressed, QTimeEdit::down-button:pressed, QDateTimeEdit::down-button:pressed {{
			background-color: {FOCUSED};
		}}
		QSpinBox::down-arrow, QDoubleSpinBox::down-arrow, QDateEdit::down-arrow, QTimeEdit::down-arrow, QDateTimeEdit::down-arrow{{
			image: url(:/icons/{ICONCOLOR}/chevron-down.svg);
		}}
		


		/* Slider ProgressBar */

		QProgressBar {{
			background-color: {SOFTDARK};
			border-radius: 6px;
			text-align: center;
		}}

		QProgressBar::chunk {{
			border-radius: 6px;
			background-color: {FOCUSED};
		}}

		QSlider{{
			background: transparent;
			min-height: 14px;
			min-width: 14px;
		}}
		
		QSlider::handle {{
			background: {FOCUSED};
			border: 1px solid {DEEPDARK};
			border-radius: 6px;
		}}

		QSlider::groove:horizontal {{
			height: 12px;
		}}
		QSlider::handle:horizontal{{
			width: 12px;
			height: 14px;
			margin: -7px;
		}}

		QSlider::groove:vertical{{
			width: 12px;
		}}
		QSlider::handle:vertical{{
			width: 14px;
			height: 12px;
			margin: -7px;
		}}
		
		QSlider::add-page{{
			/*还没有滑上去的地方*/
			background:{SOFTDARK};
		}}
		QSlider::sub-page{{
			/*已经划过的从地方*/
			background: {FOCUSED};
		}}


		/* ScrollBar */

		QScrollBar{{
			width: 16px;
			height: 16px;
			background-color: transparent;
			padding: 1px;
		}}
		QScrollBar::handle{{
			min-height: 30px;
		}}
		QScrollBar::handle{{
			border-radius: 5px;
			background: {FOCUSED};
		}}
		QScrollBar::handle:hover {{
			background: {PRESSED};
		}}
		QScrollBar::add-line, QScrollBar::sub-line, QScrollBar::add-page, QScrollBar::sub-page {{
			background: transparent;
			height: 0px;
		}}
		QScrollArea{{
			border: none;
		}}
		QAbstractScrollArea::corner {{
			background: transparent;
		}}

		/* DockWidget*/

		QDockWidget > QWidget {{
			border: transparent;
		}}

		/* GroupBox */

		QGroupBox {{
			border: 2px solid {DEEPDARK};
			border-radius: 6px;
			margin-top:1em;
		}}
		QGroupBox::title {{
			subcontrol-origin: margin;
			subcontrol-position: top left;
		}}

		/* ToolBox */

		QToolBox{{
			border: 1px solid transparent;
		}}
		QToolBox::tab {{
			font-family: {font_family}; /*"微软雅黑";*/
			font-size: 12pt;
			background: {SOFTDARK};
			border-color: transparent;
			border-radius: 6px;
			padding-left: 4px;
		}}
		QToolBox::tab:hover {{
			background-color: {FOCUSED};
			border-color: transparent;
		}}
		QToolBox::tab:pressed {{
			background-color: {PRESSED};
			border-color: transparent;
		}}
		QToolBox::tab:selected {{
			font-weight: bold;
			border-color: {DEEPDARK};
		}}


		/* TabWidget */

		QTabWidget{{
			margin-top:10px;
		}}
		QTabWidget::pane{{
			margin-top:5px;
			border: none;
		}}
		QTabWidget::tab-bar {{
			left: 0px;
		}}
		QTabBar::tab {{
			font-family: {font_family}; /*"微软雅黑";*/
			font-size: 12pt;
			background: {SOFTDARK};
			border-color: transparent;
			border-radius: 4px;
			left: -8px;
			margin-left: 8px;
		}}
		QTabBar::tab:hover {{
			background: {FOCUSED};
		}}
		QTabBar::tab:selected {{
			background: {FOCUSED};
		}}
		QTabBar::tab:pressed {{
			background: {PRESSED};
		}}
		
		/*别显示左右的按钮了，滚轮滚就行了*/
		QTabBar::scroller {{
			width: 0px;
		}}


		/* QHeaderView for list table */

		QAbstractItemView, QAbstractItemView QLineEdit {{
			font-family: {font_family};
			font-size: 12pt;
			background-color: {SOFTDARK};
		}}
		
		QHeaderView {{
			border: none;
			font-size: 10pt;
		}}
		QHeaderView::section, QTableCornerButton::section {{
			/*设置表头属性*/ /*表格左上角小框框*/
			background-color: {DIM};
			padding-top: 5px;
			border-right: 1px solid {DEEPDARK};
			border-bottom: 1px solid {DEEPDARK};
			border-radius: 0px;
		}}
		QHeaderView::section:hover, QTableCornerButton::section:hover{{
			background-color: {DIM};
		}}
		QHeaderView::section:pressed{{
			background-color: {DIM};
		}}
		QHeaderView::section:checked {{
			background-color: {DIM};
		}}


		/* QTableWidget */

		QTableWidget, QTableView
		{{
			font-size: 12pt;
			gridline-color: {DEEPDARK}; /*表格中的网格线条颜色*/
			border-color: transparent; /*边框线的宽度、颜色*/
			border-radius: 6px;
		}}
		

		QTableWidget QComboBox{{
			margin: 2px;
			border: none;
		}}

		QListView, QTreeView, QTableView {{
			font-size: 12pt;
			border-color: transparent; /*边框线的宽度、颜色*/
			border-radius: 6px;
		}}
		

		QListView::item, QTreeView::item, QTableView::item{{
			font-size: 12pt;
			background: {DIM};
			outline-style: none;
			border-left: 2px solid {PRESSED};
		}}
		QListView::item:selected , QTreeView::item:selected, QTableView::item:selected {{
			background: {FOCUSED};
			color: {TEXT};
		}}

		QListView::item:hover, QTreeView::item:hover, QTableView::item:hover {{
			background: {FOCUSED};
		}}
		

		QTreeView::branch{{
			
		}}
		QTreeView::branch:selected{{
			
		}}


		QFontDialog {{
			min-width: 900px;
			min-height: 700px;
		}}
		QFontDialog * {{
			font-size: 17px;
		}}
		
		/* QCalendar */

		/* header row */
		QCalendarWidget QWidget {{
			font-family: {font_family}; /*"微软雅黑";*/
			font-size: 12pt;
			alternate-background-color: {SOFTDARK};
		}}
		
		/* normal days */
		QCalendarWidget QAbstractItemView:enabled
		{{
			background-color: {BACKGROUND};
		}}
		
		"""
		# QStatusBar{{
		# 	background: transparent;
		# 	border-top:1px solid {DEEPDARK};
		# }}

		# QStatusBar::item {{
		# 	margin: 2px 0;
		# 	border-left: 1px solid {DEEPDARK};
		# }}

		# QStatusBar QLabel{{
		# 	background: transparent;
		# 	margin: 0  2px;
		# }}

		# QStatusBar QPushButton{{
		# 	background: transparent;
		# 	margin: 0  2px;
		# }}

		# QStatusBar QPushButton:hover{{
		# 	background: {FOCUSED};
		# 	margin: 0  2px;
		# }}
		return str.__new__(cls,stylesheet)
