from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

class windows(QWidget):

    def __init__(self):
        super().__init__()

        self.windowTitleChanged.connect(lambda biaoti: print("文字改变了", + biaoti))

        self.setWindowTitle("这是个测试")

        self.resize(500, 500)
        self.setup_ui()
        #self.test_del()
        #self.test_change()


    def setup_ui(self):

        button=QPushButton(self)
        button.setText("点击打印")
        button.resize(100,30)

        button.clicked.connect(lambda : print("点击成功"))

    #对象被销毁时信号接收
    def test_del(self):

        self.obj1 = QObject()

        self.obj1.destroyed.connect(lambda obj: print("被释放了",obj))  #建立连接，检查obj1是否已经释放销毁了

        del self.obj1

    #对象被改变时型号的接收
    def test_change(self):

        self.obj2=QObject()

        self.obj2.objectNameChanged.connect(lambda: print("obj2名字被改变")) #建立连接，监听对象名字有没有被改变

        self.obj2.setObjectName("obj2")

        print(self.obj2.signalsBlocked(), 1)   #检测是否是链接状态，如果是链接状态放回False   否则放回True

        #self.obj2.objectNameChanged.disconnect()  # 断开对obj2的连接，不在进行监听
        self.obj2.blockSignals(True)  # 临时进行链接

        self.obj2.setObjectName("obj222")
        print(self.obj2.signalsBlocked(), 2)

        self.obj2.blockSignals(False)    #临时关闭链接

        self.obj2.setObjectName("obj222222")

        print(self.obj2.signalsBlocked(), 2)


        #检查对象链接了几个槽，有几个connect
        self.obj2.objectNameChanged.connect(lambda: print("obj2名字被改变"))
        self.obj2.objectNameChanged.connect(lambda: print("obj2名字被改变"))
        self.obj2.objectNameChanged.connect(lambda: print("obj2名字被改变"))

        print(self.obj2.receivers(self.obj2.objectNameChanged)) #检查函数




win1=windows()
win1.show()

sys.exit(app.exec_())