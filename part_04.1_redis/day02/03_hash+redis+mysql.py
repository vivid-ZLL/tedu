"""
hash +redis+mysql综合使用
"""

import pymysql
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

db = pymysql.connect(
    host='localhost',
    user="root",
    password='123456',
    database='userdb'

)

cursor = db.cursor()
# 输入要查询的用户名
# 先到redis中查询
# redis中没有再到mysql中查询

username = input("请输入用户名:")
result = r.hgetall(username)
print(result)
# result -->  {}


# 存在数据:
if result:
    print('redis-result:', result)
# 不存在数据
else:
    # 1.mysql中查询
    sel = "select * from user where name = %s"
    cursor.execute(sel, [username])

    userinfo = cursor.fetchall()
    if not userinfo:
        print('用户不存在')
    else:
        print('mysql:', userinfo)
        # userinfo (('25',m,90))

        # 2.缓存到redis中一份,设置过期时间30秒(减少mysql的负载)
        user_dict = {
            'age': userinfo[0][0],
            'gender': userinfo[0][1],
            'score': userinfo[0][2],
        }
        r.hmset(username, user_dict)
        # 设置过期时间30s
        r.expire(username, 30)

# hash
# key field value
# niefeng   age
#           gender
#           score
