from bll import *
from model import *


class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    @staticmethod
    def int_repeat_input():
        """
        重新输入字符串,调用方法尝试将其转为数值类型
        :return:
        """
        param = StudentManagerController.int_inputer(input("请重新输入"))
        return param


    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students(self.__manager.stu_list)
        elif item == "3":
            self.remove_student()
        elif item == "4":
            self.update_student()
        elif item == "5":
            self.order_student()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入姓名：")

        age = StudentManagerController.int_inputer(input("请输入学生的年龄"))

        score = StudentManagerController.int_inputer(input("请输入学生的成绩"))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)


    def __output_students(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def remove_student(self):
        id = StudentManagerController.int_inputer("删除学生的id编号")
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def update_student(self):

        id = StudentManagerController.int_inputer(input("请输入修改学生的id编号"))
        name = input("请输入姓名：")

        age = StudentManagerController.int_inputer(input("请输入修改学生的年龄"))

        score = StudentManagerController.int_inputer(input("请输入修改学生的成绩"))
        stu_info = StudentModel(name, age, score, id)
        if self.__manager.update_student(stu_info):
            print("修改成功")
        else:
            print("修改失败")

    def order_student(self):
        """
            根据成绩对学生列表进行排序
        """
        self.__manager.order_student(self.__manager.stu_list)

        print("排序后结果如下")
        for item in self.__manager.stu_list:
            print("姓名:", item.name, "分数", item.score)
