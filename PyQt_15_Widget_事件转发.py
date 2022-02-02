from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)

class Window(QWidget):

    def mousePressEvent(self, QMouseEvent):
        print("外层鼠标按下")


class MidWindow(QWidget):

    def mousePressEvent(self, QMouseEvent):
        print("中间鼠标按下")

class Lable(QLabel):

    #def mousePressEvent(self, QMouseEvent):
    def mousePressEvent(self, env):
        print("内层鼠标按下")
        env.accept()               #告诉系统这个事件已经处理了，不用再转发了
        #print(env.isAccepted())    #查询事件是否被处理了
        #env.ignore()               #忽略事件

    def keyPressEvent(self, env):
        if(env.key()==Qt.Key_Tab):  #捕获tab键
            print("Tab")

        #监听修饰键ctrl需要用env.modifiers()==Qt.ControlModifier
        #监听修饰键shift需要用env.modifiers()=Qt.ShiftModifier
        #监听修饰键alt需要用env.modifiers()=Qt.AltModifier
        #if (env.modifiers() == Qt.ControlModifier  and env.key() == Qt.Key_S):
        if(env.modifiers()==Qt.ControlModifier | Qt.ShiftModifier and env.key()==Qt.Key_S):

            print("ctrl+shift+s")




if __name__=="__main__":

    window=Window()
    window.resize(500,500)
    window.setStyleSheet("background-color:red")

    midwin=MidWindow(window)
    midwin.resize(300,300)
    midwin.setAttribute(Qt.WA_StyledBackground,True)
    midwin.setStyleSheet("background-color:yellow")

    lab=Lable(midwin)
    lab.setText("hahahah")
    lab.resize(100,30)
    lab.move(100,100)
    lab.setStyleSheet("background-color:green")
    lab.grabKeyboard()   #让lab这个控件去捕获键盘事件

    but=QPushButton(midwin)
    but.setText("按钮")      #按钮默认是会自动出来鼠标点击事件，就算不重写处理系统也会处理



    window.show()

    sys.exit(app.exec_())