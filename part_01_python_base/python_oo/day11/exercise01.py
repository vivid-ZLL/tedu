class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 10 <= value <= 100:
            self.__hp = value
        else:
            raise ValueError("不在阈值内")

    hp = property(get_hp, set_hp)

    def get_atk(self):
        return self.__atk

    def set_atk(self, value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError("不在阈值内")

    atk = property(get_atk, set_atk)


e01 = Enemy("Alice", 50, 50)
# print(e01.hp, e01.atk)
# print(e01.__dict__)
print(e01.hp)