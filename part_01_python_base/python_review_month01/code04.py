"""
# 生成器原理
class MyGenerator:
    # 生成器 = 可迭代对象 + 迭代器
    def __init__(self,stop_value):
        self.begin = 0
        self.stop_value = stop_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.begin >= self.stop_value:
            raise StopIteration

        temp = self.begin
        self.begin+=1
        return temp
"""

# 面试题：
# 请简述，生成器与迭代器
# 生成器 本质就是　迭代器　＋　可迭代对象.
# 而可迭代对象就是为了可以迭代(for)，而迭代的本质就是不断调用迭代器next方法.
# 生成器最重要的特点调用一次next，计算一次结果，返回一个数据,
# 这个过程称之为惰性操作／延迟操作．
# 在海量数据下，可以大量节省内存.

# 惰性操作 --> 立即操作(灵活获取结果)
# list(生成器)












