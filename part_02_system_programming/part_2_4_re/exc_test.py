"""
    需求:按空行拆分exc.txt中的文件并存入文件temp_n
"""

s = open("exc.txt", "r")
data = s.read()

data = data.split("\n\n")
print(data)
print(len(data))

i = 1
for item in data:
    c = open("temp/temp_%s" % i, "w")
    c.write(item)
    i += 1
