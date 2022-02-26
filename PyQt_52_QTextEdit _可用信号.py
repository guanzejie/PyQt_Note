from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("光标控制")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):
        self.te = QTextEdit(self)
        self.te.resize(300, 300)
        self.te.move(100, 100)
        self.te.setPlaceholderText("请输入....")  # 设置占位文本

        # 设置普通文本内容
        self.te.setPlainText("hahahahahahahahahah\nhahahah")  # 设置普通文本
        self.te.insertPlainText("bbbbbbbb")  # 插入文本

        # 自动判断
        self.te.setText("<h1> hahahahaha</h1>""aaaaaa")  # 自动判断是普通文本还是HTML文本

        # 追加文本
        self.te.append("guanguan")


window = Mywindow()
window.show()
sys.exit(app.exec_())
