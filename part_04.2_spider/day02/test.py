import pymongo


class Solution:

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['baiduSpider']
        self.myset = self.db['tiebaImg']

    def img_is_repeat(self, img_name):

        item = {'name':img_name}
        re = self.myset.find_one(item)
        if not re:
            self.myset.insert_one(item)
        else:
            print(img_name,'数据已存在')

s01 = Solution()
s01.img_is_repeat('test_data')



