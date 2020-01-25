class Enemy:
    def __init__(self, name, hp, atk, defence):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.defence = defence

    def __str__(self):
        return ("敌人名称:%s,血量:%s,攻击力:%d,防御力:%d" %
                (self.name, self.hp, self.atk, self.defence))

    def __repr__(self):
        return ("Enemy('%s',%s,%d,%d)" %
                (self.name, self.hp, self.atk, self.defence))


s01 = Enemy("灭霸", 100, 20, 25)
print(s01)
s02 = repr(s01)
print(s02)
s03 = eval(s02)
s03.name = "天启"
print(s03.defence)
print(s03)
