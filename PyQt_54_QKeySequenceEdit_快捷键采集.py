from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("清空按钮")
window.resize(500, 500)
le = QKeySequenceEdit(window)
le.move(100, 100)

# 快捷键的设置
# qks=QKeySequence("ctrl+.")          #设置快捷键
qks = QKeySequence(QKeySequence.Copy)  # 设置快捷键
le.setKeySequence(qks)

but = QPushButton(window)
but.setText("按钮")
but.pressed.connect(lambda: print(le.keySequence().toString()))

# 发射的信号
le.editingFinished.connect(lambda: print("结束编辑"))
le.keySequenceChanged.connect(lambda key: print("快捷键变了", key.toString()))

window.show()
sys.exit(app.exec_())
