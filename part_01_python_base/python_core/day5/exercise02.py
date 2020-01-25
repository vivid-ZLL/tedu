list_grade = []
while True:
    str_input = (input("请输入学生成绩："))
    if str_input == "":
        break
    list_grade.append(int(str_input))
for item in list_grade:
    print(item)
print("最高分",max(list_grade))
print("最低分",min(list_grade))
print("平均分",sum(list_grade) / len(list_grade))
