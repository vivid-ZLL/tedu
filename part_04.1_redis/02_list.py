import redis

r = redis.Redis()

# 常见服务的端口号
# mysql --> 3306
# mongodb - 27017
# redis - 6379
# http - 80
# https - 443
# ssh - 22  此为远程连接服务
# tel net - 23  此为远程连接服务
# ftp - 21


# 列表操作
r.rpush("tedu:teachers", "LaoQi", 'Maria', 'GuoXN')
r.rpush('tedu:teachers', 'LaoWang')
r.linsert("tedu:teachers", 'after', 'Maria', 'LaoTao')
# 打印长度
print(r.llen('tedu:teachers'))
# 查看所有元素 - 列表
re = r.lrange('tedu:teachers', 0, -1)
print(re)

# 弹出一个元素
re = r.rpop('tedu:teachers')
print(re)

# 保留指定数量的元素
r.ltrim('tedu:teachers', 0, 2)

r.expire('tedu:teachers', 10)

# 阻塞弹出
# 有元素:
# (b'tedu:teachers', b'LaoTao')
# 无元素
# 返回None
while True:
    re = r.brpop('tedu:teachers', 3)
    if not re:
        break
    print(re)


