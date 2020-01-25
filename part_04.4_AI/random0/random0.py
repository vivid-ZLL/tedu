import numpy as np


class Random0:
    def erxiangfenbu(self):
        """
            二项分布
            产生size个随机数，每个随机数来自n次尝试中的成功次数，其中每次尝试成功的概率为p。
        """
        n = 100
        p = 0.5
        size = 50
        np.random.binomial(n, p, size)

        # 二项分布可以用于求如下场景的概率的近似值：

        # 某人投篮命中率为0.3，投10次，进5个球的概率。

        sum(np.random.binomial(10, 0.3, 200000) == 5) / 200000

        # 1.某人打客服电话，客服接通率是0.6，一共打了3次，都没人接的概率。

        sum(np.random.binomial(3, 0.6, 200000) == 0) / 200000

    def normal(self):
        size = 1000
        # 产生size个随机数，服从标准正态(期望=0, 标准差=1)分布。
        np.random.normal(size)
        # 产生size个随机数，服从正态分布(期望=1, 标准差=10)。
        np.random.normal(loc=1, scale=10, size=size)
