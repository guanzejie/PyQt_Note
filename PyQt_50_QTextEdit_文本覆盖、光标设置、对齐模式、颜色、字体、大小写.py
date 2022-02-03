
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)

class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("光标控制")
        self.resize(500,500)
        self.setupUi()

    def setupUi(self):
        self.te=QTextEdit(self)
        self.te.resize(300,300)
        self.te.move(100,100)
        self.te.setPlaceholderText("请输入....")  #设置占位文本

        #设置普通文本内容
        self.te.setPlainText("hahahahahahahahahah\nhahahah")   #设置普通文本
        self.te.insertPlainText("bbbbbbbb")                    #插入文本


        # 自动判断
        self.te.setText("<h1> hahahahaha</h1>""aaaaaa")       #自动判断是普通文本还是HTML文本

        #追加文本
        self.te.append("guanguan")


        but=QPushButton(self)
        but.setText("覆盖模式")
        but.pressed.connect(self.fugaimoshi)

        but1=QPushButton(self)
        but1.setText("光标设置")
        but1.pressed.connect(self.guangbiaoshezhi)
        but1.move(80,0)

        but2=QPushButton(self)
        but2.setText("对齐模式")
        but2.pressed.connect(self.duiqimoshi)
        but2.move(160,0)

        but3=QPushButton(self)
        but3.setText("字体设置")
        but3.pressed.connect(self.ziti)
        but3.move(240,0)

        but4=QPushButton(self)
        but4.setText("字体颜色")
        but4.pressed.connect(self.yanse)
        but4.move(240,50)

        but5=QPushButton(self)
        but5.setText("大小写")
        but5.pressed.connect(self.zimu)
        but5.move(160,50)


    def zimu(self):
        tcf=QTextCharFormat()
        tcf.setFontCapitalization(QFont.Capitalize)  #设置字母大小写
                                # QFont.MixedCase       不更改
                                # QFont.AllUppercase    全部大写
                                # QFont.AllLowercase     全部小写
                                # QFont.SmallCaps       小型大写字母
                                # QFont.Capitalize      每个单词第一个是大写

        self.te.setCurrentCharFormat(tcf)


    def yanse(self):
        self.te.setTextBackgroundColor(QColor(100,100,100))  #设置字体背景颜色
        self.te.setTextColor(QColor(200,50,50))   #设置字体颜色

    def ziti(self):
        QFontDialog.getFont()  #获取字体

        self.te.setFontFamily("隶书")  #设置字体样式
        self.te.setFontPointSize(10)   #设置字体大小
        self.te.setFontWeight(QFont.Black)   #设置字体粗细QFont.Thin,QFont.ExtraLight,QFont.Light,
                                                      # QFont.Normal,QFont.Medium,QFont.DemiBold,
                                                      # QFont.Bold,QFont.ExtraBold,QFont.Black
        self.te.setFontItalic(True)    #设置字体倾斜
        self.te.setFontUnderline(True) #设置下划线

    def duiqimoshi(self):
        self.te.setAlignment(Qt.AlignCenter)  # 设置对齐  Qt.AlignRight     Qt.AlignLeft   Qt.AlignCenter

    def guangbiaoshezhi(self):
        self.te.setCursorWidth(10)  #设置光标宽度
        print(self.te.cursorWidth())

    def fugaimoshi(self):
        self.te.setOverwriteMode(True)  #设置覆盖模式
        print(self.te.overwriteMode())


window=Mywindow()
window.show()
sys.exit(app.exec_())