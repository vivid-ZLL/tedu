# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class SoPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 直接交给调度器入队列
        yield scrapy.Request(
            url=item['img_link'],
            meta={'item': item}
        )

    # 重写file_path()方法:解决 路径+文件名问题
    def file_path(self, request, response=None, info=None):
        # 获取meta属性的值

        title = request.meta['item']['title']
        filename = title + '.jpg'
        return filename
