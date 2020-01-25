temp = open("test02.txt", "r")
# readline函数在参数极大时不会读取下一行元素,直至读完本行
# read函数在参数极大时会读取下一行元素,直至读完全部内容
#readlines函数会取一行所有元素并构建一个列表,如过参数值超过该行元素个数,则取至下一行元素,下一行也以此类推哦
# re = temp.readline(1000)
# print(re)
# re = temp.read(1000)
# print(re)
# re = temp.read(10)
# print(re)
# re = temp.read(10)
# print(re)

# while True:
#     input()
#     re = temp.readlines(3)
#     print(re)
