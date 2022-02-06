
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
        lcd=QLCDNumber(10,self)   #能显示10位字符
        lcd.move(100,50)
        lcd.setDigitCount(15)     #位数控制
        lcd.display(123467)     #展示内容
        print(lcd.intValue())
        print(lcd.value())
        lcd.resize(400, 100)

        lcd1=QLCDNumber(10,self)   #能显示10位字符
        lcd1.move(100,200)
        lcd1.setDigitCount(15)     #位数控制
        lcd1.display(123)          #展示内容
        lcd1.resize(400, 100)

        lcd2=QLCDNumber(10,self)   #能显示10位字符
        lcd2.move(100,350)
        lcd2.setDigitCount(15)     #位数控制
        lcd2.display(12)         #展示内容
        lcd2.resize(400, 100)

        #进制模式设置
        #lcd.setMode(QLCDNumber.Bin)  #设置为二进制
        #lcd.setMode(QLCDNumber.Oct)  # 设置为八进制
        #lcd.setMode(QLCDNumber.Hex)  # 设置为十六进制
        lcd.setMode(QLCDNumber.Dec)  # 设置为十进制

        #设置分段格式
        lcd.setSegmentStyle(QLCDNumber.Outline)    #线框显示
        lcd1.setSegmentStyle(QLCDNumber.Filled)    #立体显示
        lcd2.setSegmentStyle(QLCDNumber.Flat)      #平面显示






window=Window()
window.show()
sys.exit(app.exec_())