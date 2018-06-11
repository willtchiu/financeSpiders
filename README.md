# financeSpiders
Light weight web scraper and crawlers for various financial news sources. Aggregates article links and parses article texts using [Newspaper3k](https://github.com/codelucas/newspaper).

### Usage:
Dependencies: python3, Scrapy, Twisted
1. List stock tickers interested in separate line in a file, i.e. ```stock.txt```
2. Execute
```python3 crawlers.py -i stock.txt```
3. Data output is in current directory following '{news_source_name}\_{stock_ticker}.jl'

#### Cron job set-up:
Using bash script to execute data scraping on a daily basis
1. ```cd /etc/cron.daily/newsJob.sh```
In newsJob.sh:
```
#!/bin/bash
cd /to/root/project/directory/with/crawlers.py
python3 crawlers.py -i stocks.txt
```
2. ```chmod 755 newsJob.sh```
3. ```crontab -e```
```00 17 * * * /etc/cron.daily/newsJob.sh```
This will execute the cron job at 5:00PM system clock time every day

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

#### Feb. 19th, 2018
- Added support for MSNBC

#### Mar. 5th, 2018
- Added support for SeekingAlpha

#### Jun. 11th, 2018
- Branched to outsource article parsing (WIP)
- Updated article link scraping of supported news sites

### Overall TODOs:
```diff
+ Develop web crawlers to curate article information from current links
+ Create API for scraping specific companies by stock ticker labels
+ More dynamic crawlers that can extract from different news sites
+ Add date tags to .jl data files
- Support more market news sites, parsing wise
- Method to eliminate duplicate articles
```
