from PyQt5.Qt import *

import sys

app = QApplication(sys.argv)

window = QWidget()  # 没有标注父类对象的窗口会被当做主窗口，
window.setWindowTitle("第一个窗口")

window.resize(500, 500)  # 用户区域窗口的大小，坐标系统的原点是在窗口的左上角
window.move(100, 100)  # 吧窗口移动到屏幕的位置

lable = QLabel(window)
lable.setText("我是文字哈哈哈哈")
lable.resize(300, 300)
lable.setStyleSheet("background-color:green;font-size:30px;")

lable.setContentsMargins(100, 200, 0, 0)  # 设置lable的显示区域
print(lable.contentsRect())  # 获取lable的显示区域    #PyQt5.QtCore.QRect(0, 0, 300, 300)

window.show()  # 主窗口需要主动调用一下

sys.exit(app.exec_())
