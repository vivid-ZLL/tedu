"""
# 练习：参照day06/exercise07.py
1. 创建学生类
    -- 数据：姓名,年龄,成绩，性别
　　 -- 行为：在控制台中打印个人信息的方法
2. 在控制台中循环录入学生信息，如果名称是空字符,退出录入。
3. 在控制台中输出每个学生信息(调用打印学生类的打印方法)
4.　打印第一个学生信息
# 11:02
"""


class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print("%s的年龄是%d,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))


# s01 = Student("赵敏",26,100,"女")
# s01.print_self_info()

"""
[ 
     {
        "name": "赵敏", 
        "age": 23, 
        "score": 100, 
        "sex": “女”
     }
]
"""
list_student_info = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    # 之前使用字典表达一个具体学生信息
    # dict_info = {"name": name, "age": age, "score": score, "sex": sex}
    stu = Student(name, age, score, sex)
    list_student_info.append(stu)

for stu in list_student_info:
    stu.print_self_info()

# 获取第一个学生信息
info = list_student_info[0]
info.print_self_info()
