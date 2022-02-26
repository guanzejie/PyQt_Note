from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("清空按钮")
window.resize(500, 500)

le = QLineEdit(window)  # 单行文本输入
le.setText("bb")
# le.insert("ccc")  #插入内容
print(le.text())  # 获取文本内容

# le.setEchoMode(le.PasswordEchoOnEdit)   #设置显示模式
# NoEcho               不显示
# Normal               普通显示
# Password             密码显示
# PasswordEchoOnEdit   不是焦点之后会边为密码

# 占位文本的提示
le.setPlaceholderText("请输入")
print(le.placeholderText())


# 快速清空文本框内容
def clear_text():
    le.setClearButtonEnabled(True)
    print(le.isClearButtonEnabled())


bt = QPushButton(window)
bt.setText("按钮")
bt.move(0, 100)
bt.pressed.connect(clear_text)

action = QAction(le)
action.triggered.connect(lambda: print("点击了"))
action.setIcon(QIcon("./logo.png"))
# le.addAction(action, QLineEdit.LeadingPosition) #把logo放到输入框的左边        TrailingPosition把logo放到右边
le.addAction(action, QLineEdit.TrailingPosition)  # TrailingPosition把logo放到右边

# 自动补全
completer = QCompleter(["guan", 'guanze', "zejie", "jieshao", "wangzha"], le)  # 设置关键字
le.setCompleter(completer)  # 补全

window.show()
sys.exit(app.exec_())
