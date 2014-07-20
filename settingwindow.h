#ifndef SETTINGWINDOW_H
#define SETTINGWINDOW_H

#include <QWidget>
#include<QSystemTrayIcon>
#include<QIcon>
#include<QMenu>
#include<QAction>
#include<QKeyEvent>
#include<QListView>
#include<QStandardItem>
#include<QStandardItemModel>
#include<QSize>
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
    QStandardItemModel *listModel;
public slots:
    void quit();
    void setting();
    void keyReleaseEvent(QKeyEvent *k);
};

#endif // SETTINGWINDOW_H
