DTDarkNormalStyle="""

#TitleBarFrame * {	
	background-color: rgb(35, 35, 35);
}
#TitleBarFrame {	
	background-color: rgb(35, 35, 35);
}
#TitleBarFrame #label_titlebar {
	color: white;
}

#DTMainWindow #centralWidget {	
	background-color: rgb(53, 53, 53);
}

#DTMainWindow #statusBar{
	background-color: rgb(42, 42, 42);
}


QDialog {
	border: 2px solid #21252B;
	border-radius: 1px;
}

QPushButton {
	font-family: "Hack";
}


"""

###############################################################################################

DTDarkEffectStyle="""

* {
	background-color: transparent;
}

#TitleBarFrame * {	
	background-color: rgb(35, 35, 35);
}
#TitleBarFrame {	
	background-color: rgb(35, 35, 35);
}
#TitleBarFrame #label_titlebar {
	color: white;
}


#DTMainWindow #statusBar{
	background-color: rgb(42, 42, 42);
}



/* 设置Window Effect后有些Palette会失效，得用stylesheet补足 */

QMenu {
	background-color: rgb(53, 53, 53);
	color: white;
}
QMenu::item:selected {
	background-color: rgb(42, 130, 218);
}

QLineEdit {
	background-color: rgb(35, 35, 35);
}

QDialog {
	background-color: rgb(53, 53, 53);
	border: 2px solid #21252B;
	border-radius: 1px;
}

QPushButton {
	font-family: "Hack";
	background-color: rgb(53, 53, 53);
}


"""