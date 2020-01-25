import os
from urllib import request
import re
from useragents import ua_list
import time
import random


class MovieSpider(object):
    def __init__(self, url):
        self.url = url

    # 通用功能1 获取响应内容
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        # print(headers)
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read()
        print(html[0:15])
        return html

    # 通用功能2 解析提取数据
    def re_func(self, re_bds, html):
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        return r_list

    # 功能3  获取想要的数据 - 解析一级页面
    def parse_one_page(self, url):
        html_p01 = self.get_html(url).decode(encoding = 'GBK')
        print(html_p01)

        re_bds = '<b>.*?<a href="(.*?)" class="ulink">.*?</a>.*?</b>'
        # list_p01 =  [('','','',''),(),(),.....]
        list_p01 = self.re_func(re_bds, html_p01)
        print(list_p01)
        input()
        # 直接调用数据处理函数
        self.write_one_page(list_p01)

    # 功能4  写入一级页面
    def write_one_page(self,r_list):
        ...

    def run(self):
        for i in range(4):
            url = self.url.format(i)
            self.parse_one_page(url)


if __name__ == "__main__":
    url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    m01 = MovieSpider(url)
    m01.run()

