"""
4. 定义敌人类
    --　数据:姓名,血量,基础攻击力,防御力
    --　行为:打印个人信息

   创建敌人列表(至少４个元素),并画出内存图。
   查找姓名是"灭霸"的敌人对象
   查找所有死亡的敌人
   计算所有敌人的平均攻击力
   删除防御力小于10的敌人
   将所有敌人攻击力增加50
"""


class Enemy:
    def __init__(self, name, hp, atk, defence):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence

    def print_enemy_info(self):
        print(self.name, self.hp, self.atk, self.defence)

    @staticmethod  # 要求的操作都可以用静态方法或函数完成
    def fun01():
        for item in list01:
            if item.name == "灭霸":
                return item


list01 = [
    Enemy("毛玉", 0, 15, 10),
    Enemy("小妖精", 120, 20, 5),
    Enemy("大妖精", 400, 30, 20),
    Enemy("灭霸", 5000, 100, 200)
]

re01 = Enemy.fun01()
re01.print_enemy_info()


# ------------------------------------------------

def fun02():
    result = []
    for item in list01:
        if item.hp == 0:
            result.append(item)
    return result


re02 = fun02()
for item in re02:
    item.print_enemy_info()


# -----------------------------------------------
def fun03():
    total_value = 0
    for item in list01:
        total_value += item.atk
    ave_atk = total_value / len(list01)
    return ave_atk


re03 = fun03()
print(re03)


# ------------------------------
def fun04():
    for i in range(len(list01) - 1, -1, -1):
        if list01[i].defence < 10:
            print(list01[i].name)
            del list01[i]


# fun04()
for item in list01:
    item.print_enemy_info()


# --------------------------------
def fun05():
    for item in list01:
        item.atk += 50

fun05()
for item in list01:
    item.print_enemy_info()
