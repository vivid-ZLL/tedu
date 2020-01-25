# list01 = ["无忌", "赵敏", "周芷若"]
# dict01 = {}
# for item in list01:
#     dict01[item] = len(item)
# print(dict01)

list01 = ["无忌", "赵敏", "周芷若","灭绝师太"]
result = [101, 102, 103, 101]
# dict01 = {}
# for i in range(len(list01)):
#     dict01[list01[i]] = list02[i]
# print(dict01)

dict01 = {list01[i]: result[i] for i in range(len(list01))}
print(dict01)

list03 = [(value , key) for key , value in dict01.items()]
print(list03)

for item in range(len(list03)):
    if list03[item][0] == 101:
        print(list03[item][1])
