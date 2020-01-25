import pymysql
import re

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")
# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()
dict_txt = open("dict.txt")
id = 0

for line in dict_txt:
    c01 = re.search(r".*? ", line)
    # print(c01.group())
    word_name = c01.group()
    c02 = re.search(r" .*", line)
    # print(c02.group().strip())
    meaning = c02.group().strip()
    id += 1

    try:

        sql = "insert into words (id,word_name,meaning) values (%s,%s,%s)"

        # 可以使用列表直接给sql语句的values传值
        cur.execute(sql, [id, word_name, meaning])  # 执行sql语句

        db.commit()  # 将写操作提交,可以多次写操作一同提交

    except Exception as e:
        db.rollback()  # 退回到commit执行之前的数据库状态
        print(e)

# 关闭数据库
cur.close()  # 游标失效
db.close()  # 数据库中断
