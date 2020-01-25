list_student_info = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = input("请输入年龄:")
    grade = int(input("请输入成绩:"))
    sex = input("请输入性别:")
    list_student_info.append(
        {"name": name, "age": age, "grade": grade, "sex": sex})

for dict_info in list_student_info:
    print("%s,年龄%s,成绩%d,性别%s" %
          (dict_info["name"], dict_info["age"],
           dict_info["grade"], dict_info["sex"]))