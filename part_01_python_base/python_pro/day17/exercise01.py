list02 = ["0_zero", 233, 496, 7, 245, 56]
#
# def my_enumerate():
#     for i in range(len(list01)):
#         index = i
#         element = list01[i]
#         print (index,element)
#
# my_enumerate()


list01 = ["alice", "marisa", "flandre"]


#
#
# def my_zip():
#     if len(list01) < len(list02):
#         l = len(list01)
#     else:
#         l = len(list02)
#     for i in range(l):
#         print(list01[i], list02[i])
#
#
# my_zip()

def my_zip(*args):
    for i in range(len(args[0])):
        list_result = []
        for item in args:
            list_result.append(item[i])
        yield (tuple(list_result))


for item in my_zip(list01, list02):
    print(item)
# for item in my_zip(list02, list01):
#     print(item)
 