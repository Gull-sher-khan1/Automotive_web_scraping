"""News Spider"""
# pylint: disable=abstract-method
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
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
        self.rules = tuple(map(lambda rl: (Rule(LinkExtractor(allow=f"{rl}"),\
                                        callback="parse_item",\
                                        follow=True)), self.data['allow']))
        super().__init__(*a, **kw)
        self.start_urls = [f"https://{site + path}" for path in self.data['startPath']]
        self.allowed_domains = [site]
        self.data = self.data['format']

    def parse_item(self, response):
        """Parses scrapped data from website"""
        news = ItemLoader(item = NewsItem(), response = response)
        for attr_name, selector in self.data.items():
            news.add_css(attr_name, selector)
        return news.load_item()
