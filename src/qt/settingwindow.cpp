#include "settingwindow.h"
#include "ui_settingwindow.h"
#include<QDebug>
#include<stdlib.h>
#include <QDesktopWidget>
#include <QRect>
#include<QtGui>
SettingWindow::SettingWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SettingWindow)
{
    ui->setupUi(this);
    this->fresh();
    this->rawToRemove=-1;

}

SettingWindow::~SettingWindow()
{
    delete ui;
}






void SettingWindow::on_addButton_clicked()
{
    AddWindow *adw=new AddWindow;
    adw->set_sum(itemList.length());
    adw->show();
    this->connect(adw,SIGNAL(w_close()),this,SLOT(fresh()));

}

void SettingWindow::fresh()
{
    system("touch conf");
    ifstream confFile;
    confFile.open("conf",ios::in);
    listModel=new QStandardItemModel;
    itemList.clear();
    while(!confFile.eof())
    {
        string tmpstr;

        struct_items *item=new struct_items;
        confFile>>tmpstr;
        if("###"==tmpstr)
        {
            confFile>>tmpstr;
            confFile>>item->name;
            confFile>>tmpstr;
            confFile>>item->command;
            confFile>>tmpstr;
            confFile>>item->path;
            confFile>>tmpstr;
            confFile>>item->key;
        }
        if(item->path!="")
        {
            itemList.append(*item);
            QStandardItem *itemview=new QStandardItem(QIcon(\
            QString::fromLocal8Bit(item->path.c_str())),QString::fromLocal8Bit(item->name.c_str()));
            itemview->setEditable(false);
            listModel->appendRow(itemview);
            ui->listView->setModel(listModel);
        }
    }
}

void SettingWindow::on_okButton_clicked()
{

    this->close();
}

void SettingWindow::edit(QModelIndex index)
{

    AddWindow *aw=new AddWindow;
    aw->set_sum(itemList.length());
    aw->editmod();
    aw->show();
    aw->set_name(itemList.at(index.row()).name);
    aw->set_command(itemList.at(index.row()).command);
    aw->set_path(itemList.at(index.row()).path);
    aw->set_key(itemList.at(index.row()).key);
    this->rawToRemove=index.row();
    this->connect(aw,SIGNAL(w_close()),this,SLOT(fresh()));
    this->connect(aw,SIGNAL(edit_finish()),this,SLOT(remove_raw()));
}

void SettingWindow::remove_raw()
{
    itemList.removeAt(rawToRemove);
    listModel->removeRow(rawToRemove);
    ofstream outfile;
    outfile.open("conf",ios::out);
    int i;
    for(i=0;i<itemList.length();i++)
    {
        outfile<<"###"<<endl;
        outfile<<"[name] "<<itemList.at(i).name<<endl;
        outfile<<"[command] "<<itemList.at(i).command<<endl;
        outfile<<"[icon_path] "<<itemList.at(i).path<<endl;
        outfile<<"[key] "<<itemList.at(i).key<<endl;
    }

    outfile.close();
}

void SettingWindow::on_removeButton_clicked()
{
    int index=ui->listView->currentIndex().row();
    itemList.removeAt(index);
    listModel->removeRow(index);
    ofstream outfile;
    outfile.open("conf",ios::out);
    int i;
    for(i=0;i<itemList.length();i++)
    {
        outfile<<"###"<<endl;
        outfile<<"[name] "<<itemList.at(i).name<<endl;
        outfile<<"[command] "<<itemList.at(i).command<<endl;
        outfile<<"[icon_path] "<<itemList.at(i).path<<endl;
        outfile<<"[key] "<<itemList.at(i).key<<endl;
    }

    outfile.close();

}

void SettingWindow::on_listView_doubleClicked(const QModelIndex &index)
{
    this->edit(index);
}
