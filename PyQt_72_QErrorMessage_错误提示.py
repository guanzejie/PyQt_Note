from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):
        but = QPushButton(self)
        but.setText("按钮")

        em = QErrorMessage()  # 是一个顶级的临时窗口
        em.setWindowTitle("错误提示")
        em.showMessage("中华人民共和国万岁")

        # but.clicked.connect(lambda : em.show())
        # but.clicked.connect(lambda: em.open())
        but.clicked.connect(lambda: em.exec_())


window = Window()
window.show()
sys.exit(app.exec_())
