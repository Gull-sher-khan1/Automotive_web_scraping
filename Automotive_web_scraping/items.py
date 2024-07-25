"""Contains item loaders"""
import scrapy
from itemloaders.processors import MapCompose
from .utils.data_utils import StringTransformer

class NewsItem(scrapy.Item):
    """News item and the fields containing scraped data"""
    site_link = scrapy.Field()
    image_link = scrapy.Field()
    heading = scrapy.Field(
        output_processor = MapCompose(StringTransformer.remove_whitespaces))
    body = scrapy.Field(
        output_processor = MapCompose(StringTransformer.remove_whitespaces))
    publish_date = scrapy.Field(
        output_processor = MapCompose(StringTransformer.to_datetime))
