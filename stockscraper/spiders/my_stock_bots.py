import scrapy
from stockscraper.items import StockscraperItem
import schedule
import time

class MyStockBotsSpider(scrapy.Spider):
    name = 'my_stock_bots'
    allowed_domains = ['finance.naver.com/item/main.nhn?code=000660']
    start_urls = ['https://finance.naver.com/item/main.nhn?code=000660']

    def parse(self, response):
        time = response.css('.new_totalinfo>.blind>dd:nth-of-type(1)::text').extract()
        volume = response.css('.new_totalinfo>.blind>dd:nth-of-type(11)::text').extract()
        price = response.css('.new_totalinfo>.blind>dd:nth-of-type(4)::text').extract()
        top_price = response.css('.new_totalinfo>.blind>dd:nth-of-type(7)::text').extract()
        low_price = response.css('.new_totalinfo>.blind>dd:nth-of-type(9)::text').extract()
        code = response.css('.new_totalinfo>.blind>dd:nth-of-type(3)::text').extract()
        
        for row in zip(time, volume, price, top_price, low_price, code):
            item = StockscraperItem()
            item['time'] = row[0].replace(' 기준 장중', '')
            item['volume'] = row[1][4:]
            item['price'] = row[2].split(' ')[1]
            item['top_price'] = row[3][3:]
            item['low_price'] = row[4][3:]
            item['code'] = row[5].split(' ')[1]
            yield item
