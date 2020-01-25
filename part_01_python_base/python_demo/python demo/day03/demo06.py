"""
    循环语句
        while 条件:
            循环体
    练习:exercise08.py
"""

# 死循环：循环条件永远是满足的。
while True:
    usd = int(input("请输入美元："))
    print(usd * 6.9)
    if input("输入q键退出:") == "q":
        break  # 退出循环体

