# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan2'
    allowed_domains = ['maoyan.com']
    # start_urls = ['https://maoyan.com/board/4']
    offset = 0
    count = 0

    def parse(self, response):
        item = MaoyanItem()
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            # extract()之后:['乱世佳人']
            item['name'] = dd.xpath('./a/@title').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()
            # 把数据交给管道文件 - pipelines.py
            self.count += 1
            yield item

        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)

            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def start_requests(self):
        for offset in range(0, 91, 10):
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
            # 交给调度器入队列
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

