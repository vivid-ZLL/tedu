import pymysql
import hashlib


class AccountDatabase:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="123456",
                                  database="account",
                                  charset="utf8")
        # 获取游标  (操作数据库,执行sql语句)
        self.cur = self.db.cursor()
        self.account = "incinya"   # 默认用户名为incinya,方便测试

    # ------------------register code----------------
    def register_account(self, name, password):

        encrypted_password = self.md5_encrypt(password)
        self.add_in_database(name, encrypted_password)
        print("注册成功")
        self.account = name
        return True

    def md5_encrypt(self, password):
        e01 = hashlib.md5()
        e01.update(password.encode(encoding="utf-8"))
        return e01.hexdigest()

    def add_in_database(self, name, password):
        try:
            sql = "insert into user (user,password) values (%s,%s)"
            # 可以使用列表直接给sql语句的values传值
            self.cur.execute(sql, [name, password])  # 执行sql语句
            self.db.commit()  # 将写操作提交,可以多次写操作一同提交

        except Exception as e:
            self.db.rollback()  # 退回到commit执行之前的数据库状态
            print(e)

    def check_user_name(self, name):

        if self.name_is_single(name) and self.verify_name_format(name):
            return True
        return False

    def check_password(self, password):
        while True:
            if password.isalnum() and 6 <= len(password) <= 12:
                break
            else:
                print("密码格式错误,6 - 12位数字、字母")
                password = input("请重新输入密码:")
        return password

    def name_is_single(self, user_name):
        sql = "select * from user where user = %s"
        self.cur.execute(sql, [user_name])  # 执行正确后cur调用函数获取结果
        one_row = self.cur.fetchone()
        if one_row:
            print("用户名已存在,请重新输入(#‵′)")
            return False
        return True

    def verify_name_format(self, name):
        name = name.replace("_", "")
        if not name.isalnum():
            print("用户名格式错误(数字,字母,下划线),请重新输入(#‵′)")
        else:
            return True

    # -----------------login code------------------
    def login(self, name, password):

        if self.verify_login(name, password):
            return True
        else:
            print("输入有误!,请重新输入")
            return False

    def verify_login(self, user_name, password):
        sql = "select * from user where user = %s"
        self.cur.execute(sql, [user_name])  # 执行正确后cur调用函数获取结果

        one_row = self.cur.fetchone()  # 示例(1, 'incinya', '123456')
        if one_row and one_row[2] == password:
            print("登录成功")
            self.account = user_name
            return True
        return False

    # -------------------history code----------------------
    def update_search_history(self, word_id):
        try:
            history = self.get_history()
            history_id_list = self.set_history_list(history, word_id)
            updated_history_string = ",".join(history_id_list)
            sql = "update user set history = %s where user = %s"

            self.cur.execute(sql, [updated_history_string, self.account])  # 执行sql语句
            self.db.commit()  # 将写操作提交,可以多次写操作一同提交

        except Exception as e:
            self.db.rollback()  # 退回到commit执行之前的数据库状态
            print(e)

    def set_history_list(self, his_str, id):
        """
         # e.g  his_str = "1698,4785,236"  id = "236"
         # e.g  return['998', '1698', '4785', '236']

        """
        temp = id + "," + his_str
        temp = temp.split(",")
        while len(temp) > 10:
            del temp[-1]
        return temp

    def get_history(self):
        """
            打印历史记录字符串
        :return: e.g "3,1,3,3,10331,6597,1,3,56"
        """
        try:
            sql = "select * from user where user = %s"
            self.cur.execute(sql, [self.account])
            history = self.cur.fetchone()[3]  # e.g (1, 'incinya', '123456', '56')
            return history
        except Exception as e:
            self.db.rollback()  # 退回到commit执行之前的数据库状态
            print(e)


if __name__ == "__main__":
    d01 = AccountDatabase()
    print(d01.get_history())
