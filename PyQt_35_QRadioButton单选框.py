from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("hahahahah")
window.resize(500, 500)

but = QRadioButton(window)
but.setText("男")
but.move(0, 30)
but.setChecked(True)  # 默认选中

but1 = QRadioButton(window)
but1.setText("女")
but1.move(0, 60)
but1.toggled.connect(lambda isChecked: print(isChecked))  # 设置按钮切换时发出的型号

window.show()
sys.exit(app.exec_())
