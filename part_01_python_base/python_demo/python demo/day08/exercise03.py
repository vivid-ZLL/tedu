# 练习:定义 根据成绩计算等级 的函数
# score = int(input("请输入成绩："))
# if score > 100 or score < 0:
#     print("输入有误")
# elif 90 <= score:
#     print("优秀")
# elif 80 <= score:
#     print("良好")
# elif 60 <= score:
#     print("及格")
# else:
#     print("不及格")

# def get_score_level(score):
#     if score > 100 or score < 0:
#         return "输入有误"
#     elif 90 <= score:
#         return "优秀"
#     elif 80 <= score:
#         return "良好"
#     elif 60 <= score:
#         return "及格"
#     else:
#         return "不及格"

def get_score_level(score):
    if score > 100 or score < 0:
        return "输入有误"
    if 90 <= score:
        return "优秀"
    if 80 <= score:
        return "良好"
    if 60 <= score:
        return "及格"
    return "不及格"


print(get_score_level(80))
