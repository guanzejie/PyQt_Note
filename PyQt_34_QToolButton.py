
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("QToolButton")
window.resize(500,500)

but=QToolButton(window)
but.setText("autodesk")
icon=QIcon("./logo.png")
but.setIcon(QIcon(icon))
but.setIconSize(QSize(100,100))
but.setToolTip("autodesk")

but.setToolButtonStyle(Qt.ToolButtonIconOnly)  #设置标题显示的样式
#                      Qt.ToolButtonIconOnly
#                      Qt.ToolButtonTextBesideIcon
#                      Qt.ToolButtonTextOnly
#                      Qt.ToolButtonTextUnderIcon
#                      Qt.ToolButtonFollowStyle


but.setArrowType(Qt.UpArrow)      #默认的箭头图标
#                Qt.NoArrow 无箭头
#                Qt.UpArrow 上箭头
#                Qt.DownArrow 下箭头
#                Qt.LeftArrow  左箭头
#                Qt.RightArrow 右箭头

but.setAutoRaise(True)       #扁平化处理


menu=QMenu(but)
sub_m=QMenu(menu)
sub_m.setTitle("保存")

action1=QAction("打开",menu)

menu.addMenu(sub_m)
menu.addSeparator()
menu.addAction(action1)

but.setMenu(menu)
but.setPopupMode(QToolButton.DelayedPopup)    #设置菜单弹出模式
#                            MenuButtonPopup   有个专门箭头，点击箭头就出现
#                            DelayedPopup      鼠标点击停一会弹出
#                            InstantPopup      点击按钮立马显示 ，点击信号无效，信号是不会发生

but.triggered.connect(lambda action :print("点击了",action))   #连接模式

window.show()

#but.showMenu()                           #打开时打开菜单
sys.exit(app.exec_())