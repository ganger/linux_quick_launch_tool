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
confFile=open("conf","r")
count=1
confList=[]
order=1
for line in confFile:
	if count==2:
		arr1=line.split(" ")
		name=arr1[1]
	elif count==3:
		arr2=line.split(" ")
		command=arr2[1]
	elif count==4:
		arr3=line.split(" ")
		path=arr3[1]
		path=path.split("\n")[0]
	elif count==5:
		arr4=line.split(" ")
		key=arr4[1]
		key=key.split("\n")[0]
	count=count+1
	if count>5:
		count=1
		confList.append(d_struct(order,name,path,command,key))
		order=order+1
total=len(confList)
confFile.close()

def create_qml():
	qmlFile=open("screen.qml","w")
	qmlFile.write("import QtQuick 2\n")
	qmlFile.write('Image\n'+
		'{\nid:background\n'+
		'width: 1000\n'+
		'height: 600\n'+
		'source: "./png/screen.jpg"\n'
		'property int total:'+str(total)+'\n'+
		'property int r:0\n'+
		'Text\n'+
		'{\n'+
		'text:"press super+key to start the program"\n'+
		'anchors.centerIn: parent\n'+
		'color:"white"\n'+
		'font.pointSize: 15\n'+
		'}\n'+
		'Timer\n'+
		'{\n'+
		'id:timer\n'+
		'interval: 10\n'+
		'repeat: true\n'+
		'running:true\n'+
		'onTriggered:\n'+
		'{\n'+
		'background.r=background.r+10\n'+
		'if(background.r>=250)\n'+
		'{\n'+
		'timer.stop()\n'+
		'}\n'+
		'}\n'+
		'}\n')
	i=0
	while i<total:
		qmlFile.write('Image\n'+
			'{\n'+
			'width:50\n'+
			'height:50\n'+
			'x:parent.width/2-25+parent.r*Math.cos(degree)\n'+
			'y:parent.height/2-25+parent.r*Math.sin(degree)\n'+
			'source: "'+confList[i].path+'"\n'+
			'property int n:'+str(i)+'\n'+
			'property double degree: 2*Math.PI*n/parent.total\n'+
			'Rectangle\n'+
			'{\n'+
			'anchors.fill: parent\n'+
			'opacity: 0.6\n'+
			'color: "#000000"\n'+
			'Text\n'+
			'{\n'+
			'anchors.centerIn: parent\n'+
			'text:"'+confList[i].key+'"\n'+
			'color: "white"\n'+
			'font.pointSize: 40'+
			'}\n'+
			'}\n'+
			'}\n')
		i=i+1
	qmlFile.write("}\n")
	qmlFile.close()
