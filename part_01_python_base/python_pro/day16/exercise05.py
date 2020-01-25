list01 = [564, 564, 654, 654, 321, 897, 23, 87, 24, ]
list02 = []
for item in list01:
    if item % 2 == 0:
        list02.append(item)


# print(list02)


def my_mth(list_target):
    number = 0
    while number < len(list_target):
        if list_target[number] % 2 == 0:
            yield list_target[number]
        number += 1


m01 = my_mth(list01)
for item in m01:
    print(item)
