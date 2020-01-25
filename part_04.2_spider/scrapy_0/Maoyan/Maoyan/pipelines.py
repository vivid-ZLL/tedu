# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from .settings import *
from .mysql_helper import MysqlHelper


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'], item['time'], item['star'])
        return item


class MaoyanMysqlPipeline:
    def open_spider(self, spider):
        """
            爬虫程序开始时执行一次
            一般用于创建数据库链接
        """
        self.db = MysqlHelper(MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PWD, database=MYSQL_DB)
        print('数据库已连接')
        print('>' * 70)

    def process_item(self, item, spider):
        L = [
            item['name'],
            item['star'],
            item['time'],
        ]

        self.db.add_one('filmtab', L)
        return item

    def close_spider(self, spider):
        """
            爬虫程序结束时执行一次
            一般用于断开数据库链接
        """
        self.db.cur.close()
        self.db.db.close()
        print('数据库链接已断开')
        print('=' * 60)


class MaoyanMongoPipeline:
    def process_item(self, item, spider):
        return item


class MaoyanRedisPipeline:
    def process_item(self, item, spider):
        return item
