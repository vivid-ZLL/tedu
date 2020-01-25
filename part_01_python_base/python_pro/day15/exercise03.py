while True:
    try:
        score = int(input("请输入成绩:"))
    except:
        print("输入的不是整数")
        continue
    if 0 <= score <= 100:
        break
    else:
        print("超过范围")