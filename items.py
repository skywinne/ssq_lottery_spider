# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LotteryssqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 开奖日期
    date = scrapy.Field()
    # 期号
    issue = scrapy.Field()
    # 第一个红球号码
    red1 = scrapy.Field()
    # 第二个红球号码
    red2 = scrapy.Field()
    # 第三个红球号码
    red3 = scrapy.Field()
    # 第四个红球号码
    red4 = scrapy.Field()
    # 第五个红球号码
    red5 = scrapy.Field()
    # 第六个红球号码
    red6 = scrapy.Field()
    # 蓝球
    blue = scrapy.Field()
