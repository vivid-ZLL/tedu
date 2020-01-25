# 定义列表升序排列的函数
# list01= [43,4,5,6,7]
# for r in range(len(list01) - 1):
#     for c in range(r + 1, len(list01)):
#         if list01[r] > list01[c]:
#             list01[r], list01[c] = list01[c], list01[r]
#
# print(list01)

def sort(list_target):
    # 满足以下两个条件，就无需通过返回值传递结果。
    # 1.传入的是可变对象
    # 2.函数体修改的是传入的对象
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
list01 = [43, 4, 5, 6, 7]
sort(list01)
print(list01)
