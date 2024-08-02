"""Contains the functionality for storing scraped data"""
from datetime import datetime
import dataset
from Automotive_web_scraping.utils.data_utils import DataFormater, StringTransformer
from Automotive_web_scraping.utils.database_utils import DuplicateHeadingsHandler

class NewsPipeline:
    """Pipeline for storing and parsing news into database"""
    cred = {}
    db = None
    news = []
    date_format = None

    def open_spider(self, _spider):
        """callback when spider is opened"""
        self.cred = DataFormater("db").get_data(key = "credentials")
        self.db = dataset.connect(f"{self.cred['database']}://{self.cred['username']}:{self.cred['password']}@{self.cred['host']}:{self.cred['port']}/{self.cred['db_name']}?sslmode=require")
    
    def close_spider(self, _spider):
        """Callback the closes the db and runs query when spider is closed"""
        self.remove_unnecessary_news()
        headings_to_be_stored = DuplicateHeadingsHandler([news['heading'][0] for news in self.news],
                                                        self.db).get_stored_headings()\
                                                            .get_non_existing_headings()
        self.store_news(headings_to_be_stored)
        self.db.commit()
        self.db.close()

    def process_item(self, news, spider):
        """Method for parsing and storing item"""
        if "publish_date" in news:
            news['publish_date'] = datetime.strptime(StringTransformer.remove_whitespaces(
                                news['publish_date'][0]), spider.date_format)
        self.news.append(news)

    def store_news(self, headings):
        """Mehotd for storing news"""
        for news in self.news:
            if news['heading'][0] in headings and "publish_date" in news:
                self.db['headlines'].insert(
                    dict(
                        image_link = news['image_link'][0] if 'image_link' in news else '',\
                        site_link = news['site_link'][0],\
                        heading = news['heading'][0],\
                        body = news['body'][0],\
                        publish_date = news['publish_date'],
                        added_at = datetime.now()))

    def remove_unnecessary_news(self):
        """remove news that does not follow the basic structure needed to zstore in DB"""
        for news in self.news:
            if not all(key in news for key in ("body","heading", "publish_date")):
                self.news.remove(news)
