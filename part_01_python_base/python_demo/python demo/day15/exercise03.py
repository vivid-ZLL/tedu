"""
    定义函数，在控制台中获取成绩的函数.
    要求：如果异常，继续获取成绩，直到得到正确的成绩为止.
         成绩还必须在0--100之间
    17:05
"""


def get_score():
    while True:
        str_result = input("请输入成绩：")
        try:
            score = int(str_result)
        except:
            print("输入的不是整数")
            continue
        if 0 <= score <= 100:
            return score
        else:
            print("超过范围")


print(get_score())
