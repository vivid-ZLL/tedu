dict01 = {"城市": {"北京": {"景区": ["故宫", "天安门", "天坛"],
                        "美食": ["烤鸭", "炸酱面", "豆汁", "卤煮"]},
                 "成都": {"景区": ["九寨沟", "峨眉山", "春熙路"],
                        "美食": ["火锅", "串串香", "兔头"]}}}

for k in dict01["城市"]:
    print(k + ":")
    for k, v in dict01["城市"]["北京"].items():
        print("  ", k + ":", ",".join(v))
# print(dict01["城市"]["北京"]["景区"])
# for k in dict01["城市"]["北京"]:
#     print(k)