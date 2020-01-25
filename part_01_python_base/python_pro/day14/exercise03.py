# 在二维列表中，获取13位置，向左，3个元素
# 在二维列表中，获取22位置，向上，2个元素
# 在二维列表中，获取03位置，向下，2个元素


from homework02_DoubleListHelper import *

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
d01 = DoubleListHelper()
re = d01.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)
print(re)

re = d01.get_elements(list01, Vector2(2, 2), Vector2.up(), 2)
print(re)

re = d01.get_elements(list01, Vector2(0, 3), Vector2.down(), 2)
print(re)
