import os

import requests
from lxml.html import etree
import fake_useragent


class Code_spider:
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1905/13_redis/'
        self.auth = ('tarenacode', 'code_2013')

    def get_headers(self):
        ua = {'User-Agent': fake_useragent.UserAgent().random}
        return ua

    def parse_html(self):
        html = requests.get(
            url=self.url,
            auth=self.auth,
            headers=self.get_headers()
        ).text

        # 解析数据
        parse_obj = etree.HTML(html)
        href_list = parse_obj.xpath('//a/@href')
        print(href_list)  # ['../', 'day01/', 'day02/', 'day03/', '04_hash%2bredis%2bmysql_update.zip', ...]
        # print(html)
        for href in href_list:
            if href.endswith('.zip') or href.endswith('.rar'):
                self.save_file(href)

    def run(self):
        self.parse_html()

    def save_file(self, href):
        # href: redis_day01.rar
        base_directory = '/home/tarena/code/'
        directory = base_directory + '/'.join(self.url.split('/')[3:-1]) + '/'
        # print(directory) # /home/tarena/codeAIDCode/aid1905/13_redis/
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_url = self.url + href
        html = requests.get(file_url, auth=self.auth, headers=self.get_headers()).content
        filename = directory + href  # /home/tarena/codeAIDCode/aid1905/13_redis/redis_day01.zip
        with open(filename, 'wb') as f:
            f.write(html)
        print(filename, '下载成功!!')


if __name__ == "__main__":
    c01 = Code_spider()
    c01.run()
