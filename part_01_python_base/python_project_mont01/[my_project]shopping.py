class Commodity:
    def __init__(self, name="", price=0, id=0):
        self.name = name
        self.price = price
        self.id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class CommodityCenterController:
    def account(self, shopping_list, entered_money):
        total_price = 0
        for item in shopping_list:
            total_price += item[0].price * item[1]
        if entered_money < total_price:
            print("金额不足")
        else:
            print("共花费%d,剩余%d" % (total_price, (entered_money - total_price)))


#
#  分割线-----------------------------------------------------------------
#

class ShoppingView:
    def __init__(self):
        self.load_config()
        self.m01 = CommodityCenterController()

    def load_config(self):
        self.dict = {101: Commodity("屠龙刀", 10000, 101),
                     102: Commodity("倚天剑", 10000, 102),
                     103: Commodity("九阴白骨爪", 8000, 103),
                     104: Commodity("九阳神功", 9000, 104),
                     105: Commodity("降龙十八掌", 8000, 105),
                     106: Commodity("乾坤大挪移", 10000, 106)
                     }

    def main(self):
        shopping_list = self.create_shopping_list()
        entered_money = int(input("请输入金额"))
        self.m01.account(shopping_list, entered_money)
        # print(shopping_list)

    def create_shopping_list(self):
        shopping_list = []
        while True:
            self.print_commodity_info()
            id_number = input("请输入物品编号:")
            if id_number == "":
                break
            id_number = int(id_number)
            if id_number not in self.dict:
                print("-" * 8, "物品不存在,请重新输入", "-" * 8)
                continue
            amount = int(input("请输入购买数量"))
            shopping_list.append((self.dict[id_number], amount))
        return shopping_list

    def print_commodity_info(self):
        for item in self.dict.values():
            print("物品编号", item.id, " ", item.name, "  ", "价格", item.price)


s01 = ShoppingView()
s01.main()
