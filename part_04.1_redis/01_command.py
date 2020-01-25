import redis

r = redis.Redis()

# 通用命令行实例
# 列表
result = r.keys("*")
print(result)
print('====================')
# for item in result:
#     print(item.decode())

re = r.type('name')
print(re)
print('------------------')

# 返回列表是否存在  0或者1
re = r.exists('name')
print(re)

print('---------------------')
# 设置过期时间
# r.expire('name',5)
# ---------------------------

# 删除键,没有键是不报错的
r.delete('name02')
print('name02删除成功')


