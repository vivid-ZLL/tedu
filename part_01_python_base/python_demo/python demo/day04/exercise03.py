"""
    练习:猜数字游戏
    游戏运行产生一个１－－１００之间的随机数。
    让玩家重复猜测，直到猜对为止。
    提示:大了
    　　　小了
    　　　　猜对了，总共猜了多少次
    10:47
"""
# 随机数工具(在开头写一次)
import random

# 产生一个随机数
random_number = random.randint(1, 100)
count = 0
while True:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break
