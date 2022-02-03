
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("光标控制")
window.resize(500,500)

le=QLineEdit(window)   #单行文本输入
le.setText("")
le.move(200,200)


bt=QPushButton(window)
bt.setText("按钮")


def chufa():
    #文本编辑
    #le.backspace()   #删除
    le.backspace(True,2)   #选中两个字符并删除
    #le.del_()        #删除
    #le.clear()       #清空
    #le.copy()
    #le.cut()
    #le.paste()
    #le.undo()
    #le.isUndoAvailable()
    #le.redo()
    #le.isRedoAvailable()


    #文本选中
    #le.setSelection(3,5)         #重第三个字符起到第8个被选中
    #le.selectAll()               #选中所有
    #le.deselect()                #取消选中
    print(le.hasSelectedText())  #是否选中文本
    print(le.selectedText())     #获取选中文本
    print(le.selectionStart())   #获取选中开始位置
    print(le.selectionEnd())     #获取选中结束位置
    print(le.setMaxLength())     #选中的长度





    le.setFocus()

bt.clicked.connect(chufa)
le.setDragEnabled(True)    #设置可以拖拽


le1=QLineEdit(window)   #单行文本输入
le1.setText("")
le1.move(200,400)






window.show()
sys.exit(app.exec_())