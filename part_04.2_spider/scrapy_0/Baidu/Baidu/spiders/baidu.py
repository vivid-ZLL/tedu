# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 默认的爬虫名字
    name = 'baidu'
    # 允许爬取的域名
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # 提取'百度一下...'
        res = response.xpath('/html/head/title/text()')
        print('*' * 60)
        print(res)
        print('*' * 60)
