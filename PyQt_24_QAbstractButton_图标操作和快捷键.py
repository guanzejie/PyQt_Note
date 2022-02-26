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
but.pressed.connect(lambda: print("点击了"))
icon = QIcon("./logo.png")
but.setIcon(icon)  # 这是QAbstractButton的api,设置图标
size1 = QSize(50, 50)
but.setIconSize(size1)  # 这是QAbstractButton的api,设置图标大小

# but.setShortcut("alt+a") #是QAbstractButton的api，也可以通过这种方法设置快捷键


window.show()
sys.exit(app.exec_())
