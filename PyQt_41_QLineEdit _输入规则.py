from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)

class AValidator(QValidator):  #Validator的意思是验证器
    def validate(self, input_str, pos_int):    #（self，输入内容，光标位置）
        print(input_str, pos_int)

        try:
            if (10<=int(input_str)<=20):  #只能输入10-20直接的数
                return (QValidator.Acceptable,input_str, pos_int)    #通过验证,通过验证后值输入内容会在输入框内，光标也在指定位置

            elif (0<=int(input_str)<=10):
                return (QValidator.Intermediate, input_str, pos_int)  #报错却可以显示在输入栏内，并调用fixup()方法

            else:
                return (QValidator.Invalid, input_str, pos_int)        #返回错误

        except:
            if (len(input_str)==0):
                return (QValidator.Intermediate, input_str, pos_int)

            return (QValidator.Invalid, input_str, pos_int)

    def fixup(self, p_str):   #自动修复 如果输入的结构处于Intermediate中间状态，会把结果传达这个函数

        try:

            if (int(p_str)<10):

                return "10"

            return "20"
        except:

            return "20"

class MyAValidator(QIntValidator):
    def fixup(self,p_str):

        if (int(p_str) <10 or len(p_str)== 0):
            return "10"


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("只能输入10-20直接的数")
        self.resize(500,500)
        self.setup()

    def setup(self):
        le = QLineEdit(self)
        le.move(100,100)

        #vadidator=AValidator()
        #le.setValidator(vadidator)   #设置一个验证，需要定义一个类继承QValidator来使用

        vadidator1 = QIntValidator(10,20)
        le.setValidator(vadidator1)

        le1 = QLineEdit(self)
        le1.move(100,200)

        # 设置掩码 例如ip地址 192.168.1.1  电话号码86-383050154
        le1.setInputMask("999.999.999.999")


        def aa():
            print(le.isModified())   #查看文本框是否被编辑
            le.setModified(False)    #修改为没有被编辑了的状态


        bt=QPushButton(self)
        bt.setText("按钮")

        bt.pressed.connect(aa)







window = Window()

window.show()
sys.exit(app.exec_())