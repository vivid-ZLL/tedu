class MyRange:
    def __init__(self, stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        return MyRangeIterator(self.stop_value)


class MyRangeIterator:
    def __init__(self, stop_value):
        self.end_value = stop_value
        self.index = 0
    def __next__(self):
        if self.index == self.end_value:
            raise StopIteration

        temp = self.index
        self.index += 1
        return temp



m01 = MyRange(10)
for item in m01:
    print(item)
