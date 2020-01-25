import pymongo


class MongoHelper:
    def __init__(self, localhost, db, set):
        self.conn = pymongo.MongoClient(localhost, 27017)
        self.db = self.conn[db]
        self.myset = self.db[set]

    def add_one(self, item):
        self.myset.insert_one(item)

    def delete_one(self, item):
        """
            找到一个删除一个
        """
        self.myset.delete_one(item)

    def delete_all(self, item):
        """
            找到一个删除所有
        """
        self.myset.delete_many(item)

    def find_all(self, item):
        """
            找到所有匹配的字段
        """
        res = self.myset.find(item)
        result_list = []
        for row in res:
            result_list.append(row)
        return result_list

    def modify_one(self, old_item, new_item):
        """
        找到一个替换一个, item>>字典格式
        """
        re = self.myset.find_one_and_replace(old_item, new_item)

        return re


if __name__ == "__main__":
    m01 = MongoHelper('localhost', 'maoyandb', 'filmtab')
    item = {'name': '辛德勒的名单', 'star': '主演：连姆·尼森,拉尔夫·费因斯,本·金斯利', 'time': '上映时间：1993-12-15(美国)'}
    # m01.add_one(item)
    # m01.delete_one({'name':'辛德勒的名单'})
    # m01.delete_many({'name': '辛德勒的名单'})
    # m01.find({'name': '辛德勒的名单'})
    m01.modify_one({'name': '辛德勒的名单'}, {'name': '998'})
