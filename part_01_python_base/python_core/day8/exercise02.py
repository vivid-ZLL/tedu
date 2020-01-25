def converse_weight(param_weight):
    """
    根据两计算几斤零几两
    :param param_weight: 需要计算的两
    :return: 元组(斤,两)
    """
    jin = param_weight // 16
    liang = param_weight % 16
    return (jin, liang)


re = converse_weight(178)

print("共%d斤%d两" % re)
