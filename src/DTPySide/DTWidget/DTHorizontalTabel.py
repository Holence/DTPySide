from __future__ import annotations
from DTPySide import *

class DTHorizontalTabel(QTableWidget):

	sortReset=Signal()
	
	def __init__(self, parent):
		super().__init__(parent=parent)

		self.sort_times=0
		
		# 不知道为什么self.setSortingEnabled(True)在手动排序时会吞字
		# 下面这样设置一下就没问题……
		header = self.horizontalHeader()
		header.setSortIndicatorShown(True)
		header.sectionClicked.connect(self.sort)
		
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
	
	def	sort(self,sort_index):
		self.selected_index=[]
		self.clearSelection()

		if self.sort_times==0:
			self.horizontalHeader().setSortIndicator(sort_index,Qt.AscendingOrder)
			self.sortItems(sort_index,Qt.AscendingOrder)
			self.sort_times+=1
		elif self.sort_times==1:
			self.horizontalHeader().setSortIndicator(sort_index,Qt.DescendingOrder)
			self.sortItems(sort_index,Qt.DescendingOrder)
			self.sort_times+=1
		elif self.sort_times==2:
			self.horizontalHeader().setSortIndicator(-1,Qt.AscendingOrder)
			self.sortItems(-1,Qt.AscendingOrder)
			self.sort_times=0
			self.sortReset.emit()
	
	def dropEvent(self, event:QDropEvent):
		
		if not event.isAccepted() and event.source() == self:
			drop_row = self.drop_on(event)

			rows = sorted(set(item.row() for item in self.selectedItems()))
			rows_to_move = [[QTableWidgetItem(self.item(row_index, column_index)) for column_index in range(self.columnCount())]
							for row_index in rows]
			for row_index in reversed(rows):
				self.removeRow(row_index)
				if row_index < drop_row:
					drop_row -= 1

			for row_index, data in enumerate(rows_to_move):
				row_index += drop_row
				self.insertRow(row_index)
				for column_index, column_data in enumerate(data):
					self.setItem(row_index, column_index, column_data)
			event.accept()

			for row_index in range(len(rows_to_move)):   # maybe can be done smarter
				for col in range(self.columnCount()):
					self.item(drop_row + row_index, col).setSelected(True)
		
	def drop_on(self, event):
		index = self.indexAt(event.pos())
		if not index.isValid():
			return self.rowCount()
		return index.row() + 1 if self.is_below(event.pos(), index) else index.row()

	def is_below(self, pos, index):
		rect = self.visualRect(index)
		margin = 2
		if pos.y() - rect.top() < margin:
			return False
		elif rect.bottom() - pos.y() < margin:
			return True
		# noinspection PyTypeChecker
		return rect.contains(pos, True) and not (int(self.model().flags(index)) & Qt.ItemIsDropEnabled) and pos.y() >= rect.center().y()

	def setColumn(self,column_list:list):
		self.setColumnCount(len(column_list))
		self.setHorizontalHeaderLabels(column_list)
	
	def StoreTableStatus(self):
		self.sort_index=self.horizontalHeader().sortIndicatorSection()
		self.sort_order=self.horizontalHeader().sortIndicatorOrder()
		
		self.selected_index=self.selectedIndexes()
		self.scrollbarValue=self.verticalScrollBar().value()
	
	def Clear(self):
		self.clearContents()
		self.setRowCount(0)
		self.horizontalHeader().setSortIndicator(-1,Qt.SortOrder.AscendingOrder) #因为如果有排序的话，再insertItem会有疏漏，所以提前取消排序

	def RestoreTableStatus(self):
		# restore sorting
		
		self.horizontalHeader().setSortIndicator(self.sort_index,self.sort_order)
		self.sortItems(self.sort_index,self.sort_order)
		
		# restore selection
		for index in self.selected_index:
			self.selectionModel().select(index,QItemSelectionModel.Select | QItemSelectionModel.Rows)
		
		# restore scrollbar
		self.verticalScrollBar().setValue(self.scrollbarValue)

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