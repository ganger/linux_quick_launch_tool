#include "addwindow.h"
#include "ui_addwindow.h"
#include<QDebug>
AddWindow::AddWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::AddWindow)
{
    ui->setupUi(this);
    ui->iconText->setReadOnly(true);
    this->isEdit=false;

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
    qDebug()<<this->sumOfItems;
    QString keyText=ui->keyText->text();
    if(keyText.length()==1&&((keyText[0]>47&&keyText[0]<58)||(keyText[0]>64&&keyText[0]<91)||(keyText[0]>96&&keyText[0]<123)))
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
            confFile<<"[command] "<<ui->commandText->text().toStdString()<<endl;
            confFile<<"[icon_path] "<<ui->iconText->text().toStdString()<<endl;
            confFile<<"[key] "<<ui->keyText->text().toStdString()<<endl;
            confFile.close();
            emit w_close();
            if(true==this->isEdit)
            {
                emit edit_finish();
            }
            this->close();

        }

    }
    else
    {

        QMessageBox msgBox;
        msgBox.setText("the length of hot key must be 1 and value must be 0-9 or a-z");
        msgBox.exec();

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


void AddWindow::set_command(string command)
{

    ui->commandText->setText(QString::fromLocal8Bit(command.c_str()));
}

void AddWindow::set_key(string key)
{

    ui->keyText->setText(QString::fromLocal8Bit(key.c_str()));
}

void AddWindow::set_sum(int sum)
{
    this->sumOfItems=sum;
}
void AddWindow::editmod()
{
    this->isEdit=true;
}
