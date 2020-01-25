class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def go_to_work(self, amount):
        # name = self.name
        print("%s上班挣了%d块钱" % (self.name, amount))


class Skill:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def learn(self, master, student):
        print("%s教了%s很牛X的\"%s\"技能" % (master.amount, student.amount, self.name))


wj = Person("无忌", 0)
zm = Person("赵敏", 0)
skill01 = Skill("九阳神功")
skill02 = Skill("化妆")
Skill.learn(skill01, wj, zm)
Skill.learn(skill02, zm, wj)
wj.go_to_work(10000)
zm.go_to_work(6000)