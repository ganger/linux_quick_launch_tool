#ifndef ADDWINDOW_H
#define ADDWINDOW_H

#include <QWidget>
#include<QFileDialog>
#include<QString>
#include<fstream>
#include<QMessageBox>
using namespace std;
namespace Ui {
class AddWindow;
}

class AddWindow : public QWidget
{
    Q_OBJECT
    
public:
    explicit AddWindow(QWidget *parent = 0);
    ~AddWindow();
    void set_name(string name);
    void set_path(string path);
    void set_command(string command);
    void set_key(string key);
private slots:
    void on_selectButton_clicked();

    void on_okButton_clicked();

    void on_cancleButton_clicked();

signals:
    void w_close();
private:
    Ui::AddWindow *ui;
};

#endif // ADDWINDOW_H
