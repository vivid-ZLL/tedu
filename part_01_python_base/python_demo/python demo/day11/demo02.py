"""
    使用property(读取方法，写入方法)对象,封装变量.
"""
class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        # self.set_age(age)
        self.age = age
        # self.set_weight(weight)
        self.weight = weight

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("我不要")

    # 属性  property对象拦截对age类变量的读写操作
    age = property(get_age,set_age)

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if 40 <= value <= 60:
            self.__weight = value
        else:
            raise ValueError("我不要")

    weight = property(get_weight,set_weight)

w01 = Wife("铁锤公主", 30, 50)
# w01.set_age(25)
w01.age = 25
print(w01.age)
w01.weight = 45
print(w01.weight)

