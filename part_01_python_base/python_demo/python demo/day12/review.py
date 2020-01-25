"""
    day12 复习
    封装
        数据角度：将多个变量封装到一个自定义类中。
                优势：
                    符合人类的思考方式
                    可以将数据与对数据的操作封装到一起

        功能角度：对外提供必要的功能,隐藏实现的细节.
                 DoubleListHelper.get_elements()
                 -- 私有化：将名称命名为以双下划线开头.
                          内部修改成员名称
                 -- 属性：对实例变量的保护(拦截读/写操作)
                 -- __slots__:限定类创建的对象只能有固定的实例变量.

        设计角度：
            分而治之:将大的需求分解为多个类，每个类负责一个职责。
            变则疏之：遇到变化点单独封装为一个类
            ------------------
            高内聚：一个类有且只有一个发生变化的原因
            低耦合：类与类的关系松散
"""


# 数据角度
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # ....

    def print_self(self):
        print(self.name, self.age)


s01 = Student("无忌哥哥", 28)
# 通过对象调用实例成员
s01.name = "张无忌"
s01.print_self()


class Student02:
    def __init__(self, name, age):
        self.name = name
        # self.age = age
        # self.__age = age
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value


s01 = Student02("无忌哥哥", 28)
s01.name = "张无忌"


class Student03:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.__age = age
        # self.set_age(age)

    def __get_age(self):
        return self.__age

    def __set_age(self, value):
        self.__age = value

    age = property(__get_age,None)


# s01 = Student03("无忌哥哥", 28)
# s01.name = "张无忌"
# print(s01.age)


class Student04:
    def __init__(self, name, age):
        self.name = name
        # 只读
        self.__age = age

    @property
    def age(self):
        return self.__age


class Student05:
    def __init__(self, name, age):
        self.name = name
        # 只写
        self.__age = age

    def __set_age(self, value):
        self.__age = value

    age = property(None, __set_age)


s01 = Student05("zs", 10)
s01.age = 11


# print(s01.age)


class Student06:
    def __init__(self, name, age):
        self.name = name
        # 可读可写
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


s01 = Student06("zs", 10)
s01.name = "ls"
s01.age = 11
print(s01.age)


class Student07:
    __slots__ = ("name")

    def __init__(self, name):
        self.name = name


s01 = Student07("wj")


# s01.name = "无忌"
# print(s01.name)

# 添加了新实例变量
# s01.nmae = "无忌"
# print(s01.nmae)

class Student08:
    __slots__ = ("__age")

    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


s01 = Student08(10)
s01.age = 11
print(s01.age)
