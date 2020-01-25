# 练习2:定义根据两,计算几斤零几两的函数
# weight_liang = int(input("请输入两："))
# jin = weight_liang // 16
# liang = weight_liang % 16
# print(str(jin) + "斤零" + str(liang) + "两")

def get_weight_for_jin(liang_weight):
    """
        根据两,计算几斤零几两.
    :param liang_weight:需要计算的两
    :return: 元组 (斤,两)
    """
    jin = liang_weight // 16
    liang = liang_weight % 16
    return (jin,liang)
re = get_weight_for_jin(100)
print(str(re[0]) + "斤零" + str(re[1]) + "两")

