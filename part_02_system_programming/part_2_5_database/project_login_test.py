import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="account",
                     charset="utf8")

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()


def regist_acoount():
    while True:
        user_name = input("user:")
        if not user_name:
            break
        password = input("password:")
        one_row = fetch_user_name(user_name)
        # print(one_row) ('incinya', '123456')
        print("用户已存在") if one_row else regist_account(password, user_name)


def regist_account(password, user_name):
    sql = "insert into user values(%s,%s)"
    cur.execute(sql, [user_name, password])  # 执行正确后cur调用函数获取结果
    db.commit()
    print("ok------------")


def fetch_user_name(user_name):
    sql = "select * from user where user = %s"  # 查询多少字段元组里就有多少yuans
    cur.execute(sql, [user_name])  # 执行正确后cur调用函数获取结果
    row = cur.fetchone()
    return row





if __name__ == "__main__":
    regist_acoount()
