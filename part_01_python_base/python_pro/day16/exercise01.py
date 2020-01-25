tuple_01 = ("铁扇公主", "铁锤公主", "扳手王子")
iteration = tuple_01.__iter__()
while True:
    try:
        item = iteration.__next__()
        print(item)
    except StopIteration:
        break

dict_01 = {"铁扇公主": 101, "铁锤公主": 102, "扳手王子": 103}
iteration = dict_01.__iter__()
iteration_ex = dict_01.values().__iter__()
while True:
    try:
        item = iteration.__next__()
        print(item, end=" : ")
        item = iteration_ex.__next__()  # 此行代码可以优化,通过键直接找值
        print(item)
    except StopIteration:
        break

