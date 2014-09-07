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

from PyQt5 import QtGui
from PyQt5.QtWidgets import QSystemTrayIcon, QAction,QMenu
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, qApp,QDialog
import os
class TrayIcon(QSystemTrayIcon):
	quit=pyqtSignal()
	settingSig=pyqtSignal()
	def __init__(self):
		super(TrayIcon,self).__init__()
		self.setIcon(QIcon("./png/QL.png"))
		self.setToolTip("Linux Quick Lauch Tool")
		mainMenu=QMenu(QApplication.desktop())
		quitAction=QAction("&Quit ",self,triggered=self.close_pro)
		settingAction=QAction("setting",self,triggered=self.setting)
		mainMenu.addAction(quitAction)
		mainMenu.addAction(settingAction)
		self.setContextMenu(mainMenu)
		self.show()
	def close_pro(self):
		self.quit.emit()

	def setting(self):
		self.settingSig.emit()

