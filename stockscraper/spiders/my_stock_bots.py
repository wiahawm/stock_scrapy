import scrapy
from stockscraper.items import StockscraperItem
import schedule
import time

class MyStockBotsSpider(scrapy.Spider):
    name = 'my_stock_bots'
    allowed_domains = ['finance.naver.com/item/main.nhn?code=000660']
    start_urls = ['https://finance.naver.com/item/main.nhn?code=000660']

    def parse(self, response):
        title = response.css('.new_totalinfo>.blind>dd:nth-of-type(2)::text').extract()
        time = response.css('.new_totalinfo>.blind>dd:nth-of-type(1)::text').extract()
        volume = response.css('.new_totalinfo>.blind>dd:nth-of-type(11)::text').extract()
        price = response.css('.new_totalinfo>.blind>dd:nth-of-type(4)::text').extract()
        top_price = response.css('.new_totalinfo>.blind>dd:nth-of-type(7)::text').extract()
        low_price = response.css('.new_totalinfo>.blind>dd:nth-of-type(9)::text').extract()
        code = response.css('.new_totalinfo>.blind>dd:nth-of-type(3)::text').extract()
        
        for row in zip(title, time, volume, price, top_price, low_price, code):
            item = StockscraperItem()
            item['title'] = row[0].split(' ')[1]
            item['time'] = row[1][:21]
            item['volume'] = row[2][4:]
            item['price'] = row[3].split(' ')[1]
            item['top_price'] = row[4][3:]
            item['low_price'] = row[5][3:]
            item['code'] = row[6].split(' ')[1]
            yield item
