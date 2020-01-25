list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
result = []

for r in range(len(list01) - 1):  # 0          1      2
    for c in range(r + 1, len(list01[0])):  # 1 2 3     2 3     3
        list01[r][c], list01[c][r] = list01[c][r], list01[r][c]
        # print(list01)
print(list01)
# 这个算法只能转置方阵
