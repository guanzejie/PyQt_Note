from PyQt5.Qt import *

import sys


app =QApplication(sys.argv)

window =QWidget()
window.setWindowTitle("父子关系")  #设置标题
window.setWindowFlags(Qt.FramelessWindowHint)  #去掉标题栏
window.resize(500,500)
window.move(400,400)

#设置窗口样式
icon=QIcon("./logo.png")     #创建图标对象
window.setWindowIcon(icon)   #设置图标
#print(window.windowIcon())
window.setWindowOpacity(1) #设置窗口半透明
#print(window.windowOpacity())



#设置窗口状态，最大化，最小化等
print(window.windowState()==Qt.WindowNoState)  #获取状态判断是否等于无状态
#Qt.WindowNoState    无状态
#Qt.WindowMinimized  最小化
#Qt.WindowMaximized  最大化
#Qt.WindowFullScreen 全屏
#Qt.WindowActive     激活窗口,窗口跑到最前面
#window.setWindowState(Qt.WindowMinimized)
#window.setWindowState(Qt.WindowMaximized)
#window.setWindowState(Qt.WindowFullScreen)
#window.setWindowState(Qt.WindowActive)



#展示窗口
window.showMaximized()  #最大化窗口
#window.showMinimized()  #最小化窗口
#window.showFullScreen() #全屏窗口
print(window.isMaximized())
print(window.isMinimized())
print(window.isFullScreen())


#窗口标志

#window.setWindowFlags(Qt.WindowStaysOnBottomHint)
window.setWindowFlags(Qt.FramelessWindowHint)  #设置为无顶层栏






window.show()
sys.exit(app.exec_())


