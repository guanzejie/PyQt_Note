
from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)


window=QWidget()
window.setWindowTitle("QCommandLinkButton")
window.resize(500,500)

but=QCommandLinkButton("标题","描述",window)

but.setText("改标题语句")

but.setDescription("变描述语句")

window.show()

#but.showMenu()                           #打开时打开菜单
sys.exit(app.exec_())