"""we
位图操作寻找活跃用户
"""

import redis
import random

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# user:001 :一年中第五天和第二百天登录
r.setbit('user:001', 4, 1)
r.setbit('user:001', 200, 1)

# user:002 :一年中第100天和第300天登录
r.setbit('user:002', 99, 1)
r.setbit('user:002', 299, 1)

# user:003 : 登录了100次以上

times = random.randint(100, 365)

for i in range(times):
    r.setbit('user:003', i, 1)

# user:004  : 登录了100次以上
list01 = [1] * times + [0] * (365 - times)
random.shuffle(list01)
for i in range(365):
    r.setbit('user:004', i, list01[i])

# 列表
user_list = r.keys('user:*')

active_users = []
noactive_users = []

# 遍历作统计
for user in user_list:
    login_count = r.bitcount(user)
    if login_count >= 100:
        active_users.append((user.decode(), login_count))
    else:
        noactive_users.append((user.decode(), login_count))

print('活跃的用户:', active_users)
print('不活跃的用户:', noactive_users)
