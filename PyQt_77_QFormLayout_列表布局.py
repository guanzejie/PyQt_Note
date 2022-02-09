
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("表单布局")
        self.resize(500, 500)
        self.setupUi()

    def setupUi(self):
        name_lb=QLabel("name:")
        age_lb = QLabel("age:")
        name_le = QLineEdit()
        age_le = QLineEdit()
        ID_le = QLineEdit()

        sex = QLabel("性别")
        nan = QRadioButton("男")
        nv = QRadioButton("女")
        h_layout=QHBoxLayout()
        h_layout.addWidget(sex)
        h_layout.addWidget(nan)
        h_layout.addWidget(nv)

        sex1 = QLabel("公母")
        nan1 = QRadioButton("公")
        nv1 = QRadioButton("母")

        h_layout1=QHBoxLayout()
        h_layout1.addWidget(sex1)
        h_layout1.addWidget(nan1)
        h_layout1.addWidget(nv1)


        xuehao=QLineEdit()


        fl=QFormLayout()     #表单布局管理器

        self.setLayout(fl)   #关联给父控件


        # 添加行
        fl.addRow(name_lb,name_le)        # 添加行控件，可以由多个控件在一行,也可以是1行
        #fl.addRow(age_lb, age_le)         # 添加行控件，可以由多个控件在一行
        fl.addRow(h_layout)               # 添加一个layout
        fl.addRow("ID:", ID_le)

        #插入行
        fl.insertRow(1,"学号",xuehao)
        fl.insertRow(0,age_lb, age_le)

        #获取行信息
        print(fl.rowCount())  #有多少行
        print(fl.getWidgetPosition(name_le)) #查找组件位置（1,1），第一行的右边 ，如果是1代表是QFormLayout.FieldRole输入框角色,右边
                                                                           #如果是0代表是QFormLayout.LabelRole展标签角色，左边
        print(fl.getLayoutPosition(h_layout))                              #果是2代表是QFormLayout.SpanningRole整行


        #设置行
        # fl.setWidget(0, QFormLayout.LabelRole, name_lb)  #（第几行，左边还是右边，控件）
        # fl.setWidget(0, QFormLayout.FieldRole, name_le)  #（第几行，左边还是右边，控件）
        # fl.setLayout(1, QFormLayout.SpanningRole, h_layout1)

        #删除行
        # fl.removeRow(1)   #删除并释放
        # fl.removeRow(1)
        # fl.takeRow(1)    #删除不释放

        #标签操作
        #fl.labelForField(name_lb).setText("名字啊:")

        #包装策略，因为缩放的时候会挤压的太厉害
        fl.setRowWrapPolicy(QFormLayout.WrapLongRows)
                           #QFormLayout.DontWrapRows      字段总是放在标签旁边
                           #QFormLayout.WrapAllRows       赋予标签足够的控件
                           #QFormLayout.WrapLongRows      字段总是在标签下面

        #对齐方式
        fl.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        #设置间距
        fl.setHorizontalSpacing(10)   #横向间距
        fl.setVerticalSpacing(30)     #垂直间距












window=Window()
window.show()
sys.exit(app.exec_())