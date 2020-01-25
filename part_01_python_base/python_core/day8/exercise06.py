def order_list(list_target):
    """
    将列表降序排列
    :param list_target: 目标列表
    :return:
    """
    for i in range(len(list_target) - 1):  # 0 1 2 3 4
        for c in range(i + 1, len(list_target)):  # 1 2 3 4 5
            if list_target[i] > list_target[c]:
                list_target[i], list_target[c] = list_target[c], \
                                                 list_target[i]
    # return list_target


list01 = [3, 80, 45, 5, 45, 7, 1]  # len(list01) = 6
order_list(list01)

print(list01)
