import random
import time
from urllib import request
from hashlib import md5

import pymysql

from useragents import ua_list
import re


class FilmSkySpider:
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.db = pymysql.connect(
            'localhost', 'root', '123456', 'filmskydb', charset='utf8'
        )
        self.cursor = self.db.cursor()

    # 请求函数
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('gb2312', 'ignore')

        return html

    # 正则解析函数

    def re_func(self, re_bds, html):
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)

        return r_list

    # 解析:一级页面 - 详情页链接
    def parse_html(self, one_url):
        one_html = self.get_html(one_url)
        re_bds = '<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        # 正则表达式匹配一项数据时,返回的是一级列表
        one_list = self.re_func(re_bds, one_html)
        for href in one_list:
            two_url = 'https://www.dytt8.net' + href
            # 在此获取此电影所有数据,然后再遍历下一个
            if self.is_go_on(two_url):
                self.get_film_info(two_url)
                time.sleep(random.randint(1, 2))
                finger = self.md5_string(two_url)
                ins = 'insert into request_finger values(%s)'
                self.cursor.execute(ins, [finger])
                self.db.commit()

    def get_film_info(self, two_url):
        two_html = self.get_html(two_url)
        re_bds = '<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
        # film_list:[('xxx电影','xxx地址'),(),(),....]
        film_list = self.re_func(re_bds, two_html)

        # 电影名称 + 下载链接-
        for item0 in film_list:
            item = {}
            item['name'] = film_list[0][0].strip()
            item['download'] = film_list[0][1].strip()

            print(item)

            ins = 'insert into filmtab values(%s,%s)'
            list01 = [item['name'], item['download']]
            self.cursor.execute(ins, list01)

            self.db.commit()

    def run(self):
        for page in range(1, 2):
            url = self.url.format(page)
            self.parse_html(url)
            time.sleep(0.5)

    def is_go_on(self, two_url):
        """
        判断two_url 是否已经抓取过

        """
        # 先进行md5 加密 request_finger()存的是指纹
        md5_two_url = self.md5_string(two_url)
        # 在数据表中判断
        sel = 'select finger from request_finger where finger = %s'
        result = self.cursor.execute(sel, [md5_two_url])
        if not result:
            return True

    def md5_string(self, string):
        s = md5()
        s.update(string.encode())
        md5_two_url = s.hexdigest()
        return md5_two_url


if __name__ == "__main__":
    spider = FilmSkySpider()
    spider.run()
