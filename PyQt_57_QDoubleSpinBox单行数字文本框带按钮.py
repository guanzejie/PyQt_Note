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
        self.qsb = QDoubleSpinBox(self)
        self.qsb.resize(100, 30)
        self.qsb.move(200, 200)

        # 设置范围
        # self.qsb.setMaximum(100.00)        # 设置最大值
        # self.qsb.setMinimum(-100.00)       # 设置最小值
        self.qsb.setAccelerated(True)  # 设置可以加速

        self.qsb.setRange(-10.00, 10.00)  # 最大最小一起设置
        self.qsb.setWrapping(True)  # 设置数值在最大和最小中循环

        self.qsb.setSingleStep(0.01)  # 设置步长

        # 设置前缀和后缀
        # self.qsb.setRange(0,6)
        self.qsb.setPrefix("￥")  # 前缀
        self.qsb.setSuffix("%")  # 后缀
        # self.qsb.setSpecialValueText("周日")  #如果是最小值就调用这个

        # self.qsb.setDisplayIntegerBase(2)     #设置显示为二禁止

        # 设置小数的位数
        self.qsb.setDecimals(5)

        self.qsb.setValue(0.00523)  # 设置值为6
        print(self.qsb.value())  # 打印值
        print(self.qsb.cleanText())  # 只获取数值部分，不会四舍五入
        print(self.qsb.lineEdit().text())  # 打印文本框的内容，包括前缀后缀

        # 可使用信号
        self.qsb.valueChanged.connect(lambda: print("改变了"))


window = Window()
window.show()
sys.exit(app.exec_())
