"""
    ２０４８　游戏核心算法
"""
list_merge = None


# 练习１：零元素移至末尾
# 　　[2,0,2,0]  --> [2,2,0,0]
#    [2,0,0,2]  --> [2,2,0,0]
#    [2,4,0,2]  --> [2,4,2,0]

def zero_to_end():
    """
        零元素移动到末尾.
    """
    # 思想：从后向前，如果发现零元素，删除并追加.
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 测试．．．
# zero_to_end()
# print(list_merge)


# 练习2：将相同数字合并 14:38
# 　　[2,2,0,0]  --> [4,0,0,0]
#    [2,0,0,2]  --> [4,0,0,0]
#    [2,0,4,0]  --> [2,4,0,0]
#    [2,2,2,2]  --> [4,4,0,0]
#    [2,2,2,0]  --> [4,2,0,0]
def merge():
    """
        合并
    """
    # 先将中间的零元素移到末尾
    # 再合并相邻相同元素
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            # 将后一个累加前一个之上
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# 测试...
# merge()
# print(list_merge)

# 练习3:地图向左移动


def move_left():
    """
        向左移动
    """
    # 思想:将二维列表中每行交给merge函数进行操作
    for line in map:
        global list_merge
        list_merge = line
        merge()


# move_left()
# print(map)

def move_right():
    """
        向右移动
    """
    # 思想:将二维列表中每行(从右向左)交给merge函数进行操作
    for line in map:
        global list_merge
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge


def transpose_square_matrix():
    """
    方阵转置函数
    :param list_merge: 二维列表类型方阵
    :return:
    """

    for r in range(len(map) - 1):  # 0          1      2
        for c in range(r + 1, len(map[0])):  # 1 2 3     2 3     3
            map[r][c], map[c][r] = \
                map[c][r], map[r][c]
            # print(list01)
    # 这个算法只能转置方阵


def move_up():
    """
    方阵上移
    """
    transpose_square_matrix()
    move_left()
    transpose_square_matrix()


def move_down():
    """
    方阵下移
    """
    transpose_square_matrix()
    move_right()
    transpose_square_matrix()


map = [
    [2, 0, 0, 2],
    [4, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 2, 2],
]
# move_down()
move_down()
print(map)
