"""Contains the functionality for storing scraped data"""
import dataset
from .utils.data_utils import DataFormater

class NewsPipeline:
    """Pipeline for storing and parsing news into database"""
    cred = {}
    db = None

    def open_spider(self, _spider):
        """callback when spider is opened"""
        self.cred = DataFormater("db").get_data("postgresql")
        self.db = dataset.connect(
            f'postgresql://{self.cred['username']}:{self.cred['password']}'
            + f'@localhost:5432/{self.cred['database']}')

    def close_spider(self, _spider):
        """Callback the closes the db and runs query when spider is closed"""
        self.db.commit()
        self.db.close()

    def process_item(self, news, _spider):
        """Method for parsing and storing item"""
        table = self.db[self.cred['table']]
        table.insert(
            dict(
                image_link = news['image_link'][0] if 'image_link' in news else '',\
                site_link = news['site_link'][0],\
                heading = news['heading'][0],\
                body = news['body'][0],\
                publish_date = news['publish_date'][0]))
