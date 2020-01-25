"""
总结：
 　　存储多个学生信息(姓名,年龄,成绩,性别)的多种方式

1. exercise05字典内嵌列表:
{
    "张无忌":[28,100,"男"],
}
2. exercise06字典内嵌字典:
{
    "张无忌":{"age":28,"score":100,"sex":"男"},
}
3. exercise07列表内嵌字典:
[
    {"name":"张无忌","age":28,"score":100,"sex":"男"},
]
4. 列表内嵌列表
[
    ["张无忌",28,100男],
]
选择策略：根据具体需求，结合优缺点，综合考虑(两害相权取其轻).
    字典：
        优点：根据键获取值，读取速度快；
        　　　代码可读性相对列表更高(根据键获取与根据索引获取).
        缺点：内存占用大；
        　　　获取值只能根据键,不灵活.
    列表：
        优点：根据索引/切片，获取元素更灵活.
             相比字典占内存更小。
        缺点：通过索引获取，如果信息较多，可读性不高.
"""
"""
练习:在控制台中录入多个人的多个喜好,输入空字符停止.
例如:请输入姓名：
    请输入第1个喜好：
    请输入第2个喜好：
    ...
    请输入姓名：
    ...
   最后在控制台打印所有人的所有喜好.
[
    {“无忌”:[赵敏,周芷若,小赵]}
]

list_person_bobby = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_person = {name:[]}
    list_person_bobby.append(dict_person) 
    while True:
        bobby = input("请输入喜好：")
        if bobby == "":
            break
        dict_person[name].append(bobby)
"""

"""
{
    “无忌”:[赵敏,周芷若,小赵]
}
"""
dict_person_bobby = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_person_bobby[name] = []
    while True:
        bobby = input("请输入喜好：")
        if bobby == "":
            break
        dict_person_bobby[name].append(bobby)

for name, list_bobby in dict_person_bobby.items():
    print("%s喜欢：" % name)
    for item in list_bobby:
        print(item)

