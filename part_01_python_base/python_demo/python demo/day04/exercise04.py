# 练习:循环根据成绩判断等级,如果录入空字符串则退出程序.
# 如果成绩录入错误次数达到３．则退出成绩并提示"成绩错误过多"

count = 0
while count < 3:
    str_score = input("请输入成绩：")
    if str_score == "":
        break  # 不会执行else语句
    score = int(str_score)
    if score > 100 or score < 0:
        print("输入有误")
        count += 1
    elif 90 <= score:
        print("优秀")
    elif 80 <= score:
        print("良好")
    elif 60 <= score:
        print("及格")
    else:
        print("不及格")
else:
    print("成绩错误过多")
