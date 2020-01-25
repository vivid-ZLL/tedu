dict01 = {}
string01 = "alicemargatroid"
for i in string01:
    # print(i)
    if i not in dict01:
        dict01[i] = 1
    else:
        dict01[i] += 1
# print(dict01)
for k, v in dict01.items():
    print("%s:%s次" % (k, v))
