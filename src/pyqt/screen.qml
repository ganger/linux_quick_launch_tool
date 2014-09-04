import QtQuick 2
Image
{
id:background
width: 1000
height: 600
source: "./png/screen.jpg"
property int total:0
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
}
