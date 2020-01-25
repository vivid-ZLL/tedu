target = input("输入文件路径:")

temp_read = open(target,"rb")
temp_write = open("copy_result","wb")

while True:
    read_data = temp_read.read(1024) # 每次读写固定长度,避免内存不够
    if not read_data:
        break
    temp_write.write(read_data)

