# 练习:矩阵转置  将二维列表的列，变成行，形成一个新列表.
#   第一列变成第一行
#   第二列变成第二行
#   第三列变成第三行
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

# result = []
# for c in range(4):
#     line = []
#     result.append(line)
#     #00   10   20  30
#     for r in range(4):
#         line.append(list01[r][c])

result = []
for c in range(len(list01[0])):
    result.append([])
    for r in range(len(list01)):
        result[c].append(list01[r][c])

print(result)