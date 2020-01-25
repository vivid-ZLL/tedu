"""
    练习：定义对象计数器。
    定义老婆类，创建３个老婆对象。
    可以通过类变量记录老婆对象个数，
    可以通过类方法打印老婆对象个数。
    要求：画出内存图.
"""


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print("我有%d房" % cls.count)

    def __init__(self, name):
        self.name = name
        Wife.count += 1


w01 = Wife("如花")
w02 = Wife("小乔")
w03 = Wife("大乔")
# print(Wife.count)
Wife.print_count()
