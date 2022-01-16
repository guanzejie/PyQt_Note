
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("hahahahah")
window.resize(500,500)

but=QPushButton(QIcon("./logo.png"),"button",window)

but1=QPushButton(QIcon("./logo.png"),"button1",window)
but1.move(0,60)
but1.pressed.connect(lambda :print("默认按钮"))

#but1.setAutoDefault(True)      #设置默认按钮，选择了之后就会高亮显示，用enter和空格键可以控制
print(but1.autoDefault())

but1.setDefault(True)          #设置默认按钮，用enter和空格键可以控制
print(but1.isDefault())









window.show()

#but.showMenu()                           #打开时打开菜单
sys.exit(app.exec_())