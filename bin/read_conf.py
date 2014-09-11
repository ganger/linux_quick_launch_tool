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

from structs import d_struct
import cPickle
confFile=open("conf","r")
confList=cPickle.load(confFile)
total=len(confList)
confFile.close()
import os
backgroundPath=os.path.dirname(__file__)
def create_qml():
	qmlFile=open("screen.qml","w")
	qmlFile.write("import QtQuick 2\n")
	qmlFile.write('Rectangle\n'+
		'{\nid:background\n'+
		'width: 1000\n'+
		'height: 100\n'+
		'color:"#1c1703"\n'+
		'property int total:'+str(total)+'\n'+
		'property int r:0\n')
	i=0
	while i<total:
		qmlFile.write('Image\n'+
			'{\n'+
			'width:80\n'+
			'height:80\n'+
			'x:1000/parent.total/2+n*1000/parent.total-40\n'+
			'y:10\n'+
			'source: "'+confList[i].path+'"\n'+
			'property int n:'+str(i)+'\n'+
			'Rectangle\n'+
			'{\n'+
			'anchors.centerIn: parent\n'+
			'width:30\n'+
			'height:30\n'+
			'color: "white"\n'+
			'opacity:0.8\n'+
			'radius:180\n'+
			'Rectangle\n'+
			'{\n'+
			'anchors.centerIn:parent\n'+
			'width:24\n'+
			'height:24\n'+
			'color:"black"\n'+
			'radius:180\n'
			'Text\n'+
			'{\n'+
			'anchors.centerIn: parent\n'+
			'text:"'+confList[i].key.upper()+'"\n'+
			'color: "white"\n'+
			'font.pointSize: 18'+
			'}\n'+
			'}\n'+
			'}\n'+
			'}\n')
		i=i+1
	qmlFile.write("}\n")
	qmlFile.close()
