# 练习：定义方阵转置函数
# list01 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]
# for c in range(1, len(list01)):  # 1 2 3
#     for r in range(c, len(list01)):
#         list01[r][c - 1], list01[c - 1][r] = list01[c - 1][r], list01[r][c - 1]
# print(list01)

def square_matrix_transpose(sqr_matrix):
    """
        方阵转置
    :param sqr_matrix: 二维列表类型的方阵
    """
    for c in range(1, len(sqr_matrix)):
        for r in range(c, len(sqr_matrix)):
            sqr_matrix[r][c - 1], sqr_matrix[c - 1][r] = sqr_matrix[c - 1][r], sqr_matrix[r][c - 1]


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# 矩阵转置的转置等于原矩阵
square_matrix_transpose(list01)
print(list01)
square_matrix_transpose(list01)
print(list01)
