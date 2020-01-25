"""
# 列表内嵌字典:
[
    {"name":"张无忌","age":28,"score":100,"sex":"男"},
]
5:05 上课
"""
list_student_info = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_info = {"name": name, "age": age, "score": score, "sex": sex}
    list_student_info.append(dict_info)

for dict_info in list_student_info:
    print("%s的年龄是%d,成绩是%d,性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
# 获取第一个学生信息
dict_info = list_student_info[0]
print("第一个录入的是：%s,年龄是%d,成绩是%d,性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
