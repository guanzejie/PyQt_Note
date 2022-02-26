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
        # 静态方法
        # QMessageBox.about(self,"标题", "描述信息")
        # QMessageBox.aboutQt(self,"QT是他妈什么")
        QMessageBox.critical(self, "标题", "描述信息", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # QMessageBox.information(self,"标题", "描述信息",QMessageBox.Yes |QMessageBox.No,QMessageBox.No)
        # QMessageBox.question(self,"标题", "描述信息",QMessageBox.Yes |QMessageBox.No,QMessageBox.No)
        # QMessageBox.warning(self,"标题", "描述信息",QMessageBox.Yes |QMessageBox.No,QMessageBox.No)

        return
        but = QPushButton(self)
        but.setText("按钮")

        # em = QMessageBox(QMessageBox.Critical, "标题", "描述信息", QMessageBox.Ok, self)
        em = QMessageBox(self)
        em.setModal(False)  # 设置为非模态
        em.setWindowModality(Qt.NonModal)  # 设置为非模态

        em.setWindowTitle("杰哥的标题")  # 设置标题

        # 设置图标
        em.setIcon(QMessageBox.Critical)
        # QMessageBox.NoIcon       没图标
        # QMessageBox.Question     提问图标
        # QMessageBox.Information  信息图标
        # QMessageBox.Warning      警告图标
        # QMessageBox.Critical     严重问题图标
        # 自定义图标
        em.setIconPixmap(QPixmap("logo.png").scaled(100, 20))

        # 设置文本
        em.setText("<h1>来自杰哥的描述</h1>")  # 主文本
        em.setInformativeText("杰哥问你关闭不？")  # 副文本
        em.setCheckBox(QCheckBox("下次别他妈提醒了", em))

        # em.setTextFormat(Qt.PlainText)  #设置为普通文本    Qt.RichText     Qt.AutoText

        em.setDetailedText("你点我干嘛呢,还看")  # 设置点击观看的文本

        # 设置按钮
        # em.setStandardButtons(QMessageBox.Yes |QMessageBox.No)

        aa = em.addButton(QPushButton("好的呦", em), QMessageBox.YesRole)
        bb = em.addButton("我不要", QMessageBox.NoRole)
        # em.removeButton(bb)   #删除按钮

        print(em.button(QMessageBox.No))
        print(QMessageBox.NoRole)
        em.buttonClicked.connect(lambda but1: print(but1))  # 按下按钮后触发的信号

        em.setDefaultButton(bb)  # 设置默认按钮

        em.setEscapeButton(aa)  # 设置按下Esc后会触发的按钮

        # 文本交互
        # 设置文本交互标志
        em.setTextInteractionFlags(Qt.TextSelectableByKeyboard | Qt.NoTextInteraction | Qt.TextEditable)
        # Qt.NoTextInteraction           不可选择
        # Qt.TextSelectableByKeyboard    可以用键盘选择
        # Qt.TextSelectableByMouse       可以用鼠标选择
        # Qt.LinksAccessibleByKeyboard   可以用键盘选择,可以激活超链接
        # Qt.LinksAccessibleByMouse      可以用鼠标选择,可以激活超链接
        # Qt.TextEditable                可以编辑

        # Qt.TextEditorInteraction        可以用键盘选择,可以用鼠标选择,可以编辑
        # Qt.TextBrowserInteraction        可以用键盘和鼠标选择,可以激活超链接

        but.clicked.connect(lambda: em.show())
        # but.clicked.connect(lambda: em.open())
        # but.clicked.connect(lambda: em.exec_())


window = Window()
window.show()
sys.exit(app.exec_())
