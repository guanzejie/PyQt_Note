from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("光标控制")
window.resize(500, 500)

le = QLineEdit(window)  # 单行文本输入
le.setText("")
le.move(200, 200)
le.textEdited.connect(lambda val: print("文本框编辑信号", val))
le.textChanged.connect(lambda val: print("文本框编辑信号", val))
le.returnPressed.connect(lambda: print("按回车发出的信号"))
le.editingFinished.connect(lambda: print("结束编辑发出的信号"))
le.cursorPositionChanged.connect(lambda old_pos, new_pos: print("光标位置改变发出的信号", old_pos, new_pos))
le.selectionChanged.connect(lambda: print("选择改变发出的信号", ))

bt = QPushButton(window)
bt.setText("按钮")


def chufa():
    le.setFocus()


window.show()
sys.exit(app.exec_())
