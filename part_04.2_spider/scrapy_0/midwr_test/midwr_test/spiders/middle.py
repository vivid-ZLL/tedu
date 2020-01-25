# -*- coding: utf-8 -*-
import time
import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        for i in range(20):
            time.sleep(0.1)

            print('>' * i)
        print('this is the output of parse()')
