#! /usr/bin/python
# -*- coding: utf-8 -*-

# 
# Author:     Ganger <ganger695988290@gmail.com>
# Maintainer: Ganger <ganger695988290@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtWidgets import QWidget,QListView,QPushButton
from PyQt5.QtGui import QStandardItemModel,QStandardItem,QIcon
from PyQt5.QtCore import  pyqtSignal, pyqtSlot
from addWindow import AddWindow
import cPickle

class SettingWindow(QWidget):
#	on_addButtonClicked=pyqtSignal()
#	on_removeButtonClicked=pyqtSignal()
#	on_okButtonClicked=pyqtSignal()
	finished=pyqtSignal()
	def __init__(self):
		QWidget.__init__(self)
		self.listview=QListView(self)
		self.addButton=QPushButton(self)
		self.removeButton=QPushButton(self)
		self.resize(630,440)
		self.okButton=QPushButton(self)
		self.listview.setGeometry(30,30,410,351)
		self.addButton.setGeometry(490,40,80,22)
		self.addButton.setText("add")
		self.addButton.clicked.connect(self.click_add)
		self.removeButton.setGeometry(490,80,80,22)
		self.removeButton.setText("remove")
		self.removeButton.clicked.connect(self.click_remove)
		self.okButton.setGeometry(490,150,80,22)
		self.okButton.setText("ok")
		self.okButton.clicked.connect(self.click_ok)
#		self.aw=null


		self.fresh()
	def click_ok(self):
		self.finished.emit()
		self.close()
	def click_add(self):
		self.aw=AddWindow()
		self.aw.show()
		self.aw.okSig.connect(self.fresh)
	def click_remove(self):
		self.remove()
	def fresh(self):
		confFile=open("conf","r")
		self.listModel=QStandardItemModel()
		self.itemList=cPickle.load(confFile)
		confFile.close()
		for  item in self.itemList:
			itemView=QStandardItem(QIcon(item.path),item.name)
			itemView.setEditable(False)
			self.listModel.appendRow(itemView)
			self.listview.setModel(self.listModel)
	def remove(self):
		index=self.listview.currentIndex().row()
		self.itemList.pop(index)
		self.listModel.removeRow(index)
		confFile=open("conf","w")
		cPickle.dump(self.itemList,confFile)
		confFile.close()
