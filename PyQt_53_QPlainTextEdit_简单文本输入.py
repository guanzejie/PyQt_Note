from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


# 放大缩小
def fada():
    le.zoomIn()


def suoxiao():
    le.zoomOut()


# 滚动保证光标可见
def gundong():
    # le.centerCursor()          #使得光标所在行在屏幕中心显示
    le.ensureCursorVisible()  # 滚动最短的距离使得光标可见
    le.setFocus()


def guangbiaocaozuo():
    tc = le.textCursor()
    tc.insertImage("logo.png")  # 插入图片
    tc.insertTable(5, 6)  # 插入表格


window = QWidget()
window.setWindowTitle("清空按钮")
window.resize(500, 500)
le = QPlainTextEdit(window)
le.move(100, 100)
le.setCenterOnScroll(True)  # 设置在末行可以滚动到中心

bt = QPushButton(window)
bt.setText("放大")
bt.pressed.connect(fada)

bt1 = QPushButton(window)
bt1.setText("缩小")
bt1.pressed.connect(suoxiao)
bt1.move(80, 0)

bt2 = QPushButton(window)
bt2.setText("滚动")
bt2.pressed.connect(gundong)
bt2.move(160, 0)

bt3 = QPushButton(window)
bt3.setText("光标操作")
bt3.pressed.connect(guangbiaocaozuo)
bt3.move(240, 0)

# 文本操作
le.setPlainText("hahahahahaha")  # 设置字符
le.insertPlainText("aaaaaaaa")  # 在光标处插入内容
le.appendPlainText("bbbbbbbbbbbbbbbb")  # 把内容加入文本后面
le.appendHtml("<a href='http://www.baodu.com'>百度</a>")
print(le.toPlainText())

# 占位文本置
le.setPlaceholderText("请输入")  # 设置占位文本字符
print(le.placeholderText())

# 只读设置
# le.setReadOnly(True)   #设置只读

# 软换行
le.setLineWrapMode(QPlainTextEdit.NoWrap)  # 不自动换行，并产生横向滚动条
# le.setLineWrapMode(QPlainTextEdit.WidgetWidth)   #自动换行

# 覆盖模式
le.setOverwriteMode(True)  # 设置覆盖模式

# tab控制
le.setTabChangesFocus(True)  # 按下tab之后切换焦点
le.setTabStopDistance(10)  # 按下tab之后退多少个像素

# 快的操作     按下回车键一行是一块
le.setMaximumBlockCount(100)  # 设置最大有多少块

# 可用的信号
# le.textChanged.connect(lambda : print("文本变了"))
# le.selectionChanged.connect(lambda : print("选择变了"))
# le.modificationChanged.connect(lambda : print("修改状态变了"))   # 从编辑状态到没编辑状态
# le.cursorPositionChanged.connect(lambda : print("光标变了"))
le.updateRequest.connect(lambda: print("更新内容了"))
le.copyAvailable.connect(lambda: print("可以复制"))

window.show()
sys.exit(app.exec_())
