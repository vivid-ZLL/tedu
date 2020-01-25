list01 = []
for item in range(1, 11):
    list01.append(item ** 2)
print(list01)

list01 = [item ** 2 for item in range(1, 11)]
print(list01)

result = []
for item in list01:
    if item % 2 == 1:
        result.append(item)
print(result)
result = [item for item in list01 if item % 2 == 1]
print(result)

list03 = []
for item in list01:
    if item % 2 == 0:
        list03.append(item)
print(list03)
list03 = [item for item in list01 if item % 2 == 0]
print(list03)

list04 = []
for item in list01:
    if item % 2 == 0 and item > 5:
        list04.append(item + 1)
print(list04)
list04 = [item + 1 for item in list01 if item % 2 == 0 and item > 5]
print(list04)
