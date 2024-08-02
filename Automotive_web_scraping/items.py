"""Contains item loaders"""
import scrapy
from itemloaders.processors import MapCompose
from w3lib import html
from Automotive_web_scraping.utils.data_utils import StringTransformer

def remove_tags_and_contents(val):
    return [html.remove_tags(html.remove_tags_with_content(val[0], which_ones=['script']))]

class NewsItem(scrapy.Item):
    """News item and the fields containing scraped data"""
    date_format = scrapy.Field()
    site_link = scrapy.Field()
    image_link = scrapy.Field()
    heading = scrapy.Field(
        output_processor = MapCompose(StringTransformer.remove_whitespaces))
    body = scrapy.Field(
        input_processor = remove_tags_and_contents,
        output_processor = MapCompose(StringTransformer.remove_whitespaces))
    publish_date = scrapy.Field()
