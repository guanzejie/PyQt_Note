from PyQt5.Qt import *

import sys

class Myobject(QObject):

    def timerEvent(self, evt): #重写Object类下的timerEvent方法
        print(evt,"1")

class Mylable(QLabel):

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size:30px;background-color:cyan")
        self.time1 = self.startTimer(1000)

    def timerEvent(self, evt) :
        time=int(self.text())
        time-=1
        self.setText(str(time))

        if (time<=0):

            self.killTimer(self.time1)

app =QApplication(sys.argv)

window =QWidget()
window.setWindowTitle("窗口")
window.resize(500,500)

lable = Mylable(window)

window.show()
sys.exit(app.exec_())
