
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)
#————————————————————————————————————————————————————————————————————————————————————————————方法1
class Window(QWidget):
    def contextMenuEvent(self, evt):  #重写右键点击事件
        print("第一种方法")
        QContextMenuEvent
        but = QPushButton(QIcon("./logo.png"), "button", window)

        menu = QMenu()  # 设置一个菜单类
        op_action = QAction(menu)  # 创建一个菜单行为
        op_action.setText("open")
        op_action.setIcon(QIcon("./logo.png"))
        op_action.triggered.connect(lambda: print("打开"))  # 连接行为
        menu.addAction(op_action)  # 把行为添加到菜单上
        but.setMenu(menu)  # 把菜单设置到按钮上

        menu.exec_(evt.globalPos())   #把光标映射到整个屏幕的位置
window=Window()
window.setWindowTitle("hahahahah")
window.resize(500,500)



#————————————————————————————————————————————————————————————————————————————————————————————方法2

def youjian(point):
    print("第二种方法")
    print(window.mapToGlobal(point))     #把局部的鼠标位置信息映射到全局
    but = QPushButton(QIcon("./logo.png"), "button", window)

    menu = QMenu()  # 设置一个菜单类
    op_action = QAction(menu)  # 创建一个菜单行为
    op_action.setText("open")
    op_action.setIcon(QIcon("./logo.png"))
    op_action.triggered.connect(lambda: print("打开"))  # 连接行为
    menu.addAction(op_action)  # 把行为添加到菜单上
    but.setMenu(menu)  # 把菜单设置到按钮上
    menu.exec_(window.mapToGlobal(point))


window.setContextMenuPolicy(Qt.CustomContextMenu)  #第二种方法   ,自定义上下文菜单（定义右键菜单） 默认，如果有默认的重写的就不起作用
window.customContextMenuRequested.connect(youjian) #第二种方法   ,接收右键的信号

window.show()
sys.exit(app.exec_())