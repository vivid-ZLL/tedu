# 练习１：
# 在控制台中，录入一个商品单价。25
# 再录入一个数量  2
# 最后获取金额，60 计算应该找回多少钱。60 - 25*2
# 14:45

price = input("请输入商品单价：")
price = float(price)
count = int(input("请输入数量："))
money = float(input("请输金额："))

result = money - price * count

print("应该找回：" + str(result))





