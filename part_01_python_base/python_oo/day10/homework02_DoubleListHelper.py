"""
[
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
在二维列表中，获取13位置，向左，3个元素
在二维列表中，获取22位置，向上，2个元素
在二维列表中，获取03位置，向下，2个元素
"""


class Vector2:
    """
        二维向量
        可以表示位置/方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        """
            在二维列表中获取指定位置，指定方向，指定数量的元素.
        :param target: 二维列表
        :param vect_pos: 指定位置
        :param vect_dir: 指定方向
        :param count: 指定数量
        :return: 列表
        """
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result

    @staticmethod
    def get_all_elements(target, vect_pos, negative=False):
        """

        :param target:指定二维列表
        :param negative:指定二维列表
        :param vect_pos: 指定位置
        :return: 列表
        """
        """
                       matrix 
                ['a', 'b', 'c', 'e'],
                ['s', 'f', 'c', 's'],
                ['a', 'd', 'e', 'e'],

        """
        list_result = []

        #
        # dir = 上
        vect_pos.x -= 1
        DoubleListHelper.get_element(list_result, target, vect_pos, negative)

        # dir =  下
        vect_pos.x += 2
        DoubleListHelper.get_element(list_result, target, vect_pos, negative)

        # dir =  左
        vect_pos.y -= 1
        vect_pos.x -= 1

        DoubleListHelper.get_element(list_result, target, vect_pos, negative)

        # dir =  右
        vect_pos.y += 2
        DoubleListHelper.get_element(list_result, target, vect_pos, negative)

        return list_result

    @staticmethod
    def get_element(list_result, target, vect_pos, negative):
        if not negative:
            if vect_pos.x >= 0 and vect_pos.y >= 0:
                element = target[vect_pos.x][vect_pos.y]
                list_result.append(element)
        else:
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)


if __name__ == "__main__":
    matrix = [['a', 'b', 'c', 'd'],
              ['e', 'f', 'g', 'h'],
              ['i', 'j', 'k', 'l'],
              ]
    re = DoubleListHelper.get_all_elements(matrix, Vector2(0, 1), negative=True)

    print(matrix[0][1])
    print(re)
