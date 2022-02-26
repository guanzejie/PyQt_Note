from PyQt5.Qt import *

import sys


class Myobject(QObject):

    def timerEvent(self, evt):  # 重写Object类下的timerEvent方法
        print(evt, "1")


app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("窗口")

window.resize(500, 500)

window.move(400, 400)

obj = Myobject()

time = obj.startTimer(1000)  # 开始一个时间定时器，单位是毫秒

obj.killTimer(time)  # 关闭一个时间定时器

window.show()
sys.exit(app.exec_())
