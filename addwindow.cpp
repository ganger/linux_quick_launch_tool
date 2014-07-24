#include "addwindow.h"
#include "ui_addwindow.h"
#include<QDebug>
AddWindow::AddWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::AddWindow)
{
    ui->setupUi(this);
    ui->iconText->setReadOnly(true);
}

AddWindow::~AddWindow()
{
    delete ui;
}

void AddWindow::on_selectButton_clicked()
{
    QString filePath=QFileDialog::getOpenFileName(this,\
          tr("Open Image"), "./png", tr("Image Files (*.png *.jpg *.bmp)"));
  //  qDebug()<<filePath;
    ui->iconText->setText(filePath);


}

void AddWindow::on_okButton_clicked()
{

    if(ui->nameText->text().isEmpty()||ui->commandText->text().isEmpty()||ui->iconText->text().isEmpty())
    {
        QMessageBox msgBox;
        msgBox.setText("name command and icon cannot be null");
        msgBox.exec();
    }else
    {
        ofstream confFile;
        confFile.open("conf",ios::app);
        confFile<<"###"<<endl;
        confFile<<"[name] "<<ui->nameText->text().toStdString()<<endl;
        confFile<<"[command]  "<<ui->commandText->text().toStdString()<<endl;
        confFile<<"[icon_path]    "<<ui->iconText->text().toStdString()<<endl;
        confFile.close();
        emit w_close();
        this->close();

    }

}

void AddWindow::on_cancleButton_clicked()
{
    this->close();
}

void AddWindow::set_name(string name)
{
    ui->nameText->setText(QString::fromLocal8Bit(name.c_str()));
}

void AddWindow::set_path(string path)
{

    ui->iconText->setText(QString::fromLocal8Bit(path.c_str()));
}
