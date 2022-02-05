
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
        but=QPushButton(self)
        but.setText("按钮")

        dl=QDialog()    #是一个顶级的临时窗口


        dl.setSizeGripEnabled(True)   #右下角会出现一个可以控制缩放的箭头



        #槽函数
        bt1=QPushButton(dl)
        bt1.setText("取消")
        bt1.move(80,0)
        bt1.clicked.connect(lambda: dl.reject())   #取消按钮，关闭按钮

        bt2 = QPushButton(dl)
        bt2.setText("接受")
        bt2.move(160,0)
        bt2.clicked.connect(lambda: dl.accept())  #接受按钮命令，关闭按钮

        bt3 = QPushButton(dl)
        bt3.setText("完成")
        bt3.move(240,0)
        bt3.clicked.connect(lambda: dl.done(8))  #完成按钮，放回一个整数，关闭按钮
        # bt3.clicked.connect(lambda: dl.setResult(88888))  # 直接设置结构，不会关闭按钮


        #可用信号
        dl.accepted.connect(lambda :print("接受了"))
        dl.rejected.connect(lambda :print("取消了"))
        dl.finished.connect(lambda :print("完成了"))



        #dl.setWindowTitle("对话框")     # 这是应用程序级别的模态
        #dl.setWindowModality(Qt.WindowModal)    #窗口级别的模态
                           # Qt.ApplicationModal应用程序级别的模态
        #dl.setModal(True)
        but.pressed.connect(lambda : dl.show())     # 窗口级别的非模太，两个窗口都可以操作，两个窗口有关系
        #but.pressed.connect(lambda : dl.open())    # 窗口级别的非模太，如果控件选择了父级别窗口是窗口级别的模太,两个窗口没有任何关系
        #but.pressed.connect(lambda: dl.exec_())    # 窗口级别的模太，只能操作弹出来的这个窗口窗口，会堵塞主窗口，如果点击完成会放回一个1





window=Window()
window.show()
sys.exit(app.exec_())