"""Contains the functionality for storing scraped data"""
from datetime import datetime
import dataset
from .utils.data_utils import DataFormater, StringTransformer

class NewsPipeline:
    """Pipeline for storing and parsing news into database"""
    cred = {}
    db = None

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
        self.db.commit()
        self.db.close()

    def process_item(self, news, spider):
        """Method for parsing and storing item"""
        table = self.db['headlines']
        table.insert(
            dict(
                image_link = news['image_link'][0] if 'image_link' in news else '',\
                site_link = news['site_link'][0],\
                heading = news['heading'][0],\
                body = news['body'][0],\
                publish_date = datetime.strptime(StringTransformer.remove_whitespaces(news['publish_date'][0]), spider.date_format)))
