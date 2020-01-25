list01 = [6, "alice", 1.23, 12, True, "from", 876]

# def fun01():
#     for item in list01:
#         if type(item) == int:
#             yield item

#
# for item in fun01():
#     print(item)

def fun01():

    for item in list01:
        if type(item) == str or type(item) == float:
            yield item


for item in fun01():
    print(item)

re = (item for item in list01 if type(item) == str or type(item) == float)

for item in re:
    print(item)

re = [item for item in list01 if type(item) == str or type(item) == float]
for item in re:
    print(item)
