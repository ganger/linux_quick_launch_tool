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
    QStandardItemModel *listModel;
    QList<struct_items> itemList;
    QWidget *QMLWidget;
    int rawToRemove;
public slots:
    void fresh();
private slots:
    void on_addButton_clicked();
    void on_okButton_clicked();
    void edit(QModelIndex index);
    void on_removeButton_clicked();
    void on_listView_doubleClicked(const QModelIndex &index);
    void remove_raw();
};

#endif // SETTINGWINDOW_H
