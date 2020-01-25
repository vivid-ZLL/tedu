import  pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'test_name',
                     charset = 'utf8')

# 获取游标 （操作数据库，执行sql语句）
cur = db.cursor()


# for i in range(2000000):
#
#     try:
#         sql = "insert into name (id,name) \
#         values (%s,%s)"
#         cur.execute(sql, [i+1, "Alice%s"%(i+1)])
#         db.commit()
#         print("传入数据库次数:",i)
#
#     except Exception as e:
#         db.rollback()
#         print(e)

# 每执行一次execute()方法,意味着与数据库通信一次,所以插入海量数据的效率较慢
# 改用executemany(),减少与数据库的通信次数
    # 正则匹配列表里的sql语句,当sql语句长度超过1024000时,执行一次excute().

# 关闭数据库
cur.close()
db.close()