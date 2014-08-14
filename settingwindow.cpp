#include "settingwindow.h"
#include "ui_settingwindow.h"
#include<QDebug>
#include<stdlib.h>
#include<QDeclarativeView>
SettingWindow::SettingWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SettingWindow)
{
    ui->setupUi(this);
    this->stIcon=new QSystemTrayIcon;
    this->stIcon->setIcon(QIcon(":/SystemTrayIcon/QL.png"));
    this->stIcon->setToolTip("Linux Quick Lauch Tool");
    this->mainMenu=new QMenu((QWidget*)QApplication::desktop());
    QAction *quitAction=new QAction("quit",this->mainMenu);
    QAction *settingAction=new QAction("setting",this->mainMenu);
    this->mainMenu->addAction(quitAction);
    this->mainMenu->addAction(settingAction);
    this->connect(quitAction,SIGNAL(triggered()),this,SLOT(quit()));
    this->connect(settingAction,SIGNAL(triggered()),this,SLOT(setting()));
    this->stIcon->setContextMenu(this->mainMenu);
    bool b=this->stIcon->isSystemTrayAvailable();
    qDebug()<<b;
    this->stIcon->show();
    this->fresh();
    QxtGlobalShortcut * sc = new QxtGlobalShortcut(QKeySequence("super+S"), this);
    connect(sc, SIGNAL(activated()),this, SLOT(toggle()));

}

SettingWindow::~SettingWindow()
{
    delete ui;
}

void SettingWindow::quit()
{
    this->stIcon->hide();
    this->close();
}

void SettingWindow::setting()
{

    ifstream confFileIn;
    confFileIn.open("conf",ios::in);
    string s;
    confFileIn>>s;
    qDebug()<<QString::fromLocal8Bit(s.c_str());
    confFileIn.close();

    this->show();
}


void SettingWindow::on_addButton_clicked()
{
    AddWindow *adw=new AddWindow;
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
    ifstream confFile;
    confFile.open("conf",ios::in);
   // listModel=new QStandardItemModel;
    QList<struct_items> itemlist;
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
        }
        itemlist.append(*item);
    }
    AddWindow aw;
    aw.set_name(itemlist.at(index.row()).name);
}

void SettingWindow::toggle()
{
    QDeclarativeView *qmlView = new QDeclarativeView;
    qmlView->setSource(QUrl("./png/screen.qml"));
    QWidget *widget =new QWidget();
    QVBoxLayout *layout = new QVBoxLayout(widget);
    layout->addWidget(qmlView);
    widget->show();
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
    }
    outfile.close();

}
