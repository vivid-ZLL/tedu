class Player:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    def hp_down(self, value):
        self.hp -= value
        print("%s受到攻击,生命值为:%s" % (self.name,self.hp),end= " ")
        print("因为玩家被攻击所以屏幕晃了一下")
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("啊我死了")
        print("Game Over")

    def attack(self, enemy_name):
        Enemy.hp_down(enemy_name, self.atk)


class Enemy:
    def __init__(self, name, hp, atk):
        self.hp = hp
        self.atk = atk
        self.name = name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    def hp_down(self, value):
        self.hp -= value
        print("%s受到攻击,生命值为:%d" % (self.name, self.hp))

        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("敌人死了")
        print("敌人掉钱")
        print("获得分数404")
        print("获得金钱998")

    def attack(self, player_name):
        Player.hp_down(player_name, self.atk)


handsome_guy = Player("吴彦祖", 10, 5)
strong_man = Enemy("灭霸", 20, 1)

for i in range(4):
    strong_man.attack(handsome_guy)
    handsome_guy.attack(strong_man)

