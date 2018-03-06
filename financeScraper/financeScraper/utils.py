from financeScraper.items import FinancescraperItem
from enum import Enum
import re

"""Enum for NewsSource websites
"""
class NewsSource(Enum):
    mws = "https://www.marketwatch.com/"
    wsj = "https://www.wsj.com/"
    reu = "https://www.reuters.com/"
    blo = "https://www.bloomberg.com/"
    msn = "https://www.cnbc.com/"
    sal = "https://seekingalpha.com/"

def strip_base_url(url):
    """Strips url down to base url

    Args:
        url: news source url to strip down
    Returns:
        string of the stripped down url
    """
    return re.search("http(s)?:\/\/[a-zA-Z0-9._]+\/", url).group()

def clean_text(raw_text):
    """Removes most non-alphanumeric characters from a string

    Args:
        raw_text: the text to be filtered
    Returns:
        string of the filtered, mostly alpha-numeric text
    """
    return " ".join(map(str.strip, raw_text))

def remove_html_tags(raw_text):
    """Filters out and removes all html artifacts from a string

    Args:
        raw_text: text with html tags
    Returns:
        string of the text with html tags removed
    """
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

# Refractor to pass in dict of parser objects... cleaner and less if statements
def parse(response, tick):
    """Main parsing method to extract attributes from articles

    Able to parse multiple news source articles and extract information such as
    Headline, Author, and Text.

    Args:
        response: scrapy response object
        tick: string of the stock ticker symbol
    Returns:
        FinancescraperItem - a wrapper class for items scraped
    """
    # Switch case on news source
    base_url = strip_base_url(response.url)
    headline = author = raw_text = text = ""
    item = FinancescraperItem()

    print("Base url is: ")
    print(base_url)
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
    elif base_url == NewsSource.sal.value:
      # Do something
        print("Here--------")
        headline = response.xpath("//title/text()").extract_first()
        author   = response.xpath("//meta[@name=\"author\"]/@content").extract_first()
        raw_text = ''.join(response.xpath("//*[@class=\"p p1\" or @class=\"p p2\"]").extract())
        text     = clean_text(remove_html_tags(raw_text).split())
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
