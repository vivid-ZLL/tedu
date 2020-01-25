list01 = []
i = int(input("请输入样本总数："))
for item in range(i):
    message = "请输入第%s个数字" % (item + 1)
    int_input = input(message)
    list01.append(int_input)
print(list01)
min_valve = list01[0]
for item in range(1, len(list01)):
    if min_valve > list01[item]:
        min_valve = list01[item]
        print(min_valve)
print(min_valve)
