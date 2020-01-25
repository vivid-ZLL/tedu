"""
一级页面地址:https://careers.tencent.com/tencentcareer/api/post/Query?countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn
{index} --> postid
二级页面地址:https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1568604345180&postId={}&language=zh-cn
{postid} --> 岗位详情

"""
import json

import requests
import time
import random
import fake_useragent
from urllib import parse


class TencentSpider:
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1568604345180&postId={}&language=zh-cn'

    @staticmethod
    def get_headers():
        headers = {'User-Agent': fake_useragent.UserAgent().random}
        return headers

    # 获取json数据
    def get_json(self, url):
        html = requests.get(url=url, headers=self.get_headers()).text
        html_json = json.loads(html)

        return html_json

    def parse_html(self, one_url):
        one_html = self.get_json(one_url)
        # for 遍历每一个职位的postId
        for one in one_html['Data']['Posts']:
            postId = one['PostId']
            two_url = self.two_url.format(postId)
            self.parse_two_page(two_url)

    def parse_two_page(self, two_url):
        two_html = self.get_json(two_url)
        item = {}
        item['name'] = two_html['Data']['RecruitPostName']
        item['requirement'] = two_html['Data']['RecruitPostName']
        item['postid'] = two_html['Data']['PostId']

        print(item)

        return item

    def get_total(self, keyword):
        url = self.one_url.format(keyword, 1)
        html = self.get_json(url)
        total = html['Data']['Count'] // 10 + 1

        # print(html)
        # print(total)
        return total

    def run(self):
        keyword = input('enter your job name,master-->')
        keyword = parse.quote(keyword)

        total = self.get_total(keyword)
        for index in range(1, total+1):
            one_url = self.one_url.format(keyword,index)
            self.parse_html(one_url)
            time.sleep(random.randint(1, 2))


t01 = TencentSpider()
t01.run()
