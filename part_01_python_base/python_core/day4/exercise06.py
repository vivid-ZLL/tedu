import random
count = 0

for times in range(3):
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    code_answer = random_number1 + random_number2
    input_answer = int(input("请输入" + str(random_number1) + "+" +
                             str(random_number2) + "=?"))
    if code_answer == input_answer:
        count += 1
code_score = 10 * count
print("总分是", code_score)
