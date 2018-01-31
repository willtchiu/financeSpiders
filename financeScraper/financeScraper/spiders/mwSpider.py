from scrapy.shell import inspect_response
import scrapy

class MWSpider(scrapy.Spider):
    home = 'https://marketwatch.com'
    name = "mws"
    start_urls = ['https://www.marketwatch.com/investing/stock/aapl/news',
                  'https://www.marketwatch.com/investing/stock/nvda/news'
                 ]

    def parse(self, response):
        #inspect_response(response)

        for article in response.xpath('//li/div/p/a'):
            yield {
                'headline': article.xpath('text()').extract_first(),
                'link': "".join([self.home, article.xpath('@href').extract_first()])
            }
