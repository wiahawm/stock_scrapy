# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockscraperItem(scrapy.Item):
    time = scrapy.Field()
    volume = scrapy.Field()
    price = scrapy.Field()
    top_price = scrapy.Field()
    low_price = scrapy.Field()
    code = scrapy.Field()