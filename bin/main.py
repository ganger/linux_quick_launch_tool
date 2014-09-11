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

import os
import sys
from Xlib import display
import signal
import cPickle
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QUrl
from PyQt5.QtWidgets import QApplication, qApp
from PyQt5.QtQuick import QQuickView
from read_conf import confList, create_qml
from PyQt5 import Qt
from tray_icon import TrayIcon
from settingWindow import SettingWindow
if __name__=="__main__":
	app = QApplication(sys.argv)
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	view = QQuickView()
	view.setFlags(Qt.Qt.FramelessWindowHint)
	view.setOpacity(0.9)
	create_qml()
	t_icon=TrayIcon()
	sw=SettingWindow()
def show_window():
	path='screen.qml'
	view.engine().quit.connect(app.quit)
	view.setSource(QUrl(path))
	desktop=QApplication.desktop()
	x=(desktop.width()-1000)/2
#	x=300#here x=300 because desktop.width may got wrong value due to the bug of qt
	y=(desktop.height() - 100)/2
	view.setGeometry(x, y,1000,100)
	view.show()
def close_window():
	view.hide()
def key1_press():
	os.system(confList[0].command)
def key2_press():
	os.system(confList[1].command)
def key3_press():
	os.system(confList[2].command)
def key4_press():
	os.system(confList[3].command)
def key5_press():
	os.system(confList[4].command)
def key6_press():
	os.system(confList[5].command)
def key7_press():
	os.system(confList[6].command)
def key8_press():
	os.system(confList[7].command)
def key9_press():
	os.system(confList[8].command)
def key10_press():
	os.system(confList[9].command)
def quit():
	sys.exit(app.exec_())
def setting():
	sw.show()
	sw.finished.connect(setting_window_finish)
def setting_window_finish():
	create_qml()
from record_event import RecordEvent
from event_handler import EventHandler
event_handler = EventHandler()
##
event_handler.show_window.connect(show_window)
event_handler.close_window.connect(close_window)
event_handler.press_key1.connect(key1_press)
event_handler.press_key2.connect(key2_press)
event_handler.press_key3.connect(key3_press)
event_handler.press_key4.connect(key4_press)
event_handler.press_key5.connect(key5_press)
event_handler.press_key6.connect(key6_press)
event_handler.press_key7.connect(key7_press)
event_handler.press_key8.connect(key8_press)
event_handler.press_key9.connect(key9_press)
event_handler.press_key10.connect(key10_press)
t_icon.quit.connect(quit)
t_icon.settingSig.connect(setting)
##
record_event = RecordEvent()
record_event.capture_event.connect(event_handler.handle_event)
record_event.start()


sys.exit(app.exec_())
