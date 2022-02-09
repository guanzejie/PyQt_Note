
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):

        lb1=QLabel("lable1")
        lb1.setStyleSheet("background-color:cyan")

        lb2=QLabel("lable2")
        lb2.setStyleSheet("background-color:red")

        lb3=QLabel("lable3")
        lb3.setStyleSheet("background-color:yellow")

        lb4=QLabel("lable4")
        lb4.setStyleSheet("background-color:green")

        #1创建布局管理器对象
        layout=QBoxLayout(QBoxLayout.TopToBottom)



        #2把对象设置给布局管理器的父控件
        self.setLayout(layout)


        # #3添加控件
        # layout.addWidget(lb1)
        # layout.addWidget(lb2)
        # layout.addWidget(lb3)


        #设置间距离
        layout.setSpacing(10)   #控件和控件之间的间距
        layout.setContentsMargins(30,30,30,30)   #设置控件和窗口之间的距离

        #替换子控件
        # layout.replaceWidget(lb1,lb4)   #lb4替换控件lb1   ，lb1就不会受到管理需要隐藏
        # lb1.hide() #隐藏控件
        # lb1.setParent(None)  #断开父子连接


        #布局的嵌套添加
        lb5=QLabel("lable5")
        lb5.setStyleSheet("background-color:red")

        lb6=QLabel("lable6")
        lb6.setStyleSheet("background-color:yellow")

        lb7=QLabel("lable6")
        lb7.setStyleSheet("background-color:green")

        layout1 = QBoxLayout(QBoxLayout.LeftToRight)
        layout1.addWidget(lb5)
        layout1.addWidget(lb6)
        layout1.addWidget(lb7)

        #添加layout控件
        layout.addWidget(lb1,1)            #          占地面值6/1
        #layout.addSpacing(50)             #添加一个空白
        layout.addStretch(1)               #添加一个弹簧占地面值6/1
        layout.addWidget(lb2,2)            #          占地面值6/2
        #layout.addLayout(layout1)         #添加layout控件
        layout.addWidget(lb3,2)            #          占地面值6/3


        # 设置布局类型
        layout.setDirection(QBoxLayout.RightToLeft)
        #layout.direction(QBoxLayout.LeftToRight)
        #layout.Direction(QBoxLayout.RightToLeft)
        #layout.Direction(QBoxLayout.TopToBottom)
        #layout.Direction(QBoxLayout.BottomToTop)

        #添加元素
        layout.insertWidget(1,lb3)      #插入控件到1的位置
        #layout.insertLayout(0,layout1)  #插入一个布局到0的位置

        #移除控件
        # layout.removeWidget(lb2)
        # lb2.setParent(None)
        #
        # lb1.hide()     #隐藏一个控件

        #插入空白
        #layout.insertSpacing(1,50)

        #更改弹簧
        layout.setStretchFactor(lb2,5)    #占地面值5/10



        #扩展
        #QHBoxLayout()     #等于QBoxLayout(QBoxLayout.LeftToRight)
        #QVBoxLayout()
        #








window=Window()
window.show()
sys.exit(app.exec_())