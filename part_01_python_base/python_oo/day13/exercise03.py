class Grenade:
    def __init__(self, atk):
        self.atk = atk

    def explode(self, damage_target):
        print("蹦(⊙o⊙)")
        damage_target.damage(self.atk)


class Target:
    def damage(self, value):
        pass

# -----------------------------------------------

class Player(Target):
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("哦豁")


class Enemy(Target):
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("敌人掉血")


class Unknown(Target):
    pass


g01 = Grenade(100)
e01 = Enemy(150)
p01 = Player(200)

g01.explode(e01)
g01.explode(p01)
print(isinstance(p01,Player))
print(isinstance(p01,Target))