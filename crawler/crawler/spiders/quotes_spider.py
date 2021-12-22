import scrapy
from datetime import datetime

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://www.trendyol.com/msi/mpg-x570-gaming-plus-ddr4-4400-oc-mhz-atx-am4-p-6989910',
    ]

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'satici': response.css('a.merchant-text::text').get(),
            'fiyati': response.css("div.product-price-container span.prc-dsc::text").get(),
            'urun-adi': response.css("div.product-container h1.pr-new-br a::text").get() + response.css("div.product-container h1.pr-new-br span::text").get(),
            'fetch-time' : datetime.now()
        }
