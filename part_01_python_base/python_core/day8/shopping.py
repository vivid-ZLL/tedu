dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def select_menu():
    """
        选择菜单
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def settlement():
    """
        结算
    """
    total_price = caculate_total_price()
    print_list_order()
    count_money(total_price)


def print_list_order():
    for item in list_order:
        commodity = dict_commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))


def buying():
    """
        购买
    """
    print_commodity()
    get_list_order()
    print("添加到购物车。")


def count_money(total_price):
    while True:
        money = float(input("总价%d元，请输入金额：" % total_price))
        if money >= total_price:
            print("购买成功，找回：%d元。" % (money - total_price))
            list_order.clear()
            break
        else:
            print("金额不足.")


def caculate_total_price():
    total_price = 0
    for item in list_order:
        commodity = dict_commodity_info[item["cid"]]
        total_price += commodity["price"] * item["count"]
    return total_price


def get_list_order():
    cid = get_cid()
    count = int(input("请输入购买数量："))
    list_order.append({"cid": cid, "count": count})


def get_cid():
    while True:
        cid = int(input("请输入商品编号："))

        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    return cid


def print_commodity():
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"],
                                      value["price"]))


select_menu()
