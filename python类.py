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
# class Ren(metaclass=lei):  # metaclass是指定哪个类是这个类的元类
class Ren:
    """
    类的描述，必须放在类的最前面
    """
    __metaclass__ = lei  # 指定元类的另一种方法

    def aa(self):
        """
        方法的描述，必须放在方法的最前面
        """
        pass


# help(Ren)  # 打印描述信息

# 导出描述信息
# 在terminal里输入 python -m python类 -w 文件名

# ————————————————————————————————————————————————————————————————————————————私有


class Fu:
    x = 10
    _y = 11  # 当前模块调用会出现警告，外部模块如果使用"from python类 import * "的方式导入会报错
    __Z = 12  # 只能在当前类的内部使用

    # __all__ = [_y]   # 这个方法表示在外部文件里可以使用这个受到保护的模块

    def __init__(self):  # 初始化方法
        pass

    def test(self):
        print(self.x)
        print(Fu.x)
        print(self._y)
        print(Fu._y)
        print(self.__Z)
        print(Fu.__Z)

    def __run(self):  # 定义私有方法
        print("私有方法")


class Zi(Fu):

    def test1(self):
        print(self._y)
        print(Zi._y)
        # print(self.__Z)    #不能调用父类的私有属性，外部模块也不能调用这个模块的私有属性
        # print(Zi.__Z)
        print(Zi._Fu__Z, "aaaaaaaa")  # 可以使用 " _父类名字__属性" 的方式访问父类的私有属性


a = Zi()
a.test()
a.test1()
print(Fu._Fu__Z, "bbbbbbbb")  # 可以使用 " _父类名字__属性" 的方式访问父类的私有属性
print(a._Fu__run())  # 访问私有方法


# _______________________________________________________________________________只读 1


class P1(object):
    def __init__(self):
        self.__age = 18

    def writ(self, value):
        self.__age = value

    def read(self):
        return self.__age

    @property  # 以调用属性的方式调用方法，调用的时候不需要加括号
    def age(self):
        return self.__age

    age1 = property(read, writ)


p = P1()
print(p.read())
print(p.age)  # 以调用属性的方式调用方法
print(p.age1)
p.age1 = 100
print(p.age1)


# _______________________________________________________________________________只读 2


class P2:
    # 当我们通过实例.属性=值，给一个实例增加一个属性或者修改属性值得时候，会调用这个方法
    # 在这个方法内部才会真正的把这个属性以及对应的数据给存储到__dict__字典里面
    def __setattr__(self, key, value):
        print(key, value)
        if key == "age" and key in self.__dict__.keys():
            print("%s这他妈的是只读的属性" % key)
        else:
            self.__dict__[key] = value


p2 = P2()
p2.age = 18
p2.aa = 1

print(p2.__dict__)


# __________________________________________________________________________________系统内置属性

class P3:
    """
    描述xxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxx
    """

    def __init__(self):
        self.name = "guan"

    def run(self):
        print("跑步")


p3 = P3()
print(P3.__dict__)  # 类属性
print(P3.__bases__)  # 所有的父类
print(P3.__doc__)  # 文档描述
print(P3.__name__)  # 查看类名
print(P3.__module__)  # 类定义的所在模块
print(p3.__class__)  # 实例对应的类


# ——————————————————————————————————————————————————————————————————————————内置方法


class P4:

    def __init__(self, name, age):  # 自动初始化
        self.name = name
        self.age = age

    def __str__(self):  # 格式化信息字符串，print(p4)直接打印实例的时候会调用这一个方法，这个方法放回的必须是字符串
        return (self.name)

    def __repr__(self):  # 重写rapr函数
        return "__repr__"


p4 = P4("guan", 18)

print(p4)
print(repr(p4))  # 放回实例的内存地址和父类


# __________________________________字典操作


class P5:
    def __init__(self):
        self.cache = {}

    def __call__(self, *args, **kwargs):  # 如果需要把实例对象当做函数来调用可以使用这个方法
        print("__call__")

    def __setitem__(self, key, value):  # 可以实现以字典的方式赋值   p5["aa"] = 10
        # print("值是",key,value)
        self.cache[key] = value

    def __getitem__(self, item):  # 可以实现以字典的方式获取值   print(p5["aa"])
        # print("值是",item)
        return self.cache[item]

    def __delitem__(self, key):  # 可以实现以字典的方式删除元素
        # print("值是",key)
        del self.cache[key]


p5 = P5()

p5()  # __call__    用调用函数的方式来调用实例   p5()  实例名字加上个（）号
p5["aa"] = 10  # __setitem__
print(p5["aa"])  # __getitem__
del p5["aa"]  # __delitem__


# __________________________________切片操作


class P6:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]

    def __setitem__(self, key, value):
        print(key.start)
        print(key.stop)
        print(key.step)
        self.items[key] = value

    def __getitem__(self, item):
        # print("值是",item)
        return self.items[item]

    def __delitem__(self, key):
        # print("值是",key)
        del self.items[key]


p6 = P6()
p6[0:4:2] = [1, 2]


# __________________________________比较操作

class P7:
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def __eq__(self, other):  # 比较操作的相等规则
        print(other)
        return self.age == other

    def __ne__(self, other):  # 比较操作的不相等规则
        print(other)
        return self.age == other

    def __gt__(self, other):  # 比较操作的大于规则
        print(other)
        return self.age > other

    def __ge__(self, other):  # 比较操作的大于等于规则
        print(other)
        return self.age >= other

    def __lt__(self, other):  # 比较操作的小于规则
        print(other)
        return self.age < other

    def __le__(self, other):  # 比较操作的小于等于规则
        print(other)
        return self.age <= other

    def __bool__(self):
        return True


aa = P7(3, 2)
bb = P7(3, 2)
print(aa == bb)
print(aa != bb)


# __________________________________遍历操作


class P8:
    def __init__(self):
        self.result = 1

    # def __getitem__(self, item):
    #     self.result += 1
    #     if self.result >= 6:
    #         raise StopIteration("stop")
    #
    #     return self.result

    def __iter__(self):  # 实现迭代功能
        self.result = 1
        # return iter([1, 2, 3])
        return self

    def __next__(self):  # 实现next功能
        self.result += 1
        if self.result >= 6:
            raise StopIteration("stop")

        return self.result


p8 = P8()

pp8 = P8()
print(pp8)
print(next(pp8))
print(next(pp8))
print(next(pp8))
print(next(pp8))


# for i in p8:
#     print(i)


# __________________________描述器

class P9:
    def __init__(self):
        self.__age = 10
        self.height = 15

    # def get_age(self):
    @property
    def age(self):
        return self.__age

    @age.setter
    # def set_age(self, value):
    def age(self, value):
        if value < 0:
            value = 0
        self.__age = value

    @age.deleter
    # def del_age(self):
    def age(self):
        del self.__age

    # age = property(get_age, set_age, del_age)     # 以调用属性的方式调用方法，调用的时候不需要加括号


# aa = P9()
# aa.set_age(10)
# print(aa.get_age())

aa.age = 100

print(aa.age)


# _____________________________________

class Age:
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, instance):
        print("del")


class P10:
    age = Age()


p10 = P10()
p10.age = 1000
print(p10.age)


# ______________________________________ 类的装饰器


class check:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):  # 把类当做函数调用
        print("登录")
        self.func()


@check
def fatupuan():
    print("发图片")


fatupuan()
# send = check(fatupuan)
# send()                     #只要是这个形式就会调用__call__方法
