#! /usr/bin/python
from PyQt5.QtWidgets import QApplication
from settingWindow import SettingWindow
import sys
app = QApplication( sys.argv )
sw = SettingWindow()
sw.show()
app.exec_()

