from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("交互学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        lable = QLabel(self)
        lable.setText("标签")

        le = QLineEdit(self)
        le.move(0, 50)

        bt = QPushButton(self)
        bt.setText("按键")
        bt.move(0, 100)
        bt.setEnabled(False)

        le.textChanged.connect(lambda: bt.setEnabled(True))

        bt.pressed.connect(lambda: print(le.text()))


if __name__ == "__main__":
    window = Window()

    window.show()

    sys.exit(app.exec_())
