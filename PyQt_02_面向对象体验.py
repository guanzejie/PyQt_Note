from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("面向对象")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        lable=QLabel(self)
        lable.setText("面向对象的程序")
        lable.move(210,250)


if __name__=="__main__":

    window=Window()

    window.show()

    sys.exit(app.exec_())