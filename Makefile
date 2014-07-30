#############################################################################
# Makefile for building: linux_quick_launch_tool
# Generated by qmake (2.01a) (Qt 4.8.4) on: Wed Jul 30 19:48:00 2014
# Project:  linux_quick_launch_tool.pro
# Template: app
# Command: /usr/bin/qmake-qt4 -o Makefile linux_quick_launch_tool.pro
#############################################################################

####### Compiler, tools and options

CC            = gcc
CXX           = g++
DEFINES       = -DQT_NO_DEBUG -DQT_GUI_LIB -DQT_CORE_LIB -DQT_SHARED
CFLAGS        = -pipe -O2 -Wall -W -D_REENTRANT $(DEFINES)
CXXFLAGS      = -pipe -O2 -Wall -W -D_REENTRANT $(DEFINES)
INCPATH       = -I/usr/share/qt4/mkspecs/linux-g++ -I. -I/usr/include/qt4/QtCore -I/usr/include/qt4/QtGui -I/usr/include/qt4 -I. -I.
LINK          = g++
LFLAGS        = -Wl,-O1
LIBS          = $(SUBLIBS)  -L/usr/lib/i386-linux-gnu -lQtGui -lQtCore -lpthread 
AR            = ar cqs
RANLIB        = 
QMAKE         = /usr/bin/qmake-qt4
TAR           = tar -cf
COMPRESS      = gzip -9f
COPY          = cp -f
SED           = sed
COPY_FILE     = $(COPY)
COPY_DIR      = $(COPY) -r
STRIP         = strip
INSTALL_FILE  = install -m 644 -p
INSTALL_DIR   = $(COPY_DIR)
INSTALL_PROGRAM = install -m 755 -p
DEL_FILE      = rm -f
SYMLINK       = ln -f -s
DEL_DIR       = rmdir
MOVE          = mv -f
CHK_DIR_EXISTS= test -d
MKDIR         = mkdir -p

####### Output directory

OBJECTS_DIR   = ./

####### Files

SOURCES       = main.cpp \
		settingwindow.cpp \
		addwindow.cpp moc_settingwindow.cpp \
		moc_addwindow.cpp \
		qrc_png.cpp
OBJECTS       = main.o \
		settingwindow.o \
		addwindow.o \
		moc_settingwindow.o \
		moc_addwindow.o \
		qrc_png.o
DIST          = /usr/share/qt4/mkspecs/common/unix.conf \
		/usr/share/qt4/mkspecs/common/linux.conf \
		/usr/share/qt4/mkspecs/common/gcc-base.conf \
		/usr/share/qt4/mkspecs/common/gcc-base-unix.conf \
		/usr/share/qt4/mkspecs/common/g++-base.conf \
		/usr/share/qt4/mkspecs/common/g++-unix.conf \
		/usr/share/qt4/mkspecs/qconfig.pri \
		/usr/share/qt4/mkspecs/features/qt_functions.prf \
		/usr/share/qt4/mkspecs/features/qt_config.prf \
		/usr/share/qt4/mkspecs/features/exclusive_builds.prf \
		/usr/share/qt4/mkspecs/features/default_pre.prf \
		/usr/share/qt4/mkspecs/features/release.prf \
		/usr/share/qt4/mkspecs/features/default_post.prf \
		/usr/share/qt4/mkspecs/features/unix/gdb_dwarf_index.prf \
		/usr/share/qt4/mkspecs/features/warn_on.prf \
		/usr/share/qt4/mkspecs/features/qt.prf \
		/usr/share/qt4/mkspecs/features/unix/thread.prf \
		/usr/share/qt4/mkspecs/features/moc.prf \
		/usr/share/qt4/mkspecs/features/resources.prf \
		/usr/share/qt4/mkspecs/features/uic.prf \
		/usr/share/qt4/mkspecs/features/yacc.prf \
		/usr/share/qt4/mkspecs/features/lex.prf \
		/usr/share/qt4/mkspecs/features/include_source_dir.prf \
		linux_quick_launch_tool.pro
QMAKE_TARGET  = linux_quick_launch_tool
DESTDIR       = 
TARGET        = linux_quick_launch_tool

first: all
####### Implicit rules

.SUFFIXES: .o .c .cpp .cc .cxx .C

.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o "$@" "$<"

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o "$@" "$<"

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o "$@" "$<"

.C.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o "$@" "$<"

