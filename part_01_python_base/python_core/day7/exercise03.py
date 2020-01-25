# for r in range(4):
#     for c in range(5):
#         if r % 2 == 0:
#             print("*", end=" ")
#         else:
#             print("#", end=" ")
#     print()

# for r in range(4):
#     for
# ------------------------分割线-------------------------------
# c = 1
# for r in range(4):
# for c in range(4):
#     print("*"*c)
#     c += 1
# print()

# -------------------------分割线------------------------------
# for r in range(4):
#     for c in range(r + 1):
#         print("*", end="")
#
#     print()

# -------------------------分割线-------------------------------
# list01 = [3, 80, 45, 5, 45, 7, 1]  # len(list01) = 6
# for i in range(len(list01) - 1):  # 0 1 2 3 4
#     for c in range(i + 1, len(list01)):  # 1 2 3 4 5
#         if list01[i] > list01[c]:
#             list01[i], list01[c] = list01[c], list01[i]
# print(list01)
# ------------------------分割线----------------------------
list01 = [3, 80, 45, 5, 1, 1, 80]
count = True
for i in range(len(list01) - 1):  # 0 1 2 3 4
    for c in range(i + 1, len(list01)):  # 1 2 3 4 5
        if list01[i] == list01[c]:
            count = False
if count:
    print("没有发现相同项")
else:
    print("有相同项")

# list01 = [3, 80, 45, 5, 1, 80, 3]
# for i in range(len(list01) - 1):  # 0 1 2 3 4
#     for c in range(i + 1, len(list01)):  # 1 2 3 4 5
#         if list01[i] == list01[c]:
#             print("相同元素为:")
#             print(list01[i])
