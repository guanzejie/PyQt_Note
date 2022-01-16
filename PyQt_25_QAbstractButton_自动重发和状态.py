#QAbstractButton  是一个抽象类，时所有的button按钮类的父类
#QAbstractButton  抽象类时不可以直接被使用必须要新建一个子类取继承它
#QAbstractButton  新建的子类必须要重写paintEvent方法


from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("hahahahah")
window.resize(500,500)


but = QPushButton(window)
but.setText("a&b按钮")     #这是QAbstractButton的api，并设置快捷键为alt+b   （&b）
but.resize(100,40)
but.pressed.connect(lambda :print("点击了"))

#这是QAbstractButton的api
but.setAutoRepeat(True)           #设置点击重复
but.setAutoRepeatDelay(1000)      #设置按定多少毫秒开始重复
but.setAutoRepeatInterval(1000)   #设置重复的间隔时间
print(but.autoRepeat())           #查看是否点击重复
print(but.autoRepeatDelay())      #查看延迟
print(but.autoRepeatInterval())   #查看间隔

#but.setDown(True)        #设置为按下状态
but.setCheckable(True)    #设置按钮可以被选中
print(but.isCheckable())  #查看按钮是否可以被选中
but.setChecked(True)      #设置按钮是否可以被选中
print(but.isChecked())   #查看按钮是否被选中

but.toggle()             #如果没选中就变为选中，如果选中就变为没选择




window.show()
sys.exit(app.exec_())