.c.o:
	$(CC) -c $(CFLAGS) $(INCPATH) -o "$@" "$<"

####### Build rules

all: Makefile $(TARGET)

$(TARGET): ui_settingwindow.h ui_addwindow.h $(OBJECTS)  
	$(LINK) $(LFLAGS) -o $(TARGET) $(OBJECTS) $(OBJCOMP) $(LIBS)

Makefile: linux_quick_launch_tool.pro  /usr/share/qt4/mkspecs/linux-g++/qmake.conf /usr/share/qt4/mkspecs/common/unix.conf \
		/usr/share/qt4/mkspecs/common/linux.conf \
		/usr/share/qt4/mkspecs/common/gcc-base.conf \
		/usr/share/qt4/mkspecs/common/gcc-base-unix.conf \
		/usr/share/qt4/mkspecs/common/g++-base.conf \
		/usr/share/qt4/mkspecs/common/g++-unix.conf \
		/usr/share/qt4/mkspecs/qconfig.pri \
		/usr/share/qt4/mkspecs/features/qt_functions.prf \
		/usr/share/qt4/mkspecs/features/qt_config.prf \
		/usr/share/qt4/mkspecs/features/exclusive_builds.prf \
		/usr/share/qt4/mkspecs/features/default_pre.prf \
		/usr/share/qt4/mkspecs/features/release.prf \
		/usr/share/qt4/mkspecs/features/default_post.prf \
		/usr/share/qt4/mkspecs/features/unix/gdb_dwarf_index.prf \
		/usr/share/qt4/mkspecs/features/warn_on.prf \
		/usr/share/qt4/mkspecs/features/qt.prf \
		/usr/share/qt4/mkspecs/features/unix/thread.prf \
		/usr/share/qt4/mkspecs/features/moc.prf \
		/usr/share/qt4/mkspecs/features/resources.prf \
		/usr/share/qt4/mkspecs/features/uic.prf \
		/usr/share/qt4/mkspecs/features/yacc.prf \
		/usr/share/qt4/mkspecs/features/lex.prf \
		/usr/share/qt4/mkspecs/features/include_source_dir.prf \
		/usr/lib/i386-linux-gnu/libQtGui.prl \
		/usr/lib/i386-linux-gnu/libQtCore.prl
	$(QMAKE) -o Makefile linux_quick_launch_tool.pro
/usr/share/qt4/mkspecs/common/unix.conf:
/usr/share/qt4/mkspecs/common/linux.conf:
/usr/share/qt4/mkspecs/common/gcc-base.conf:
/usr/share/qt4/mkspecs/common/gcc-base-unix.conf:
/usr/share/qt4/mkspecs/common/g++-base.conf:
/usr/share/qt4/mkspecs/common/g++-unix.conf:
/usr/share/qt4/mkspecs/qconfig.pri:
/usr/share/qt4/mkspecs/features/qt_functions.prf:
/usr/share/qt4/mkspecs/features/qt_config.prf:
/usr/share/qt4/mkspecs/features/exclusive_builds.prf:
/usr/share/qt4/mkspecs/features/default_pre.prf:
/usr/share/qt4/mkspecs/features/release.prf:
/usr/share/qt4/mkspecs/features/default_post.prf:
/usr/share/qt4/mkspecs/features/unix/gdb_dwarf_index.prf:
/usr/share/qt4/mkspecs/features/warn_on.prf:
/usr/share/qt4/mkspecs/features/qt.prf:
/usr/share/qt4/mkspecs/features/unix/thread.prf:
/usr/share/qt4/mkspecs/features/moc.prf:
/usr/share/qt4/mkspecs/features/resources.prf:
/usr/share/qt4/mkspecs/features/uic.prf:
/usr/share/qt4/mkspecs/features/yacc.prf:
/usr/share/qt4/mkspecs/features/lex.prf:
/usr/share/qt4/mkspecs/features/include_source_dir.prf:
/usr/lib/i386-linux-gnu/libQtGui.prl:
/usr/lib/i386-linux-gnu/libQtCore.prl:
qmake:  FORCE
	@$(QMAKE) -o Makefile linux_quick_launch_tool.pro

