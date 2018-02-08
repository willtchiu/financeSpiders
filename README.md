# financeSpiders
Light weight web scraper and crawlers for various financial news sources.
Disclaimer: Developed for educational purposes only.

### Financial News Sources Supported:
- Wall Street Journal (WIP: Workaround to curate more relevant news articles from specific company pages)
- Market Watch (WIP: Handle crawling of infinite scrolling article list, check out https://stackoverflow.com/questions/25583414/working-with-post-request-to-load-more-articles-with-scrapy-python)
    - 100% able to extract author name from MarketWatch, but not from links to other sites
### Current Status:
#### Version 0.01
- Basic scraping of current related news article headlines, links, and texts
- Examples of scraped data in `financeScraper/*.jl`

### Overall TODOs:
```diff
+ Develop web crawlers to curate article information from current links
- Create API for scraping specific companies by stock ticker labels
- More dynamic crawlers that can extract from different html formatting
```
