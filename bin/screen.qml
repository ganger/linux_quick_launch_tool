import QtQuick 2
Image
{
id:background
width: 1000
height: 600
source:"/home/ganger/project/linux_quick_launch_tool/bin/png/screen.jpg"
property int total:4
property int r:0
Text
{
text:"press super+key to start the program"
anchors.centerIn: parent
color:"white"
font.pointSize: 15
}
Timer
{
id:timer
interval: 10
repeat: true
running:true
onTriggered:
{
background.r=background.r+10
if(background.r>=250)
{
timer.stop()
}
}
}
Image
{
width:50
height:50
x:parent.width/2-25+parent.r*Math.cos(degree)
y:parent.height/2-25+parent.r*Math.sin(degree)
source: "/home/ganger/project/linux_quick_launch_tool/bin/png/firefox.png"
property int n:0
property double degree: 2*Math.PI*n/parent.total
Rectangle
{
anchors.fill: parent
opacity: 0.6
color: "#000000"
Text
{
anchors.centerIn: parent
text:"F"
color: "white"
font.pointSize: 40}
}
}
Image
{
width:50
height:50
x:parent.width/2-25+parent.r*Math.cos(degree)
y:parent.height/2-25+parent.r*Math.sin(degree)
source: "/home/ganger/project/linux_quick_launch_tool/bin/png/qt.png"
property int n:1
property double degree: 2*Math.PI*n/parent.total
Rectangle
{
anchors.fill: parent
opacity: 0.6
color: "#000000"
Text
{
anchors.centerIn: parent
text:"Q"
color: "white"
font.pointSize: 40}
}
}
Image
{
width:50
height:50
x:parent.width/2-25+parent.r*Math.cos(degree)
y:parent.height/2-25+parent.r*Math.sin(degree)
source: "/home/ganger/project/linux_quick_launch_tool/bin/png/freemind.png"
property int n:2
property double degree: 2*Math.PI*n/parent.total
Rectangle
{
anchors.fill: parent
opacity: 0.6
color: "#000000"
Text
{
anchors.centerIn: parent
text:"R"
color: "white"
font.pointSize: 40}
}
}
Image
{
width:50
height:50
x:parent.width/2-25+parent.r*Math.cos(degree)
y:parent.height/2-25+parent.r*Math.sin(degree)
source: "/home/ganger/project/linux_quick_launch_tool/bin/png/eclipse.png"
property int n:3
property double degree: 2*Math.PI*n/parent.total
Rectangle
{
anchors.fill: parent
opacity: 0.6
color: "#000000"
Text
{
anchors.centerIn: parent
text:"E"
color: "white"
font.pointSize: 40}
}
}
}
