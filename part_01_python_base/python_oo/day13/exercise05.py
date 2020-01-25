"""
    小明爱跑步,爱吃东西
    1.小明体重75.0公斤
    2.每次跑步减肥0.5公斤
    3.每次吃东西体重会增加1公斤
    4.小美体重是45.0公斤
"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def move_up(self, activity):
        activity.act(self)


class Sport:
    def act(self, person):
        pass


class Run(Sport):
    def act(self, person):
        person.weight -= 0.5
        print("跑步", end="  ")
        print("现在小明的体重是%.1f" % person.weight)


class Eat(Sport):
    def act(self, person):
        person.weight += 1
        print("吃东西", end="  ")
        print("现在小明的体重是%.1f" % person.weight)


p01 = Person("Alice", 45)
p02 = Person("Marisa", 48)
a01 = Run()
a02 = Eat()

p01.move_up(a01)
p02.move_up(a02)