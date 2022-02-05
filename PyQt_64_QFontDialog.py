
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
        but.setText("获取字体")

        but1=QPushButton(self)
        but1.setText("获取字体1")
        but1.move(80,0)
        but1.clicked.connect(self.getfont)

        self.lb=QLabel(self)
        self.lb.setText("中华人民共和国")
        self.lb.move(80,50)

        font=QFont()
        font.setFamily("宋体")
        font.setPointSize(36)

        # df = QFontDialog()    # 是一个顶级的临时字体窗口
        # df.setCurrentFont(font)  #设置字体
        df = QFontDialog(font,self)    # 是一个顶级的临时字体窗口
        self.df = df


        #but.pressed.connect(lambda : df.show())
        #but.pressed.connect(lambda: df.open(self.select_font))    #df.open(select_font)会放回一个字体对象
        but.pressed.connect(lambda: df.exec_())



        df.setOption(QFontDialog.NoButtons)   #不显示按钮


        #信号
        df.currentFontChanged.connect(self.changed)   #当字体发生变化时信号
        df.fontSelected.connect(self.changed)         #当选择字体发生变化时信号


    def changed(self,font):
        self.lb.setFont(font)

    def getfont(self):

        font=QFontDialog.getFont(self)   #这个也是可以
        self.lb.setFont(font[0])




    #获取选择内容
    def select_font(self):
            print("选择了字体")
            print(self.df.selectedFont().family())
            print(self.df.selectedFont().pointSize())











window=Window()
window.show()
sys.exit(app.exec_())