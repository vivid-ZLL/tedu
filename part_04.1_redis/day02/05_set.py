import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# python操作redis  set
r.sadd('myset1', 'A', 'B')
re = r.smembers('myset1')
print(re)
print(r.scard('myset1'))
print(r.sismember('myset1', 'B'))

# 交集&并集
r.sadd('myset2', "A", 'B', "C")
r.sadd('myset3', "D", 'B', "C")
re = r.sinter('myset1', 'myset2', "myset3")
print(re)

re = r.sunion('myset1', 'myset2', 'myset3')
print(re)

for item in re:
    re.remove(item)
    re.add(item.decode())

print(re)




