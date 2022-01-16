import scrapper_vi.hidden_variables_wb as vars # not included in public repo
import scrapy
from scrapy.loader import ItemLoader
from scrapper_vi.items import ViItem


class WbSpider(scrapy.Spider):
    name = 'wb'
    start_urls = vars.START_URLS

    def parse(self, response):
        self.logger.info('Scraping wb')
        loader = ItemLoader(item=ViItem(), response=response)

        title = f"{response.css('h1.same-part-kt__header').css('span::text')[0].get()} / {response.css('h1.same-part-kt__header').css('span::text')[1].get()}"
        loader.add_value('title', title)

        price = response.css('span.price-block__final-price::text').get().replace(u'\xa0', u' ')
        loader.add_value('price', price)

        yield loader.load_item()
