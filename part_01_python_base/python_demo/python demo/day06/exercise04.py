"""
    练习1:在控制台中循环录入商品信息(名称,单价).
    　　　如果名称输入空字符,则停止录入.
         将所有信息逐行打印出来.
    15:42
"""
dict_commodity_info = {}
while True:
    name = input("请输入商品名称：")
    if name == "":
        break
    price = int(input("请输入商品单价："))
    dict_commodity_info[name] = price

for key,value in dict_commodity_info.items():
    print("%s商品单价是%d"%(key,value))







