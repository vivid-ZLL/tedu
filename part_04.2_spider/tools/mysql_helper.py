"""
version 2.0
"""
import pymysql


class MysqlHelper:

    def __init__(self, host='localhost',
                 port=3306,
                 user='root',
                 password='123456',
                 database='testdb',
                 charset='utf8'):
        # 连接数据库
        self.db = pymysql.connect(host=host,
                                  port=port,
                                  user=user,
                                  password=password,
                                  database=database,
                                  charset=charset)

        # 获取游标 （操作数据库，执行sql语句）
        self.cur = self.db.cursor()

    def add_one(self, table, val_list):
        try:
            s_num = ('%s,' * len(val_list))[:-1]

            sql = "insert into {} values({})".format(table,s_num)

            self.cur.execute(sql, val_list)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def delete_all(self, table, where_claus):
        """
        输入表名和where字句进行删除,返回删除数量

        """
        try:
            sql = "delete from {} {}".format(table, where_claus)

            res = self.cur.execute(sql)
            self.db.commit()
            return res
        except Exception as e:
            print(e)
            self.db.rollback()

    def modify(self, table, values, where_claus):
        """
            注意修改字段的引号
            格式 m01.modify('t01','name = "alice"','where id = 4')
        """
        try:
            sql = f'update {table} set {values} {where_claus}'
            res = self.cur.execute(sql, )
            self.db.commit()
            return res
        except Exception as e:
            print(e)
            self.db.rollback()

    def find(self, table, where_clause, range='*'):
        """
            注意查询字段的引号
            格式 -- > m01.find('t01','where name = "alice"','name')
            返回查询结果 (('alice',),.....)
        """
        sql = f"select {range} from {table} {where_clause}"
        self.cur.execute(sql, )
        res = self.cur.fetchall()
        return res

    def add_many(self, table, val_lists):

        try:
            # sql = "insert into {} values(%s,%s)".format(table)
            s_num = ('%s,' * len(val_lists[0]))[:-1]
            # print('snum:',s_num)
            sql_ex = "insert into {} values({})".format(table,s_num)
            # print('sqlex:',sql_ex)
            # sql = "insert into t01 values(%s,%s)"
            # print('sql:',sql)
            self.cur.executemany(sql_ex, val_lists)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()


if __name__ == "__main__":
    m01 = MysqlHelper()
    m01.add_one('t01',[998,'alincia'])
    # m01.add_many('t01', [[998, 'iris'],[1024,'lovince']])
    # re = m01.delete_all('t01', '')
    # print(re)
    # m01.modify('t01', 'name = "alice"', 'where id = 4')
    # m01.find('t01', 'where name = "alice"', 'name')
