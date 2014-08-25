import QtQuick 1.1

Image
{
    width: 1000
    height: 800
    source:"screen.jpg"
    property string source1: png

    Image
    {
        width:500
        height:500
        source: parent.source1
    }

}
