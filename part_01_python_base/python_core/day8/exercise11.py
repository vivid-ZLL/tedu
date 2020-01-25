result = 0


def count_number(*args):
    global result

    for item in args:
        result += item


tuple01 = (564, 564, 21, 35, 8, 654, 86, 213, 543, 4)
count_number(tuple01)
print(result)
