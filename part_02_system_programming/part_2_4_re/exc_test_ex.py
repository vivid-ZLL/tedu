"""
    需求:编写接口函数，从终端输入端口名称获取端口运行状态中的地址值
"""
import re

with open("exc.txt", "r") as file_exc:
    data = file_exc.read()
    target = input("port:")

c = re.search(r"\b%s\b is.*" % target, data)
print(c.group())


def read_data_line():
    global data
    data = [file_exc.readline()]
    data = [s.strip() for s in data]


with open("exc.txt", "r") as file_exc:
    while True:
        read_data_line()
        result = re.search(r"address is .*",data[0])
        if result:
            print(target,result.group())
            break

