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
def generate_article_list(response, tick):
    """Helper to extract article links and format into a FinancescraperItem()

    Args:
        response: scrapy response object
        tick: string of the stock ticker symbol
    Returns:
        FinancescraperItem - a wrapper class for items scraped
    """
    base_url = strip_base_url(response.url)
    item = FinancescraperItem()

    item['tick']     = tick
    item['link']     = response.url
    item['source']   = base_url

    return item
