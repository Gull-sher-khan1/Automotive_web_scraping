"""News Spider"""
# pylint: disable=abstract-method
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy import Selector
from ..items import NewsItem
from ..utils.data_utils import DataFormater

class NewsSpider(CrawlSpider):
    """Generic spider class for scraping news on websites"""
    name = "news"
    start_urls = []
    allowed_domains = []

    def __init__(self, *a, site = None, **kw):
        if site is None:
            return

        self.data = DataFormater(self.name).get_data(site)
        self.rules = (Rule(LinkExtractor(allow=self.data['allow'], deny=self.data['deny']),\
                                        callback="parse_item", follow=True),)
        super().__init__(*a, **kw)
        self.start_urls = [f"https://{site + path}" for path in self.data['startPath']]
        self.allowed_domains = [site]
        self.data = self.data['format']
        self.individual_ojects = self.data['individual_objects']
        self.date_format = self.data['date_format']
        for key in ['individual_objects', 'date_format']:
            del self.data[key]

    def parse_item(self, response):
        """Parses scrapped data from website"""
        items = response.css(self.individual_ojects)
        for item in items.getall():
            news = ItemLoader(item = NewsItem())
            news.add_value('site_link', [response.url])
            for attr_name, selector in self.data.items():
                news.add_value(attr_name, Selector(text = item).css(selector).get())
            yield news.load_item()
