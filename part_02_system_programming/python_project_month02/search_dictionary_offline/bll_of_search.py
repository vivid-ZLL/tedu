import pymysql
import re
from bll_of_account import AccountDatabase


class SearchDatabase:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="123456",
                                  database="dict",
                                  charset="utf8")
        self.cur = self.db.cursor()  # 获取游标  (操作数据库,执行sql语句)
        self.account = AccountDatabase()

    # -------------- init database code -------------------------------------
    def store_word_in_database(self):
        dict_txt = open("dict.txt")
        id = 1
        for line in dict_txt:
            word_name, meaning, = self.get_line_info(line)
            self.insert_into_database(id, meaning, word_name)
            id += 1

    def insert_into_database(self, id, meaning, word_name):
        try:
            sql = "insert into words (id,word_name,meaning) values (%s,%s,%s)"  # 可以使用列表直接给sql语句的values传值
            self.cur.execute(sql, [id, word_name, meaning])  # 执行sql语句
            self.db.commit()  # 将写操作提交,可以多次写操作一同提交

        except Exception as e:
            self.db.rollback()  # 退回到commit执行之前的数据库状态
            print(e)

    def get_line_info(self, line):
        re_word = re.search(r".*? ", line)
        word_name = re_word.group()
        re_meaning = re.search(r" .*", line)
        meaning = re_meaning.group().strip()
        return word_name, meaning

    # ---------------search code------------------------------

    def access_database_by_word(self, target):
        sql = "select * from words where word_name = %s"  # 查询多少字段元组里就有多少yuans
        try:
            self.cur.execute(sql, [target])  # 执行正确后cur调用函数获取结果
            return self.cur.fetchone()
        except Exception as e:
            print(e)

    def access_database_by_id(self, target):
        sql = "select * from words where id = %s"  # 查询多少字段元组里就有多少yuans
        try:
            self.cur.execute(sql, [target])  # 执行正确后cur调用函数获取结果
            return self.cur.fetchone()
        except Exception as e:
            print(e)

    def search_word(self, word):
        """
        传入单词就查单词意思,传入单词id就查单词id对应的意思
        :param word:
        :return:
        """
        if type(word) == int:
            temp = self.access_database_by_id(word)
        else:
            temp = self.access_database_by_word(word)  # e.g  temp = (1, 'a ', 'indef art one')

        if temp:
            self.account.update_search_history(str(temp[0]))
            print(temp[1] + ":", temp[2])
        else:
            print("灰常不好意思,我是个词典,我莫得这个词")

    # ----------------history code ----------------------------------------
    def print_history(self):
        if self.account.get_history():
            history_list = self.account.get_history().split(",")  # e.g ['3', '1', '3', '3', '10331', '6597']
            print("您查询的历史记录为:")
            for item in history_list:
                self.search_word(int(item))
        else:
            print("--------------没有您的查询记录-------------")

if __name__ == "__main__":
    d01 = SearchDatabase()
    d01.print_history()
