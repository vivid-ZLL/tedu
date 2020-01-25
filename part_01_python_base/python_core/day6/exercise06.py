dict_student_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    grade = int(input("请输入成绩:"))
    sex = input("请输入性别:")
    dict_student_info[name] = {"age": age, "grade": grade, "sex": sex}

for key, dict_value in dict_student_info.items():
    print("%s,年龄%d,成绩%d,性别%s" % (key, dict_value["age"],
                                 dict_value["grade"],
                                 dict_value["sex"]))


