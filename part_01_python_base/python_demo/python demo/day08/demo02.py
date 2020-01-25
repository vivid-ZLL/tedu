"""
    函数返回值　应用
    10:35
"""


# 设计思想：分而治之
#         干一件事

# 需求：定义两个数字相加的函数
# def add():
#     1. 获取数据
#     number01 = int(input("请输入第一个数字："))
#     number02 = int(input("请输入第二个数字："))
#     2. 逻辑计算
#     result = number01 + number02
#     3. 显示结果
#     print(result)
#
# add()

def add(number01, number02):
    # 逻辑处理
    return number01 + number02


# 调用者提供数据
number01 = int(input("请输入第一个数字："))
number02 = int(input("请输入第二个数字："))
result = add(number01, number02)
# 调用者负责显示结果
print("结果是:" + str(result))
