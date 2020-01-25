def count_total_seconds(hour=0, minute=0, sec=0, ):
    return hour * 3600 + minute * 60 + sec
    # 函数传入的是可变对象
    # 函数修改的不是传入的对象


print(count_total_seconds(1))
