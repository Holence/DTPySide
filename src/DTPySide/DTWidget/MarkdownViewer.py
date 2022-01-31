from __future__ import annotations
from DTPySide import *

class MarkdownViewer(QTextBrowser):

	# def eventFilter(self, watched: QObject, event:QEvent) -> bool:
	
	# 	if event.type()==QEvent.ShortcutOverride:
	# 		self.shortcut_queue.append(event.key())
	# 		self.shortcut_queue.pop(0)
	# 		if self.shortcut_queue==[16777249, 67]:
	# 			print("Copied")
	# 			# self.copyMarkdown()
	# 		return True #好像不起作用……
	# 	return False

	def __init__(self, parent):
		super().__init__(parent=parent)
		# self.installEventFilter(self)
		# self.shortcut_queue=[0, 0]
	
	def contextMenuEvent(self, e: QContextMenuEvent):
		menu=self.createStandardContextMenu()

		new_CopyAction=QAction("Copy Markdown")
		new_CopyAction.triggered.connect(self.copyMarkdown)
		menu.insertAction(menu.actions()[1], new_CopyAction)
		
		menu.exec_(e.globalPos())
		del menu
	
	def copyMarkdown(self):
		clip=QGuiApplication.clipboard()
		
		# 只能给我html……
		html=self.textCursor().selection().toHtml()
		
		# 找个做苦力的来转换哈哈哈哈
		temp=QTextEdit()
		temp.setHtml(html)
		text=temp.toMarkdown()
		
		clip.setText(text)