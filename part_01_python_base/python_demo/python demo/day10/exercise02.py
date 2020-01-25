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
    Student("明玉", 30, 95, "女"),
    Student("无忌", 29, 70, "男"),
    Student("张三丰", 130, 96, "男"),
]


# 练习1:定义函数,在list01中查找name是"苏大强"的对象.
#      将名称与年龄打印在控制台中
# 14:12
def find01():
    for item in list01:
        if item.name == "苏大强":
            return item
            # 如果没找到，则返回空。而函数返回值默认就是空,所以可以不写.
            # return None


stu = find01()
print(stu.name, stu.age)


# 练习2:定义函数,在list01中查找所有女同学.
#      将名称与性别打印在控制台中
# 14:33
def fun02():
    result = []
    for item in list01:
        if item.sex == "女":
            result.append(item)
    return result


re = fun02()
for item in re:
    print(item.name, item.sex)


# 练习3:定义函数,查找年龄>=30的学生数量
def fun03():
    count = 0
    for item in list01:
        if item.age >= 30:
            count += 1
    return count


print(fun03())


# 练习4:定义函数,将list01中所有学生的成绩归零.
# 14:52
def set01():
    for item in list01:
        item.score = 0


set01()
for item in list01:
    print(item.name, item.score)


# 练习5:获取list01中所有学生的名字
# 15:00
def find04():
    result = []
    for item in list01:
        result.append(item.name)
    return result


re = find04()
print(re)


# 练习6:定义函数，在list01中查找年龄最大的学生对象
def find05():
    max_stu = list01[0]
    for i in range(1, len(list01)):
        if max_stu.age < list01[i].age:
            max_stu = list01[i]
    return max_stu


re = find05()
re.print_self_info()
