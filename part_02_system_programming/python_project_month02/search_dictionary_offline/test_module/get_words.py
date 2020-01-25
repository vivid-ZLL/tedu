target = input("请输入单词:")
# (6377, 'extortionist ', '[ extort: ] to secure (money, favours, etc.) by intimidation, violence, or the misuse of
#  influence or authority')

import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()

try:
    sql = "select * from words where word_name = %s"  # 查询多少字段元组里就有多少yuans
    cur.execute(sql,[target])  # 执行正确后cur调用函数获取结果

    one_row = cur.fetchone()

    print(one_row)
except Exception as e:
    print(e)

