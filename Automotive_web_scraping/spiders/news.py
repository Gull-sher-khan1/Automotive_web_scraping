import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..utils.data_utils import FormatData

class NewsSpider(CrawlSpider):
    name = "news"
    start_urls = []
    allowed_domains = []


    def __init__(self, site = None, *a, **kw):
        super().__init__(*a, **kw)
        if(site is None): return

        self.data = FormatData(self.name).get_data(site)
        self.start_urls = map(lambda path: f"https://{site + path}", self.data['startPath'])
        self.rules = tuple(map(lambda rl: (Rule(LinkExtractor(allow=f"{rl}"), callback="parse_item", follow=True)), self.data['allow']))
        self.allowed_domains = [site]
        self.data = self.data['format']

    def parse_item(self, response):
        item = {}
        
        return item
