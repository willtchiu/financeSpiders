# DEBUG
from scrapy.shell import inspect_response

import scrapy

class MWSpider(scrapy.Spider):
    home = 'https://marketwatch.com'
    name = "mws"
    """
    start_urls = [#'https://www.marketwatch.com/investing/stock/aapl/news',
                  #'https://www.marketwatch.com/investing/stock/nvda/news'#
                  'https://www.marketwatch.com/investing/stock/baba/news'
                 ]
    """
    def __init__(self, *args, **kwargs):
        super(MWSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        for article in response.xpath('//li/div/p/a'):
            article_link = article.xpath('@href').extract_first()
            yield response.follow(article_link, callback=self.parse_article) if article_link is not None else ""

    def parse_article(self, response):
        headline = response.xpath('//title/text()').extract_first()
        author   = response.xpath('//meta[@name=\'author\']/@content').extract_first()

        raw_text = response.xpath('//p/text()').extract()
        text     = " ".join(map(str.strip, raw_text))

        return { 'tick': "",
                 'head': headline,
                 'author': author,
                 'link': response.url,
                 'text': text
               }

