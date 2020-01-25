"""
    古代的秤一斤是１６两  33  二斤　　一两
    练习：在控制台中获取两，计算是几斤零几两。
    　　　显示几斤零几两
    15:43
"""
weight_liang = int(input("请输入两："))
jin = weight_liang // 16
liang = weight_liang % 16
print(str(jin) + "斤零" + str(liang) + "两")











