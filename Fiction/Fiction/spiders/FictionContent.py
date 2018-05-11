# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import scrapy
from Fiction.items import FictionItem
import re
from scrapy.http import Request


class FictioncontentSpider(scrapy.Spider):
    name = 'FictionContent'
    allowed_domains = ['top.17k.com']
    start_urls = [
        'http://top.17k.com/top/top100/01_subscribe/01_subscribe__top_100_pc.html']
    top_urls = [
        'http://top.17k.com/top/top100/06_vipclick/06_vipclick_serialWithLong_top_100_pc.html',
        'http://top.17k.com/top/top100/06_vipclick/06_vipclick_new_top_100_pc.html',
        'http://top.17k.com/top/top100/15_hongbao/15_hongbao_top_100_pc.html',
        'http://top.17k.com/top/top100/12_hotcomment/12_hotcomment_top_100_pc.html',
    ]

    def parse(self, response):
        pattern = re.compile(
            '<td width="30">([\s\S]*?)</td><td width="60">[\s\S]*?target="_blank">([\s\S]*?)</a></td><td><a class="red" href="([\s\S]*?)" title="([\s\S]*?)" target="_blank">[\s\S]*?</td>[\s\S]*?</td><td>([\s\S]*?)</td><td>[\s\S]*?" title="([\s\S]*?)"[\s\S]*?<td width="30">')
        data = re.findall(pattern, response.body.decode('utf-8'))
        # print(data)
        for item in data:
            top = item[0]
            url = item[2]
            type_ = item[1]
            name = item[3]
            update_time = item[4]
            author = item[5]

            # 存入items容器中
            item = FictionItem()
            item['top'] = top
            item['url'] = url
            item['type_'] = type_
            item['name'] = name
            item['update_time'] = update_time
            item['author'] = author
            yield item
        for top in self.top_urls:
            yield Request(top, callback=self.parse)
