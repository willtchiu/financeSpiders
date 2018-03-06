# financeSpiders
Light weight web scraper and crawlers for various financial news sources.
Disclaimer: Developed for educational purposes only.

### Usage:
Dependencies: python3, Scrapy, Twisted
1. List stock tickers interested in separate line in a file, i.e. ```stock.txt```
2. Execute
```python3 crawlers.py -i stock.txt```
3. Data output is in current directory following '{news_source_name}\_{stock_ticker}.jl'

### Financial News Sources Supported:
- Wall Street Journal (HOLD: Needs subscription to view articles...)
- Market Watch (WIP: Handle crawling of infinite scrolling article list, check out https://stackoverflow.com/questions/25583414/working-with-post-request-to-load-more-articles-with-scrapy-python)
    - 100% able to extract from MarketWatch
- Bloomberg (Supported)
- Reuters (Supported)
- MSNBC (Supported)
- TheStreet (Not supported)
- MarketRealist (Hold: paywall)
- SeekingAlpha (Supported)
- Fool (Not supported)
- Investopedia (Not supported)

### Changelog:

- Basic scraping of current related news article headlines, links, and texts
- Examples of scraped data in `financeScraper/*.jl`

- Centralized script: ```crawlers.py``` to simplify execution and pipelining
- Crawls all MarketWatch links and scrapes their articles
- Supports scraping of multiple stock ticker symbols

- Added dynamic parsing based on source news website
- Added support for Reuters articles
- Hold on WSJ, needs subscription

#### Feb. 19th, 2018
- Added support for MSNBC

#### Mar. 5th, 2018
- Added support for SeekingAlpha

### Overall TODOs:
```diff
+ Develop web crawlers to curate article information from current links
+ Create API for scraping specific companies by stock ticker labels
+ More dynamic crawlers that can extract from different news sites
- Support more market news sites, parsing wise
- Add date tags to .jl data files
- Add chron job to periodically scrape at some `time`
- Method to eliminate duplicate articles
```
