import scrapper_vi.hidden_variables as vars # not included in public repo
import scrapy
from scrapy.loader import ItemLoader
from scrapper_vi.items import ViItem

class ViSpider(scrapy.Spider):
    name = 'vi'

    start_urls = vars.START_URLS

    def parse(self, response):
        self.logger.info('Scraping vi')
        loader = ItemLoader(item=ViItem(), response=response)
        loader.add_css('title', 'h1.title::text')
        loader.add_css('price', 'span.current-price::text')

        yield loader.load_item()
