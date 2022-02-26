# QAbstractButton  是一个抽象类，时所有的button按钮类的父类
# QAbstractButton  抽象类时不可以直接被使用必须要新建一个子类取继承它
# QAbstractButton  新建的子类必须要重写paintEvent方法


from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("hahahahah")
window.resize(500, 500)

but = QPushButton(window)
but.setText("a&b按钮")  # 这是QAbstractButton的api，并设置快捷键为alt+b   （&b）
but.resize(100, 40)
but.pressed.connect(lambda: print("点击了1"))
but.setCheckable(True)  # 设置按钮可以被选中

but1 = QPushButton(window)
but1.setText("&ab按钮")  # 这是QAbstractButton的api，并设置快捷键为alt+a   （&a）
but1.resize(100, 40)
but1.move(0, 60)
but1.pressed.connect(lambda: print("点击了2"))
but1.setCheckable(True)  # 设置按钮可以被选中

but2 = QPushButton(window)
but2.setText("&ab按钮")  # 这是QAbstractButton的api，并设置快捷键为alt+a   （&a）
but2.resize(100, 40)
but2.move(0, 120)
but2.pressed.connect(lambda: print("点击了3"))
but2.setCheckable(True)  # 设置按钮可以被选中

# 排他性是指，几个按钮中只能选一个，例如”男“和“女”两选项只能选一个
print(but.autoExclusive())  # 查看当前按钮的排他性
print(but1.autoExclusive())  # 查看当前按钮的排他性
print(but2.autoExclusive())  # 查看当前按钮的排他性
but.setAutoExclusive(True)  # 设置排他性
but1.setAutoExclusive(True)  # 设置排他性
but2.setAutoExclusive(True)  # 设置排他性

but.click()  # 模拟用户按了一下按钮
but1.animateClick(2000)  # 模拟用户按了一下按钮2秒之后再松开

window.show()
sys.exit(app.exec_())
