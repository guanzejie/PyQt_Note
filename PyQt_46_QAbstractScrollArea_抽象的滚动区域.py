from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("光标控制")
window.resize(500, 500)

te = QTextEdit(window)
te.resize(100, 100)

te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 设置垂直滚动条
te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 设置水平滚动条
# Qt.ScrollBarAlwaysOff   #滚动条永久关闭
# Qt.ScrollBarAlwaysOn    #滚动条永久开启

bt = QPushButton(window)
te.setCornerWidget(bt)  # 边角处设置一个控件

window.show()
sys.exit(app.exec_())
