"""
    使用标准属性,封装变量.
"""

class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    @property  # 创建property对象，只负责拦截读取操作
    def age(self):
        return self.__age

    @age.setter  # 只负责拦截写入操作
    def age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("我不要")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if 40 <= value <= 60:
            self.__weight = value
        else:
            raise ValueError("我不要")

w01 = Wife("铁锤公主", 30, 50)
w01.age = 25
print(w01.age)
w01.weight = 45
print(w01.weight)
