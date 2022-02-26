from PyQt5.Qt import *

import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("父子关系")
window.resize(500, 500)
window.move(400, 400)

lable1 = QLabel(window)
lable1.resize(50, 70)
lable1.setText("标签1")
lable1.setStyleSheet("background-color:red")

lable2 = QLabel(window)
lable2.setText("标签2")
lable2.resize(50, 70)
lable2.move(25, 50)
lable2.setStyleSheet("background-color:blur")

lable3 = QLabel(window)
lable3.setText("标签3")
lable3.resize(50, 70)
lable3.move(50, 100)
lable3.setStyleSheet("background-color:green")

lable3.lower()  # 把lable3放下一层
lable1.raise_()  # 把lable1放上一层
lable1.stackUnder(lable3)  # 把lable1放到lable3上面

window.show()
sys.exit(app.exec_())
