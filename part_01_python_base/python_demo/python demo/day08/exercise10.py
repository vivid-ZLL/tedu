# 练习:定义函数，数值相加的函数.
def adds(*args):
    # result = 0
    # for item in args:
    #     result += item
    # return result

    return sum(args)


print(adds(1, 22, 3, 3, 4, 5, 6))
print(adds(1, 4, 5, 6))
