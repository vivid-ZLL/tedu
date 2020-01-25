import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()

try:

    # name = input("name:")
    # age = input("age:")
    # score = input("score:")
    # sql = "insert into class values (9,%s,%s,'w',%s)"
    #
    # # 可以使用列表直接给sql语句的values传值
    # cur.execute(sql, [name, age, score])  # 执行sql语句



    # 修改操作 ----------------------------------------

    # sql = "update class set age = 18 where name = 'alicinya'"

    sql = "delete from class where name = 'alicinya'"
    cur.execute(sql)



    db.commit()  # 将写操作提交,可以多次写操作一同提交

except Exception as e:
    db.rollback()  # 退回到commit执行之前的数据库状态
    print(e)

# 关闭数据库
cur.close()  # 游标失效
db.close()  # 数据库中断
