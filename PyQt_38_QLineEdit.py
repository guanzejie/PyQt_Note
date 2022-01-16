
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("hahahahah")
window.resize(500,500)

le=QLineEdit(window)   #单行文本输入
#le.setText("bb")
#le.insert("ccc")  #插入内容
print(le.text())  #获取文本内容

#le.setEchoMode(le.PasswordEchoOnEdit)   #设置显示模式
                  #NoEcho               不显示
                  #Normal               普通显示
                  #Password             密码显示
                  #PasswordEchoOnEdit   不是焦点之后会边为密码

#占位文本的提示
le.setPlaceholderText("请输入")



window.show()
sys.exit(app.exec_())