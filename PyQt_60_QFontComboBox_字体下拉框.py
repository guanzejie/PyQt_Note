
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):

        cbb = QFontComboBox(self)
        self.cbb=cbb
        cbb.move(100,0)

        #添加下拉列表
        cbb.addItem("aa1")
        cbb.addItem("aa2")
        cbb.addItem(QIcon("logo.png"),"logo",1)   #(图标,名字,数据)
        cbb.addItems(["bb1","bb2"])

        #插入下拉表
        cbb.insertItem(1,"xx")
        cbb.insertItems(3,["a","b","c","d"])

        #设置列表
        cbb.setItemText(0,"guangua")
        cbb.setItemIcon(1, QIcon("logo.png"))

        #删除列表元素
        cbb.removeItem(5)

        #插入分割线
        cbb.insertSeparator(3)

        #设置默认选中
        cbb.setCurrentText("a")
        #cbb.setCurrentIndex(1)

        #设置编辑文本
        cbb.setEditable(True)  #动态添加

        #设置当前的元素的字符
        cbb.setEditText("aaaaaaaaaaaa")

        bu=QPushButton(self)
        bu.setText("按钮")
        bu.pressed.connect(self.test_1)

        #设置最大的元素数量
        #cbb.setMaxCount(10)

        #设置最大可见元素数量
        #cbb.setMaxVisibleItems(3)

        #设置可以重复的元素
        cbb.setDuplicatesEnabled(True)

        #设置为有框架
        cbb.setFrame(True)

        #设置图标尺寸
        cbb.setIconSize(QSize(60,60))

        #清空所有条目
        #cbb.clear()

        cbb.clearEditText()   #清空当前选择

        #弹出
        #cbb.showPopup()

        #完成器
        qc=QCompleter(["a","aa","12","324","1234","5","a34"])
        cbb.setCompleter(qc)


        #发生的信号
        cbb.activated.connect(lambda val: print("被激活",val))
        cbb.activated[str].connect(lambda val: print("被激活",val))
        cbb.currentIndexChanged.connect(lambda val: print("索引改变了",val))
        cbb.currentIndexChanged[str].connect(lambda val: print("索引改变了",val))
        cbb.currentTextChanged.connect(lambda val: print("文本改变了",val))
        cbb.editTextChanged.connect(lambda val: print("文本编辑了",val))
        cbb.highlighted.connect(lambda val: print("高亮模式",val))
        cbb.highlighted[str].connect(lambda val: print("亮模式",val))





        lable=QLabel(self)
        lable.setText("中国人民共和")
        lable.move(200,200)

        cbb.currentFontChanged.connect(lambda font: lable.setFont(font))






        #获取元素
    def test_1(self):

        print(self.cbb.count())          #一共有多少个
        print(self.cbb.currentIndex())   #当前是第几个
        print(self.cbb.currentText())    #当前文本
        print(self.cbb.currentData())    #当前的数据
        print(self.cbb.itemIcon(self.cbb.currentIndex()))  #获取当前图标












window=Window()
window.show()
sys.exit(app.exec_())