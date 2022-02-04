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



class Person:

     def shili(self):
          print('实例方法',self)

     @classmethod
     def lei(cls):
          print('类方法',cls)

     @staticmethod
     def jintai():
          print("静态方法")


p1=Person()
p1.shili()
Person.lei()
Person.jintai()
print(Person.__dict__)     #可以使用类名.__dict__来查看类里面的方法
#print(p1.__dict__)        #不能使用对象名.__dict__来查看类里面的方法

