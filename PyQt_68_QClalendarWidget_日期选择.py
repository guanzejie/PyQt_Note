from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("日历")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):
        but = QPushButton(self)
        but.setText("按钮")

        rl = QCalendarWidget()  # 日历

        rl.setSelectedDate(QDate(2012, 12, 12))  # 设置当前时间

        # 日期范围
        # rl.setMinimumDate(QDate(1,1,1))
        # rl.setMaximumDate(QDate(9999,12,31))
        rl.setDateRange(QDate(1, 1, 1), QDate(9999, 12, 31))

        # 使用键盘编辑
        rl.setDateEditEnabled(True)  # 可以使用键盘编辑
        rl.setDateEditEnabled(False)  # 不可以使用键盘编辑

        # 接收键盘输入的延迟
        rl.setDateEditAcceptDelay(3000)  # 键盘输入后3秒之后自动选择日期

        # 设置导航栏是否可见
        # rl.setNavigationBarVisible(False)    #不可见

        rl.setFirstDayOfWeek(Qt.Sunday)  # 设置一周里的第一天

        # 网格显示
        rl.setGridVisible(True)

        # 选中模式
        rl.setSelectedDate(QDate(2012, 12, 12))

        # 获取日期
        print(rl.monthShown())
        print(rl.yearShown())
        print(rl.selectedDate().toString())

        but.pressed.connect(lambda: rl.show())
        # but.pressed.connect(lambda: rl.showToday())
        # but.pressed.connect(lambda: rl.showSelectedDate())
        # but.pressed.connect(lambda: rl.showNextMonth())
        but.pressed.connect(lambda: rl.showNextYear())
        but.pressed.connect(lambda: rl.showPreviousMonth())
        but.pressed.connect(lambda: rl.showPreviousYear())

        # 信号
        rl.activated.connect(lambda date: print("双击了", date))
        rl.clicked.connect(lambda date: print("点击了", date))
        rl.currentPageChanged.connect(lambda date: print("换页了", date))
        rl.selectionChanged.connect(lambda: print("选择变了"))


window = Window()
window.show()
sys.exit(app.exec_())
