# imports
import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

# initialize crawler
class ultrasignupSpider(CrawlSpider):
    urls = []
    for i in range(1,100000):
        urls.append(f"http://ultrasignup.com/register.aspx?did={i}")
    name = "ultrasignupSpider"
    allowed_domains = ["ultrasignup.com"]
    ''' This will do until I feel like dealing with selenium '''
    start_urls = urls
    # extract links
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self,response):
        # logging
        self.log(f'A response from {response.url} just arrived!')
        with open('races.txt','a') as f:
                # write out the title and add a newline.
                # only save event results
            try:
                if response.url[:46] == 'http://ultrasignup.com/results_event.aspx?did=':
                    f.write(response.url + "\n")
            except IndexError:
                pass
