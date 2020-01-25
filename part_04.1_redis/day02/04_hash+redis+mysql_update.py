"""
hash +redis+mysql综合使用
"""

import pymysql
import redis


# 输入要查询的用户名
# 先到redis中查询
# redis中没有再到mysql中查询

class Update:
    def __init__(self):
        self.db = pymysql.connect('127.0.0.1', 'root', '123456', 'userdb', charset='utf8')
        self.cursor = self.db.cursor()
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    # 更新mysql表记录
    def update_mysql(self, score, username):

        upd = 'update user set score = %s where name = %s'
        try:
            code = self.cursor.execute(upd, [score, username])
            if code == 1:
                # 如果code不为1,说明新成绩与原成绩相同或者查询的username不存在
                self.db.commit()
                return True
        except Exception as e:
            self.db.rollback()
            print('Failed', e)

    # 更新update表记录
    def update_redis(self, username, score):
        result = self.r.hgetall(username)
        if result:
            # 存在该字段,更新该值
            self.r.hset(username, 'score', score)
        else:
            # 不存在该字段,缓存整个用户信息
            # 在mysql中查询数据,缓存到redis
            self.select_mysql(username)

    def select_mysql(self, username):
        sel = 'select age,gender,score from user where name = %s'
        self.cursor.execute(sel, [username])
        result = self.cursor.fetchall()

        # 缓存到mysql数据库
        user_dict = {
            'age': result[0][0],
            'gender': result[0][1],
            'score': result[0][2]
        }
        self.r.hmset(username, user_dict)
        self.r.expire(username, 60)

    def main(self):
        username0 = input('请输入用户名')
        new_score = input('请输入新成绩')
        if self.update_mysql(new_score, username0):
            print("mysql更新成功")
            self.update_redis(username0, new_score)
            print("redis更新成功")
        else:
            print('mysql更新失败')


if __name__ == "__main__":
    ...
    syn = Update()
    syn.main()
    # if update_mysql():
    #     print('mysql更新成功')
    #     update_redis()
    #     print("redis更新成功")
    # else:
    #     print("更改信息失败")
