
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("日历")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):
        jdt=QProgressBar(self)   #进度条
        jdt.move(100,50)
        jdt.resize(300,20)

        #范围设置
        jdt.setMinimum(0)
        jdt.setMaximum(100)
        jdt.setRange(0,100)
        #jdt.setRange(0, 0)    #繁忙提示
        jdt.setValue(0)       #数值设置
        print(jdt.value())
        #jdt.reset()           #重置当为当前设置的最小值

        #格式设置，展现的文本
        #jdt.setFormat("%p%")    #展现当前值
        jdt.setFormat("%v%")     #展现当前值
        #jdt.setFormat("%m%")    #最大值和最小值得差，展现总值
        #jdt.resetFormat()       #重置默认
        jdt.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        #文本标签控制
        #jdt.setTextVisible(False)   #隐藏文本标签
        print(jdt.text())

        #设置方向
        # jdt.resize(30, 200)
        # jdt.setOrientation(Qt.Vertical)    #竖状进度条
        jdt.setTextDirection(0)  #设置文本方向

        #jdt.setInvertedAppearance(True)    #反过来显示


        #案例
        timer_ = QTimer(jdt)      #创建一个时间对象
        def time_ch():

            if jdt.value()==100:
                jdt.setValue(0)
            else:
                jdt.setValue(jdt.value()+1)

        timer_.timeout.connect(time_ch)      #现在时间的型号

        timer_.start(100)                    #设置开始的速度

        jdt.valueChanged.connect(lambda val: print("当前的进度值是{}%".format(val)))





window=Window()
window.show()
sys.exit(app.exec_())


