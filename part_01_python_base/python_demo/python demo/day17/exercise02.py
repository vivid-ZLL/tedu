"""
# 练习: 定义生成器函数my_zip,实现下列现象.
# 将多个列表的每个元素合成一个元组.
list02  = ["孙悟空","猪八戒","唐僧","沙僧"]
list03  = [101,102,103,104]
for item in zip(list02,list03):
    print(item)
"""

# 练习: 定义生成器函数my_zip,实现下列现象.
# 将多个列表的每个元素合成一个元组.
list02  = ["孙悟空","猪八戒","唐僧","沙僧"]
list03  = [101,102,103,104]

def my_zip(list01,list02):
    for i in range(len(list01)):
        yield (list01[i],list02[i])

for item in my_zip(list02,list03):
    print(item)

# (扩展)
def my_zip2(*args):
    # 根据星号元组形参args第一个参数的长度生成索引len(args[0])
    for i in range(len(args[0])):
        list_result = []
        for item in args:
            list_result.append(item[i])
        yield tuple(list_result)

for item in my_zip2(list02,list03):
    print(item)