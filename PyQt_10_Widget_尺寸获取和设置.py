from PyQt5.Qt import *

import sys

app = QApplication(sys.argv)

window = QWidget()  # 没有标注父类对象的窗口会被当做主窗口，
window.setWindowTitle("第一个窗口")

window.resize(500, 500)  # 用户区域窗口的大小，坐标系统的原点是在窗口的左上角
window.move(100, 100)  # 吧窗口移动到屏幕的位置
# window.setGeometry(0,0,500,500)    #同时设置用户区域的窗口位置和窗口大小
# window.adjustSize()     #根据里面的控件去自动匹配大小
# window.setFixedSize()   #设置固定大小

# 获取最大和最小的尺寸
print(window.minimumWidth())
print(window.minimumHeight())
print(window.minimumSize())

print(window.maximumWidth())
print(window.maximumHeight())
print(window.maximumSize())

# 设置最大和最小的尺寸
window.setMinimumWidth(100)
window.setMinimumHeight(100)
window.setMinimumSize(100, 100)

window.setMaximumWidth(500)
window.setMaximumHeight(500)
window.setMaximumSize(500, 500)

window.show()  # 主窗口需要主动调用一下

print(window.x())  # 打印屏幕右上角到窗口右上角x轴的距离
print(window.y())  # 打印屏幕右上角到窗口右上角y轴的距离
print(window.pos())  # 打印屏幕右上角到窗口右上角y轴和y轴的距离

print(window.width())  # 打印窗口宽度
print(window.height())  # 打印窗口高度
print(window.size())  # 打印窗口高度和宽度

print(window.geometry())  # 打印窗口用户区的位置和尺寸
print(window.rect())  # 打印窗口高度宽度和相对窗口的原点位置，父窗口的原点是0,0

print(window.frameGeometry())  # 打印窗口框架尺寸
print(window.frameSize())  # 打印窗口框架大小

sys.exit(app.exec_())
