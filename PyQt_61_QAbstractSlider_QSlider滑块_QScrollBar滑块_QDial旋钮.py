
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

        print(QAbstractSlider.__subclasses__())
        tt=QLabel(self)
        tt.setText("0")
        tt.resize(100,30)

        sl = QSlider(self)
        sl.move(100,100)
        sl.resize(200,20)
        sl.valueChanged.connect(lambda val: tt.setText(str(val)))

        sl.setMaximum(100)    #设置最大
        sl.setMinimum(-100)   #设置最小

        sl.setValue(88)       #设置默认值

        #sl.setSingleStep(2)   #设置上下键步长
        #sl.setPageStep(8)     #设置page键步长

        #sl.setTracking(False)    #是否跟踪，鼠标停止是出现数值

        sl.setSliderPosition(88)  #修改滑块位置

        sl.setInvertedAppearance(True)  #数值翻转
        sl.setInvertedControls(True)    #键盘控制数值翻转

        sl.setOrientation(Qt.Horizontal) #水平滑块

        sl.setSliderDown(True)    #设置滑块按下

        sl.setTickPosition(QSlider.TicksRight)   #刻度控制
                          #QSlider.NoTicks            没有刻度
                          #QSlider.TicksBothSides     两侧有刻度
                          #QSlider.TicksAbove         上方有刻度
                          #QSlider.TicksBelow         下方有刻度
                          #QSlider.TicksLeft           左
                          #QSlider.TicksRight          右

        sl.setTickInterval(10)      #刻度的密度

        print(sl.tickPosition())   #获取刻度线信息

        sl.setPageStep(10)  # 使用设置page键步长来控制刻度的密度



        sb=QScrollBar(self)   #滚动条
        sb.resize(300,20)
        sb.setOrientation(Qt.Horizontal) #水平滑块
        sb.move(20,200)
        sb.valueChanged.connect(lambda val: print(val))

        qd=QDial(self)
        qd.setRange(-100,100)
        qd.move(300,350)
        qd.setNotchesVisible(QSlider.TicksRight)   #显示刻度

        qd.setPageStep(5)    #显示大刻度

        #qd.setWrapping(True)   #在360度都画上刻度

        qd.setNotchTarget(20)   #控制刻度密度

        qd.valueChanged.connect(lambda val: print(val))















window=Window()
window.show()
sys.exit(app.exec_())