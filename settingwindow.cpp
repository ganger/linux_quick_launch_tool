#include "settingwindow.h"
#include "ui_settingwindow.h"
#include<QDebug>
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
    this->setFocus();
    this->stIcon->show();
    this->show();
    this->setVisible(false);
    QStandardItem *item=new QStandardItem(QIcon(":/SystemTrayIcon/QL.png"),"test");
    QStandardItem *item1=new QStandardItem(QIcon(":/SystemTrayIcon/QL.png"),"test");
    listModel=new QStandardItemModel;
    listModel->appendRow(item);
    listModel->appendRow(item1);
    ui->listView->setFixedSize(400,300);
    ui->listView->setGridSize(QSize(200,20));
    ui->listView->setModel(listModel);

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
    this->setVisible(true);
}

void SettingWindow::keyReleaseEvent(QKeyEvent *k)
{
    if(k->key()==Qt::Key_Super_L)
        qDebug()<<"pressed";
    else
        qDebug()<<"err";
    if(k->key()==Qt::Key_0)
        qDebug()<<"0";
}
