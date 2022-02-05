
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("拆分")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):
        but=QPushButton(self)
        but.setText("拆分")
        dl=QInputDialog(self)    #是一个顶级的临时窗口

        #dl.setOption(QInputDialog.UseListViewForComboBoxItems)

        #输入模式
        #dl.setComboBoxItems(["1","2","3"])    #下拉类别模式
        #dl.setInputMode(QInputDialog.TextInput)   #字符输入
        dl.setInputMode(QInputDialog.IntInput)     #整数输入
        #dl.setInputMode(QInputDialog.DoubleInput) #浮点数输入


        #设置最大最小输入
        # dl.setIntMaximum(100)
        # dl.setIntMinimum(-100)
        # dl.setIntRange(-100,100)
        # dl.setIntStep(5)
        # dl.setIntValue(10)
        #
        # dl.setDoubleMaximum(10.00)
        # dl.setDoubleMinimum(-10.00)
        # dl.setIntRange(-10.00,10.00)
        # dl.setDoubleDecimals(3)       #设置小数位的个数
        # dl.setDoubleStep(0.5)
        # dl.setDoubleValue(0.2)



        #UI设置
        dl.setLabelText("给杰哥输入一下")
        dl.setOkButtonText("O鸡巴K")
        dl.setCancelButtonText("取他妈消")




        #信号
        dl.intValueChanged.connect(lambda val: print(val))
        dl.intValueSelected.connect(lambda val: print(val))
        dl.doubleValueChanged.connect(lambda val: print(val))
        dl.doubleValueSelected.connect(lambda val: print(val))
        dl.textValueChanged.connect(lambda val: print(val))
        dl.textValueSelected.connect(lambda val: print(val))






        #dl.setModal(True)
        but.pressed.connect(lambda : dl.show())
        #but.pressed.connect(lambda : dl.open())
        #but.pressed.connect(lambda: dl.exec_())



#________________________________静态方法_____________________________________________
        def jintai():
            #res=QInputDialog.getInt(self, "杰哥标题", "杰哥的提示",2022,-2022,step=5)
            #res = QInputDialog.getDouble(self, "杰哥标题", "杰哥的提示", 2022.00, -2022.00,decimals=2)
            #res = QInputDialog.getText(self, "杰哥标题", "杰哥的提示")
            res = QInputDialog.getItem(self, "杰哥标题", "杰哥的提示",['1','2','3','4'])
            print(res)


        but1=QPushButton(self)
        but1.setText("静态按钮")
        but1.move(100,0)
        but1.clicked.connect(jintai)







window=Window()
window.show()
sys.exit(app.exec_())