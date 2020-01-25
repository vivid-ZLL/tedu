class Student:
    def __init__(self, name, age, grade, sex):
        self.name = name
        self.age = age
        self.grade = grade
        self.sex = sex

    def print_self_info(self):
        print("%s,年龄%s,成绩%s,性别%s" % (self.name, self.age, self.grade, self.sex))


def find01():
    for item in list01:
        if item.name == "苏大强":
            return item
        # return None 可以不写


list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 62, "男"),
    Student("明玉", 30, 95, "女"),
    Student("无忌", 29, 70, "男"),
    Student("张三丰", 130, 96, "男"),
    Student("❤Alice❤", 21, 99, "女")
]


# stu = find01()
# print(stu.name,stu.age)

def find02():
    global result
    result = []
    for item in list01:
        if item.sex == "女":
            result.append(item)
    return result


# stu = find02()
# for item in stu:
#     item.print_self_info()


def find03():
    count = 0
    for item in list01:
        if item.age >= 30:
            count += 1
    return count


# print("年龄大于30岁的人共有%d个" % find03())


def find04():
    for item in list01:
        item.grade = 0

#
# find04()
# for item in list01:
#     item.print_self_info()

def find05():
    result = []
    for item in list01:
        result.append(item.name)
    return result


# print(find05())

def find06():
    max_stu = list01[0]
    for i in range(1, len(list01)):
        if list01[i].age > max_stu.age:
            max_stu = list01[i]
    return max_stu


re = find06()
re.print_self_info()