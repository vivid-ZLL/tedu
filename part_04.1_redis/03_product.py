"""
生产者:生产url地址
"""
import time
import random
import redis

r = redis.Redis()

# 生产者生产url
for page in range(67):
    url = 'http://app.mi.com/category/2#page={}'.format(page)
    r.lpush('xiaomi:spider', url)
    time.sleep(random.randint(1, 3))
