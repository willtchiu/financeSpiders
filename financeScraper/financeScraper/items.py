# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinancescraperItem(scrapy.Item):
    # define the fields for your item here like:
    tick     = scrapy.Field()
    headline = scrapy.Field()
    author   = scrapy.Field()
    link     = scrapy.Field()
    text     = scrapy.Field()
    source   = scrapy.Field()
