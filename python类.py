# # 定义类的名字必须是大驼峰命名法
# class GuanZeJie:
#      # __slots__ = ["name", "aa", "bb", "age", "aa1", "bb1", "id_g"]   # 限制往后的对象只能创建这些属性
#      id_g = 8361
#
#
# # 对象不可以修改类的属性的值，只能更改对象属性的值
# guan=GuanZeJie()
# guan.aa=10         # 外部定义对象的属性
# guan.bb=20
# GuanZeJie.age=18   # 外部定义类属性
#
#
# # 类属性的值可以使用类名去修改类内部的属性
# GuanZeJie.id_g += 1
# guan.id_g += 1
# del guan.bb        # 删除属性
#
# print(GuanZeJie.id_g)
# print(guan.__class__)       # 查看对象指向了哪个类
# print(guan.id_g)
# print(GuanZeJie.age)
# print(guan.__dict__)       # 以字典的方式打印所有的属性
# print(GuanZeJie.__dict__)  # 以字典的方式打印所有的属性
#
#
# # 对象的属性可以使用__dict__以字典的方式去修改
# # 对象的属性是可以通过__dict__去修改或添加
# zejie = GuanZeJie()
# zejie.name ="zhejie"
# zejie.__dict__ = {"aa1": 10, "bb1": 20}     # 直接赋予对象属性
# zejie.__dict__["name"] = "guanzejie"
#
# print(zejie.bb1)
# print(zejie.name)
#
#
# # 类对象的属性是不可以使用类名和__dict__字典的方式去修改，类对象属性是不可以通过__dict__去修改或添加
# # GuanZeJie.__dict__["name"]="guanzejie"  # 这样是错误的，类对象不可以这样修改类属性
# # GuanZeJie.__dict__["tianjia"]="123456"  # 这样也是错的，类对象不可以这样加类属性

# ----------------------------------------------------------------------------------------------

class Person:

    def eat(self, fool):
        print('在吃', fool)

    def shili(self):
        print('实例方法', self)

    @classmethod
    def lei(cls):  # 对象调用类方法，类方法内部会忽略对象使用类来调用，如果有父类类方法会使用父类去调用
        print('类方法', cls)

    @staticmethod
    def jintai():  # 不能访问类方法类属性，对象方法和对象属性
        print("静态方法")


p1 = Person()
p1.shili()
p1.eat("屎")
p1.lei()  # 对象调用类方法，类方法内部会忽略对象使用类来调用，如果有父类类方法会使用父类去调用
Person.lei()
Person.jintai()
print(Person.__dict__)  # 可以使用类名.__dict__来查看类里面的方法


# print(p1.__dict__)        # 不能使用对象名.__dict__来查看类里面的方法

# ------------------------------------------------------------------------------------
# 创建类对象的类  被称为元类   如  (str.__class__)==(int.__class__)==type      type类是元类,祖宗类

def fun(self):
    print(str.__class__)
    if (str.__class__) == (int.__class__) == type:
        print(1)


# 使用元类创建一个类
lei = type("Class", (), {"eat_": "屎", "fun": fun})  # (类名,(继承), {属性})

c = lei()

print("______", c.__class__)

c.fun()


# 指定一个元类
class Ren(metaclass=lei):  # metaclass是指定哪个类是这个类的元类
    # __metaclass__=lei    # 指定元类的另一种方法
    pass
