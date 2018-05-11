# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FictionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 排名
    top = scrapy.Field()
    # 类别
    url = scrapy.Field()
    type_ = scrapy.Field()
    # 作品
    name = scrapy.Field()
    # 最后章节
    # 更新时间
    update_time = scrapy.Field()
    # 作者
    author = scrapy.Field()
