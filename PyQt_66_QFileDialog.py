
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
        but=QPushButton(self)
        but.setText("按钮")

        dl=QFileDialog(self, "选择", './', "all(*.*);;images(*.jpg *.png);;python(*.py)")

        dl.setAcceptMode(QFileDialog.AcceptSave)    #设置为保存模式

        #dl.setAcceptMode(QFileDialog.AcceptOpen)  # 设置为打开模式

        #文件的选中模式
        dl.setFileMode(QFileDialog.AnyFile)               # 文件名，无论是否存在
        #dl.setFileMode(QFileDialog.ExistingFile)         # 单个现有的文件名称
        #dl.setFileMode(QFileDialog.ExistingFiles)        # 多个现有的文件名称
        #dl.setFileMode(QFileDialog.Directory)            # 目录的名称

        dl.setDefaultSuffix("txt")   #设置默认后缀

        #修改UI的文字
        dl.setLabelText(QFileDialog.FileName,"杰哥的文件")
        dl.setLabelText(QFileDialog.Accept,"杰哥确认")
        dl.setLabelText(QFileDialog.Reject,"杰哥拒绝")
        dl.setLabelText(QFileDialog.FileType,"杰哥类型")
        dl.setLabelText(QFileDialog.LookIn,"杰哥请看")

        #设置名称过滤器
        #dl.setNameFilter("images(*.jpg *.png)")
        #dl.setNameFilters("all(*.*);;images(*.jpg *.png);;python(*.py)")


        #dl.setModal(True)
        but.pressed.connect(lambda : dl.show())
        dl.filesSelected.connect(lambda file: print(file) )
        #but.pressed.connect(lambda : dl.open())
        #but.pressed.connect(lambda: dl.exec_())

        dl.setFileMode((QFileDialog.ExistingFiles))   #可以选择多个文件


        #可用信号
        dl.currentChanged.connect(lambda file: print("文件选择变了", file))
        dl.currentUrlChanged.connect(lambda file: print("url文件选择变了", file))
        dl.directoryEntered.connect(lambda file: print("进入文件夹", file))
        dl.directoryUrlEntered.connect(lambda file: print("进入url文件夹", file))
        dl.filterSelected.connect(lambda file: print("选中过滤", file))
        dl.fileSelected.connect(lambda file: print("点击OK选择文件", file))      #
        dl.filesSelected.connect(lambda file: print("点击OK选择多个文件", file))
        dl.urlSelected.connect(lambda file: print("点击OK选择url文件", file))
        dl.urlsSelected.connect(lambda file: print("点击OK选择多个url文件", file))



 # ___________________________________________________

        but1=QPushButton(self)
        but1.setText("按钮1")
        but1.move(80,0)
        but1.pressed.connect(self.file)
        #取文件的静态方法
    def file(self):
        # go = QFileDialog.getOpenFileUrl(self,"选择",'./',"all(*.*);;images(*.jpg *.png);;python(*.py)","python(*.py)")
        # go = QFileDialog.getOpenFileUrls(self,"选择",'./',"all(*.*);;images(*.jpg *.png);;python(*.py)","python(*.py)")
        #获取一个文件路径
        #go = QFileDialog.getOpenFileName(self,"选择",'./',"all(*.*);;images(*.jpg *.png);;python(*.py)","python(*.py)")   # (父类，标题栏名称，哪个文件夹，什么类型的文件，过滤字符,初始化)
        #获取多个文件路径
        # go = QFileDialog.getOpenFileNames(self,"选择",'./',"all(*.*);;images(*.jpg *.png);;python(*.py)","python(*.py)")
        # go = QFileDialog.getSaveFileName(self,"选择",'./',"all(*.*);;images(*.jpg *.png);;python(*.py)","python(*.py)")
        # go = QFileDialog.getSaveFileUrl((self,"选择",'./',"all(*.*);;images(*.jpg *.png);;python(*.py)","python(*.py)")
        #print(go)

        #获取文件夹的静态方法
        dir = QFileDialog.getExistingDirectory(self,"选择",'./')
        #dir = QFileDialog.getExistingDirectoryUrl()
        print(dir)


window=Window()
window.show()
sys.exit(app.exec_())