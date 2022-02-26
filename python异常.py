# 1/0                      ZeroDivisionError    除0异常
# ————————————————————————————————————————————————————
# print(aa)               NameError            名字异常
# ————————————————————————————————————————————————————
# 1+"a"                   TypeError            类型异常
# ————————————————————————————————————————————————————
# a=[1,2]
# a[10]                   IndexError            索引异常
# ————————————————————————————————————————————————————
# dic={'bb':10,'ee':1}
# dic[aa]                KeyError             字典键异常
# ————————————————————————————————————————————————————
# int("a")                  ValueError           值异常
# ————————————————————————————————————————————————————
# a=10
# a.append()                AttributeError     属性异常
# ————————————————————————————————————————————————————
# it=iter([0,1])
# next(it)
# next(it)
# next(it)                   StopIteration     迭代异常
# ————————————————————————————————————————————————————

# 异常继承数   BaseException   ->   SystemExit            由系统函数所触发的异常类
#                                 KeyboardInterrupt     当用户使用键盘点击中断时所产生的异常类
#                                 GeneratorExit         调用生成器是产生的异常类
#                                 Exception             内置的非系统的异常派生类（手动抛出异常）

try:  # 尝试代码，如果出现异常跳过代码行进入except
    1 / 1
    print(aa)

except ZeroDivisionError:  # 要捕捉什么类型的异常，如果没出现异常将跳过此语句
    print("除0错误")

except NameError as ne:  # except语句可以出现多条
    print("名字异常", ne)  # 可以把异常打印出来

except (ValueError, IndexError):  # 同时处理多个异常
    print("多个异常", )

else:  # 如果没出现异常将执行此语句
    print("没有异常")

finally:  # 不管有没有异常都会执行
    print("不管有没有异常都会执行")

# with语句  语法   with 上下文表达式 [as target]:     #as是可选的，意义是将上下文对象赋予给target
#                      with-body                  执行完语句体会自动调用__exit__方法

with open("shotgun.txt", "r+") as f:
    pass
    # print(f.read())


# 手动抛出异常
def age(age):
    if age <= 0 or age > 200:
        raise ValueError("年龄错误")  # 手动抛出异常
    else:
        print("张三的年龄是：%d" % age)


try:
    age(-1)
except ValueError as v:
    print(v)


# 上下文管理器
class Test:  # 自定义上下文管理器
    def __enter__(self):  # 在执行with语句前会执行的代码
        print("enter")

        return self  # 返回值是用于as的将上下文对象赋予as的对象

    def __exit__(self, exc_type, exc_val, exc_tb):  # 执行完with-body后自动调用退出，exc_type异常的类别
        # exc_val 错误提示信息
        print(self, exc_type, exc_val, exc_tb)  # exc_tb  追踪的信息
        import traceback
        print(traceback.extract_tb(exc_tb))  # 打印出追踪信息，错误在哪个文件那一行

        # return True     #表示接收到异常后不做处理
        # return False    #表示接收到异常后会往外抛


with Test() as x:  # 在执行这语句之前会先调用__enter__(self)，然后调用Test() as x，再调用__exit__(self)
    print("body", x)

# 使用生成器来制作上下文管理器
# import contextlib
# @contextlib.contextmanager
# def test():
#     print(1)
#     yield "aaaaa"    # 返回值是用于as的将上下文对象赋予te的对象
#     print(3)
#
# with test() as te:
#     print(2,te)

import contextlib


@contextlib.contextmanager
def zero():
    try:
        yield

    except ZeroDivisionError as z:
        print("Error", z)


with zero():
    print(1 / 0)


# 定义异常类
class lessZero(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "他妈的小于零了"


def age(age):
    if age <= 0 or age > 200:
        raise lessZero("负数错误")  # 手动抛出异常
    else:
        print("张三的年龄是：%d" % age)


try:
    age(-1)
except lessZero as l:
    print(l)
