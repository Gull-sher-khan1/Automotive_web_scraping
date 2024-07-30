"""python script for running multiple spiders"""
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Automotive_web_scraping.spiders.news import NewsSpider
from Automotive_web_scraping.utils.data_utils import DataFormater

process = CrawlerProcess(get_project_settings())
sites = DataFormater('news').get_data()
for site, _data in sites.items():
    process.crawl(NewsSpider, site = site)

process.start()
