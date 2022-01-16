from PyQt5.Qt import *              #导入所有的类

import sys

#QApplication创建一个应用程序的对象，包括主事件循环，在其中来自窗口系统和其他资源的所有事件被处理和调度。
#                               #处理应用程序初始化和结束，并且提供对话管理。
#                               #处理绝大多数系统范围和应用程序的设置，如设置背景颜色等
app =QApplication(sys.argv)     #sys.argv代表这个程序可以在外部传递一个或多个参数。

window =QWidget()     #创建一个空的窗口控件   QPushButton()是按钮控件    QLable()标签控件
window.setWindowTitle("第一个窗口")   #在顶层控件里可以设置标题栏的文本
window.resize(500,500)
window.move(400,400)
window.setObjectName("aa")

lable=QLabel(window)   #创建一个QLable()标签非顶层控件，为window的子控件。
lable.setText("第一个窗口")
lable.move(210,250)

window.show()               #展示控件
sys.exit(app.exec_())       #app.exec_()相当于让代码处于消息循环 ，并监听用户的交互信息。
#sys.exit的作用是检测退出码，如果为0则是正常退出，1或-1为不正常退出。

