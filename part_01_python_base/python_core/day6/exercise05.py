dict_student_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    grade = int(input("请输入成绩:"))
    sex = input("请输入性别:")
    dict_student_info[name] = [age, grade, sex]
for key, list_value in dict_student_info.items():
    print("%s,年龄%d,成绩%d,性别%s" % (key, list_value[0],
                                 list_value[1], list_value[2]))
