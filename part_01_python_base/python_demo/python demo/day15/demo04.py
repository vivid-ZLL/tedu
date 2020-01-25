"""
    异常处理
    练习:exercise03.py
"""

def div_apple(apple_count):
    # ValueError
    person_count = int(input("请输入人数："))
    # ZeroDivisionError
    result = apple_count /  person_count
    print("每人%d个苹果"%result)


"""
try:
    # 可能出错的代码
    div_apple(10)
except Exception:
    print("出错喽")
"""

"""
# "建议"分门别类的处理
try:
    # 可能出错的代码
    div_apple(10)
except ValueError:
    print("输入的人数必须是整数")
except ZeroDivisionError:
    print("输入的人数不能是零")
except Exception:
    print("未知错误")
"""

"""
try:
    # 可能出错的代码
    div_apple(10)
except Exception:
    print("出错喽")
else:
    # 如果异常，不执行else语句.
    print("没有出错")
"""

try:
    # 可能出错的代码
    div_apple(10)
finally:
    # 无论是否异常，一定会执行的代码.
    print("finally")
    # 作用：不能处理的错误，但是一定要执行的代码，就定义到finally语句中。

print("后续逻辑.....")

