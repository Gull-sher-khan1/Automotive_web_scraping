"""python script for running multiple spiders"""
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Automotive_web_scraping.spiders.news import NewsSpider
from Automotive_web_scraping.utils.data_utils import DataFormater
from Automotive_web_scraping.utils.mailer_utils import MailerUtils

process = CrawlerProcess(get_project_settings())
sites = DataFormater('news').get_data()
exception_handler = MailerUtils()
for site, _data in sites.items():
    process.crawl(NewsSpider, site = site, exception_handler = exception_handler, script = True)

process.start()
if len(exception_handler.context) != 0:
    exception_handler.send_email()
