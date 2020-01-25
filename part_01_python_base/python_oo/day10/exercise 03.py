class Wife:
    count = 0

    def __init__(self, name):
        self.name = name
        Wife.count += 1

    @classmethod
    def print_count(cls):
        print(Wife.count)


w01 = Wife("alice")
w02 = Wife("marisa")
w03 = Wife("flandre")

Wife.print_count()

