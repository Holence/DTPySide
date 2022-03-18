from __future__ import annotations
from DTPySide import *

class DTTree(QTreeWidget):
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setSortingEnabled(True)
		self.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.setAnimated(True)

		self.setExpandsOnDoubleClick(False)

		self.horizontalScrollBar().setVisible(False)
		
		self.header().setStretchLastSection(True)
		self.header().setDefaultSectionSize(80)
		self.header().setMinimumSectionSize(80)

		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.setSelectionBehavior(QAbstractItemView.SelectRows)

		self.setDragEnabled(True)
		self.setDragDropMode(QAbstractItemView.DragDrop)

		self.header().setDefaultAlignment(Qt.AlignCenter)
		self.setIndentation(20)
		
		self.ExpandDict={}
		self.ExpandCheckingColumn=-1 #不设置的话，就是全部expand
	
	def setColumn(self,column_list:list):
		self.setColumnCount(len(column_list))
		self.setHeaderLabels(column_list)
	
	def setExpandCheckingColumn(self,column:int):
		self.ExpandCheckingColumn=column

	def StoreTreeStatus(self):

		def ExpandCheck(root:QTreeWidgetItem):
			
			if self.ExpandDict.get(root.text(self.ExpandCheckingColumn))==None:
				self.ExpandDict[root.text(self.ExpandCheckingColumn)]=root.isExpanded()
			
			for index in range(root.childCount()):
				child=root.child(index)
				ExpandCheck(child)
		
		if self.ExpandCheckingColumn!=-1:
			self.ExpandDict={}
			ExpandCheck(self.invisibleRootItem())
		
		self.sort_index=self.header().sortIndicatorSection()
		self.sort_order=self.header().sortIndicatorOrder()
		self.header().setSortIndicator(-1,Qt.SortOrder.AscendingOrder) #因为如果有排序的话，再insertItem会有疏漏，所以提前取消排序

	def RestoreTreeStatus(self):
		def ExpandRestore(root:QTreeWidgetItem):
			try:
				root.setExpanded(self.ExpandDict[root.text(self.ExpandCheckingColumn)])
			except:
				pass
			for index in range(root.childCount()):
				child=root.child(index)
				ExpandRestore(child)
		
		def ExpandAll(root:QTreeWidgetItem):
			root.setExpanded(True)
			for index in range(root.childCount()):
				child=root.child(index)
				ExpandAll(child)
		
		if self.ExpandCheckingColumn!=-1:
			ExpandRestore(self.invisibleRootItem())
		else:
			ExpandAll(self.invisibleRootItem())
		
		self.header().setSortIndicator(self.sort_index,self.sort_order) # insertItem完了后，再把sort_index,sort_order设置回来