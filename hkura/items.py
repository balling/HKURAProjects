# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import MapCompose, Join, TakeFirst
from w3lib.html import remove_tags


class UrbanRenewalItem(scrapy.Item):
    title = scrapy.Field(input_processor=MapCompose(remove_tags),
                         output_processor=TakeFirst(), )
    link = scrapy.Field(output_processor=TakeFirst(),)
    html = scrapy.Field(output_processor=TakeFirst(),)
    text = scrapy.Field(input_processor=MapCompose(remove_tags, unicode.strip),
                        output_processor=Join(), )
    last_updated = scrapy.Field(input_processor=MapCompose(remove_tags),
                         output_processor=TakeFirst(),)
    file_urls = scrapy.Field()
