# 大于60
# list01 = [21, 78, 25, 64, 58, 98, ]
# list02 = []
# for item in list01:
#     if item > 60:
#         list02.append(item)
# print(list02)

# list03 = []
# item_max = 0
# for item in range(5):
#     count = item + 1
#     list03.append(int(input("请输入第%s个数字" % count)))
#     if item_max < list03[item]:
#         item_max = list03[item]
# print(item_max)
#
# list04 = [32, 21, 45, 36, 25, 14]
# max_item = list04[0]
# for i in range(len(list04)):
#     if max_item < list04[i]:
#         max_item = list04[i]
# print(max_item)

list06 = []
list05 = [9, 25, 12, 8]
for item in list05:
    if item <= 10:
        list06.append(item)
list05 = list06[:]
print(list05)
