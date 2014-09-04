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

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from Xlib import X
from threading import Timer
from xutils import get_keyname, delete_selection
import commands
from read_conf import confList
class EventHandler(QObject):
    press_super = pyqtSignal()
    release_super = pyqtSignal()
    press_key1=pyqtSignal()
    press_key2=pyqtSignal()
    press_key3=pyqtSignal()
    show_window=pyqtSignal()
    close_window=pyqtSignal()
    def __init__(self):
        QObject.__init__(self)
       	self.superFlag=False
        self.windowFlag=False 
        self.superDelay=0.2
        self.timer=None
        # Delete selection first.
        delete_selection()
    def emit_show_window(self):
		self.show_window.emit()
		self.windowFlag=True
    @pyqtSlot("QVariant")    
    def handle_event(self, event):
        if self.timer and self.timer.is_alive():
            self.timer.cancel()
        if event.type == X.KeyPress:
            keyname = get_keyname(event)
            if keyname in ["Super_L"]:
				self.superFlag=True
				self.timer=Timer(self.superDelay,self.emit_show_window)
				self.timer.start()
	    for l in confList:
		if keyname ==l.key[0]:
		    if int(l.order)==1 and self.superFlag==True:
				self.press_key1.emit()
		    elif int(l.order)==2 and self.superFlag==True:
				self.press_key2.emit()
		    elif int(l.order)==3:
				self.press_key3.emit()
			
	elif event.type == X.KeyRelease:
            keyname = get_keyname(event)
	    if keyname in ["Super_L"]:
			self.superFlag=False
			if self.timer and self.timer.is_alive():
				self.timer.cancel()
			if self.windowFlag==True:
				self.close_window.emit()
