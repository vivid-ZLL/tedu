"""
    练习:敌人类(攻击力0--100)
        抛出异常的信息：消息/错误行/攻击力/错误编号
"""

class AtkError(Exception):
    """
        攻击错误
    """
    def __init__(self,message,age_value,code_line,error_number):
        super().__init__("出错啦啦啦")
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.error_number = error_number


class Enemy:
    def __init__(self,age):
        self.atk = age

    @property
    def atk(self):
        return self.__age

    @atk.setter
    def atk(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            # 5
            raise AtkError("超过我想要的范围啦",value,26,1001)

try:
    w01 = Enemy(81)
except AtkError as e:
    print("请重新输入")
    print(e.message)
    print(e.age_value)
    print(e.code_line)
