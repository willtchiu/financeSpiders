from financeScraper.items import FinancescraperItem
from enum import Enum
import re

class NewsSource(Enum):
    mws = "https://www.marketwatch.com/"
    wsj = "https://www.wsj.com/"
    reu = "https://www.reuters.com/"
    blo = "https://www.bloomberg.com/"
    msn = "https://www.cnbc.com/"

def strip_base_url(url):
    return re.search("http(s)?:\/\/[a-zA-Z0-9._]+\/", url).group()

def clean_text(raw_text):
    return " ".join(map(str.strip, raw_text))

def remove_html_tags(raw_text):
    filtered = []
    tag_stack = []
    for ch in raw_text:
        if ch == '<':
            tag_stack.append(ch)
        elif ch == '>':
            tag_stack.pop()
        else:
            if not tag_stack:
                filtered.append(ch)
    return ''.join(filtered)

def parse(response, tick):
    # Switch case on news source
    base_url = strip_base_url(response.url)
    headline = author = raw_text = text = ""
    item = FinancescraperItem()

    print("Base url is: ")
    print(base_url)
    print(NewsSource.mws.value)
    if base_url == NewsSource.mws.value:
        # DO something
        headline = response.xpath('//title/text()').extract_first()
        author   = response.xpath('//meta[@name=\'author\']/@content').extract_first()
        raw_text = response.xpath('//p/text()').extract()
        text     = clean_text(raw_text)

    elif base_url == NewsSource.wsj.value:
        # DO something
        pass
    elif base_url == NewsSource.reu.value:
        # Do Something
        headline = response.xpath('//title/text()').extract_first()
        headline = clean_text(headline.split())
        author   = response.xpath('//meta[@name=\'Author\']/@content').extract_first()
        raw_text = response.xpath('//p[not(@class)]/node()[not(self::a or self::span)]').extract()
        text     = clean_text(raw_text)

    elif base_url == NewsSource.blo.value:
        # Do something
        headline = response.xpath('//title/text()').extract_first()
        author   = response.xpath('//address[@class]/text()').extract_first()
        raw_text = response.xpath('//div[@class=\"body-copy\"]/p/text()').extract()
        text     = clean_text(raw_text)
    elif base_url == NewsSource.msn.value:
        # Do Something
        headline = response.xpath('//title/text()').extract_first()
        author   = response.xpath('//meta[@name=\"author\"]/@content').extract_first()
        raw_text = ' '.join(response.xpath('//div[@class=\"group\"]/p').extract())
        text     = remove_html_tags(raw_text)
    else:
        # Handle unknown news source scraping
        print("--------- Unknown news source -------")
        print(base_url)
        pass

    item['tick']     = tick
    item['headline'] = headline
    item['author']   = author
    item['link']     = response.url
    item['text']     = text
    item['source']   = base_url

    return item
