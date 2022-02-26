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
        for i in range(90):
            cb = QCheckBox(self)
            cb.setText(str(i))
            cb.move(i % 10 * 50, i // 10 * 60)

        # 创建橡皮筋控件
        self.rb = QRubberBand(QRubberBand.Rectangle, self)  # 创建橡皮筋控件

    def mousePressEvent(self, Event):
        # 尺寸大小
        self.origin_size = Event.pos()  # 获取鼠标的当前位置
        self.rb.setGeometry(QRect(self.origin_size, QSize()))  # 获取鼠标的当前位置，和一个空的尺寸
        # 展示橡皮筋
        self.rb.show()

    def mouseMoveEvent(self, Event):

        # 调整橡皮筋控件的位置和尺寸
        self.rb.setGeometry(QRect(self.origin_size, Event.pos()).normalized())  # 获取鼠标上一个位置和鼠标的当前位置

    def mouseReleaseEvent(self, Event):
        # 获取橡皮筋控件的尺寸和范围
        rect = self.rb.geometry()  # 获取范围
        # 便利室友的子控件，查看那些控制在区域范围内
        for i in self.children():  # 获取window窗口的子控件

            if (rect.contains(i.geometry())) and i.inherits("QCheckBox"):  # 如果哪个子控件在橡皮筋的范围

                i.toggle()
        self.rb.hide()


window = Window()
window.show()
sys.exit(app.exec_())
