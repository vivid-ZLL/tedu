# 创建 类
class ThouhouProjectCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def show_ability(self):
        print(self.name, self.ability)


class Capability:
    def __init__(self, level, number):
        self.level = level
        self.number = number

    def show_ability(self):
        print(self.level, self.number)


# 创建对象
c01 = ThouhouProjectCharacter("alice", "manipulate dolls")
c02 = ThouhouProjectCharacter("marisa", "manipulate magic")
c03 = ThouhouProjectCharacter("flandre scarlet", "destruction")

c_alice = Capability("level_s", "No.1")

c01.show_ability()
c_alice.show_ability()
