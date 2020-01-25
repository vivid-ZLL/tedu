dict_commodity_info = {}
while True:
    str_name = input("请输入商品名称：")
    if str_name == "":
        break
    int_price = input("请输入商品单价：")

    dict_commodity_info[str_name] = int_price
for k, v in dict_commodity_info.items():
    print(k, v)
