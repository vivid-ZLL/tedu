import re

import requests
from lxml import etree


class GovSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    # 提取最新的行政区划代码链接
    def get_false_url(self):
        html = requests.get(self.url, headers=self.headers).text
        parse_html = etree.HTML(html)
        # 把14个a节点对象提取出来
        # for 依次遍历,寻找最新的链接
        # 判断名字是否以 行政区划代码 结尾
        name_list = parse_html.xpath("//a[@class='artitlelist']/text()")
        href_list = parse_html.xpath("//a[@class='artitlelist']/@href")
        # print(name_list)
        # input()
        for i in range(len(name_list)):
            if name_list[i].endswith('行政区划代码'):
                return 'http://www.mca.gov.cn' + href_list[i]
                # break

    def get_real_url(self):
        false_url = self.get_false_url()
        # print(false_url)
        html = requests.get(false_url, headers=self.headers).text
        # print(html)
        re_bds = 'window.location.href="(.*?.html)'
        pattern = re.compile(re_bds)
        result = pattern.findall(html)
        # print(result) #['http://www.mca.gov.cn/article/sj/xzqh/2019/201908/201908271607.html']
        return result[0]

    def get_data(self, real_url):
        result = self.get_real_url()
        print(result)
        html = requests.get(result, headers=self.headers).text
        # print(html)
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//tr[@height="19"]')
        # print(r_list)
        # input()
        for tr in tr_list:
            code = tr.xpath('./td[2]/text()')[0]
            name = tr.xpath('./td[3]/text()')[0]
            print(code, name)

    def run(self):
        real_url = self.get_real_url()
        self.get_data(real_url)


if __name__ == "__main__":
    s01 = GovSpider()
    s01.run()
    # print(res)
