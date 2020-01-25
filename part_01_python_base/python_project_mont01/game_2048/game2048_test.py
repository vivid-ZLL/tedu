"""
    2048游戏核心算法
"""


# list_merge = [4, 0, 0, 8]


def zero_to_end(list_merge):
    """
    零元素移动至末尾
    """
    list02 = None
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            list02 = list_merge[i]
            list_merge.remove(list_merge[i])
            list_merge.append(list02)
    # print(list_merge)


def merge(list_merge):
    """
    先将中间的零元素移到末尾
    再合并相邻相同元素
    """
    zero_to_end(list_merge)
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] *= 2
            del list_merge[i + 1]
            list_merge.append(0)


# list_merge = [2, 2, 2, 0]


def move_left(map):
    """
    地图向左移动
    """
    for i in range(len(map)):
        global list_merge
        list_merge = map[i]
        merge(list_merge)


def move_right(map):
    """
    地图向右移动
    """
    for line in map:
        global list_merge
        list_merge = line[::-1]
        # print(list_merge)
        merge(list_merge)
        # line = list_merge
        map.append(list_merge)
        # print(list_merge)
        # print(line)


list_merge = None

map = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [0, 0, 2, 2]
]

move_right(map)

print(map)
