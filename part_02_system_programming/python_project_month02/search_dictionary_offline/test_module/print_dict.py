import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()

sql = "select * from words "  # 查询多少字段元组里就有多少yuans
cur.execute(sql)  # 执行正确后cur调用函数获取结果


all_row = cur.fetchall()


print(all_row ,end= "")   # 一次获取视为一次迭代,获取完毕后就取不到数据了
# (6377, 'extortionist ', '[ extort: ] to secure (money, favours, etc.) by intimidation, violence, or the misuse of influence or authority')

# 关闭数据库
cur.close()  # 游标失效
db.close()  # 数据库中断
