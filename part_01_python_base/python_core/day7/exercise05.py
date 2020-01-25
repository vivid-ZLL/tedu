list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

result = []
result = []
for r in range(len(list01[0])):
    for c in range(len(list01)):
        result.append(list01[c][r])
    result.append(result)
    result = []
print(result)

# result = []
# for c in range(4):
#     line = []
#     result.append(line)
#     #00   10   20  30
#     for r in range(4):
#         line.append(list01[r][c])
