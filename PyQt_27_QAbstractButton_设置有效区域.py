#QAbstractButton  是一个抽象类，时所有的button按钮类的父类
#QAbstractButton  抽象类时不可以直接被使用必须要新建一个子类取继承它
#QAbstractButton  新建的子类必须要重写paintEvent方法


from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("hahahahah")
window.resize(500,500)

class But(QPushButton):
    def hitButton(self, point):  #重写点击的有效区域
        print(point)
        if(point.x()>self.width()/2):
            return True   #响应按钮点击，发送信号给but.pressed.connect函数
        else:
            return False  #不会响应按钮点击，but.pressed.connect函数收不到点击信号

but = But(window)
but.setText("a&b按钮")
but.resize(100,40)
but.pressed.connect(lambda :print("点击了1"))
but.setCheckable(True)    #设置按钮可以被选中


window.show()
sys.exit(app.exec_())