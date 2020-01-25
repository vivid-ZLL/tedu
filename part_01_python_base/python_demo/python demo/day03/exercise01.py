"""
# 练习:当钱不够时，提示"金额不足",
#      钱够时，提示"应找回"
#      调试程序.
price = input("请输入商品单价：")
price = float(price)
count = int(input("请输入数量："))
money = float(input("请输金额："))
result = money - price * count
print("应该找回：" + str(result))
"""

# 练习:当钱不够时，提示"金额不足",
#      钱够时，提示"应找回"
#      调试程序.

price = input("请输入商品单价：")
price = float(price)
count = int(input("请输入数量："))
money = float(input("请输金额："))
result = money - price * count
if result >= 0:
    print("应该找回：" + str(result))
else:
    print("金额不足")
