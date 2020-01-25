code_grade = float(input("请输入成绩："))

if code_grade > 100 or code_grade < 0:
    print("输入有误")
if code_grade >= 90:
    print("优秀")
elif code_grade >= 80:
    print("良好")
elif code_grade >= 60:
    print("及格")
else:
    print("不及格")
