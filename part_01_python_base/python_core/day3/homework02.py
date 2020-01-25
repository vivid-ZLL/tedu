code_age = float(input("请输入年龄："))
if 0 < code_age < 150:
    if code_age < 2:
        print("婴儿")
    if code_age < 13:
        print("儿童")
    if code_age < 20:
        print("青少年")
    if code_age < 65:
        print("成年人")
    else:
        print("老年人")
elif code_age >= 150:
    print("那不可能")
else:
    print("输入有误")
