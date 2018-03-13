# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime

class FinancescraperPipeline(object):

    def open_spider(self, spider):
        fn = ''
        if spider.tick:
            if spider.name:
                date = "{:%b-%d-%Y}".format(datetime.now())
                fn = "./data/{}_{}-{}.jl".format(spider.name, spider.tick, date)
        self.file = open(fn, 'a')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
