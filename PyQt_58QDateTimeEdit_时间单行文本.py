from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):
        # dt=QDateTime(2020,1,1,1,1)     #设置时间
        dt = QDateTime.currentDateTime()  # 获取当前时间
        # dt = dt.addYears(5)               #加时间

        print(dt.offsetFromUtc())  # 获取本地时间和世界时间的时间差
        # print(dt.secsTo())      #间隔秒数
        # print(dt.msecsTo())

        # self.qsb=QDateTimeEdit(dt,self)
        self.qsb = QDateTimeEdit(QDateTime.currentDateTime(), self)  # 展示时间和日期
        # self.qsb = QDateTimeEdit(QDate.currentDate(), self)            #只展示日期
        # self.qsb = QDateTimeEdit(QTime.currentTime(), self)            #只展示时间

        self.qsb.setDisplayFormat("yy-MM-dd  || HH:mm:ss")  # 设置显示格式
        print(self.qsb.displayFormat())
        # d=1~31, dd=01~31,  ddd=Mon~sun,  dddd=星期一到星期日
        # M,MM,MMM,MMMM,yy,yyy,h,hh,H,HH,m,mm,s,ss,z,zz,AP/A,ap/a

        self.qsb.resize(200, 50)
        self.qsb.move(200, 200)

        print(self.qsb.sectionCount())  # 获取有多少个显示格式   yy-MM-dd-HH:mm:ss   有6个
        print(self.qsb.currentSectionIndex())  # 当前光标在哪个

        self.qsb.setCurrentSectionIndex(3)  # 把光标移动到第2个

        self.qsb.setMaximumDateTime(QDateTime(9999, 12, 31, 24, 60))  # 设置最大时间
        # self.qsb.clearMaximumDateTime() #恢复默认

        self.qsb.setMinimumDateTime(QDateTime(0, 0, 0, 0, 0))  # 设置最小时间
        # self.qsb.clearMinimumDateTime()#恢复默认

        # self.qsb.setDateTimeRange(QDateTime(0,0,0,0,0),QDateTime(9999,12,31,24,60))   #设置最大最小时间

        # 弹出日历选择控件
        self.qsb.setCalendarPopup(True)

        # 获取日期和时间
        print(self.qsb.dateTime().toString())
        print(self.qsb.date().toString())
        print(self.qsb.time().toString())

        # 使用信号
        self.qsb.dateTimeChanged.connect(lambda: print("时间日期改变了"))
        self.qsb.dateChanged.connect(lambda: print("日期改变了"))
        self.qsb.timeChanged.connect(lambda: print("时间改变了"))


window = Window()
window.show()
sys.exit(app.exec_())
