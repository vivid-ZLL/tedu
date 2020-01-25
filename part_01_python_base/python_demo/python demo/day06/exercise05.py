# 练习2: 在控制台中循环录入学生信息(姓名,年龄,成绩,性别).
# 　　　如果名称输入空字符, 则停止录入.
# 将所有信息逐行打印出来.
"""16:08
# 字典内嵌列表:
{
    "张无忌":[28,100,"男"],
}
"""
dict_student_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_student_info[name] = [age, score, sex]

# 打印所有学生信息
for name,list_info in dict_student_info.items():
    print("%s的年龄是%d,成绩是%d,性别是%s"%(name,list_info[0],list_info[1],list_info[2]))

