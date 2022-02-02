
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("hahahahah")
window.resize(500,500)

but=QPushButton(QIcon("./logo.png"),"button",window)


menu=QMenu()                               #设置一个菜单类
op_action=QAction(menu)                       #创建一个菜单行为
op_action.setText("open")
op_action.setIcon(QIcon("./logo.png"))
op_action.triggered.connect(lambda :print("打开"))  #连接行为

ex_action=QAction("exit",menu)
ex_action.triggered.connect(lambda :sys.exit())  #连接行为


save_menu=QMenu()                             #设置一个菜单
save_menu.setTitle("保存")                     #添加提示

save_action=QAction("save",menu)
save_action.triggered.connect(lambda :print("save"))  #连接行为

save_menu.addAction(save_action)             #把行为添加到子菜单上


menu.addAction(op_action)                     #把行为添加到菜单上
menu.addMenu(save_menu)                       #添加一个菜单
menu.addSeparator()                           #添加分割线
menu.addAction(ex_action)

but.setMenu(menu)                          #把菜单设置到按钮上

print(but.isFlat())
but.setFlat(True)              #不显示边框和背景颜色

window.show()

#but.showMenu()                           #打开时打开菜单
sys.exit(app.exec_())