"""
    总结不建议的写法：
        1. 在类外添加实例成员
        2. 通过类访问实例方法(特殊情况除外)
        3. 通过实例访问类成员
    17:10
"""


class Student:
    count = 0

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_self(self):
        print(self.name, self.sex)


s01 = Student("无忌", "男")
s02 = Student("赵敏", "女")
s01.print_self()
print(Student.count)

"""
#不建议的写法:
        self.fun01()
    def fun01(self):
        # 也是创建实例变量
        self.aaa = 10

class Student:
    pass

s01 = Student()
s01.name = "无忌"
s01.sex = "男"
print(s01.name)
print(s01.sex)

# 可以通过类名访问实例方法,但必须手动传递对象地址
Student.print_self(s02)

# 也可以通过对象地址访问类成员
print(s01.count)
"""
