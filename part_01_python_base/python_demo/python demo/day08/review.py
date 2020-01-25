"""
    day07 复习
    能力提升for for
        # 结论：外层循环执行一次，内层循环执行多次。
        　　　　外层控制行，内层控制列.

        for r in range(2):#     0     1
            for c in range(3):#012   012
                pass

    函数
        定义:功能，使用一个名称，包装多个语句。
        语法:
            做
                def 名字(形参):
                    函数体

            用
                名字(实参)
"""
















list01 = [23,34,4,6]
for r in range(len(list01) - 1):
    # 作比较
    for c in range(r + 1, len(list01)):
        # list01[2]  list01[c]
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
