from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings

from financeScraper.items import FinancescraperItem
from financeScraper import settings as my_settings

import financeScraper.utils as utils

import scrapy
import sys, getopt

"""
    Class: MWSpider
    Description: Spider for crawling MarketWatch links given a stock
    ticker symbol and its own articles. Currently does not support
    scraping of outside linked articles.
"""
class MWSpider(scrapy.Spider):
    home       = 'https://marketwatch.com'
    name       = "mws"

    def create_start_url(self, tick):
        return "".join(["https://www.marketwatch.com/investing/stock/", tick, "/news"])

    def __init__(self, *args, **kwargs):
        super(MWSpider, self).__init__(*args, **kwargs)
        self.tick = kwargs.get('tick')
        self.start_urls = [self.create_start_url(self.tick)]

    
    def parse(self, response):
        for article in response.xpath('//li/div/p/a'):
            article_link = article.xpath('@href').extract_first()
            yield response.follow(article_link, callback=self.parse_article) if article_link is not None else ""

    def parse_article(self, response):
        yield utils.parse(response, self.tick)

"""
    Class: ReutersSpider
"""
class ReutersSpider(scrapy.Spider):

    home = 'https://www.reuters.com'
    name = 'reu'

    def create_start_url(self, tick):
        return "".join(["https://www.reuters.com/finance/stocks/company-news/", tick, ".OQ"])

    def __init__(self, *args, **kwargs):
        super(ReutersSpider, self).__init__(*args, **kwargs)
        self.tick = kwargs.get('tick')
        self.start_urls = [self.create_start_url(self.tick)]

    def parse(self, response):
        for article in response.xpath('//div[@class=\'feature\']'):

            article_link = article.xpath('h2/a/@href').extract_first()
            article_link = "".join([self.home, article_link])
            yield response.follow(article_link, callback=self.parse_article) if article_link is not None else ""

    def parse_article(self, response):
        yield utils.parse(response, self.tick)

"""
    Class: WSJSpider
    Description: Spider for Wall Street Journal. Currently WIP to
    obtain more relevant article links. Does not scrap articles.
"""
class WSJSpider(scrapy.Spider):

    home = 'https://www.wsj.com'
    name = 'wsj'

    def __init__(self, *args, **kwargs):
        super(WSJSpider, self).__init__(*args, **kwargs)
        self.tick = kwargs.get('tick')
        self.start_urls = [self.create_start_url(self.tick)]

    def parse(self, response):
        for article in response.xpath(
                '//ul[@class=\'cr_newsSummary\']//span[@class=\'headline\']'
            ):

            article_link = article.xpath('a/@href').extract_first()
            yield response.follow(article_link, callback=self.parse_article) if article_link is not None else ""

    """
    TODO: Subscriber/Login Wall...
    """
    def parse_article(self, response):
        return


def read_file(fn):
    with open(fn, 'r') as f:
        for ticker in f.readlines():
            yield ticker.strip()

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print ('crawlers.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('crawlers.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile="):
            inputfile = arg
    
    ticks = list(read_file(inputfile))
    # Create and run spiders
    configure_logging()
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    runner = CrawlerRunner(settings=crawler_settings)

    for tick in ticks:
        kwargs = {'tick': tick}
        runner.crawl(MWSpider, **kwargs)
        runner.crawl(ReutersSpider, **kwargs)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

if __name__ == "__main__":
    main(sys.argv[1:])
