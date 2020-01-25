"""
    练习：在不该变原有功能(存取钱)的定义与调用情况下.
         增加验证账号的功能．
"""

# 验证账号
def verify_account(func):
    def wrapper(*args, **kwargs):
        print("验证账号")
        return func(*args, **kwargs)

    return wrapper

@verify_account
def deposit(money):
    print("存%d钱喽" % money)

@verify_account
def withdraw(login_id, pwd):
    print("取钱喽", login_id, pwd)

deposit(10000)
withdraw("zs", 123)
