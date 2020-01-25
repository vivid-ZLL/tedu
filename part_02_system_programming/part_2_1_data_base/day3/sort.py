def choose(list_):
    for r in range(len(list_)):
        for c in range(r, len(list_)):
            if list_[r] > list_[c]:
                list_[r], list_[c] = list_[c], list_[r]


def bubble(list_):
    for c in range(1, len(list_)):
        for r in range(len(list_) - c):
            if list_[r] > list_[r + 1]:
                list_[r], list_[r + 1] = list_[r + 1], list_[r]


def insert(list_):
    for r in range(1, len(list01)):
        for c in range(r):
            if list01[r] < list01[c]:
                list01.insert(c, list01.pop(r))
                continue


list01 = [64984, 87, 13, 4, 654, 35186, 687, 35, 897, 231, 897, 54867,
          6879, 3, 897, 67, 97, 687, 64, 97, 1867, 689, 87]

# choose(list01)
# bubble(list01)
insert(list01)
print(list01)
