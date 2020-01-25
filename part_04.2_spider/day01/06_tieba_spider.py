from urllib import request, parse
import random
import time
import os
# 查看是否为静态页面
# 找url规律
#  获取网页内容
# 提取数据
# 保存数据
from useragents import ua_list


class TiebaSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        # self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}

    def get_page(self, url):
        # 随机user_agent,避免被反爬
        headers = {'User-Agent': random.choice(ua_list)}
        print(url)
        print('headers:-->', headers)
        req = request.Request(url=url, headers=headers)

        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def parse_page(self, name):
        """
        解析,提取数据
        """
        pass

    # 保存数据
    def write_page(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    # 接口函数
    def run(self):
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        kw = parse.quote(name)
        if not os.path.exists(name):
            os.mkdir(name)
        # 拼接 + 获取内容 + 保存
        for i in range(start, end + 1):
            pn = (i - 1) * 50
            url = self.url.format(kw, pn)
            html = self.get_page(url)
            filename = name + '/' + name + "第{}页.html".format(i)
            self.write_page(filename, html)
            print('第%d页抓取成功' % i)

            # 每爬取一个页面,休眠1-3秒
            time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    spider = TiebaSpider()
    begin = time.time()
    spider.run()
    stop = time.time()
    time0 = stop - begin
    print('总执行的时间为%.2f' % time0)
