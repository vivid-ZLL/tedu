def star_printer(row, counter,char):
    """

    :param row: 行数
    :param counter: 列数
    :param char: 填充字符
    :return:
    """
    for r in range(row):
        for c in range(counter):
            print(char, end=" ")

        print()


row_input = int(input("请输入行数:"))
counter_input = int(input("请输入列数:"))
char_input = input("请输入填充字符:")
star_printer(row_input, counter_input,char_input)
