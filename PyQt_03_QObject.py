from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("面向对象")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject_test1()
        # elf.QObject_test()
        # self.Qobject_fuzi()

    def QObject_test1(self):
        subcla = QObject.__subclasses__()  # 查看QObject的所有子类
        mros = QObject.mro()  # 查看QObject的所有父类
        bases = QObject.__bases__  # 查看Object当前的父类

        print(subcla)
        print(bases)
        print(mros)

    # 属性设置和名称设置
    def QObject_test(self):
        # 设置名称
        obj = QObject()
        obj.setObjectName("newName")  # 设置QObject名称，这是一个唯一的名称，可以当做对象的ID
        print(obj.objectName())  # 获取QObject的名称

        # 设置属性
        obj.setProperty("attrName", "attrValue")  # 设置QObject属性
        obj.setProperty("attrName1", "attrValue2")
        print(obj.property("attrName"))  # 获取QObject属性的值

        print(obj.dynamicPropertyNames())  # 动态获取所有设置的属性的名称

    # QObject父子关系
    def Qobject_fuzi(self):
        obj1 = QObject()
        obj2 = QObject()
        obj2.setObjectName("2")
        obj3 = QObject()
        obj3.setObjectName("3")
        obj2.setParent(obj1)  # 设置obj2的父物体为obj1，就是说obj1是obj2他爹
        obj3.setParent(obj1)
        print(obj2.parent())  # 打印一下obj2他爹
        print(obj1.children())  # 打印一下obj1的直接儿子   应该有两一个是obj2和obj3
        print(obj1.findChild(QObject))  # 随机找一下obj1的儿子  ，找到第一个就停止
        print(obj1.findChild(QObject, "3", Qt.FindChildrenRecursively))  # 递归查找ObjectName=3的儿子，第三个参数可不写，默认是递归
        print(obj1.findChild(QObject, "2", Qt.FindDirectChildrenOnly))  # 只找ObjectName=2的直接儿子

    def QObject_neichun(self):
        pass  # 父控件被释放子控件也会被释放 ，用于把最外的窗口关闭子窗口也会自动关闭


def fuziguanxi():
    win1 = QWidget()
    win1.resize(600, 600)

    win1.show()

    win2 = QWidget()

    win2.setParent(win1)  # 设置为父子关系之后在win1关闭的时候Win2也会关闭这一句相当于win2 = QWidget(win1)

    win2.setStyleSheet("background-color:red;")

    win2.resize(300, 300)

    win2.move(200, 200)

    win2.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    window = Window()

    window.show()

    # fuziguanxi()

    sys.exit(app.exec_())
