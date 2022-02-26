from PyQt5.Qt import *

import sys

app = QApplication(sys.argv)

window = QWidget()  # 没有标注父类对象的窗口会被当做主窗口，
window.setWindowTitle("鼠标操作")

window.resize(500, 500)  # 用户区域窗口的大小，坐标系统的原点是在窗口的左上角
window.move(100, 100)  # 吧窗口移动到屏幕的位置

lable = QLabel(window)
lable.setText("我是文字哈哈哈哈")

lable.resize(300, 100)
lable.setStyleSheet("background-color:green;font-size:30px;")

window.setCursor(Qt.BusyCursor)  # 设置鼠标的形状
# Qt.ArrowCursor        普通箭头
# Qt.UpArrowCursor      向上箭头
# Qt.CrossCursor        截图
# Qt.IBeamCursor        拖选字符
# Qt.WaitCursor         等待
# Qt.BusyCursor         忙
# Qt.ForbiddenCursor    禁止
# Qt.PointingHandCursor 小手指
# Qt.WhatsThisCursor    问好
# Qt.SizeVerCursor      上下拖动大小
# Qt.SizeHorCursor      左右拖动大小
# Qt.SizeBDiagCursor    斜角拖动大小
# Qt.SizeAllCursor      缩放拖动大小
# Qt.SplitHCursor       左右分割
# Qt.SplitVCursor       上下分割
# Qt.OpenHandCursor     五指张开
# Qt.ClosedHandCursor   握拳
# Qt.BlankCursor        空白


# 自定义鼠标的形状
pixmap = QPixmap("./logo.png")  # 设置图标对象
scale_map = pixmap.scaled(20, 20)  # 缩放图片大小
cursor = QCursor(scale_map, 1, 1)  # 设置鼠标对象, 可不填（，1,1）设置图片点击中心位置
lable.setCursor(cursor)  # 设置鼠标

print(lable.cursor())  # 获取鼠标类别
loc = window.cursor()
print(loc.pos())  # 获取鼠标在屏幕的位置
loc.setPos(0, 0)  # 设置鼠标在屏幕的位置

lable.unsetCursor()  # 恢复默认鼠标
window.unsetCursor()  # 恢复默认鼠标

window.show()  # 主窗口需要主动调用一下

sys.exit(app.exec_())
