# 练习２：在控制台中获取分钟
# 　　　　再获取小时
# 　　　　再获取天
#       计算总秒数
# 15:35

minute = int(input("请输入分钟："))
hour = int(input("请输入小时："))
day = int(input("请输入天："))
result = minute * 60 + hour * 60 * 60 + day * 24 * 60*60
print("总秒数是:"+str(result))