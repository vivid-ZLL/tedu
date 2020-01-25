class GraphManager:
    @staticmethod
    def transfer_method(target_graph):
        return target_graph.calculate_area()


class Graph:
    """
        父类:图像
    """

    def calculate_area(self):
        raise NotImplementedError


class Rectangle(Graph):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b


class Circle(Graph):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return self.r ** 2 * 3.14


c01 = Circle(3)
r01 = Rectangle(4, 6)
g01 = GraphManager()

a = g01.transfer_method(c01)
print(a)
print(g01.transfer_method)
print(g01.transfer_method(r01))
