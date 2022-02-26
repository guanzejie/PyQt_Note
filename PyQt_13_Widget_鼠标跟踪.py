from PyQt5.Qt import *

import sys

app = QApplication(sys.argv)


class Mywindow(QWidget):
    def mouseMoveEvent(self, move):  # 重写鼠标移动事件
        # QMouseEvent                  #这个就是鼠标事件
        # QKeyEvent
        print(move.globalPos())  # 获得鼠标全局位置
        print(move.localPos())


window = Mywindow()
window.setWindowTitle("鼠标操作")

window.resize(500, 500)
window.move(100, 100)
window.setMouseTracking(True)  # 设置鼠标跟踪

window.show()

sys.exit(app.exec_())
