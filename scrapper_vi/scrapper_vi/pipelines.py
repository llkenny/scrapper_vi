# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from scrapper_vi.models import Item, db_connect, create_table


class ScrapperViPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save product in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        new_item = Item()
        new_item.title = item['title']
        new_item.price = item['price']

        try:
            session.add(new_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        
        return item

