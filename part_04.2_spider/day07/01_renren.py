import fake_useragent
import requests
from lxml import etree


class RenRenLogin:
    def __init__(self):
        self.url = 'http://www.renren.com/972267469/profile'

        # 抓取数据 个人信息
        ''

        self.headers = {
            # 'cookie': 'anonymid=k0n5mrnh16qfl1; depovince=GW; _r01_=1; JSESSIONID=abcJ1x3-DUqAI8qzH080w; ick_login=b93b8e8b-f8be'
            #           '-430a-b3fc-45dffd643f75; ick=7d2cb8ec-127a-4b8f-b23f-794ef96c60ef; t=c2e24ee673b458b65497e2c20fd832af9; '
            #           'societyguester=c2e24ee673b458b65497e2c20fd832af9; id=972267469; xnsid=c31f164e; XNESSESSIONID=d68d04e25ee'
            #           'b; WebOnLineNotice_972267469=1; jebecookies=0722d56d-6f76-4884-99db-d528f2175262|||||; ver=7.0; loginfro'
            #           'm=null; jebe_key=00754bf4-792b-40f9-b599-19d9e23a6a60%7C6e61b9d6a9a2e642af28c9d0dc47f41e%7C156868452422'
            #           '1%7C1%7C1568684526311; jebe_key=00754bf4-792b-40f9-b599-19d9e23a6a60%7C6e61b9d6a9a2e642af28c9d0dc47f41e%7'
            #           'C1568684524221%7C1%7C1568684526317; wp_fold=0',

            'User-Agent': fake_useragent.UserAgent().random
        }

        self.cookie = "anonymid=k0n5mrnh16qfl1; depovince=GW; _r01_=1; JSESSIONID=abcJ1x3-DUqAI8qzH080w; ick_login=b93b8e8b-f8be-430a-b3fc-45dffd643f75; ick=7d2cb8ec-127a-4b8f-b23f-794ef96c60ef; t=c2e24ee673b458b65497e2c20fd832af9; societyguester=c2e24ee673b458b65497e2c20fd832af9; id=972267469; xnsid=c31f164e; XNESSESSIONID=d68d04e25eeb; ver=7.0; loginfrom=null; jebe_key=00754bf4-792b-40f9-b599-19d9e23a6a60%7C6e61b9d6a9a2e642af28c9d0dc47f41e%7C1568684524221%7C1%7C1568684526311; jebe_key=00754bf4-792b-40f9-b599-19d9e23a6a60%7C6e61b9d6a9a2e642af28c9d0dc47f41e%7C1568684524221%7C1%7C1568684526317; wp_fold=0; jebecookies=03ab6c93-c02b-4cc1-acbd-93a8452ce617|||||"


    def get_cookies(self):
        cookie_dict = {}
        for kv in self.cookie.split('; '):
            # kv: 'td_cookie=184xxx'
            key = kv.split('=')[0]
            value = kv.split('=')[1]
            cookie_dict[key] = value
        print(cookie_dict)

        return cookie_dict

    def parse_html(self):
        html = requests.get(self.url, headers=self.headers,cookies = self.get_cookies()).text
        parse_obj = etree.HTML(html)
        xpath_bds = '//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'
        r_list = parse_obj.xpath(xpath_bds)
        # r_list   ['就读于成都冶金职工大学']
        print(r_list)

    def run(self):
        self.parse_html()


r01 = RenRenLogin()
r01.run()