dist: 
	@$(CHK_DIR_EXISTS) .tmp/linux_quick_launch_tool1.0.0 || $(MKDIR) .tmp/linux_quick_launch_tool1.0.0 
	$(COPY_FILE) --parents $(SOURCES) $(DIST) .tmp/linux_quick_launch_tool1.0.0/ && $(COPY_FILE) --parents settingwindow.h addwindow.h structs.h .tmp/linux_quick_launch_tool1.0.0/ && $(COPY_FILE) --parents png/png.qrc .tmp/linux_quick_launch_tool1.0.0/ && $(COPY_FILE) --parents main.cpp settingwindow.cpp addwindow.cpp .tmp/linux_quick_launch_tool1.0.0/ && $(COPY_FILE) --parents settingwindow.ui addwindow.ui .tmp/linux_quick_launch_tool1.0.0/ && (cd `dirname .tmp/linux_quick_launch_tool1.0.0` && $(TAR) linux_quick_launch_tool1.0.0.tar linux_quick_launch_tool1.0.0 && $(COMPRESS) linux_quick_launch_tool1.0.0.tar) && $(MOVE) `dirname .tmp/linux_quick_launch_tool1.0.0`/linux_quick_launch_tool1.0.0.tar.gz . && $(DEL_FILE) -r .tmp/linux_quick_launch_tool1.0.0


clean:compiler_clean 
	-$(DEL_FILE) $(OBJECTS)
	-$(DEL_FILE) *~ core *.core


####### Sub-libraries

distclean: clean
	-$(DEL_FILE) $(TARGET) 
	-$(DEL_FILE) Makefile


check: first

mocclean: compiler_moc_header_clean compiler_moc_source_clean

mocables: compiler_moc_header_make_all compiler_moc_source_make_all

compiler_moc_header_make_all: moc_settingwindow.cpp moc_addwindow.cpp
compiler_moc_header_clean:
	-$(DEL_FILE) moc_settingwindow.cpp moc_addwindow.cpp
moc_settingwindow.cpp: addwindow.h \
		structs.h \
		settingwindow.h
	/usr/lib/i386-linux-gnu/qt4/bin/moc $(DEFINES) $(INCPATH) settingwindow.h -o moc_settingwindow.cpp

moc_addwindow.cpp: addwindow.h
	/usr/lib/i386-linux-gnu/qt4/bin/moc $(DEFINES) $(INCPATH) addwindow.h -o moc_addwindow.cpp

compiler_rcc_make_all: qrc_png.cpp
compiler_rcc_clean:
	-$(DEL_FILE) qrc_png.cpp
qrc_png.cpp: png/png.qrc \
		png/QL.png
	/usr/lib/i386-linux-gnu/qt4/bin/rcc -name png png/png.qrc -o qrc_png.cpp

compiler_image_collection_make_all: qmake_image_collection.cpp
compiler_image_collection_clean:
	-$(DEL_FILE) qmake_image_collection.cpp
compiler_moc_source_make_all:
compiler_moc_source_clean:
compiler_uic_make_all: ui_settingwindow.h ui_addwindow.h
compiler_uic_clean:
	-$(DEL_FILE) ui_settingwindow.h ui_addwindow.h
ui_settingwindow.h: settingwindow.ui
	/usr/lib/i386-linux-gnu/qt4/bin/uic settingwindow.ui -o ui_settingwindow.h

ui_addwindow.h: addwindow.ui
	/usr/lib/i386-linux-gnu/qt4/bin/uic addwindow.ui -o ui_addwindow.h

compiler_yacc_decl_make_all:
compiler_yacc_decl_clean:
compiler_yacc_impl_make_all:
compiler_yacc_impl_clean:
compiler_lex_make_all:
compiler_lex_clean:
compiler_clean: compiler_moc_header_clean compiler_rcc_clean compiler_uic_clean 

####### Compile

main.o: main.cpp settingwindow.h \
		addwindow.h \
		structs.h
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o main.o main.cpp

settingwindow.o: settingwindow.cpp settingwindow.h \
		addwindow.h \
		structs.h \
		ui_settingwindow.h
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o settingwindow.o settingwindow.cpp

addwindow.o: addwindow.cpp addwindow.h \
		ui_addwindow.h
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o addwindow.o addwindow.cpp

moc_settingwindow.o: moc_settingwindow.cpp 
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o moc_settingwindow.o moc_settingwindow.cpp

moc_addwindow.o: moc_addwindow.cpp 
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o moc_addwindow.o moc_addwindow.cpp

qrc_png.o: qrc_png.cpp 
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o qrc_png.o qrc_png.cpp

####### Install

install:   FORCE

uninstall:   FORCE

FORCE:

