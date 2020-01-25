class A01:
    def __init__(self, a = "998"):
        self.a = a


    # def f01(self):
    #     print("A01")


class B01(A01):
    def __init__(self):
        super().__init__()

    def f01(self):
        print(super().a)


c01 = B01()
print(c01.a)
