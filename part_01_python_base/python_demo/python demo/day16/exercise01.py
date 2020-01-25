# 练习1：使用迭代器原理，遍历元组.
# ("铁扇公主","铁锤公主",“扳手王子”)
tuple01 = ("铁扇公主","铁锤公主","扳手王子")
# for item in tuple01:
#     print(item)


iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

