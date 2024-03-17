import scrapy
from scrapy.loader import ItemLoader

# import sys
# sys.path.append(r'C:\Users\malof\PycharmProjects\task_3_4\parser_ozon\parser_ozon')
# from items import ParserOzonItem
from ..items import ParserOzonItem


class SmartCrawlerSpider(scrapy.Spider):
    name = "smart_crawler"
    allowed_domains = ['ozon.ru']
    start_urls = ["https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?sorting=rating"]

    smartphone_links = []
    next_page = "/category/telefony-i-smart-chasy-15501/?sorting=rating&page="
    page_counter = 1

    def parse(self, response, **kwargs):
        products = response.xpath('//a[@class="tile-hover-target a9i i9a"]')
        for product in products:
            if 'Смартфон' in product.xpath("div/span/text()").get():
                clear_link = product.xpath('@href').get().split("?")[0]
                self.smartphone_links.append(response.urljoin(clear_link))
        print(len(self.smartphone_links))
        if len(self.smartphone_links) < 4:
            self.page_counter += 1
            yield scrapy.Request(
                url=response.urljoin(f'{self.next_page}{self.page_counter}'),
                callback=self.parse
            )
        # else:
        #     for link in self.smartphone_links[0:2]:
        #         yield scrapy.Request(
        #             url=f'{link}features/',
        #             callback=self.parse_detail, dont_filter=True
        #         )

    def parse_detail(self, response):
        loader = ItemLoader(item=ParserOzonItem(), response=response)
        receiving_os = '//dt[span[contains(text(), "Операционная")]]/following-sibling::dd'
        receiving_version = '//dt[span[contains(text(), "Версия")]]/following-sibling::dd'

        loader.add_xpath("os", receiving_os)
        loader.add_xpath("version", receiving_version)
        yield loader.load_item()