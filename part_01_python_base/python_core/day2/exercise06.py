# distance = float(input("请输入距离："))
# time = float(input("请输入时间："))
# initial_velocity = float(input("请输入初速度："))
#
# acceleration = (distance - initial_velocity
#                 * time) * 2 /time ** 2
# print("加速度是："+str(acceleration))

# int_num = int(input("请输入一个四位整数："))
# unit_1 = int_num % 10
# unit_2 = int_num // 10 % 10
# unit_3 = int_num // 100 % 10
# unit_4 = int_num // 1000
#
# result = unit_1 + unit_2 + unit_3 + unit_4
# print(result)

# 方法2
int_num = int(input("请输入一个四位整数："))
result = int_num % 10
result += int_num // 10 % 10
result += int_num // 100 % 10
result += int_num // 1000
print(result)

