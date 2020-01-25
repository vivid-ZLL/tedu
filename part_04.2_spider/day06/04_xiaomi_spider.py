import requests
from lxml.html import etree
import fake_useragent
from threading import Thread
from queue import Queue
import time
import csv
from threading import Lock


class XiaomiSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        # 创建空队列
        self.q = Queue()
        # 打开文件 存csv
        self.f = open('xiaomi.csv', 'a')
        self.writer = csv.writer(self.f)
        self.lock = Lock()
        self.i = 0

    # 随机headers
    @staticmethod
    def get_headers():
        headers = {'User-Agent': fake_useragent.UserAgent().random}
        return headers

    # 类型+类型码
    def get_code(self):
        one_url = 'http://app.mi.com/'
        html = requests.get(url=one_url, headers=self.get_headers()).text
        # 解析
        parse_obj = etree.HTML(html)
        li_list = parse_obj.xpath('//ul[@class="category-list"]/li')
        for li in li_list:
            app_type = li.xpath('./a/text()')[0]
            app_code = li.xpath('./a/@href')[0].split('/')[-1]
            app_total = self.get_app_total(app_code)

            # 把每个应用类别的url地址入队列
            self.url_in(app_total, app_code)

    # url入队列
    def url_in(self, app_total, app_code):
        if not app_total:
            return
        for page in range(0, app_total):
            url = self.url.format(page, app_code)
            self.q.put(url)

    # 线程事件函数 - 请求+解析+保存
    def parse_page(self):
        # 队列不为空时,get()
        while True:
            # 每抓取一页,将数据写入csv文件
            app_list = []

            if not self.q.empty():
                url = self.q.get()
                try:
                    html = requests.get(url, self.get_headers())
                    html = html.json()
                except Exception:
                    return

                for app in html['data']:
                    name = app['displayName']
                    link = 'http://app.mi.com/details?id=' + app['packageName']
                    print(name, link)
                    app_list.append((name, link))
                    self.lock.acquire()
                    self.writer.writerows(app_list)
                    self.lock.release()
                    self.i += 1

            else:
                break

    # 入口函数
    def run(self):
        # url入队列
        self.get_code()
        # 创建多线程
        t_list = []
        for i in range(10):
            t = Thread(target=self.parse_page)
            t_list.append(t)
            t.start()
        for t in t_list:
            t.join()
        self.f.close()
        print(self.i)

    def get_app_total(self, app_code):
        """
        获取应用分类的总页数
        """
        url = self.url.format(1, app_code)
        try:
            html = requests.get(url, self.get_headers())

            html = html.json()
        except Exception:
            return
        # print(html) {'count': 2000, 'data': [{'appId': 869814, 'displayName': '恋爱辅助器',
        app_total = html['count'] // 30 + 1

        return app_total


if __name__ == "__main__":
    begin = time.time()
    x01 = XiaomiSpider()
    x01.run()
    end = time.time()
    print('执行时间:%.2f' % (end - begin))
