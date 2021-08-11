from __future__ import annotations
from DTPySide import *

class DTHorizontalTabel(QTableWidget):
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setSortingEnabled(True)
		self.setEditTriggers(QAbstractItemView.NoEditTriggers)
		
		self.horizontalScrollBar().setVisible(False)
		# self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
		# self.horizontalScrollBar().setSingleStep(4)
		# self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
		# self.verticalScrollBar().setSingleStep(4)

		self.horizontalHeader().setStretchLastSection(True)
		self.horizontalHeader().setMinimumSectionSize(80)
		self.horizontalHeader().setDefaultSectionSize(80)
		self.verticalHeader().setVisible(False)
		
		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.setSelectionBehavior(QAbstractItemView.SelectRows)

		self.setDragEnabled(True)
		self.setDragDropMode(QAbstractItemView.DragDrop)

		def	slot():
			self.selected_row=0
			self.clearSelection()
		# 手动sort后清空选区
		self.horizontalHeader().sectionPressed.connect(slot)
	
	def setColumn(self,column_list:list):
		self.setColumnCount(len(column_list))
		self.setHorizontalHeaderLabels(column_list)
	
	def StoreTableStatus(self):
		self.selected_row=self.currentRow()
		self.sort_index=self.horizontalHeader().sortIndicatorSection()
		self.sort_order=self.horizontalHeader().sortIndicatorOrder()
	
	def Clear(self):
		self.clearContents()
		self.setRowCount(0)
		self.horizontalHeader().setSortIndicator(-1,Qt.SortOrder.AscendingOrder) #因为如果有排序的话，再insertItem会有疏漏，所以提前取消排序

	def RestoreTableStatus(self):
		self.horizontalHeader().setSortIndicator(self.sort_index,self.sort_order) # insertItem完了后，再把sort_index,sort_order设置回来
		self.selectRow(self.selected_row)

	def addRow(self, row:int, column_item_list:list):
		
		if len(column_item_list)>self.columnCount():
			raise("column_item_list out of bounds")
		
		self.insertRow(row)
		i=0
		for item in column_item_list:
			self.setItem(row,i,item)
			i+=1
	
	def findRowInColumn(self,):
		pass