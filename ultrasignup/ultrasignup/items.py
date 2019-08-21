# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class UltrasignupItem(CrawlSpider):
    name = "ultrasignupSpider"
    allowed_domains = ["ultrasignup.com"]
    start_urls = ["http://www.ultrasignup.com/"]
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self,response):
        self.log('A response from %s just arrived!' % response.url)
