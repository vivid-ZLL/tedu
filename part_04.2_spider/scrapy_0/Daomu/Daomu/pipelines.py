# -*- coding: utf-8 -*-
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DaomuPipeline(object):
    def process_item(self, item, spider):
        # print(item['content'])
        # print(item['name'])
        # print(item['title'])
        directory = '/home/tarena/novel/{}/'.format(item['title'])
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = directory + item['name'] + '.txt'
        with open(filename,'w') as f:
            f.write(item['content'])

        return item
