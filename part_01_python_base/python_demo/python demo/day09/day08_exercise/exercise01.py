"""
自学(参照菜鸟教程)字符串/列表/字典常用函数(方法),实现如下功能。
    字符串："　校　训：自　强不息、厚德载物。　　"
    查找空格的数量
    删除字符串前后空格
    删除字符串所有空格
    查找"载物"的位置
    判断字符串是否以"校训"开头.
    10:50
"""
str01 = "校训：自　强不息、厚德载物。　　"
print(str01.count("　"))

str02 = str01.rstrip().lstrip()
print(str02)

str03 = str01.replace("　","")
print(str03)

print(str01.index("载物"))

print(str01.startswith("校训"))