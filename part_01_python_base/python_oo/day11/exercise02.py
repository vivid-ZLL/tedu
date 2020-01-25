"""
    小明在招商银行取钱
"""


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


class Bank:
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

    def draw_money(self, person, value):
        """
        取钱
        :param person:
        :param value:
        :return:
        """
        self.money -= value
        person.atk += value
        print("%s取了%d" % (person.hp, value))
        print(("银行有还有%d,小明还有%d" % (self.money, person.atk)))


xm = Person("小明", 0)
bank = Bank("招商银行", 200000)

bank.draw_money(xm, 6000)
