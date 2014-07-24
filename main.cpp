#include <QApplication>
#include"settingwindow.h"
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    SettingWindow sw;
  //  sw.show();
    return a.exec();
}
