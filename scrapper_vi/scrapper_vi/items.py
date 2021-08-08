# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
import re

def parse_price(price):
    integer_price = price.split(',')[0]
    only_digits = re.findall(r'\d+', integer_price)
    return int(''.join(only_digits))

class ViItem(Item):
    title = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    price = Field(
        input_processor=MapCompose(parse_price),
        output_processor=TakeFirst()
    )
