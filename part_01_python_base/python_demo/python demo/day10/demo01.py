"""
    实例对象内存图
    练习：exercise01.py
"""


class Student:
    def __init__(self, name, age, score, sex):
        # 创建实例变量
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        # 读取实例变量
        print("%s的年龄是%d,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))


list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 62, "男"),
]

s01 = list01[0]
s01.name = "小赵"
s01.score = 98

print(list01[0].name, list01[0].score)
print(list01[1].name, list01[1].score)

list01[0].print_self_info()  # 小赵的年龄是28,成绩是98,性别是女
list01[1].print_self_info()  # 苏大强的年龄是68,成绩是62,性别是男
