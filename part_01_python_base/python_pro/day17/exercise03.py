"""
    参照day10/exercise02.py
    完成下列练习
"""


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能信息:%s,%s,攻击比例%s,持续时间%s" % (self.id, self.name, self.atk_ratio, self.duration)


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]


# 练习1:获取攻击比例大于6的所有技能
# 要求:使用生成器函数/生成器表达式完成

def fun01():
    for item in list_skill:
        if item.atk_ratio > 6:
            yield item.__str__()


# for item in fun01():
#     print(item.name, item.atk_ratio)
#
#
# re = (item for item in list_skill if item.atk_ratio > 6)
# for item in re:
#     print(item.name, item.atk_ratio)

def fun02():
    for item in list_skill:
        if 4 < item.duration < 11:
            yield item


def fun03():
    for item in list_skill:
        if item.id == 102:
            return item


def fun04():
    for item in list_skill:
        if len(item.name) > 4 and item.duration < 6:
            yield item


for item in fun02():
    print(item.__str__())

print(fun03().__str__())

for item in fun04():
    print(item.__str__())
