f = open("test01.py", "r")



"""
while True:
    data = f.read(3)
    if not data:
        break
    print(data)
data = f.readlines()
print(data)
"""


# while 遍历
# while True:
#     re = f.readline()
#     if not re:
#        break
#     print([re])


# for line in f:
#     list01 = [line]
#     print(list01)

for line in f:
    print(line)
    print(line.split("l"))

f.close()
