# 练习:定义　判断列表中是否存在相同元素的　函数
# list01 = [3, 81, 3, 5, 81, 5]
# result = False
# for r in range(0, len(list01) - 1):
#     for c in range(r + 1, len(list01)):
#         if list01[r] == list01[c]:
#             print("具有相同项")
#             result = True
#             break  # 退出循环
#     if result:
#         break
# if result == False:
#     print("没有相同项")

# def is_repeating(list_target):
#     for r in range(0, len(list_target) - 1):
#         for c in range(r + 1, len(list_target)):
#             if list_target[r] == list_target[c]:
#                 return "具有相同项"
#     return "没有相同项"

def is_repeating(list_target):
    for r in range(0, len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True  # 有重复
    return False  # 没有重复


print(is_repeating([3, 8, 23, 5, 81, 1]))
