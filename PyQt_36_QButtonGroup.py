from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("hahahahah")
window.resize(500, 500)

but = QRadioButton(window)
but.setText("男")
but.move(0, 30)

but1 = QRadioButton(window)
but1.setText("女")
but1.move(0, 60)
but1.toggled.connect(lambda isChecked: print(isChecked))  # 设置按钮切换时发出的型号
but1.setChecked(True)  # 默认选中

human_group = QButtonGroup(window)  # 定义一个按钮组，按钮组是一个抽象类是不可见的
human_group.addButton(but, 0)  # 把需要的按键添加到按钮组里
human_group.addButton(but1, 1)

but2 = QRadioButton(window)
but2.setText("是")
but2.move(100, 30)

but3 = QRadioButton(window)
but3.setText("中")
but3.move(100, 60)

but4 = QRadioButton(window)
but4.setText("否")
but4.move(100, 90)
but3.setChecked(True)  # 默认选中

daan = QButtonGroup(window)
daan.addButton(but2)
daan.addButton(but3)
daan.addButton(but4)

daan.setId(but2, 1)  # 设置ID
daan.setId(but3, 2)
daan.setId(but4, 3)
print(daan.id(but2))  # 查看ID
print(daan.id(but3))
print(daan.id(but4))
print(daan.checkedId())  # 查看被选中按钮的ID

# daan.setExclusive(False) #设置组内的按钮为独占，不互斥


print(human_group.buttons())  # 查看组里的按钮
print(human_group.button(0))  # 查看组里id为0的按钮
print(human_group.checkedButton())  # 查看组里哪个按键被选中了


# daan.removeButton(but3)               #组里移除按钮


# 触发的可用信号
def test(val):
    print(val)


# daan.buttonToggled.connect(test)  #接收的是被切换按钮的信号
# daan.buttonClicked.connect(test)  #接收的是被点击按钮的信号,返回的是按钮的对象
daan.buttonClicked[int].connect(test)  # 接收的是被点击按钮的信号，返回的是按钮的ID

window.show()
sys.exit(app.exec_())
