from PyQt5.Qt import *

import sys

# 用户交互状态是指这哪个按钮是否可以点击或者哪个输入栏是否可以输入

app = QApplication(sys.argv)


class Mybutton(QPushButton):
    def paintEvent(self, env):
        print("画上了")
        return super().paintEvent(env)


window = QWidget()
window.setWindowFlags(Qt.WindowStaysOnTopHint)  # 在顶层
window.setWindowTitle("编辑[*]")  # 设置标题，如果用户调用了setWindowModified星号回被显示在标题栏
window.resize(500, 500)
window.move(400, 400)

bt = Mybutton(window)
bt.setText("按钮")
bt.pressed.connect(lambda: print("点击了"))

# bt.setEnabled(False)   #按钮设置为禁用状态
# print(bt.isEnabled())


# bt.setVisible(False)   #设置为不可见
# bt.setHidden(True)      #设置为不可见
# bt.hide()
print(bt.isVisible())  # 相对于父控件而言是否显示
print(bt.isHidden())  # 相对于父控件而言是否隐藏
print(bt.isVisibleTo(window))  # 如果window被显示的时候bt按钮是否被显示

bt.setAttribute(Qt.WA_DeleteOnClose, True)  # 当检测到bt.close()时关闭按钮并释放掉
bt.close()  # 关闭按钮但是不释放，相对于隐藏了但是不能再显示了

# 控件是否被编辑了
window.setWindowModified(True)
print(window.isWindowModified())

# 如果处于多个窗口同时显示状态判断窗口是否是被选中状态（活跃状态）
print(window.isActiveWindow())  # 判断窗口是否是激活状态

window.show()
sys.exit(app.exec_())
