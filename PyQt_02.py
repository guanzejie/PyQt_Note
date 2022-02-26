from PyQt_02_面向对象体验 import *

window = Window()

window.show()

print(QWidget.__subclasses__())  # 当前类的所有子类

sys.exit(app.exec_())
