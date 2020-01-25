# while True:
#     int_number = int(input("请输入一个正整数："))
#     kind_number = ""
#
#     if int_number <= 1:
#         kind_number = "不是素数"
#     else:
#         for item in range(2, int_number):
#             if int_number % item == 0:
#                 kind_number = "不是素数"
#                 break
#         else:
#             kind_number = "是素数"
#     print(kind_number)

number = int(input("请输入整数:"))
#判断2 到number之间的数字，能否整除number.
for item in range(2, number):  # 2 3 4 5 ...
    if number % item == 0:
        print("不是素数")
        break  # 如果发现满足条件的数字，就不再判断后面的了。
else:
    print("是素数")

number = int(input("请输入正整数："))
for item in range(2,number):
    if number % item == 0:
        print("不是素数")
        break
else:
    print("是素数")

number = int(input("请输入正整数："))
for item in range(2,number):
    if number % item == 0 :
        print("是素数")
        break
else:
    print("不是素数")

number = int(input("请输入正整数："))
for item in range(2,number):
    if number % item ==0:
        print("是素数")
        break
else:
    print("不是素数")

number = int(input("请输入正整数"))
for item in range(2,number):
    if number % item == 0:
        print("是素数")
        break
else:
    print("不是素数")

number = int(input("请输入正整数："))
for item in range(2,number):
    if number % item == 0:
        print("是素数")
        break
else:
    print("不是素数")

number = int(input("请输入正整数："))
for item in range(2,number):
    if number % item == 0 :
        print("是素数")
        break
else:
    print("不是素数")

number = int(input("请输入正整数："))
for item in range(2,number):
    if number % item == 0 :
        print("是素数")
        break
else:
    print("不是素数")

number = int(input("请输入正整数："))
for item in range(2,number):
    if number % item == 0 :
        print("是素数")
        break
else:
    print("不是素数")

number = int(input("请输入正整数："))
for item in range(2,number):
    if number % item == 0:
        print("是素数")
        break
else:
    print("不是素数")

number= int(input("请输入正整数："))
for item in range(2,number):
    if number % item == 0 :
        print("是素数")
        break
else:
    print("不是素数")