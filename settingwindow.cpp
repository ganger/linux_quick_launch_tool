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
    this->stIcon->show();
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
    this->show();
}
