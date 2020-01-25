unit_price = float(input("请输入商品单价"))
amount = int(input("请输入商品数量"))
sum_money = float(input("请输入获取金额"))
result = sum_money - unit_price * amount
print("应找回金额"+str(result))

