from scrapy.shell import inspect_response
import scrapy

class WSJSpider(scrapy.Spider):

    home = 'https://www.wsj.com'
    name = 'wsj'
    start_urls = ['https://www.wsj.com/search/term.html?KEYWORDS=Apple']

    def parse(self, response):
        #inspect_response(response)
        self.log('parsed')

        for article in response.xpath('//h3/a'):
            yield {
                'headline': article.xpath('text()').extract_first(),
                'links': "".join([self.home, article.xpath('@href').extract_first()])
            }
