from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)

class Window(QMainWindow): #组合控件

    def __init__(self):
        super().__init__()

        self.setWindowTitle("提示")
        self.setWindowFlags(Qt.WindowContextHelpButtonHint)    #顶层窗口会出现一个？按钮
        self.statusBar()           #懒加载状态栏
        self.resize(500,500)

        self.setStatusTip("提示")   #如果鼠标在窗口工作区域内状态栏会提示这句话
        print(self.statusTip())

        but=QPushButton(self)
        but.setText("按钮")
        but.setStatusTip("按钮")
        but.setToolTip("按钮")          #鼠标停留之后会出现的提示
        but.setToolTipDuration(2000)   # 两秒后提示消失
        print(but.toolTipDuration())
        print(but.toolTip())
        but.setWhatsThis("这是个按钮啊") #设置提问的答案
        print(but.whatsThis())


if __name__=="__main__":

    window=Window()

    window.show()

    sys.exit(app.exec_())