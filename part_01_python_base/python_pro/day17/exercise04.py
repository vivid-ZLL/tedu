list01 = [864, 867, 21, 876, 342, 897, 13
    , 687, 12, 7, 34, 9, 15, 876, 564, 9, 3, 15, 35, 7, 354]


def condition01():
    for item in list01:
        if item % 2 == 0:
            yield item


for item in condition01():
    print(item, end=" ")
print()


def condition02():
    for item in list01:
        if item > 10:
            yield item


for item in condition02():
    print(item, end=" ")
print()


def condition03():
    for item in list01:
        if 50 > item > 10:
            yield item


for item in condition03():
    print(item, end=" ")
print()


def value01(item):
    return item % 2 == 0


def value02(item):
    return item > 10


def value03(item):
    return 50 > item > 10


def find(val):
    for item in list01:
        if val(item):
            yield item


for item in find(value01):
    print(item,end=" ")
print()

for item in find(value02):
    print(item,end=" ")
print()

for item in find(value03):
    print(item,end=" ")
print()
# ------------------------------------------------------------


