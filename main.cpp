#include <QApplication>
#include"settingwindow.h"
#include"addwindow.h"
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
  //  SettingWindow sw;
  //  sw.show();
    AddWindow ad;
    ad.show();
    return a.exec();
}
