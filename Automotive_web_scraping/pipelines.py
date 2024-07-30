"""Contains the functionality for storing scraped data"""
from datetime import datetime
import dataset
from .utils.data_utils import DataFormater, StringTransformer
from .utils.database_utils import DuplicateHeadingsHandler

class NewsPipeline:
    """Pipeline for storing and parsing news into database"""
    cred = {}
    db = None
    news = []
    date_format = None

    def open_spider(self, _spider):
        """callback when spider is opened"""
        self.cred = DataFormater("db").get_data("credentials")
        self.db = dataset.connect(
            f'{self.cred['database']}://'+\
            f'{self.cred['username']}:{self.cred['password']}'+\
            f'@{self.cred['host']}:{self.cred['port']}/{self.cred['db_name']}'
        )

    def close_spider(self, _spider):
        """Callback the closes the db and runs query when spider is closed"""
        headings_to_be_stored = DuplicateHeadingsHandler([key['heading'][0] for key in self.news],
                                                         self.db).get_stored_headings()\
                                                            .get_non_existing_headings()
        self.store_news(headings_to_be_stored)
        self.db.commit()
        self.db.close()

    def process_item(self, news, spider):
        """Method for parsing and storing item"""
        self.news.append(news)
        self.date_format = spider.date_format

    def store_news(self, headings):
        """Mehotd for storing news"""
        for news in self.news:
            if news['heading'][0] in headings:
                self.db['headlines'].insert(
                    dict(
                        image_link = news['image_link'][0] if 'image_link' in news else '',\
                        site_link = news['site_link'][0],\
                        heading = news['heading'][0],\
                        body = news['body'][0],\
                        publish_date = datetime.strptime(StringTransformer.remove_whitespaces(
                            news['publish_date'][0]), self.date_format)))
