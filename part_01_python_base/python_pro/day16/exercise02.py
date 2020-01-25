# 练习：图形管理器记录多个图形
#      迭代图形管理器对象

class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        # 创建一个迭代器对象,并传递需要迭代的数据。
        return GraphicIterator(self.__graphics)


class Graphic:
    pass


class GraphicIterator:
    def __init__(self, target):
        self.__target = target
        self.index = 0

    def __next__(self):
        if self.index == len(self.__target):
            raise StopIteration
        temp = self.__target[self.index]
        self.index += 1
        return temp


m01 = GraphicManager()
m01.add_graphic(Graphic())
m01.add_graphic(Graphic())
m01.add_graphic(Graphic())

# 对象具有了可迭代属性
for item in m01:
    print(item)

# 本质如下↓
iterator = m01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

