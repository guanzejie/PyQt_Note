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
        gl = QGridLayout()
        self.setLayout(gl)

        lb1 = QLabel("lable1")
        lb1.setStyleSheet("background-color:cyan")

        lb2 = QLabel("lable2")
        lb2.setStyleSheet("background-color:red")

        lb3 = QLabel("lable3")
        lb3.setStyleSheet("background-color:yellow")

        lb4 = QLabel("lable4")
        lb4.setStyleSheet("background-color:green")

        lb5 = QLabel("lable5")
        lb5.setStyleSheet("background-color:blue")

        gl.addWidget(lb1, 0, 0)  # 第0行第一列
        gl.addWidget(lb2, 0, 1)  # 第0行第二列
        gl.addWidget(lb3, 1, 0)  # 第1行第一列
        gl.addWidget(lb4, 1, 1)  # 第1行第二列
        gl.addWidget(lb5, 2, 0, 1, 2)  # 第2行一列的位置，并占有1行，和2列的内容

        lb6 = QLabel("lable6")
        lb6.setStyleSheet("background-color:yellow")

        lb7 = QLabel("lable6")
        lb7.setStyleSheet("background-color:green")

        lb8 = QLabel("lable5")
        lb8.setStyleSheet("background-color:red")

        layout1 = QBoxLayout(QBoxLayout.LeftToRight)
        layout1.addWidget(lb6)
        layout1.addWidget(lb7)
        layout1.addWidget(lb8)

        gl.addLayout(layout1, 3, 0, 1, 2)

        # 限制最小列宽和最小行高
        gl.setColumnMinimumWidth(0, 100)  # 那一列，最小多宽
        gl.setRowMinimumHeight(0, 100)  # 那一行，最小多高

        # 拉伸系数
        gl.setColumnStretch(0, 2)  # 第0列的宽度是3分2
        gl.setColumnStretch(1, 1)  # 第1列的宽度是3分1         2+1=3

        gl.setRowStretch(0, 2)  # 第0行为的高度度是6分2
        gl.setRowStretch(1, 1)  # 第0行为的高度度是6分1
        gl.setRowStretch(2, 1)  # 第0行为的高度度是6分1
        gl.setRowStretch(3, 2)  # 第0行为的高度度是6分2       2+1+1+2=6

        # 间距控制
        gl.setHorizontalSpacing(20)  # 垂直间距
        gl.setVerticalSpacing(30)  # 水平间距
        gl.setSpacing(30)
        print(gl.spacing())

        # 信息获取
        print(gl.rowCount())  # 获取多少行
        print(gl.columnCount())  # 获取多少列


window = Window()
window.show()
sys.exit(app.exec_())
