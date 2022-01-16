from PyQt5.Qt import *

import sys


app =QApplication(sys.argv)

window =QWidget()
window.setWindowTitle("父子关系")
window.resize(500,500)
window.move(400,400)

lable1=QLabel(window)
lable1.resize(50,70)
lable1.setText("标签1")
lable1.setStyleSheet("background-color:red")


lable2=QLabel(window)
lable2.setText("标签2")
lable2.resize(50,70)
lable2.move(25,50)
lable2.setStyleSheet("background-color:blur")


lable3=QLabel(window)
lable3.setText("标签3")
lable3.resize(50,70)
lable3.move(50,100)
lable3.setStyleSheet("background-color:green")


print(window.childAt(0,50)) #查看窗口坐标（0，,50）这个位置上有没有window对象的子控件
print(lable3.parentWidget()) #查看lable3的父控件
print(window.childrenRect()) #查看所有子控件在窗口里的bbox



window.show()
sys.exit(app.exec_())


