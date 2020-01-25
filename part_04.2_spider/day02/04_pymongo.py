import pymongo
from urllib import request
import re
import time
import random
from useragents import ua_list


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.i = 0
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['filmtab']

    # 请求
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        print(headers)
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()

        print(html[0:15])

        # 调用解析函数
        r_list = self.parse_html(html)
        self.write_html(r_list)

    # 解析
    def parse_html(self, html):
        """
            [('Alice梦游仙境','Alice','????-??-??'),(),()...]
        """
        re_bds = '<p class="name"><a href=".*?" title=.*?data-act="boarditem-click" \
data-val=".*?">(.*?)</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">.*?(\d+.\d+.\d+).*?</p>'
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)

        return r_list

    def write_html(self, r_list):
        """
            多行写入
        """
        for r in r_list:
            item = {}
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()
            # 插入到Mongodb数据库
            self.myset.insert_one(item)
        # print(item)
        # {'name': '辛德勒的名单', 'star': '主演：连姆·尼森,拉尔夫·费因斯,本·金斯利', 'time': '上映时间：1993-12-15(美国)'}

    # 主函数
    def run(self):
        for offset in range(0, 31, 10):
            try:
                url = self.url.format(offset)
                print(url)
                self.get_html(url)
                # 随机休眠
                time.sleep(random.uniform(3, 4))
            except Exception:
                pass


if __name__ == "__main__":
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    period = end - start
    print("爬取完毕,总计时间:", period)
    print('共获取信息数:', spider.i)
