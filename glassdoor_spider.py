import scrapy

from urllib.parse import urljoin
from glassdoor.items import GlassdoorItem

class glasdoorSpider(scrapy.Spider):
    name = "glassdoor"
    allowed_domains = ["glassdoor.co.uk","glassdoor.com" ]

    while True:
        start_url = input("the full glassdoor url, including the https://   ")
        break
      
    start_urls = []
    start_urls.append(start_url)

    def parse(self,response):
        item = GlassdoorItem()
            
        for sel in response.xpath('*//ol/li/div'):
            date = sel.xpath('div/div/time/text()').extract()
            post_title = sel.xpath('div[2]/div[2]/h2/a/text()').extract()
            employee_position = sel.xpath('div[2]/div[2]/div[2]/div/span/span/text()').extract()
            post_text_pros = sel.xpath('div[2]/div[2]/div[4]/p[2]/text()').extract()
            post_text_cons = sel.xpath('div[2]/div[2]/div[5]/p[2]/text()').extract()
            item['post_title'] = post_title
            item['date'] = date
            item['employee_position'] = employee_position
            item['post_text_pros'] = post_text_pros
            item['post_text_cons'] = post_text_cons
            yield item
            
        next_page = response.xpath('.//li[@class="pagination__PaginationStyle__next"]/a[@class="pagination__ArrowStyle__nextArrow  "]/@href').extract()
        print(next_page)
        if next_page:
            next_href = next_page[0]
            next_page_url = urljoin('https://www.glassdoor.co.uk/',next_href)
            request = scrapy.Request(url=next_page_url)
            yield request
