from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


class MyASB(QAbstractSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lineEdit().setText("0")

    def stepEnabled(self):  # 重写按钮，用户点击按钮的时候会自动调用这个方法
        # if (int(self.text()) == 0 ):
        #     return QAbstractSpinBox.StepUpEnabled   #按钮启动 +1
        #
        # elif (int(self.text()) == 9):
        #     return QAbstractSpinBox.StepDownEnabled  #按钮启动 -1
        #
        # elif (int(self.text()) < 0 or int(self.text()) > 9):
        #     return QAbstractSpinBox.StepNone         #关闭按钮

        # else:
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled  # 启动按钮

    def stepBy(self, p_int):  # 重写接收按钮的数字
        # print(p_int)
        current_num = int(self.text()) + p_int
        self.lineEdit().setText(str(current_num))  # 设置数值

    def validate(self, p_str, p_int):  # 数值验证器

        # 10-100
        num = int(p_str)
        if num < 10:
            return (QValidator.Intermediate, p_str, p_int)

        elif num <= 180:
            return (QValidator.Acceptable, p_str, p_int)

        else:
            return (QValidator.Invalid, p_str, p_int)

    def fixup(self, p_str):
        print(p_str)
        return "18"


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):
        self.abs = MyASB(self)
        self.abs.resize(200, 50)
        self.abs.move(200, 200)

        self.but = QPushButton(self)
        self.but.setText("按钮")
        self.but.pressed.connect(self.but_test)

        self.abs.setAccelerated(True)  # 长按是否加速
        # self.abs.setReadOnly(True)                 #设置只读

        cl = QCompleter(["1", "45", "75"], self.abs)  # 设置快速查找
        self.abs.lineEdit().setCompleter(cl)

        self.abs.setAlignment(Qt.AlignCenter)  # 设置对齐方式

        self.abs.setFrame(True)  # 设置边框

        # self.abs.clear()           #清空内容

        self.abs.editingFinished.connect(lambda: print("结束编辑"))  # 结束编辑信号

    def but_test(self):
        print(self.abs.text())  # 打印数值
        print(self.abs.lineEdit().text())
        # self.abs.lineEdit().setText("100")    #设置数值


window = Window()
window.show()
sys.exit(app.exec_())
