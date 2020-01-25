while True:
    int_side = int(input("请输入边长："))
    int_space = int_side - 2
    str_space = int_space * " "
    print("*" * int_side)
    for item in range(int_space):
        print("*%s*" % str_space)
    if int_side > 1:
        print("*" * int_side)
