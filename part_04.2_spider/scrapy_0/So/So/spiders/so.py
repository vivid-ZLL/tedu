# -*- coding: utf-8 -*-
import json

import scrapy
from ..items import SoItem

"""
https://image.so.com/j?q=alice+margatroid&src=srp&correct=alice+margatroid&pn=60&ch=&sn=180&ps=177&pc=59&pd=1&prevsn=120&sid=aa47667b237bcaf3a3e0c0cfe5aa6686&ran=0&ras=0&cn=0&gn=0&kn=0&comm=1
"""
"""
https://image.so.com/j?q=alice+margatroid&pn=60&sn=180
"""


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    # start_urls = ['http://image.so.com/']
    url = 'https://image.so.com/zjl?ch=wallpaper&sn=60&pn={}&prevsn=30'

    def start_requests(self):
        for pn in range(0, 100, 30):
            url = self.url.format(pn)
            yield scrapy.Request(

                url=url,
                callback=self.parse_image
            )

    def parse_image(self, response):
        html = json.loads(response.text)
        for img in html['list']:
            item = SoItem()
            item['img_link'] = img['qhimg_url']
            item['title'] = img['title']
            yield item
