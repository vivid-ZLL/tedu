import redis

r = redis.Redis()
r.delete('user001:age')
# python操作字符串string

# 1.字符串操作
r.set('user001:name', 'guods')
m_dict = {
    'user001:age': 34,
    'user001:gender': 'M',
}

r.mset(m_dict)
re1 = r.get('user001:name')
# b'guods'

re2 = r.mget('user001:age', 'user001:gender', 'user001:name')
# [b'34', b'M', b'guods']
print(re1)
print(re2)
re = r.strlen('user001:name')
print(re)

# 2.数值类型的字符串操作
r.incr('user001:age')
r.decr('user001:age')

r.incrby('user001:age', 3)
r.decrby('user001:age', 3)

r.incrbyfloat('user001:age', 3)
r.incrbyfloat('user001:age', -3)

print(r.get("user001:age"))


