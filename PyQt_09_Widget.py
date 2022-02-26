from PyQt5.Qt import *

import sys

app = QApplication(sys.argv)

window = QWidget()  # 没有标注父类对象的窗口会被当做主窗口，
window.setWindowTitle("第一个窗口")
window.resize(500, 500)  # 坐标系统的原点是在窗口的左上角

red = QWidget(window)  # 标注有window父类对象的窗口会被当做子窗口，不需要主动调用
red.resize(100, 100)
red.setStyleSheet("background-color:red")

window.show()  # 主窗口需要主动调用一下
sys.exit(app.exec_())
