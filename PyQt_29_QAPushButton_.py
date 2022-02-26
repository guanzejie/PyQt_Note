from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("hahahahah")
window.resize(500, 500)

but = QPushButton(window)
but.setText("button")

but1 = QPushButton("button", window)
but1.move(0, 60)

but2 = QPushButton(QIcon("./logo.png"), "button", window)
but2.move(0, 120)

window.show()
sys.exit(app.exec_())
