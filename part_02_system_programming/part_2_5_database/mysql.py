import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()

# 执行sql语句
sql = "insert into class values (7,'Emma',17,'w',76.5)"

cur.execute(sql)  # 执行sql语句

db.commit()  # 将写操作提交,可以多次写操作一同提交

# 关闭数据库
cur.close()  # 游标失效
db.close()  # 数据库中断
