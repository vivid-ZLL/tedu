class Vector1:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "一维向量的分量是:" + str(self.x)

    def __sub__(self, other):
        return Vector1(self.x - other)

    def __mul__(self, other):
        return Vector1(self.x * other)

    def __rsub__(self, other):
        return Vector1(other - self.x)


v02 = Vector1(12)
print(v02 - 4)
print(v02 * 2)

print(24 - v02)
