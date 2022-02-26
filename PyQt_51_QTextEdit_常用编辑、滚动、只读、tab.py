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

        but = QPushButton(self)
        but.setText("常用编辑")
        but.pressed.connect(self.bianji)

        but1 = QPushButton(self)
        but1.setText("滚动")
        but1.pressed.connect(self.gundong)
        but1.move(80, 0)

        but2 = QPushButton(self)
        but2.setText("只读")
        but2.pressed.connect(self.zhidu)
        but2.move(160, 0)

        but3 = QPushButton(self)
        but3.setText("读写")
        but3.pressed.connect(self.duxie)
        but3.move(240, 0)

        but4 = QPushButton(self)
        but4.setText("tab控制")
        but4.pressed.connect(self.tabkongzhi)
        but4.move(320, 0)

    def tabkongzhi(self):
        # self.te.setTabChangesFocus(True)  #设置tab键只能改变焦点
        self.te.setTabStopDistance(8)  # 设置按下tab键出现多少像素空格
        self.te.setTabStopWidth(8)  # 设置按下tab键出现多少像素空格
        print(self.te.tabStopDistance())
        print(self.te.tabStopWidth())

    def zhidu(self):
        self.te.setReadOnly(True)

    def duxie(self):
        self.te.setReadOnly(False)

    def bianji(self):
        self.te.copy()
        self.te.paste()
        self.te.canPaste(True)
        self.te.setUndoRedoEnabled(True)
        self.te.redo()
        self.te.undo()
        self.te.selectAll()

    def gundong(self):
        self.te.scrollToAnchor("aa")


window = Mywindow()
window.show()
sys.exit(app.exec_())
