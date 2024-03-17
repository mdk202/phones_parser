import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def clear_version(value):
    if value != 'None':
        value = remove_tags(value).strip(' AndroidOS.x')
    return value


class ParserOzonItem(scrapy.Item):
    os = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )
    version = scrapy.Field(
        input_processor=MapCompose(clear_version),
        output_processor=TakeFirst(),
        defaut=None
    )
