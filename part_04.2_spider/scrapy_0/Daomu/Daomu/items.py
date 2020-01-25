# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # 确定需要的数据
    # 一级页面标题 - 创建文件夹
    title = scrapy.Field()
    # 二级页面标题 - 文件名称
    name = scrapy.Field()
    # 小说的内容
    content = scrapy.Field()


