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
        lb = QLabel("中华 人民 共和 国&a", self)
        lb.setStyleSheet("background-color:cyan")
        lb.move(100, 100)
        lb.resize(300, 300)
        # lb.adjustSize()      #自动调整边框

        # 对齐方式
        # lb.setAlignment(Qt.AlignRight)
        lb.setAlignment(Qt.AlignCenter)
        lb.setAlignment(Qt.AlignLeft)
        # lb.setAlignment(Qt.AlignTop)
        # lb.setAlignment(Qt.AlignBottom)

        # 控制边距
        lb.setIndent(20)  # 设置左边距
        lb.setMargin(20)  # 设置上下左右的边距

        # 文本格式Html
        # lb.setText("<h1>中华人民共和国</hq>")
        # lb.setTextFormat(Qt.PlainText)     #把HTML文本当做普通文本展示

        # 快捷键
        ql = QLineEdit(self)
        ql1 = QLineEdit(self)
        ql1.move(0, 50)
        lb.setBuddy(ql)  # 快速切换焦点

        # 图片设置，缩放内容
        # lb.setPixmap(QPixmap("haha.jpg"))
        # lb.setScaledContents(True)        #自动缩放内容

        # 设置文本交互标志
        # lb.setTextInteractionFlags(Qt.TextSelectableByKeyboard | Qt.NoTextInteraction | Qt.TextEditable)
        # Qt.NoTextInteraction           不可选择
        # Qt.TextSelectableByKeyboard    可以用键盘选择
        # Qt.TextSelectableByMouse       可以用鼠标选择
        # Qt.LinksAccessibleByKeyboard   可以用键盘选择,可以激活超链接
        # Qt.LinksAccessibleByMouse      可以用鼠标选择,可以激活超链接
        # Qt.TextEditable                可以编辑

        # Qt.TextEditorInteraction        可以用键盘选择,可以用鼠标选择,可以编辑
        # Qt.TextBrowserInteraction        可以用键盘和鼠标选择,可以激活超链接

        # 是否可以打开超链接
        # lb.setText("<a href='http://www.baidu.com'>百度</a>")
        # lb.setOpenExternalLinks(True)     #打开超链接

        # 可以换行
        lb.setText("中华人民共和国 中华人民共和国 中华人民共和国 中华人民共和国 中华人民共和国 中华人民共和国\n中华人民共和国 中华人民共和国")
        # lb.setText("\n".join("中华人民共和国"))
        lb.setWordWrap(True)

        # 标签的内容操作
        lb.setText("aaaaa")  # 设置普通文本
        lb.setText("<img src='haha.jpg'>")  # 设置图片
        lb.setNum(10010.0000)  # 设置数字

        # 设置Gif
        move = QMovie("gif.gif")
        lb.setMovie(move)

        move.start()  # 播放
        # move.stop()           #停止

        move.setSpeed(500)  # 设置速度

        # 清空
        # lb.clear()

        # 可用信号
        lb.setText("<a href='http://www.baidu.com'>百度</a>")
        lb.setOpenExternalLinks(True)  # 打开超链接
        lb.linkActivated.connect(lambda a: print("超链接被激活了", a))
        lb.linkHovered.connect(lambda a: print("鼠标放在了超链接上", a))


window = Window()
window.show()
sys.exit(app.exec_())
