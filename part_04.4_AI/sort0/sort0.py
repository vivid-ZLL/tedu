import numpy as np


class Sort0:
    @staticmethod
    def basic():
        """
        联合间接排序支持为待排序列排序，若待排序列值相同，则利用参考序列作为参考继续排序。最终返回排序过后的有序索引序列。
        """
        # 案例：先按价格排序，再按销售量倒序排列。

        prices = np.array([92, 83, 71, 92, 40, 12, 64])
        volumes = np.array([100, 251, 4, 12, 709, 34, 75])
        print(volumes)
        names = ['Product1', 'Product2', 'Product3', 'Product4', 'Product5', 'Product6', 'Product7']
        ind = np.lexsort((volumes * -1, prices))
        print(ind)
        for i in ind:
            print(names[i], end=' ')

    @staticmethod
    def complex0():
        # 复数数组排序
        #
        # 按照实部的升序排列，对于实部相同的元素，参考虚部的升序，直接返回排序后的结果数组。
        target = '负数数组'
        np.sort_complex(target)

    @staticmethod
    def charu_sort():
        """
        若有需求需要向有序数组中插入元素，使数组依然有序，numpy提供了searchsorted方法查询并返回可插入位置数组。
        """
        #             0  1  2  3  4  5  6
        a = np.array([1, 2, 4, 5, 6, 8, 9])
        b = np.array([7, 3])
        c = np.searchsorted(a, b)
        print(c)
        d = np.insert(a, c, b)
        print(d)


if __name__ == '__main__':
    s01 = Sort0()
    # s01.basic()
    s01.charu_sort()
