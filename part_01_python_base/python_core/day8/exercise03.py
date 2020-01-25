def grade_evaluation(taget_grade):
    """
    根据成绩计算等级
    :param taget_grade: 成绩分数
    :return: 成绩判定结果
    """
    if taget_grade > 100 or taget_grade < 0:
        return "输入有误"
    if taget_grade >= 90:
        return "优秀"
    if taget_grade >= 80:
        return "良好"
    if taget_grade >= 60:
        return "及格"

    return "不及格"


while True:
    grade = float(input("请输入成绩："))
    re = grade_evaluation(grade)
    print(re)

