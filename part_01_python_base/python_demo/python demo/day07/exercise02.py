# 练习2:["无忌","赵敏","周芷若"]  [101,102,103]
#  {"无忌":101,"赵敏":102,"周芷若":103}
# 10:18
list01 = ["无忌", "赵敏", "周芷若"]
result = [101, 101, 103]
dict01 = {}
# 通过索引同时在多个列表中获取元素
for i in range(len(list01)):
    # key = list01[i]
    # value = list02[i]
    # dict01[key] = value
    dict01[list01[i]] = result[i]

print(dict01)
# 11:00
# 需求：字典如何根据value查找key
# 解决方案１:键值互换
dict02 = {value: key for key, value in dict01.items()}
print(dict02)
print(dict02[101])
# 缺点:如果key重复,交换或则丢失数据。
# 如果需要保持所有数据
# [(k,v),]
result = [(value, key) for key, value in dict01.items()]
print(result)
