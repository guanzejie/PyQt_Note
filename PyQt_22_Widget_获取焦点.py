from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)



class Window(QMainWindow): #组合控件

    def __init__(self):
        super().__init__()

        self.setWindowTitle("焦点")
        self.statusBar()           #懒加载状态栏
        self.resize(500,500)

        self.le=QLineEdit(self)
        self.le.move(0,0)

        self.le1=QLineEdit(self)
        self.le1.move(200, 0)
        self.le1.setFocus()            #设置初始光标位置（焦点）

        self.le2=QLineEdit(self)
        self.le2.move(400, 0)
        self.le2.setFocus()            #设置初始光标位置（焦点）

        #le1.setFocusPolicy(Qt.NoFocus)      #焦点的获取方式
        #                  Qt.ClickFocus    只可以通过点击获取
        #                  Qt.TabFocus      只可以通过tab获取
        #                  Qt.StrongFocus   只可以通过tab和点击获取
        #                  Qt.NoFocus       不能通过tab和点击获取

        #le1.clearFocus()   #不设置这个控件为焦点

    def mousePressEvent(self, Eve):

        print(self.focusWidget())     #打印现在时那个控件获取了焦点
        self.focusNextChild()         #鼠标点击之后会切换到下一个子控件
        #self.focusPreviousChild()     #鼠标点击之后会切换到下一个子控件
        #self.focusNextPrevChild(True)  #鼠标点击之后会切换到下一个子控件



if __name__=="__main__":

    window=Window()

    window.setTabOrder(window.le, window.le2)   #修改Tab的切换顺序，给焦点获取顺序进行排序
    window.setTabOrder(window.le2, window.le2)

    window.show()
    sys.exit(app.exec_())