result = []
str01 = "How are you"
list01 = str01.split(" ")
print(list01)
for i in range(-1, -len(list01) - 1, -1):
    result.append(list01[i])
print(result)
result = " ".join(result)
print(result)
