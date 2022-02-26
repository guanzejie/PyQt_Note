from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("光标控制")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):
        self.te = QTextEdit(self)
        self.te.resize(300, 300)
        self.te.move(100, 100)
        self.te.setPlaceholderText("请输入....")  # 设置占位文本

        # 设置普通文本内容
        self.te.setPlainText("hahahahahahahahahah\nhahahah")  # 设置普通文本

        # self.te.clear()#清空文本

        but = QPushButton(self)
        but.setText("字符")
        but.pressed.connect(self.ziti_)

        but1 = QPushButton(self)
        but1.setText("图片")
        but1.move(80, 0)
        but1.pressed.connect(self.tupian_)

        but2 = QPushButton(self)
        but2.setText("句子")
        but2.move(160, 0)
        but2.pressed.connect(self.juzi_)

        but3 = QPushButton(self)
        but3.setText("列表")
        but3.move(240, 0)
        but3.pressed.connect(self.leibiao_)

        but4 = QPushButton(self)
        but4.setText("表格")
        but4.move(240, 50)
        but4.pressed.connect(self.biaoge_)

        but5 = QPushButton(self)
        but5.setText("段落")
        but5.move(160, 50)
        but5.pressed.connect(self.duanluo_)

        but6 = QPushButton(self)
        but6.setText("框架")
        but6.move(80, 50)
        but6.pressed.connect(self.kuangjia_)

        but7 = QPushButton(self)
        but7.setText("格式设置合并")
        but7.move(0, 50)
        but7.pressed.connect(self.geshi_)

        but8 = QPushButton(self)
        but8.setText("获取格式")
        but8.move(0, 100)
        but8.pressed.connect(self.huoqu_)

        but9 = QPushButton(self)
        but9.setText("移动光标")
        but9.move(0, 150)
        but9.pressed.connect(self.yidongguangbiao)

        but10 = QPushButton(self)
        but10.setText("其他操作")
        but10.move(0, 200)
        but10.pressed.connect(self.other)

        but11 = QPushButton(self)
        but11.setText("删除一个")
        but11.move(0, 250)
        but11.pressed.connect(self.deleteText)

        but12 = QPushButton(self)
        but12.setText("文本光标位置")
        but12.move(0, 300)
        but12.pressed.connect(self.weizhi)

        but12 = QPushButton(self)
        but12.setText("开始和结束（undo，redo）")
        but12.move(0, 300)
        but12.pressed.connect(self.kaishijieshu)

    def kaishijieshu(self):  # 打包代码使得undo的时候一起undo，redo的时候意识一起
        hq = self.te.textCursor()  # 获取内容光标对象

        hq.beginEditBlock()  # 打包代码的开始
        hq.insertText("123")
        hq.insertBlock()
        hq.insertText("123")
        hq.endEditBlock()  # 打包代码的结束

        hq.insertBlock()
        hq.insertText("123")
        hq.insertBlock()
        hq.insertText("123")
        hq.insertBlock()
        hq.insertText("123")
        hq.insertBlock()
        hq.insertText("123")

    def weizhi(self):
        hq = self.te.textCursor()  # 获取内容光标对象
        print(hq.atBlockEnd())  # 光标是否在段落结尾
        print(hq.atBlockStart())  # 光标是否在段落开头
        print(hq.atEnd())  # 光标是否在文档结尾
        print(hq.atStart())  # 光标是否在文档开头
        print(hq.columnNumber())  # 在第几列
        print(hq.position())  # 在光标的位置
        print(hq.positionInBlock())  # 在文本块中的文位置

    def deleteText(self):
        hq = self.te.textCursor()  # 获取内容光标对象
        # hq.deleteChar()           #删除光标后面的字符
        hq.deletePreviousChar()  # 删除光标前面的字符
        self.te.setFocus()

    def other(self):
        hq = self.te.textCursor()  # 获取内容光标对象
        print(hq.selectionStart())  # 打印光标的选中位置的开始
        print(hq.selectionEnd())  # 打印光标的选中位置的结束

        print(hq.hasSelection())  # 判断是否有选中的文本

        hq.removeSelectedText()  # 删除选中的文本

        hq.clearSelection()  # 取消选中设置
        self.te.setTextCursor(hq)  # 设置取消

        self.te.setFocus()

    def yidongguangbiao(self):
        hq = self.te.textCursor()  # 获取内容光标对象
        # hq.setPosition(6)          # 设置移动信息
        # hq.movePosition(QTextCursor.Up, QTextCursor.KeepAnchor, 1)# 设置移动信息
        hq.select(QTextCursor.Document)
        # Document             全选文本
        # lockUnderCursor      选择光标下的文本
        # LineUnderCursor      选择光标下的文本行
        # WordUnderCursor      选择光标下的单词

        self.te.setTextCursor(hq)  # 设置移动光标
        self.te.setFocus()

        print(hq.selectedText())  # 打印选择的字符
        print(hq.selection().toPlainText())  # 打印选择的字符
        print(hq.selectedTableCells())  # 打印表格的选中区域

    def huoqu_(self):
        hq = self.te.textCursor()  # 获取内容光标对象
        print(hq.block().text())  # 获取光标信息
        print(hq.blockNumber())  # 获取第几行
        print(hq.currentList().count())  # 获取一共有多少个文本列表

    def geshi_(self):  # 格式设置合并
        gs = self.te.textCursor()  # 获取内容光标对象
        # gsf=QTextCharFormat()
        # gsf.setFontFamily("幼圆")
        # gsf.setFontPointSize(30)
        # gsf.setFontOverline(True)
        # gsf.setFontUnderline(True)
        # gs.setBlockCharFormat(gsf)

        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignVCenter)
        tbf.setIndent(1)
        gs.setBlockFormat(tbf)

    def kuangjia_(self):  # 设置一个文本的框架
        duanluo = self.te.textCursor()  # 获取内容光标对象
        tff = QTextFrameFormat()
        tff.setBorder(10)
        tff.setBorderBrush(QColor(100, 50, 50))
        tff.setRightMargin(50)

        duanluo.insertFrame(tff)

    def duanluo_(self):  # 相当于设置一个换行
        duanluo = self.te.textCursor()  # 获取内容光标对象
        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignLeft)  # 设置右对齐
        tbf.setIndent(1)  # 设置缩进

        tcf = QTextCharFormat()  # 设置字体样式
        tcf.setFontFamily("隶书")
        tcf.setFontItalic(True)

        duanluo.insertBlock(tbf, tcf)

        self.te.setFocus()

    def biaoge_(self):
        table = self.te.textCursor()  # 获取内容光标对象
        # lc4.insertTable(5,3)
        ttf = QTextTableFormat()  # 设置表格样式
        ttf.setAlignment(Qt.AlignRight)  # 右对齐
        ttf.setCellPadding(1)  # 设置边框
        ttf.setCellSpacing(0.5)  # 设置边框
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength, 33),
                                       QTextLength(QTextLength.PercentageLength, 33),
                                       QTextLength(QTextLength.PercentageLength, 33)))  # 设置宽度
        table.insertTable(5, 3, ttf)

    def leibiao_(self):
        tc3 = self.te.textCursor()  # 获取内容光标对象
        # tc3.insertList(QTextListFormat.ListLowerRoman)   #在当前的光标处插入一个标头
        # tc3.createList(QTextListFormat.ListLowerAlpha)  # 在当前的光标的行头插入一个标头
        # ListDisc圆点
        # ListCircle 圈圈
        # ListSquare  方形
        # ListDecimal 数字
        # ListLowerAlpha 小写字母
        # ListUpperAlpha 大写字母
        # ListLowerRoman  小罗马字母
        # ListUpperRoman  大罗马字母

        tlf = QTextListFormat()
        tlf.setIndent(1)  # 设置缩进
        tlf.setNumberPrefix("<")  # 设置前缀
        tlf.setNumberSuffix(">")  # 设置后缀
        tlf.setStyle(QTextListFormat.ListLowerAlpha)  # 设置样式

        tc3.createList(tlf)

    def juzi_(self):  # 插入段落

        tc2 = self.te.textCursor()  # 获取内容光标对象

        # jz=QTextDocumentFragment.fromHtml("<h1>hahahah</h1>")        # 创建html句子对象
        jz = QTextDocumentFragment.fromPlainText("<h1>hahahah</h1>")  # 创建普通句子对象

        tc2.insertFragment(jz)

    def tupian_(self):  # 插入图片

        tc1 = self.te.textCursor()  # 获取内容光标对象

        tp = QTextImageFormat()  # 创建图片对象
        tp.setName("logo.png")  # 设置图片
        tp.setWidth(300)
        tp.setHeight(100)
        tc1.insertImage(tp)

    def ziti_(self):  # 插入字符
        # self.te.document()
        ziti = QTextCharFormat()  # 创建字体对象
        ziti.setToolTip("自定义的")  # 字体对象的提示
        ziti.setFontFamily("隶书")  # 设置字体类型
        ziti.setFontPointSize(20)  # 设置字体大小

        tc = self.te.textCursor()  # 获取内容光标对象

        tc.insertText("添加的内容", ziti)  # 插入字体

        tc.insertHtml("<a href='http://www.baidu.com' >百度 </a>")  # 插入一个超链接


window = Mywindow()
window.show()
sys.exit(app.exec_())
