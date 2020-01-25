"""
5.(扩展)计算一个字符串中的字符以及出现的次数.
# 思想：
# 逐一判断字符出现的次数.
# 如果统计过则增加１，如果没统计过则等于１.

abcdefce
a 1
b 1
c 2
d 1
e 2
f 1
"""

dict_result = {}
str_target = "abcdefce"
for item in str_target:
    if item not in dict_result:
        dict_result[item] = 1
    else:
        dict_result[item] += 1

print(dict_result)
