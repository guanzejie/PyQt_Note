from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("光标控制")
window.resize(500, 500)

le = QLineEdit(window)  # 单行文本输入
le.setText("bbxxxxxxxxaaaaa")
le.move(200, 200)
le.resize(100, 100)

bt = QPushButton(window)
bt.setText("按钮")


def chufa():
    # le.cursorBackward(True, 2)          #光标往左边移动2个字符并选择
    # le.cursorBackward(False,2)          #光标往左边移动2个字符
    # le.cursorForward(True,2)            #光标往右边移动2个字符并选择
    # le.cursorWordBackward(True)         #光标往左边移动1个字符并选择
    # le.cursorWordForward(True)          #光标往右边移动1个字符并选择
    le.home(False)  # 光标移动到行首
    # le.end(True)                        #光标移动到行尾并选择
    # le.cursorPosition(5)                #光标移动起始到第5个字符
    # print(le.cursorPosition())          #获取光标位置
    # le.cursorPositionAt(QPoint(10,20))  #根据坐标找位置
    le.setFocus()


bt.clicked.connect(chufa)

# 文本边距
# le.setContentsMargins(40,0,0,0)   #设置文本框的外边距
# le.setTextMargins(40,0,0,0)    #设置文本框的外边距

# 对齐方法
# le.setAlignment(Qt.AlignLeft)     #左对齐
# le.setAlignment(Qt.AlignRight)    #右对齐
# le.setAlignment(Qt.AlignHCenter)  #居中对齐
# le.setAlignment(Qt.AlignJustify)  #自适应对齐
# le.setAlignment(Qt.AlignTop)      #上对齐
# le.setAlignment(Qt.AlignBottom)   #下对齐
# le.setAlignment(Qt.AlignVCenter)  #中间对齐
# le.setAlignment(Qt.AlignBaseline) #基线对齐

le.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # 左上对齐

window.show()
sys.exit(app.exec_())
