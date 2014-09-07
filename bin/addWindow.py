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

from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QLabel,QFileDialog,QMessageBox
import cPickle
from PyQt5.QtCore import pyqtSignal

from structs import d_struct
class AddWindow(QWidget):
	okSig=pyqtSignal()
	def __init__(self):
		QWidget.__init__(self)
		self.resize(480,350)
		self.nameText=QLineEdit(self)
		self.nameText.setGeometry(110,30,240,30)
		self.commandText=QLineEdit(self)
		self.commandText.setGeometry(110,90,240,30)
		self.iconText=QLineEdit(self)
		self.iconText.setGeometry(110,150,240,30)
		self.iconText.setReadOnly(True)
		self.keyText=QLineEdit(self)
		self.keyText.setGeometry(180,200,120,30)
		is_edit=False
		self.nameLabel=QLabel(self)
		self.nameLabel.setText("name:")
		self.nameLabel.setGeometry(30,40,65,20)
		self.commandLabel=QLabel(self)
		self.commandLabel.setText("command:")
		self.commandLabel.setGeometry(30,90,65,20)
		self.pathLabel=QLabel(self)
		self.pathLabel.setText("icon path:")
		self.pathLabel.setGeometry(30,150,65,20)
		self.keyLabel=QLabel(self)
		self.keyLabel.setText("hot key:     super+")
		self.keyLabel.setGeometry(30,200,160,20)
		self.okButton=QPushButton(self)
		self.okButton.setText("ok")
		self.okButton.clicked.connect(self.on_ok_clicked)
		self.okButton.setGeometry(50,280,100,30)
		self.cancelButton=QPushButton(self)
		self.cancelButton.setText("cancel")
		self.cancelButton.setGeometry(310,280,100,30)
		self.cancelButton.clicked.connect(self.on_cancel_clicked)
		self.selectButton=QPushButton(self)
		self.selectButton.setText("select icon")
		self.selectButton.setGeometry(360,150,100,30)
		self.selectButton.clicked.connect(self.on_select_clicked)
	def on_ok_clicked(self):
		key=self.keyText.text()
		if(len(key)==1 and (key.islower() or key.isupper() or key.isdigit())):
			name=self.nameText.text()
			command=self.commandText.text()
			path=self.iconText.text()
			if(len(name)<1 or len(command)<1 or len(path)<1):	
				msgBox=QMessageBox()
				msgBox.setText("name command and icon cannot be nul")
				msgBox.exec_()
			else:
				readFile=open("conf","r")
				objs=cPickle.load(readFile)
				readFile.close()
				order=len(objs)+1
				obj=d_struct(order,name,path,command,key)
				objs.append(obj)
				writeFile=open("conf","w")
				cPickle.dump(objs,writeFile)
				writeFile.close()
				self.okSig.emit()
				self.close()
		else:
			msgBox=QMessageBox()
			msgBox.setText("the length of hot key must be 1 and value must be 0-9 or a-z")
			msgBox.exec_()
	def on_cancel_clicked(self):
		self.close()
	def on_select_clicked(self):
		filepath=QFileDialog.getOpenFileName(self,"Open Image", "./png", "Image Files (*.png *.jpg *.bmp)")
		self.iconText.setText(filepath[0])





