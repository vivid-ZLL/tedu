tuple01 = ([1, 1, 1], [2, 2], [3, 3, 3, 3])
re = max(tuple01,key= lambda item:len(item))
print(re)

class Enemy:
    def __init__(self, name, hp, atk, defence):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence

    def __str__(self):
        return "名字:%s, hp:%s, atk:%s, defence:%s" % (self.name, self.hp, self.atk, self.defence)


list01 = [
    Enemy("毛玉", 0, 15, 10),
    Enemy("小妖精", 120, 20, 5),
    Enemy("大妖精", 400, 30, 20),
    Enemy("灭霸", 5000, 200, 200)
]


re = map(lambda item:(item.name,item.hp,item.atk),list01)
print(re)
for item in re:
    print(item)
print("-----------------")


re = filter(lambda item:item.atk > 100 and item.hp > 0,list01)
for item in re:
    print(item)

print("---------------------------")

re = sorted(list01,key= lambda item:item.defence,reverse=True)
for item in re:
    print(item)
