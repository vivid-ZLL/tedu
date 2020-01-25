# 练习:将下列代码，定义到函数中，再调用一次.
def print_rectangle(r_count,c_count,char):
    """
        打印矩形
    :param r_count: 行数
    :param c_count: 列数
    :param char: 填充的字符　
    """
    for r in range(r_count):
        # 内层循环控制列　
        for c in range(c_count):
            print(char, end=" ")
        print()

print_rectangle(5,2,"#")

