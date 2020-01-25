"""
使用executemany方法插入多条表记录
"""

import pymysql

db = pymysql.connect(
    'localhost', 'root', '123456', 'maoyandb', charset='utf8'
)

cursor = db.cursor()
# 执行sql命令
ins = 'insert into filmtab values(%s,%s,%s)'
film_list = [('Alice梦游仙境', 'Alice', '1993'), ('Alice', 'Alice', '1993')]
cursor.executemany(ins, film_list)

# 提交到数据库执行
db.commit()
cursor.close()
db.close()
