"""
    练习:随机加法考试
      随机产生两个数字(1--10),
      在控制台中获取两个数相加的结果
      如果用户输入正确得１０分
    　总共３道题，最后输出得分.
    　例如:"请输入8+3=?"   10   不得分
    　　　　"请输入4+3=?"   7   得10分
    　　　　"请输入4+4=?"   8   得10分
          　”总分是20“
    　14:15
"""
import random

score = 0
for item in range(3):
    random_number01 = random.randint(1, 10)
    random_number02 = random.randint(1, 10)
    input_number = int(input("请输入" + str(random_number01) + "+" + str(random_number02) + "=?"))
    if input_number == random_number01 + random_number02:
        score += 10
print("总分：" + str(score))
