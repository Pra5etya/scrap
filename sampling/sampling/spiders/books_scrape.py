from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime, timedelta

class CrawlingSpider(CrawlSpider): 
    
    # crawling sections
    name = 'my_crawler'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    # PROXY_SERVER = ''

    rules = (
        Rule(LinkExtractor(allow = 'catalogue/category')), 
        Rule(LinkExtractor(allow = 'catalogue', deny = 'category'), callback = 'parse_item')
    )

    # scraping sections
    def parse_item(self, response): 
        scrape_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        yield {
            'title': response.css('.product_main h1::text').get(), 
            'price': response.css('.price_color::text').get(), 
            'availability': response.css('.availability::text')[1].get().replace('\n', '').replace(' ', ''), 
            'scrape_time': scrape_time  # Add the timestamp here
        }