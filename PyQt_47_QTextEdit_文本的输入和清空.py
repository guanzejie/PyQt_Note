
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)

class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("光标控制")
        self.resize(500,500)
        self.setupUi()

    def setupUi(self):
        te=QTextEdit(self)
        te.resize(300,300)
        te.move(100,100)
        te.setPlaceholderText("请输入....")  #设置占位文本

        #设置普通文本内容
        te.setPlainText("hahahahahahahahahah\nhahahah")   #设置普通文本
        te.insertPlainText("bbbbbbbb")                    #插入文本
        print(te.toPlainText())                           #获取文本内容

        #HTML文本设置
        te.setHtml("<h3> hahahahaha</h3>")
        te.insertHtml("<h1> wewewewewewewe</h1>")
        print(te.toHtml())

        # 自动判断
        te.setText("<h1> hahahahaha</h1>""aaaaaa")       #自动判断是普通文本还是HTML文本

        #追加文本
        te.append("guanguan")


        #清空文本
        but=QPushButton(self)
        but.setText("按钮")
        but.pressed.connect(lambda : te.clear())#清空文本内容


window=Mywindow()
window.show()
sys.exit(app.exec_())