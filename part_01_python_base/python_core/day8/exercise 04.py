def judge_list_same(list_target):
    """
    判断列表中的元素是否重复
    :param list_target: 目标猎豹
    :return: 有重复返回True ,没有重复返回 False
    """
    for r in range(0, len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True

    return False


list01 = [1, 2, 3, 4, 56, 6, 4, 6, 4, 1]
print(judge_list_same(list01))
