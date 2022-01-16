
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("QCheckBox")
window.resize(500,500)

but=QCheckBox(window)
but.setText("button1")

but1=QCheckBox("button2",window)
but1.move(0,60)

but2=QCheckBox("button3",window)
but2.move(0,120)

but2.setTristate(True)  #设置第三种状态
print(but2.isTristate())

#but2.setChecked(True) #设置默认为选中状态
#but2.setChecked(False) #设置默认为未选中状态
but2.setCheckState(Qt.PartiallyChecked) #设置默认为中间状态   1   Qt.Checked选中   2  Qt.Unchecked未选中


but2.stateChanged.connect(lambda state :print(state))   #发出三态型号



window.show()
sys.exit(app.exec_())