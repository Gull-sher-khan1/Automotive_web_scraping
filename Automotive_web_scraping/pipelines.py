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
        for i in range(len(news['head'])):
            table.insert(
                dict(
                    image_link = news['image_link'][i],\
                    site_link = news['site_link'][i],\
                    heading = news['heading'][i],\
                    body = news['body'][i],\
                    publish_date = news['publish_date'][i]))
