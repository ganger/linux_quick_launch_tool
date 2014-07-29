#-------------------------------------------------
#
# Project created by QtCreator 2014-07-11T20:23:20
#
#-------------------------------------------------

QT       += core gui
CONFIG	+=qxt
QXT	+= core gui
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = linux_quick_launch_tool
TEMPLATE = app


SOURCES += main.cpp\
    settingwindow.cpp \
    addwindow.cpp

HEADERS  += \
    settingwindow.h \
    addwindow.h \
    structs.h

FORMS    += \
    settingwindow.ui \
    addwindow.ui

RESOURCES += \
    png/png.qrc
