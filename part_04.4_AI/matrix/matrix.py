"""
矩阵相关操作
"""
import math

import numpy as np


class Matrix:
    def __init__(self):
        self.ary = np.arange(1, 10).reshape(3, 3)
        self.m = np.matrix(self.ary)
        self.m02 = np.mat('1,2,3;4,5,6')

    @staticmethod
    def solute_equation():
        """
            解二元一次方程
            3x + 3.2y = 118.4
            3.5x + 3.6y = 135.2
        """
        prices = np.mat('3 3.2;3.5 3.6')
        totals = np.mat('118.4;135.2')
        x = np.linalg.lstsq(prices, totals)
        print(x)
        x_ = np.linalg.solve(prices, totals)
        print(x_)

    @staticmethod
    def fibo():
        """
            用矩阵实现斐波那契数列
            1  1   2   1    3   2    5   3
            1  0   1   1    2   1    3   2
             F^1    F^2      F^3 	  F^4  .
        """
        for n in range(2, 10):
            print(int((np.mat('1. 1.; 1. 0.') ** (n - 1))[0, 0]))

    @staticmethod
    def funcs():
        """
            数组的通用函数
        """
        a = np.array([1, 2, 3, 4, 5, 6])
        b = np.mat('10 20 30;40 50 60')
        print(b.clip(20, 40))
        """
        数组的裁剪
        [[20 20 30]
        [40 40 40]]
        """

        print(a.compress(a > 2))
        """
        数组的压缩
        [3 4 5 6]      
        """

        print(a.prod())
        """
        所有元素进行累乘
        """

        print(a.cumprod())
        """
        返回逐一累乘数组
        [  1   2   6  24 120 720]
        """

        # 加法通用函数
        print('初始数组:', a)
        print('两数组相加:', np.add(a, a))  # 两数组相加
        print('数组累加和:', np.add.reduce(a))  # a数组元素累加和
        print('累加和过程:', np.add.accumulate(a))  # 累加和过程
        print('外和:', np.add.outer([10, 20, 30], a))  # 外和
        print('外积:', np.outer([10, 20, 30], a))  # 外积

        print('-------------除法通用函数----------------')
        a = np.array([20, 20, -20, -20])
        b = np.array([3, -3, 6, -6])
        print('真除:', np.true_divide(a, b))  # a 真除 b  （对应位置相除）
        print('真除_:', np.divide(a, b))  # a 真除 b
        print('地板除:', np.floor_divide(a, b))  # a 地板除 b	（真除的结果向下取整）
        print('天花板除:', np.ceil(a / b))  # a 天花板除 b	（真除的结果向上取整）
        print('截断除:', np.trunc(a / b))  # a 截断除 b	（真除的结果直接干掉小数部分）

    @staticmethod
    def bit():
        """
        矩阵的位操作
        """
        a = np.array([-9, -5, 2, 1, -9])
        b = np.array([-2, 6, -2, 3, -4])

        c = a ^ b
        # print(c)
        # c = a.__xor__(b)
        # print(c)
        # c = np.bitwise_xor(a, b)
        print(c)
        print(np.where(a < 0))
        print(a < 0)
        # 按位异或操作可以很方便的判断两个数据是否同号。
        #
        e = a & b
        print(e)
        # e = a.__and__(b)
        # e = np.bitwise_and(a, b)
        # 0 & 0 = 0
        # 0 & 1 = 0
        # 1 & 0 = 0
        # 1 & 1 = 1
        # 利用位与运算计算某个数字是否是2的幂

        e = math.log2(8)
        print(len(str(e)))

        #
        # #已知n阶方阵A， 求特征值与特征数组
        # # eigvals: 特征值数组
        # # eigvecs: 特征向量数组
        # eigvals, eigvecs = np.linalg.eig(A)
        # #已知特征值与特征向量，求方阵
        # S = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * np.mat(eigvecs逆)


if __name__ == '__main__':
    m01 = Matrix()
    # m01.solute_equation()
    # m01.fibo()
    # m01.funcs()
    m01.bit()
