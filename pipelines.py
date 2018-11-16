# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class LotteryssqPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='mysql', db='spider', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        lottery_date = item['date']
        issue = item['issue']
        red1 = item['red1']
        red2 = item['red2']
        red3 = item['red3']
        red4 = item['red4']
        red5 = item['red5']
        red6 = item['red6']
        blue = item['blue']
        sql = "insert into lottery_ssq(date, issue, red1, red2, red3, red4, red5, red6, blue) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (lottery_date, issue, red1, red2, red3, red4, red5, red6, blue))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
