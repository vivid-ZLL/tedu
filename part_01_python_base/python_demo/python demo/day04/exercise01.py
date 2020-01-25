"""
    练习1:在控制台中，获取一个开始值，一个结束值。
        　将中间的数字打印出来。
        例如：开始值3  结束值10
              打印4  5  6  7  8  9
    9:43
"""

begin = int(input("请输入开始值："))
end = int(input("请输入结束值："))

while begin < end - 1:
    begin += 1
    print(begin)







