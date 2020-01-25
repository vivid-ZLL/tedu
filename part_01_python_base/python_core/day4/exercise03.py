import random

random_number = random.randint(1,100)
code_answer = int(input("请输入猜测的数字大小"))
count = 0
while True:
    count += 1
    if code_answer < random_number:
        print("您猜小了")
        code_answer = int(input("请重新输入猜测的数字大小"))
    elif code_answer > random_number:
        print("您猜大了")
        code_answer = int(input("请重新输入猜测的数字大小"))
    else:
        print("恭喜您答对了")
        break

print("您总共猜了",count,"次")