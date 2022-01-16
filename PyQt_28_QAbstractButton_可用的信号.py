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
        #print(point)

        return True   #响应按钮点击，发送信号给but.pressed.connect函数


but = But(window)
but.setText("a&b按钮")
but.resize(100,40)
but.setCheckable(True)    #设置按钮可以被选中

#but.pressed.connect(lambda :print("按下了"))      #按钮按下的信号
#but.released.connect(lambda :print("松开了"))     #按钮松开的

#but.clicked.connect(lambda :print("按下又松开了")) #按钮再有效区域呢按下和松开才会触发
#but.clicked.connect(lambda value :print("按下又松开了",value)) #clicked函数可以放回一个值，这个值是检测按钮是否别选中

but.toggled.connect(lambda: print("选中状态发生了改变")) #如果选中的时候被点击了会取消选中，如果没选中状态点击会选中
but.toggled.connect(lambda value :print("选中状态发生了改变",value))  #这个值是检测按钮是否别选中




window.show()
sys.exit(app.exec_())