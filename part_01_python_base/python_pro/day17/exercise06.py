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


def find(val, list_target):
    for item in list_target:
        if val(item):
            return item


def value04(item):
    return item.name == "葵花宝典"


def value05(item):
    return item.id == 101


def value06(item):
    return item.duration > 0


print(find(value04, list_skill))
print(find(value05, list_skill))
print(find(value06, list_skill))

print("---------------------------------------------")

print(find(lambda item: item.name == "葵花宝典", list_skill))
print(find(lambda item: item.id == 101, list_skill))
print(find(lambda item: item.duration > 0, list_skill))


def f01():
    count = 0
    for item in list_skill:
        if len(item.name) > 4:
            count += 1
    return count


print(f01())
print("------------------------------------------")


def f001(value, list_target):
    count = 0
    for item in list_target:
        if value(item):
            count += 1
    return count


print(f001(lambda item: len(item.name) > 4, list_skill))
print(f001(lambda item: item.duration <= 5, list_skill))
