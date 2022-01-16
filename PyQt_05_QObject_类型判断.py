from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)
class window(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.isQWidget()
        self.xiaoanli()

    def isQWidget(self):

        a=QObject()
        b=QWidget()
        c=QPushButton()

        list_obj = [a, b, c]

        for i in list_obj:

            #print(i.isWidgetType())#判断是否为QWidget类型的对象
            print(i.inherits("QWidget"))  #判断这个对象的父类是否是QWidget

    def xiaoanli(self):

        label1=QLabel(self)
        label1.setText("我是 label1")

        label2=QLabel(self)
        label2.setText("我是 label2")
        label2.move(0,30)

        button1=QPushButton(self)
        button1.setText("按钮1")
        button1.move(0,60)

        button2=QPushButton(self)
        button2.setText("按钮2")
        button2.move(0,90)

        for i in self.children():

            if(i.inherits("QLabel")):

                 i.setStyleSheet("background-color:cyan")




win1=window()

win1.show()

sys.exit(app.exec())