dict_name = {}
count = 1
while True:
    name = input("请输入姓名：")

    if name == "":
        break
    dict_name[name] = []

    while True:
        interest = input("请输入第%s个喜好" % count)
        if interest == "":
            count = 1
            break
        count += 1
        dict_name[name].append(interest)
        # print(dict_name[name])

# print(dict_name)

for name, interest in dict_name.items():
    print("姓名：%s" % name)
    for i in range(len(interest)):
        print("第%d个喜好是：%s" % (i + 1, interest[i]))
