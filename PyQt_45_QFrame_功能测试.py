from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("光标控制")
window.resize(500, 500)

frame = QFrame(window)  # QTextEdit的父级
frame.resize(100, 100)
frame.move(200, 200)
frame.setStyleSheet("background:red")

# 设置边框
# frame.setFrameShape(QFrame.Box)
# QFrame.NoFrame       #没效果
# QFrame.Box           #框
# QFrame.Panel         #面片
# QFrame.HLine         #垂直线
# QFrame.VLine         #水平线
# QFrame.StyledPanel   #取决于GUI样式表

# 设置阴影
# frame.setFrameShadow(QFrame.Raised)
# QFrame.Plain   #水平阴影
# QFrame.Raised  #凸起阴影
# QFrame.Sunken  #凹陷阴影

# 一起设置
frame.setFrameStyle(QFrame.Box | QFrame.Raised)

# 框架矩形，修改边框的外形
frame.setFrameRect(QRect(20, 20, 60, 60))

frame.setLineWidth(6)  # 设置边框线大小
frame.setMidLineWidth(12)  # 设置中间线大小

window.show()
sys.exit(app.exec_())
