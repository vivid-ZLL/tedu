# dict_student_info = {"Alice": ["Alice", 18, 99, "女"],
#                      "Marisa": ["Marisa", 18, 75, "女"]
#                      }
#


class Student:
    def __init__(self, name, age, grade, sex):
        self.name = name
        self.age = age
        self.grade = grade
        self.sex = sex

    def print_self_info(self):
        print("%s,年龄%s,成绩%s,性别%s" % (self.name, self.age, self.grade, self.sex))


c01 = Student("alice", 18, 99, "女")
