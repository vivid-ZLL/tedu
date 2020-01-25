import pymysql

class Database:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="123456",
                                  database="dict",
                                  charset="utf8")
        self.cur = self.db.cursor()  # 获取游标  (操作数据库,执行sql语句)

    def main(self):
        sql = "create database create_database_test"  # 查询多少字段元组里就有多少
        try:
            self.cur.execute(sql)  # 执行正确后cur调用函数获取结果

            self.db.commit()  # 将写操作提交,可以多次写操作一同提交
        except Exception as e:
            print(e)


if __name__ == "__main__":
    d01 = Database()
    d01.main()
