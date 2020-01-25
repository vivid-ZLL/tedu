"""
python-redis 操作哈希类数据
"""
import redis

r = redis.Redis()

r.hset('user000', 'name', 'alice')
re = r.hget('user000', 'name')
print(re)

# hmset + hmget
# hmget返回的是列表
# hkeys 和 hvals 返回的是列表
user_dict = {
    'password': 123456,
    'gender': 'M',
    'girlfriend': 'chuchu'
}

r.hmset('user0', user_dict)
re = r.hmget('user0', 'password', 'gender', 'girlfriend')
print(re)

re = r.hgetall('user0')
re1 = r.hkeys('user0')
re2 = r.hvals('user0')

print(re)
print(re1)
print(re2)

r.hdel('user0', 'password', 'gender')
print(r.hgetall('user0'))
