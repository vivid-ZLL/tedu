import random
import time
import requests
from fake_useragent import UserAgent
from lxml.html import etree
import csv


class LianjiaSpider:
    def __init__(self):
        self.url = 'https://cd.lianjia.com/ershoufang/pg{}?'

    # 通用功能 获取随机的user-agent
    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        return headers

    # 获取页面
    def get_html(self, url):
        for i in range(3):
            try:
                # 爬取超时时间  5秒
                res = requests.get(url=url, headers=self.get_headers(), timeout=5)
                res.encoding = 'utf-8'
                html = res.text
                return html
            except Exception as e:
                print('Failed,Retry:', i)
                continue

    def parse_html(self, url):
        # html返回值有2种: 1-html 2-none
        html = self.get_html(url)
        if html:
            parse_obj = etree.HTML(html)
            # 基准xpath:li节点对象列表

            li_list = parse_obj.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
            # for 循环遍历,获取一个房源所有信息
            item = {}
            for li in li_list:
                # 名称
                item['name'] = li.xpath('.//a[@data-el="region"]/text()')[0].strip()  # ['兰德华庭']
                # 户型+面积+方位+精装
                # '|x室x厅|xxx平米|南北|精装'
                info_list = li.xpath('.//div[@class="houseInfo"]/text()')[0].split('|')
                item['model'] = info_list[1].strip() if len(info_list) == 5 else None
                item['area'] = info_list[2].strip() if len(info_list) == 5 else None
                item['direction'] = info_list[3].strip() if len(info_list) == 5 else None
                item['perfect'] = info_list[4].strip() if len(info_list) == 5 else None
                # 楼层 + 地区 + 总价 + 单价
                item['floor'] = li.xpath('.//div[@class="positionInfo"]/text()')[0].strip().split('-')[0].strip()
                item['address'] = li.xpath('.//div[@class="positionInfo"]/a/text()')[0].strip()
                item['total'] = li.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()
                item['unit'] = li.xpath('.//div[@class="unitPrice"]/span/text()')[0].strip()

                r_list = [item['name'], item['model'], item['area'], item['direction'], item['perfect'],
                          item['floor'], item['address'], item['total'], item['unit']]

                self.write_item(r_list)

                print(item)
    def write_item(self, r_list):
        """
            单行
            ['alice', 'alicinya']
            多行写入
            [('alice02', 'alicinya02'), ('alice03', 'alicinya03')]
        """
        item = {}
        # 若以w方式打开,则只保留最后一页数据
        with open('lianjia.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(r_list)

    def run(self):
        for pg in range(1, 101):
            url = self.url.format(pg)
            self.parse_html(url)
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    l01 = LianjiaSpider()
    l01.run()
