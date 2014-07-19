#ifndef SETTINGWINDOW_H
#define SETTINGWINDOW_H

#include <QWidget>
#include<QSystemTrayIcon>
#include<QIcon>
#include<QMenu>
#include<QAction>
namespace Ui {
class SettingWindow;
}

class SettingWindow : public QWidget
{
    Q_OBJECT
    
public:
    explicit SettingWindow(QWidget *parent = 0);
    ~SettingWindow();
    
private:
    Ui::SettingWindow *ui;
    QSystemTrayIcon *stIcon;
    QMenu *mainMenu;
public slots:
    void quit();
    void setting();
};

#endif // SETTINGWINDOW_H
