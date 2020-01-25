from multiprocessing import Process
"""
图片文件开头有解析标识符,所以下半部分图片看不到
"""


file = open("Alice_moe.jpg", "rb")
re = file.read()
# print(re)
# print(type(re))


def copy_upper_file(copied_string):
    file = open("upper_copy.jpg", "wb")
    file.write(copied_string[:len(copied_string) // 2])


def copy_lower_file(copied_string):
    file = open("lower_copy.jpg", "wb")
    file.write(copied_string[len(copied_string) // 2:])


work_list = [copy_lower_file, copy_upper_file]
complete_list = []

for item in work_list:
    p = Process(target=item, args=(re,))
    complete_list.append(p)
    p.start()

for item in complete_list:
    item.join()
