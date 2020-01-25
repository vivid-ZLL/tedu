total_sec = int(input("请输入秒钟数："))

hour = total_sec // 3600
min = (total_sec - hour * 3600) // 60
sec = total_sec % 60

print("共", hour, "小时", min, "分", sec, "秒")
