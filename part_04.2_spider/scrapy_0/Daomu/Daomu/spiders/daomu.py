# -*- coding: utf-8 -*-
import scrapy

from ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        # 基准xpath
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for a in a_list:
            item = DaomuItem()
            item['title'] = a.xpath('./text()').get()
            link = a.xpath('./@href').get()
            yield scrapy.Request(
                url=link,
                callback=self.parse_two_page,
                # 不同解析函数之间传递数据
                meta={'item': item}
            )

    # 解析二级页面函数 : 文件名 + 内容链接
    def parse_two_page(self, response):
        article_list = response.xpath('//article')
        item = response.meta['item']
        for article in article_list:
            name = article.xpath('./a/text()').get()
            two_link = article.xpath('./a/@href').get()
            # 继续交给调度器入队列
            yield scrapy.Request(
                url=two_link,
                meta={'item': item,
                      'name':name},
                callback=self.parse_three_page
            )

    # 解析三九页面函数 : 小说内容
    def parse_three_page(self, response):
        item = response.meta['item']
        # ['<p>','<p>'...]
        p_list = response.xpath('//article[@class="article-content"]//p/text()').extract()
        content = "\n".join(p_list)
        item['content'] = content
        item['name'] = response.meta['name']
        yield item
