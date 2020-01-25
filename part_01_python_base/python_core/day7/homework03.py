list_01 = [
    [1, 2, 3, 44],
    [4, 5, 5, 5, 65, 6, 87],
    [7, 5]
]


def print_list(list_target):
    for r in list_target:
        for c in r:
            print(c, end=" ")
        print()


print_list(list_01)
