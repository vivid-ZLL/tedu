"""
 存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
  　北京：
        景区：故宫,天安门,天坛.
        美食: 烤鸭,炸酱面,豆汁,卤煮.
    四川:
        景区：九寨沟,峨眉山,春熙路．
        美食: 火锅,串串香,兔头.
"""
dict01 = {
    "北京":
        {
            "景区": ["故宫", "天安门", "天坛"],
            "美食": ["烤鸭", "炸酱面", "豆汁", "卤煮"]
        },
    "四川":
        {
            "景区": ["九寨沟", "峨眉山", "春熙路"],
            "美食": ["火锅", "串串香", "兔头"]
        }
}
# 需求:获取四川的所有美食
print(dict01["四川"]["美食"])
# 需求:获取所有城市

for key in dict01:
    print(key)

# 需求：所有城市的景区
# print(dict01["四川"]["景区"])
# print(dict01["北京"]["景区"])
# print(dict01["xxx"]["景区"])

result = []
# 遍历大字典，获取的是地区
for key in dict01:
    # 遍历景区列表
    for item in dict01[key]["景区"]:
        # 地区+景区
        result.append(key + ":" + item)

print(result)
