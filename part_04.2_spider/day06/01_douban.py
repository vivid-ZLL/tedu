import random
import time
import re

import requests
import json
import fake_useragent


class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
        self.i = 1

    def get_headers(self):
        headers = {'User-Agent': fake_useragent.UserAgent().random}
        return headers

    # 获取响应内容
    def get_html(self, url):
        html = requests.get(
            url=url,
            headers=self.get_headers()
        ).text

        return html

    # 提取数据 电影名称+评分
    def parse_page(self, url):

        html_json = self.get_html(url)
        # 把json-text 类型转为python 数据类
        html_py = json.loads(html_json)
        for one_film in html_py:
            name = one_film['title']
            score = one_film['score']

            print(name, score)

    def get_total(self, type_code):

        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type_code)
        html = self.get_html(url)
        html = json.loads(html)
        total = html['total']
        return total

    def run(self):
        menu = self.get_code()[1]
        print(menu)
        name = input("请输入抓取的电影类别:")
        # 　通过用户输入，查找对应的类型码
        type_code = self.get_code(name)[0]
        total = self.get_total(type_code)

        for start in range(0, total, 20):
            url = self.url.format(type_code, start)
            self.parse_page(url)
            time.sleep(random.randint(1, 3))

        print('总数', total)

    def get_code(self, name=""):
        # 给定类别返回对应的类型码
        url = 'https://movie.douban.com/chart'
        html = self.get_html(url)
        re_bds = r'type_name=(.*?)&type=(.*?)&interval_id'
        pattern = re.compile(re_bds, re.S)

        r_list = pattern.findall(html)
        menu = ''
        ncode_dic = {}
        i = 1
        for tup in r_list:
            ncode_dic[tup[0]] = tup[1]
            # menu += (tup[0]+'({})|'.format(tup[1]))
            menu += (tup[0]+'|')
            i += 1
        type_code = ncode_dic[name] if name else None
        return type_code,menu

d01 = DoubanSpider()
d01.run()
