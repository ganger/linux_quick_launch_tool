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
#include<fstream>
#include"addwindow.h"
#include"structs.h"
#include<QList>
#include<QVBoxLayout>
#include<QDeclarativeComponent>
#include<QDeclarativeView>
#include<QDeclarativeContext>
using namespace std;
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
    QList<struct_items> itemList;
    QDeclarativeView *qmlView;
    QWidget *QMLWidget;
public slots:
    void quit();
    void setting();
    void fresh();
    void toggle();
private slots:
    void on_addButton_clicked();
    void on_okButton_clicked();
    void edit(QModelIndex index);
    void on_removeButton_clicked();
    void on_listView_doubleClicked(const QModelIndex &index);
};

#endif // SETTINGWINDOW_H
