import QtQuick 2
Rectangle
{
id:background
width: 1000
height: 100
color: Qt.rgba(0, 0, 0, 0.6)
radius: 6
property int total:9
property int r:0
Image
{
width:80
height:80
x:1000/parent.total/2+n*1000/parent.total-40
y:10
source: "png/freemind.png"
property int n:0
Rectangle
{
anchors.centerIn: parent
width:30
height:30
color: "white"
opacity:0.8
radius:180
Rectangle
{
anchors.centerIn:parent
width:24
height:24
color:"black"
radius:180
Text
{
anchors.centerIn: parent
text:"R"
color: "white"
font.pointSize: 18}
}
}
}
Image
{
width:80
height:80
x:1000/parent.total/2+n*1000/parent.total-40
y:10
source: "png/fetion.png"
property int n:1
Rectangle
{
anchors.centerIn: parent
width:30
height:30
color: "white"
opacity:0.8
radius:180
Rectangle
{
anchors.centerIn:parent
width:24
height:24
color:"black"
radius:180
Text
{
anchors.centerIn: parent
text:"O"
color: "white"
font.pointSize: 18}
}
}
}
Image
{
width:80
height:80
x:1000/parent.total/2+n*1000/parent.total-40
y:10
source: "png/firefox.png"
property int n:2
Rectangle
{
anchors.centerIn: parent
width:30
height:30
color: "white"
opacity:0.8
radius:180
Rectangle
{
anchors.centerIn:parent
width:24
height:24
color:"black"
radius:180
Text
{
anchors.centerIn: parent
text:"F"
color: "white"
font.pointSize: 18}
}
}
}
Image
{
width:80
height:80
x:1000/parent.total/2+n*1000/parent.total-40
y:10
source: "png/qt.png"
property int n:3
Rectangle
{
anchors.centerIn: parent
width:30
height:30
color: "white"
opacity:0.8
radius:180
Rectangle
{
anchors.centerIn:parent
width:24
height:24
color:"black"
radius:180
Text
{
anchors.centerIn: parent
text:"Q"
color: "white"
font.pointSize: 18}
}
}
}
Image
{
width:80
height:80
x:1000/parent.total/2+n*1000/parent.total-40
y:10
source: "png/eclipse.png"
property int n:4
Rectangle
{
anchors.centerIn: parent
width:30
height:30
color: "white"
opacity:0.8
radius:180
Rectangle
{
anchors.centerIn:parent
width:24
height:24
color:"black"
radius:180
Text
{
anchors.centerIn: parent
text:"E"
color: "white"
font.pointSize: 18}
}
}
}
Image
{
width:80
height:80
x:1000/parent.total/2+n*1000/parent.total-40
y:10
source: "png/gimp.png"
property int n:5
Rectangle
{
anchors.centerIn: parent
width:30
height:30
color: "white"
opacity:0.8
radius:180
Rectangle
{
anchors.centerIn:parent
width:24
height:24
color:"black"
radius:180
Text
{
anchors.centerIn: parent
text:"G"
color: "white"
font.pointSize: 18}
}
}
}
Image
{
width:80
height:80
x:1000/parent.total/2+n*1000/parent.total-40
y:10
source: "png/chrome.png"
property int n:6
Rectangle
{
anchors.centerIn: parent
width:30
height:30
color: "white"
opacity:0.8
radius:180
Rectangle
{
anchors.centerIn:parent
width:24
height:24
color:"black"
radius:180
Text
{
anchors.centerIn: parent
text:"C"
color: "white"
font.pointSize: 18}
}
}
}
Image
{
width:80
height:80
x:1000/parent.total/2+n*1000/parent.total-40
y:10
source: "png/libreoffice.png"
property int n:7
Rectangle
{
anchors.centerIn: parent
width:30
height:30
color: "white"
opacity:0.8
radius:180
Rectangle
{
anchors.centerIn:parent
width:24
height:24
color:"black"
radius:180
Text
{
anchors.centerIn: parent
text:"L"
color: "white"
font.pointSize: 18}
}
}
}
Image
{
width:80
height:80
x:1000/parent.total/2+n*1000/parent.total-40
y:10
source: "png/blender.png"
property int n:8
Rectangle
{
anchors.centerIn: parent
width:30
height:30
color: "white"
opacity:0.8
radius:180
Rectangle
{
anchors.centerIn:parent
width:24
height:24
color:"black"
radius:180
Text
{
anchors.centerIn: parent
text:"B"
color: "white"
font.pointSize: 18}
}
}
}
}
