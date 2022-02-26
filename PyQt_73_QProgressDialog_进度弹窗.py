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
        but = QPushButton(self)
        but.setText("按钮")

        pd = QProgressDialog(self)
        # pd.setAutoClose(False)    #设置100%之后自动关闭
        pd.open()
        pd.setMinimumDuration(0)  # 设置延迟打开
        pd.setMaximum(100)
        pd.setMinimum(0)
        pd.setRange(0, 100)
        pd.setWindowTitle("aaaaaaaaaaaaaa")
        pd.setLabelText("进度")
        pd.setCancelButtonText("杰哥的取消")

        timer_ = QTimer(pd)  # 创建一个时间对象
        print(pd.maximum())

        def time_ch():
            if pd.value() + 1 == pd.maximum() or pd.wasCanceled():  # wasCanceled用户是否按下取消按钮

                timer_.stop()
            print(pd.value())
            pd.setValue(pd.value() + 1)

        timer_.timeout.connect(time_ch)  # 现在时间的型号

        timer_.start(100)  # 设置开始的速度

        # 信号
        pd.canceled.connect(timer_.stop)


window = Window()
window.show()
sys.exit(app.exec_())
