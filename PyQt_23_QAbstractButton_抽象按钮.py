#QAbstractButton  是一个抽象类，时所有的button按钮类的父类
#QAbstractButton  抽象类时不可以直接被使用必须要新建一个子类取继承它
#QAbstractButton  新建的子类必须要重写paintEvent方法


from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("hahahahah")
window.resize(500,500)

class Btn(QAbstractButton):   #这是一个抽象类，不可以直接实例化，只能重写
    def paintEvent(self, env):
        #print("aa")
        painter=QPainter(self)              #创建一个画图的人，self是画纸
        pen=QPen(QColor(111,200,20),5)     #设置笔对象，（rgb，粗细）
        painter.setPen(pen)                 #设置一支笔给人
        painter.drawText(30,40,self.text()) #画一个文本（x,y,内容）

        painter.drawEllipse(0,0,80,80)      #画一个椭圆




but = Btn(window)

but.setText("按钮")     #这是QAbstractButton的api
print(but.text())      #这是QAbstractButton的api

but.resize(100,100)
but.pressed.connect(lambda :print("点击了"))

window.show()

sys.exit(app.exec_())

