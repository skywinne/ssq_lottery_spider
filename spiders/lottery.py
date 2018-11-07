# -*- coding: utf-8 -*-
import scrapy
from ..items import LotteryssqItem


class LotterySpider(scrapy.Spider):
    name = 'lottery'
    allowed_domains = ['zhcw.com']
    start_urls = ['http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html']
    index = 1

    def parse(self, response):

        node_list = response.xpath("//tr")
        node_list.pop(0)
        node_list.pop(0)
        node_list.pop()

        for node in node_list:
            item = LotteryssqItem()

            item["date"] = node.xpath("./td[1]/text()").extract_first()
            item["issue"] = node.xpath("./td[2]/text()").extract_first()
            item["red1"] = node.xpath("./td[3]/em[1]/text()").extract_first()
            item["red2"] = node.xpath("./td[3]/em[2]/text()").extract_first()
            item["red3"] = node.xpath("./td[3]/em[3]/text()").extract_first()
            item["red4"] = node.xpath("./td[3]/em[4]/text()").extract_first()
            item["red5"] = node.xpath("./td[3]/em[5]/text()").extract_first()
            item["red6"] = node.xpath("./td[3]/em[6]/text()").extract_first()
            item["blue"] = node.xpath("./td[3]/em[7]/text()").extract_first()

            yield item

        self.index += 1
        next_url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_{}.html".format(self.index)
        yield scrapy.Request(url=next_url, callback=self.parse)