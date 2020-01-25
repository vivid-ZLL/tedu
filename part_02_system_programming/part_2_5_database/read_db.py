import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()

sql = "select * from class where sex = 'w'"  # 查询多少字段元组里就有多少yuans
cur.execute(sql)  # 执行正确后cur调用函数获取结果

# 获取一个查询结果
one_row = cur.fetchone()

# 获取多个查询结果

many_row = cur.fetchmany(6)

all_row = cur.fetchall()

print(one_row)  # 元组
print(one_row[1])  # 元组
print(many_row)  # 元组套元组
print(all_row)   # 一次获取视为一次迭代,获取完毕后就取不到数据了


# 关闭数据库
cur.close()  # 游标失效
db.close()  # 数据库中断
