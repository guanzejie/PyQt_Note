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

        pass

    def showEvent(self, QShowEvent):
        print("打开")

    def closeEvent(self, QCloseEvent):
        print("关闭")

    def moveEvent(self, QMoveEvent):
        print("移动")

    def resizeEvent(self,QResizeEvent):
        print("改变了窗口大小")

    def enterEvent(self, QEvent):
        print("鼠标进来")

    def leaveEvent(self,QEvent):
        print("鼠标走了")

    def mousePressEvent(self, QMouseEvent):
        print("鼠标按下")

    def mouseReleaseEvent(self, QMouseEvent):
        print("鼠标抬起")

    def mouseDoubleClickEvent(self,QMouseEvent):
        print("鼠标双击")

    def mouseMoveEvent(self,QMouseEvent):
        print("鼠标移动")

    def keyPressEvent(self, QKeyEvent):
        print("键盘按下")

    def keyReleaseEvent(self, QKeyEvent):
        print("键盘释放了")





if __name__=="__main__":

    window=Window()

    window.show()

    sys.exit(app.exec_())