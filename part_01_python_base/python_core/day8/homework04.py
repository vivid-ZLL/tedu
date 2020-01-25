def judge_prime_number(number_target):
    """
    判断素数
    :return: 是则返回True,不是则返回False
    """
    for item in range(2, number_target):  # 2 3 4 5 ...
        if number_target % item == 0:
            return False
    return True


# list01 = []
# for item in number_list:
#     if judge_prime_number(item):
#         list01.append(item)
def get_prime(begin, end):
    """
    获取范围内的素数
    :param begin:开始的数字(包含)
    :param end:结束的数字(不包含)
    """
    return [number for number in range(2, end) if judge_prime_number(number)]


print(get_prime(-2, 39))
