from PyQt5.Qt import *
import sys


# app=QApplication(sys.argv)
# 如果一个qt程序的QApplication对象启动了之后会在后台循环监听用户是否对窗口进行操作
# 如果接受到用户的操作后会将消息打包成“QEvent”的对象进行分发处理
# 将事件接收者，和事件对象传递给QApplication对象的notify（receiver.ect）方法
# 再将事件分发给具体的函数，例如是点击了按钮，还是按下了某个键盘上的键

class App(QApplication):

    def notify(self, recevier, evt):  # 重写QApplication对象的notify方法
        if (recevier.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress):
            print(recevier, evt)  # 查看监听消息

        return super().notify(recevier, evt)


class Btn(QPushButton):  # 重写QPushButton类
    def event(self, evt):  # 重写QPushButton类的event方法
        if (evt.type() == QEvent.MouseButtonPress):
            print(evt)

        return super().event(evt)

    def mousePressEvent(self, *args, **kwargs):  # 重写QPushButton类的mousePressEvent方法

        print("被内部拦截了")

        return super().mousePressEvent(*args, **kwargs)


app = App(sys.argv)

window = QWidget()

# window.resize(200,200)

btn = Btn(window)

btn.setText("按钮")

btn.move(100, 100)

btn.clicked.connect(lambda: print("被点了"))

window.show()
sys.exit(app.exec())
