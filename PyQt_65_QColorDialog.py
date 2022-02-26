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
        dl = QColorDialog(QColor(10, 100, 200))  # 是一个顶级的临时颜色选择窗口
        dl.setWindowTitle("选择颜色")

        def color(col):
            print(col)
            pal = QPalette()
            pal.setColor(QPalette.Background, col)
            self.setPalette(pal)

        dl.colorSelected.connect(color)  # 颜色选择信号
        dl.currentColorChanged.connect(color)  # 当前颜色变化信号

        # dl.setModal(True)
        but.pressed.connect(lambda: dl.show())
        # but.pressed.connect(lambda : dl.open())
        # but.pressed.connect(lambda: dl.exec_())

        # 静态方法
        btn = QPushButton(self)
        btn.setText("aaaa")
        btn.move(160, 0)

        # btn.clicked.connect(lambda : print(dl.customCount()))  #获取自定义颜色的数量
        # btn.clicked.connect(lambda : dl.setCustomColor(8,QColor(10,100,200))) #获取自定义颜色

        def test():
            color1 = QColorDialog.getColor(QColor(10, 20, 30))
            color(color1)

        btn.clicked.connect(test)


window = Window()
window.show()
sys.exit(app.exec_())
