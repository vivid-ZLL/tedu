def sum_of_each_unit(target_number):
    """
    计算四位整数每位相加的和
    :param target_number: 四位整数
    :return: 每位相加的和
    """
    result_of_function = target_number % 10
    result_of_function += target_number // 10 % 10
    result_of_function += target_number // 100 % 10
    result_of_function += target_number // 1000
    return result_of_function


int_number = int(input("请输入四位整数:"))
result = sum_of_each_unit(int_number)
print("结果是:" + str(result))
