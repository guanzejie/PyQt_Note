from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("清空按钮")
window.resize(500, 500)

le = QLineEdit(window)  # 单行文本输入
le.setText("bb")

le1 = QLineEdit(window)  # 单行文本输入
le1.setText("bbasdasdfasdf")
le1.move(0, 50)

# 输入限制
le.setMaxLength(50)  # 最大长度
print(le.maxLength())

le1.setReadOnly(False)  # 设置只读模式
print(le1.isReadOnly())

# 输入规则


window.show()
sys.exit(app.exec_())
