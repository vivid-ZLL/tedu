# 列表排序(升序小　-->  大)
# [3,80,45,5,7,1]
# 目标:列表中所有元素两两比较
# 思想:
# 　取出第一个元素,与后面元素进行比较.
# 　取出第二个元素,与后面元素进行比较.
# 　取出第三个元素,与后面元素进行比较.
#   ...
#   取出倒数第二个元素,与后面元素进行比较.
#   如果取出的元素大于(>)后面的元素,
#       则交换
# 14:47
list01 = [3, 80, 45, 5, 7, 1]

# 取出第一个元素,与后面元素进行比较
# list01[0]  list01[1]
# list01[0]  list01[2]
# list01[0]  list01[3]
# for c in range(1,len(list01)):
#     # list01[0]  list01[c]
#     pass
# 取出第二个元素,与后面元素进行比较
# for c in range(2,len(list01)):
#     # list01[1]  list01[c]
#     pass
# 取出第三个元素,与后面元素进行比较
# for c in range(3,len(list01)):
#     # list01[2]  list01[c]
#     pass
# 15:22 上课
# 取数据
for r in range(len(list01) - 1):
    # 作比较
    for c in range(r + 1, len(list01)):
        # list01[2]  list01[c]
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]

print(list01)
