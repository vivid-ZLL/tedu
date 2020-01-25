import json
import time
import random
from hashlib import md5
# -*- coding: utf-8 -*-
import scrapy
from ..items import YoudaoItem


class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']
    word = input("请输入要翻译的单词")
    # F12 抓到的url地址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    print("class>>>>>>>>>>>>>>>>>>>>>")
    start_urls = [url]

    @staticmethod
    def get_ts_salt_sign(word):
        # ts
        ts = int((time.time() * 1000))
        # salt
        salt = str(ts) + str(random.randint(0, 9))
        # sign
        # "fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj"
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts, salt, sign

    # 攻克有道
    def attack_yd(self, word):
        print('attack youdao >>>>>>>>>>>>>>>>>')
        ts, salt, sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "59a2ee1b62619c43589e27bb52c2517a",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }

        yield scrapy.FormRequest(url=self.url, formdata=data)

    def parse(self, response):
        print('parse >>>>>>>>>>>>>>>')
        item = YoudaoItem()
        html = json.loads(response.text)
        item['result'] = html['translateResult'][0][0]['tgt']

        yield item
