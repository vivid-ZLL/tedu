"""
    迭代器
    练习:exercise03.py
"""


class Skill:
    pass


class SkillManager:
    """
        技能管理器  可迭代对象
    """

    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        # 创建一个迭代器对象,并传递需要迭代的数据。
        return SkillIterator(self.__skills)


class SkillIterator:
    """
        技能迭代器
    """

    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        # 如果没有数据了，则抛出异常
        if self.__index > len(self.__target) - 1:
            raise StopIteration

        # 返回下一个数据
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


manager = SkillManager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())

for item in manager:
    print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break



