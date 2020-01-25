list01 = []
count_red = 1
while count_red <= 6:
    int_red = int(input("请输入第%d个红球号码：" % count_red))

    if int_red in list01:
        print("号码重复")
    elif 1 <= int_red <= 33:
        list01.append(int_red)
        count_red += 1
    else:
        print("号码不在范围内")

result = []
count_blue = 1
while count_blue <= 1:
    int_blue = int(input("请输入第%s个蓝球号码：" % count_blue))
    if 1 <= int_blue <= 16:
        result.append(int_blue)
        count_blue += 1
    else:
        print("号码不在范围内")

print(result)
print(list01)
