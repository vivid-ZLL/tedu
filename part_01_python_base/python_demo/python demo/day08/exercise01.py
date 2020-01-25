"""
    练习1:定义计算四位整数，每位相加和的函数.
    测试："1234"   "5428"
"""


def each_unit_sum(number):
    """
        计算整数的每位相加和
    :param number: 四位整数
    :return: 相加的结果
    """
    result = number % 10
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000
    return result


# 测试
re01 = each_unit_sum(1234)
print(re01)
re01 = each_unit_sum(4875)
print(re01)
