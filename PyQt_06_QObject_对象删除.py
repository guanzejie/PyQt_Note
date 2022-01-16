from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)
class window(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.isQWidget()

    def isQWidget(self):

        obj1 = QObject()
        self.obj1 =obj1
        obj2 = QObject()

        obj2.setParent(obj1)

        obj3 = QObject()

        obj3.setParent(obj2)

        obj1.destroyed.connect(lambda: print("obj1断开了"))
        obj2.destroyed.connect(lambda: print("obj2断开了"))
        obj3.destroyed.connect(lambda: print("obj3断开了"))

        #del obj2  #只能删除了obj2这个对象，并不能断开引用的关系
        obj2.deleteLater()  #下一个循环的时候会先断开与父对象链接然后删除







win1=window()

win1.show()

sys.exit(app.exec())