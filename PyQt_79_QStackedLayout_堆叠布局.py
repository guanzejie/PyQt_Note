
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):

        sl=QStackedLayout()
        self.setLayout(sl)

        lb1=QLabel("lable1")
        lb1.setStyleSheet("background-color:cyan")

        lb2=QLabel("lable2")
        lb2.setStyleSheet("background-color:red")

        lb3=QLabel("lable3")
        lb3.setStyleSheet("background-color:yellow")

        lb4=QLabel("lable4")
        lb4.setStyleSheet("background-color:green")

        lb5=QLabel("lable5")
        lb5.setStyleSheet("background-color:blue")


        lb6=QLabel("lable6")
        lb6.setStyleSheet("background-color:yellow")

        lb7=QLabel("lable6")
        lb7.setStyleSheet("background-color:green")

        lb8=QLabel("lable5")
        lb8.setStyleSheet("background-color:red")



        print(sl.addWidget(lb1))
        print(sl.addWidget(lb2))
        print(sl.addWidget(lb4))
        print(sl.insertWidget(0,lb3))

        #切换子控件
        sl.setCurrentIndex(0)      #索引值切换法
        #sl.setCurrentWidget(lb2)   #控件名切换法

        #展示模式
        sl.setStackingMode(QStackedLayout.StackAll)   #展示所有
        #sl.setStackingMode(QStackedLayout.StackOne)  # 展示当前一个

        #信号
        sl.currentChanged.connect(lambda index_: print("当前展示控件变了",index_))
        sl.widgetRemoved.connect(lambda index_: print("控件被删除",index_))









window=Window()
window.show()
sys.exit(app.exec_())