def transpose_square_matrix(list_target):
    """
    方阵转置函数
    :param list_target: 二维列表类型方阵
    :return:
    """

    for r in range(len(list_target) - 1):  # 0          1      2
        for c in range(r + 1, len(list_target[0])):  # 1 2 3     2 3     3
            list_target[r][c], list_target[c][r] = \
                list_target[c][r], list_target[r][c]
            # print(list01)
    # 这个算法只能转置方阵


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

transpose_square_matrix(list01)
print(list01)
