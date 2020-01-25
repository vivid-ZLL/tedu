import re


dict_txt = open("dict.txt")

for line in dict_txt:

    c01 = re.search(r".*? ", line)
    print(c01.group())

    c02 = re.search(r" .*", line)
    print([c02.group()])
    print(c02.group().strip())
