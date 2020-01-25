"""
    练习:
    判断列表中元素是否具有相同的[3,80,45,5,80,1]
    思路：所有元素俩俩比较,发现相同的则打印结果
    　　　所有元素比较结束，都没有发现相同项，则打印结果.
    15:35
"""
list01 = [3, 81, 3, 5, 81, 5]
# 取出第一个，与后面比较
# list01[0]  list01[1]

# list01[0]  list01[2]
# list01[0]  list01[3]
# for c in range(1,len(list01)):
#     # list01[0]  list01[c]
#     pass
# for c in range(2,len(list01)):
#     # list01[1]  list01[c]
#     pass
# for c in range(3,len(list01)):
#     # list01[2]  list01[c]
#     pass

# 结果：假设没有相同项
result = False
for r in range(0, len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] == list01[c]:
            print("具有相同项")
            result = True
            break  # 退出循环
    if result:
        break

if result == False:
    print("没有相同项")


