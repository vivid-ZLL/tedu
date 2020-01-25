class AtkError(Exception):
    def __init__(self,msg,row,atk,error_number):

        self.msg = msg
        self.atk = atk
        self.row = row
        self.error_number = error_number

class Enemy:
    def __init__(self,atk):
        self.atk = atk

    def get_atk(self):
        if 0 <= self.atk <= 100:
            return self.atk
        else:
            raise AtkError("攻击力数据错误",14,self.atk,998)

def test_enemy_atk():
    while True:
        try:
            e01.get_atk()
        except:
            e01.atk = int(input("请重新输入攻击力"))
            continue
        break

e01 = Enemy(404)
test_enemy_atk()